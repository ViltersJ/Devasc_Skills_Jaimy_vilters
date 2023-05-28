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

commands = ['interface gig 0/1', 'description testjv']

for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()

    output = connection.send_config_set(commands)
    print(output)
    print('uitgevoerd')

    connection.disconnect()