from netmiko import ConnectHandler
from getpass import getpass

cisco1 = { 
    "device_type": "cisco_ios",
    "host": "172.16.9.7",
    "username": "cisco",
    "password": getpass(),
    "secret": "cisco"
}
connection = ConnectHandler(**cisco1)
connection.enable()

commands = ['vlan 50', 'name testjv', 'exit']
connection.send_config_set(commands)

print('Uitgevoerd')
connection.disconnect()