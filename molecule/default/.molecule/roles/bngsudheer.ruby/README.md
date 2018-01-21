Role Name
=========

Install Ruby 2.2, Ruby 2.3 or Ruby 2.4 on CentOS 7. The role utilizes Red Hat software collections.

Description
============

After running the role, the selected version of Ruby will be enabled for new login shell. If you are already logged onto the server, you will not see updated Ruby version. Logout and log back in and you will see newer Ruby version.

```sh
ruby --version
```

Requirements
------------

None. We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/).


Role Variables
--------------

* ruby_version: 2.4

By default, Ruby 2.4 will be installed and enabled for all users on the system.


Dependencies
------------

None. We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/).

Example Playbook
----------------

    - hosts: servers
      vars:
        ruby_version: 2.3
      roles:
         - bngsudheer.ruby

License
-------

BSD

Author Information
------------------

Sudheer Satyanarayana.
* [Twitter](https://twitter.com/bngsudheer)
* [GitHub](https://github.com/bngsudheer)
* [Work](https://www.gavika.com/)