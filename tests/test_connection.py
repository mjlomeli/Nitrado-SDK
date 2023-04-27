"""
Tests Nitrado connections. If any fail, then this means any of the following:
    - something is wrong with Nitrado
    - the URLs are no longer valid
    - responses from Nitrado has changed
"""
from nitrado import Global
from nitrado.lib import Client




def test_health_check():
    health = Global.health_check()
    error_message = f"Nitrado's API is down or the url is invalid."
    assert health.success, error_message


def test_maintenance():
    maintenance = Global.maintenance_status()
    error_message = f"Nitrado's API is down or the url is invalid."
    assert maintenance.dns_backend is not None, error_message
    assert maintenance.cloud_backend is not None, error_message
    assert maintenance.domain_backend is not None, error_message


def test_version():
    version = Global.version()
    error_message = f"Nitrado's API is down or the url is invalid."
    assert version is not None, error_message

