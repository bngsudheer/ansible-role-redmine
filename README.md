Redmine On CentOS 7
=========

Install Redmine 3 on CentOS. The role installs Redmine via Unicorn and Nignx.

This module is in beta. Your feedback is appreciated.

We focus on RHEL/CentOS/Fedora family
of distributions until version 1.0 is released. In future versions, we will support Ubuntu and other Linux distributions. Right now, only CentOS 7 is supported.

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
* redmine_nginx_bind_ip: 0.0.0.0


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
* Blog: https://www.techchorus.net
* Twitter: https://www.twitter.com/bngsudheer
* Work: https://www.gavika.com
