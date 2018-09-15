import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_postgresql_devel_is_installed(host):
    package = host.package("postgresql-devel")
    assert package.is_installed


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
