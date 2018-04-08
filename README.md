Redmine On CentOS 7
=========

Install Redmine 3.x and Redmine plugins on CentOS. The role installs Redmine
along with Unicorn and Nignx.

In future versions, we will support other Linux distributions.
Right now, only CentOS 7 is supported.

Note On Debian And Ubuntu:
===========
* Debian Stretch provides the [Redmine package](https://packages.debian.org/stable/web/redmine)
and can be installed via apt.
* Ubuntu multiverse provides the [Redmine package](https://packages.ubuntu.com/xenial/web/redmine) and can be installed via apt.


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
If you are using MySQL or PostgreSQL, you have to provide the database server name,
database name, database username and password via the variables:
* redmine_sql_username
* redmine_sql_password
* redmine_sql_database_name
* redmine_sql_database_host

Make sure port 80 is open in your firewall. If you serve Redmine over HTTPS
make sure port 443 is open too.

If you set *redmine_configure_selinux* to *yes* then *libselinux-python* and
*policycoreutils-python* packages are required. These packages can be installed
via [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/).
```
centos_base_selinux_packages: true.
```

If you are using a container with minimal packages, you will have to install
some essential packages like *@Developement Tools*, *zlib*, etc. You
can install them via [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/)
by setting the variable:
```
centos_base_basic_packages: true.
```
If you use *redmine_nginx_config_template: tls*, make sure the file
/etc/ssl/private/dhparam.pem is present so that [Diffie-Hellman key exchage](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) works.

Ruby >= 2.1 maybe required at some point. If somewhere in the gems dependency chain,
Ruby 2.1 is set as a required package, you could use
[Ruby Ansible role](https://galaxy.ansible.com/bngsudheer/ruby/). At the moment,
 Redmine works on Ruby 2.0.

Role Variables
--------------

These variables are available with the following default values:

| Variable | Default Value | Description | Required? |
|----------|---------------|---------|-----------|
| redmine_version |  3.4.5 | Redmine version | No |
| redmine_sql_driver | mysql2 | Database driver. Valid choice is either *mysql2* or *postgresql* | Yes |
| redmine_sql_username |redmine| MySQL or PostgreSQL username| No |
| redmine_sql_password | localhost | Datagase server password| No |
| redmine_sql_database_name | redmine| Database name | No |
| redmine_sql_database_host | localhost| Database hostname | No |
| redmine_unicorn_worker_processes | 2 | Number of Unicorn worker processes | No |
| redmine_domain_name| redmine.example.com | domain name to use in Nginx | No |  
| redmine_configure_nginx | yes | Whether to configure Nginx | No |
| redmine_nginx_config_template| plain | Name of the Nginx template to use. Choice must be one of *plain*, *tls*, *custom*  | Yes |
| redmine_nginx_custom_config_path | | Path to your Nginx custom configuration template file | No |
| redmine_configure_unicorn | yes | Whether to configure Unicorn | No |
| redmine_unicorn_port| 5000 | Port number on which Unicorn serves | No |
| redmine_configure_firewalld | yes | Whether to configure Firewalld | No|
| redmine_nginx_bind_ip | (Empty string) |  IP address to bind Nginx to | No | |
| redmine_plugins| [] | List of Redmine plugins to install. Each item in the list is a dictionary with keys *name*, *base_name* and *url*. The *base_name* is the directory name that will be used in the plugins directory. *name* is for human reference. *url* is the location from where the plugin has to be downloaded.| No |
| redmine_configure_selinux| no | Whether to configure Redmine to support SELinux | No |
| redmine_bundler_version| 1.16.1 | Bunder version. If you use a recent version, you will probably require Ruby >= 2.1 | No |
| redmine_additional_configuration | false | In addition to database configuration, setup Redmine configuration | No |
| redmine_enable_smtp_email | false | Enable SMTP email | No |
| redmine_smtp_settings_address | localhost | SMTP server hostname | No |
| redmine_smtp_settings_port | 25 | SMTP port | No |
| redmine_smtp_settings_authentication |  plain | SMTP authentication method. Valid choices are *plain* and *login* | No |
| redmine_smtp_settings_domain | redmine.example.com | SMTP domain name | No |
| redmine_smtp_settings_user_name | | SMTP authentication username | No |
| redmine_smtp_settings_password | | SMTP authentication password | No |
| redmine_smtp_settings_enable_starttls_auto | false | Use TLS in SMTP | No |

Dependencies
------------

- [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/)

If you need a recent version of Ruby use:
- [Ruby](https://galaxy.ansible.com/bngsudheer/ruby/)

Example playbook

```yml
    - hosts: servers
      vars:
       - centos_base_enable_epel: true
       - centos_base_basic_packages: true
       - redmine_sql_username: redmine
       - redmine_sql_password: password
       - redmine_sql_database_name: redmine
       - remmine_sql_database_host: localhost
       - redmine_version: 3.4.2
       - redmine_nginx_bind_ip: 192.168.100.130
       - redmine_configure_selinux: yes
      remote_user: root
      roles:
         - bngsudheer.centos_base
         - bngsudheer.redmine
```

 Example playbook to install Redmine with plugins
```yml
     - hosts: servers
       vars:
        - centos_base_enable_epel: true
        - centos_base_basic_packages: true
        - redmine_sql_username: redmine
        - redmine_sql_password: password
        - redmine_sql_database_name: redmine
        - remmine_sql_database_host: localhost
        - redmine_version: 3.4.2
        - redmine_nginx_bind_ip: 192.168.100.130
        - redmine_configure_selinux: yes
        - redmine_plugins:
          - name: scrum
            base_name: scrum
            url: https://redmine.ociotec.com/attachments/download/481/scrum-v0.18.1.tar.gz
       remote_user: root
       roles:
          - bngsudheer.centos_base
          - bngsudheer.redmine
```


License
-------

BSD

Developement
------------
To run molecule tests locally, you might want to set the ANSIBLE_ROLES_PATH
  variable.
```sh
export ANSIBLE_ROLES_PATH=/path/to/ansible-role-redmine/molecule/default/roles
```

Author Information
------------------

Sudheer Satyanarayana
* Blog: https://www.techchorus.net
* Twitter: https://www.twitter.com/bngsudheer
* Work: https://www.gavika.com
