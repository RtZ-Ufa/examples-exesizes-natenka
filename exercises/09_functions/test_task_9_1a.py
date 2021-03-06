import pytest
import task_9_1a
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_function_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_9_1a, "generate_access_config")


def test_function_params():
    """
    Checking names and number of parameters
    """
    check_function_params(
        function=task_9_1a.generate_access_config,
        param_count=3,
        param_names=["intf_vlan_mapping", "access_template", "psecurity"],
    )


def test_function_return_value():
    """
    Function check
    """
    template_psecurity = [
        "switchport port-security maximum 2",
        "switchport port-security violation restrict",
        "switchport port-security",
    ]
    access_vlans_mapping = {
        "FastEthernet0/12": 10,
        "FastEthernet0/14": 11,
        "FastEthernet0/16": 17,
    }
    template_access_mode = [
        "switchport mode access",
        "switchport access vlan",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ]
    correct_return_value_without_psecurity = [
        "interface FastEthernet0/12",
        "switchport mode access",
        "switchport access vlan 10",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
        "interface FastEthernet0/14",
        "switchport mode access",
        "switchport access vlan 11",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
        "interface FastEthernet0/16",
        "switchport mode access",
        "switchport access vlan 17",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ]
    correct_return_value_with_psecurity = [
        "interface FastEthernet0/12",
        "switchport mode access",
        "switchport access vlan 10",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
        "switchport port-security maximum 2",
        "switchport port-security violation restrict",
        "switchport port-security",
        "interface FastEthernet0/14",
        "switchport mode access",
        "switchport access vlan 11",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
        "switchport port-security maximum 2",
        "switchport port-security violation restrict",
        "switchport port-security",
        "interface FastEthernet0/16",
        "switchport mode access",
        "switchport access vlan 17",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
        "switchport port-security maximum 2",
        "switchport port-security violation restrict",
        "switchport port-security",
    ]

    return_value = task_9_1a.generate_access_config(
        access_vlans_mapping, template_access_mode
    )
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == list
    ), f"The function should return a list, instead it returns a {type(return_value).__name__}"
    assert (
        return_value == correct_return_value_without_psecurity
    ), "The function returns an incorrect value when called with psecurity == None"
    return_value_with_psecurity = task_9_1a.generate_access_config(
        access_vlans_mapping, template_access_mode, template_psecurity
    )
    assert (
        return_value_with_psecurity == correct_return_value_with_psecurity
    ), "The function returns an incorrect value when called with psecurity"
