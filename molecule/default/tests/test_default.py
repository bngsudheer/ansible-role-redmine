import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed


def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


def test_firewalld_running_and_enabled(host):
    firewalld = host.service("firewalld")
    assert firewalld.is_running
    assert firewalld.is_enabled


def test_unicorn_is_running(host):
    master = host.process.filter(user='redmine', comm='unicorn_rails')
    for p in master:
        assert 'unicorn' in p


def unicorn_is_listening(host):
    assert host.socket("tcp://5777").is_listening


def test_redmine_running_and_enabled(host):
    redmine = host.service("redmine")
    assert redmine.is_running
    assert redmine.is_enabled


def test_ruby_packages_installed(host):
    for package_name in ['ImageMagick', 'ruby-devel']:
        package = host.package(package_name)
        assert package.is_installed


def test_redmine_user(host):
    assert 'redmine' == host.user("redmine").name


def test_redmine_db_configuration_file(host):
    f = host.file("/srv/redmine/redmine/config/database.yml")
    assert f.exists
    assert f.user == 'redmine'
    assert f.group == 'redmine'


def test_redmine_configuration_file(host):
    f = host.file('/srv/redmine/redmine/config/configuration.yml')

    assert f.exists
    assert f.user == 'redmine'
    assert f.group == 'redmine'
