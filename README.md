Role Name
=========

THIS MODULE IS IN BETA. YOUR FEEDBACK IS APPRECIATED.

Install Redmine 3 on CentOS. We restrict ourselves to RHEL/CentOS/Fedora family of distributions. 
Right now, only CentOS 7 is supported.

Requirements
------------

This role will install the necessary components from official CentOS 7
repositories. Redmine will be downloaded from redmine.org and required Ruby
gems from rubygems.org.


Role Variables
--------------

* redmine_version
* sql_username
* sql_password
* sql_database_name
* sql_database_host


Dependencies
------------

No other dependencies.


Example Playbook
----------------

Example playbook

    - hosts: servers
      remote_user: root
      roles:
         - { role: bngsudheer.redmine, sql_username: redmine, sql_password: password, sql_database_name: redmine, sql_database_host: localhost, redmine_version: 3.2.1}

License
-------

BSD

Author Information
------------------

Sudheer Satyanarayana
Blog: http://www/techchorhs.net
Twitter: http:/www.twitter.com/bngsudheer
