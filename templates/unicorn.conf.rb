worker_processes {{ redmine_unicorn_worker_processes }}

working_directory "{{ redmine_runtime_directory }}" # available in 0.94.0+

listen 8080, :tcp_nopush => true
#listen "/var/run/redmine/redmine.unicorn.sock", :backlog => 64

# nuke workers after 30 seconds instead of 60 seconds (the default)
timeout 30

# feel free to point this anywhere accessible on the filesystem
pid "/var/run/redmine/unicorn.pid"

# By default, the Unicorn logger will write to stderr.
# Additionally, ome applications/frameworks log to stderr or stdout,
# so prevent them from going to /dev/null when daemonized here:
stderr_path "{{ redmine_runtime_directory }}/shared/log/unicorn.stderr.log"
stdout_path "{{ redmine_runtime_directory }}/shared/log/unicorn.stdout.log"

# combine Ruby 2.0.0+ with "preload_app true" for memory savings
preload_app true

# Enable this flag to have unicorn test client connections by writing the
# beginning of the HTTP headers before calling the application.  This
# prevents calling the application for connections that have disconnected
# while queued.  This is only guaranteed to detect clients on the same
# host unicorn runs on, and unlikely to detect disconnects even on a
# fast LAN.
check_client_connection false

# local variable to guard against running a hook multiple times
run_once = true

before_fork do |server, worker|
  # the following is highly recomended for Rails + "preload_app true"
  # as there's no need for the master process to hold a connection
  defined?(ActiveRecord::Base) and
    ActiveRecord::Base.connection.disconnect!

  # Occasionally, it may be necessary to run non-idempotent code in the
  # master before forking.  Keep in mind the above disconnect! example
  # is idempotent and does not need a guard.
  if run_once
    # do_something_once_here ...
    run_once = false # prevent from firing again
  end

end

after_fork do |server, worker|
  # per-process listener ports for debugging/admin/migrations
  # addr = "127.0.0.1:#{9293 + worker.nr}"
  # server.listen(addr, :tries => -1, :delay => 5, :tcp_nopush => true)

  # the following is *required* for Rails + "preload_app true",
  defined?(ActiveRecord::Base) and
    ActiveRecord::Base.establish_connection

  # if preload_app is true, then you may also want to check and
  # restart any other shared sockets/descriptors such as Memcached,
  # and Redis.  TokyoCabinet file handles are safe to reuse
  # between any number of forked children (assuming your kernel
  # correctly implements pread()/pwrite() system calls)
end
