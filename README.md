Redmine On CentOS 7
=========

This module is in beta. your feedback is appreciated.

Install Redmine 3 on CentOS. We restrict ourselves to RHEL/CentOS/Fedora family of distributions. 
Right now, only CentOS 7 is supported.
The role supports setting up Redmine via Unicorn and Nignx.

Requirements
------------

This role will install the required RPM packages from the official CentOS 7
repositories. Redmine will be downloaded from redmine.org and required Ruby
gems from rubygems.org.


Role Variables
--------------

These variables are available with the following default values:
* redmine_version: "3.4.2"
* sql_username: "redmine"
* sql_password: "localhost"
* sql_database_name: "redmine"
* sql_database_host: "localhost"
* unicorn_worker_processes: 2
* domain_name:  redmine.example.com (domain name on which you want to serve Nginx->Unicorn->Redmine).  
* configure_nginx: default value is yes
* configure_unicorn: default value yes


Dependencies
------------

No other dependencies.

We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/)


Example Playbook
----------------

Example playbook

    - hosts: servers
      vars:
       - redmine_sql_username: redmine 
       - redmine_sql_password: password
       - redmine_sql_database_name: redmine 
       - remmine_sql_database_host: localhost 
       - redmine_version: 3.4.2
      remote_user: root
      roles:
         - role: bngsudheer.redmine 
      
License
-------

BSD

Author Information
------------------

Sudheer Satyanarayana
Blog: http://www.techchorus.net
Twitter: http://www.twitter.com/bngsudheer
