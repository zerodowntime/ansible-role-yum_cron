import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_yumcron_installed(host):
    yumcron = host.package("yum_cron")
    yumcron.is_installed


def test_config_file_daily(host):
    f = host.file('/etc/yum/yum-cron.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('exclude = kernel*')


def test_config_file_hourly(host):
    f = host.file('/etc/yum/yum-cron-hourly.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('exclude = kernel*')


def test_cron_file_daily(host):
    f = host.file('/etc/cron.daily/0yum-daily.cron')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755


def test_cron_file_hourly(host):
    f = host.file('/etc/cron.hourly/0yum-hourly.cron')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755


# def test_config_file_content(host):
#     distribution = host.system_info.distribution
#
#     if distribution == 'centos':
#         filename = '/etc/yumcron.conf'
#     elif distribution == 'ubuntu':
#         filename = '/etc/yumcron/yumcron.conf'
#
#     f = host.file(filename)
#
#     assert f.contains('0.pool.ntp.org')
#
#


def test_yumcron_running_and_enabled(host):
    yum_cron = host.service('yum-cron')

    assert yum_cron.is_running
    assert yum_cron.is_enabled
