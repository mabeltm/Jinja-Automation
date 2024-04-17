"""
Example configuration after jinja2 templates the configuration from port-config.yaml:
int GigabitEthernet 0/0
    description THIS_IS_A_DESCRIPTION
    switchport mode access
    switchport access vlan 100
    switchport voice vlan 1000
    switchport port-security
    device-tracking attach-policy IPDT_MAX_10
    spanning-tree portfast
    no shutdown
"""

from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)

port_config = yaml.safe_load(open("port-config.yaml"))

template = ENV.get_template("jinja-template.j2")

configuration = template.render(port_config)

print(configuration)