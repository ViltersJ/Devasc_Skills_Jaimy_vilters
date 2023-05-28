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


config_file = "config.txt"


with open(config_file) as file:
    config_commands = file.read().splitlines()


for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()  
    output = connection.send_config_set(config_commands)
    print(output)
    connection.disconnect()