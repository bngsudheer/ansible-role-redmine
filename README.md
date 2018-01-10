Redmine On CentOS 7
=========

Install Redmine 3.x and Redmine plugins on CentOS. The role installs Redmine via Unicorn and Nignx.

In future versions, we will support Ubuntu and other Linux distributions. Right now, only CentOS 7 is supported.

This role will install the required RPM packages from the official CentOS 7
repositories. Redmine will be downloaded from redmine.org and required Ruby
gems from rubygems.org.

To start Redmine use the command:
```sh
    systemctl start redmine
 ```

To stop Redmine use the command:
```sh
    systemctl stop redmine
 ```

Requirements
------------
Ruby >= 2.1 maybe required. If somewhere in the gems dependency chain,
Ruby 2.1 is set as a required package, you could use [Ruby Ansible role](https://galaxy.ansible.com/bngsudheer/ruby/). At the moment, Redmine works on Ruby 2.0.

If you are using MySQL or PostgreSQL, you have to provide the database server name,
database name, database username and password via the variables:
* redmine_sql_username
* redmine_sql_password
* redmine_sql_database_name
* redmine_sql_database_host

Make sure port 80 is open in your firewall. If you serve Redmine over HTTPS
make sure port 443 is open too.

Role Variables
--------------

These variables are available with the following default values:
* redmine_version: "3.4.2"

Database related variables:
* redmine_sql_username: "redmine"
* redmine_sql_password: "localhost"
* redmine_sql_database_name: "redmine"
* redmine_sql_database_host: "localhost"
* redmine_unicorn_worker_processes: 2
* redmine_domain_name: redmine.example.com (domain name on which you want to serve Nginx->Unicorn->Redmine).  

Other variables
* redmine_configure_nginx: yes
* redmine_configure_unicorn: yes
* redmine_unicorn_port: 5000
* redmine_configure_firewalld: yes
* redmine_nginx_bind_ip:
* redmine_plugins: []
* redmine_configure_selinux: no


Dependencies
------------

No other dependencies.

We recommend using the roles:
- [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/)
- [Ruby](https://galaxy.ansible.com/bngsudheer/ruby/)

Example playbook

    - hosts: servers
      vars:
       - redmine_sql_username: redmine
       - redmine_sql_password: password
       - redmine_sql_database_name: redmine
       - remmine_sql_database_host: localhost
       - redmine_version: 3.4.2
       - redmine_nginx_bind_ip: 192.168.100.130
      remote_user: root
      roles:
         - bngsudheer.ruby
         - bngsudheer.redmine

 Example playbook to install Redmine with plugins

     - hosts: servers
       vars:
        - redmine_sql_username: redmine
        - redmine_sql_password: password
        - redmine_sql_database_name: redmine
        - remmine_sql_database_host: localhost
        - redmine_version: 3.4.2
        - redmine_nginx_bind_ip: 192.168.100.130
        - redmine_plugins:
          - name: scrum
            base_name: scrum
            url: https://redmine.ociotec.com/attachments/download/481/scrum-v0.18.1.tar.gz
       remote_user: root
       roles:
          - bngsudheer.ruby
          - bngsudheer.redmine

The variable *redmine_plugins* is a directory with the keys *name*, *base_name* and the *url*.
The *base_name* is the directory name that will be used in the plugins directory. *name*
is for human reference. *url* is the location from where the plugin has to be downloaded.

License
-------

BSD

Author Information
------------------

Sudheer Satyanarayana
* Blog: https://www.techchorus.net
* Twitter: https://www.twitter.com/bngsudheer
* Work: https://www.gavika.com
