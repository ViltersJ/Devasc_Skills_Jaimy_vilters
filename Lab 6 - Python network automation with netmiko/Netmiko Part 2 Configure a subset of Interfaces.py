from netmiko import ConnectHandler
from getpass import getpass

cisco1 = { 
    "device_type": "cisco_ios",
    "host": "172.16.9.7",
    "username": "cisco",
    "password": getpass(),
    "secret": "cisco"
}
cisco2 = { 
    "device_type": "cisco_ios",
    "host": "172.16.9.4",
    "username": "cisco",
    "password": getpass(),
    "secret": "cisco"
}
devices = [cisco1, cisco2]

interfaces = ['GigabitEthernet0/0', 'GigabitEthernet0/1']

config_commands = [
    'interface ' + intf for intf in interfaces
] + [
    'ip address 172.168.8.4 255.255.255.0',
    'no shutdown'
]

for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()  # Enter enable mode (if applicable)
    output = connection.send_config_set(config_commands)
    print(output)
    connection.disconnect()