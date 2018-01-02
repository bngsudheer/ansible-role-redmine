Redmine On CentOS 7
=========

This module is in beta. Your feedback is appreciated.

Install Redmine 3 on CentOS. We restrict ourselves to RHEL/CentOS/Fedora family
of distributions. (This many change in future.) Right now, only CentOS 7 is supported.
The role supports setting up Redmine via Unicorn and Nignx.

This role will install the required RPM packages from the official CentOS 7
repositories. Redmine will be downloaded from redmine.org and required Ruby
gems from rubygems.org.

To stop redmine use the command:
    systemctl stop redmine

To start redmine use the command:
    systemctl start redmine

Requirements
------------
Ruby >= 2.1 is required. Somewhere in the gems dependency chain recently, Ruby 2.1 has been set as a required package.
Make sure Ruby >= 2.1 is installed or use [Ruby Ansible role](https://galaxy.ansible.com/bngsudheer/ruby/).

If you are using MySQL or PostgreSQL, you have to provide the database server name,
database name, database username and password via the variables:
* redmine_sql_username
* redmine_sql_password
* redmine_sql_database_name
* redmine_sql_database_host

Make sure port 80 is open in your firewall. If you serve Redmine over https
make sure port 443 is open too.

Role Variables
--------------

These variables are available with the following default values:
* redmine_version: "3.4.2"
* redmine_sql_username: "redmine"
* redmine_sql_password: "localhost"
* redmine_sql_database_name: "redmine"
* redmine_sql_database_host: "localhost"
* redmine_unicorn_worker_processes: 2
* redmine_domain_name: redmine.example.com (domain name on which you want to serve Nginx->Unicorn->Redmine).  
* redmine_configure_nginx: yes
* redmine_configure_unicorn: yes

These variables are available with the no default values:
* redmine_nginx_bind_ip:


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

License
-------

BSD

Author Information
------------------

Sudheer Satyanarayana
Blog: http://www.techchorus.net
Twitter: http://www.twitter.com/bngsudheer
