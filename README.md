Role Name
=========

Install Redmine 3 on CentOS. Eventually, we will support other operating
systems. Right now, only CentOS 7.

Requirements
------------

This role will install the necessary components from official CentOS 7
repositories. Redmine will be downloaded from redmine.org and required Ruby
gems from rubygems.org.


Role Variables
--------------

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
         - { role: bngsudheer.ansible-role-redmine, sql_username: redmine, sql_password: password, sql_database_name: redmine, sql_database_host: localhost}

License
-------

BSD

Author Information
------------------

Sudheer Satyanarayana
Blog: http://www/techchorhs.net
Twitter: http:/www.twitter.com
