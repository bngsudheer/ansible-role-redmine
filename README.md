Redmine On CentOS 7
=========

This module is in beta. your feedback is appreciated.

Install Redmine 3 on CentOS. We restrict ourselves to RHEL/CentOS/Fedora family of distributions. 
Right now, only CentOS 7 is supported.

Requirements
------------

This role will install the required RPM packages from the official CentOS 7
repositories. Redmine will be downloaded from redmine.org and required Ruby
gems from rubygems.org.


Role Variables
--------------

* redmine_version: default value is "3.4.2"
* sql_username: default value is "redmine"
* sql_password: default value is "localhost"
* sql_database_name: default value is "redmine"
* sql_database_host: default value is "localhost"
* unicorn_worker_processes: default value is 2


Dependencies
------------

No other dependencies.


Example Playbook
----------------

Example playbook

    - hosts: servers
      remote_user: root
      roles:
         - role: bngsudheer.redmine 
         - sql_username: redmine 
         - sql_password: password
         - sql_database_name: redmine 
         - sql_database_host: localhost 
         - redmine_version: 3.4.2

License
-------

BSD

Author Information
------------------

Sudheer Satyanarayana
Blog: http://www.techchorus.net
Twitter: http:/www.twitter.com/bngsudheer
