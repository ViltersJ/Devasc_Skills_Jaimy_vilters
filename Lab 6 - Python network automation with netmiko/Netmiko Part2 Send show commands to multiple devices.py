from netmiko import ConnectHandler
from getpass import getpass

cisco1 = { 
    "device_type": "cisco_ios",
    "host": "172.16.9.7",
    "username": "cisco",
    "password": getpass()
}
cisco2 = { 
    "device_type": "cisco_ios",
    "host": "172.16.9.4",
    "username": "cisco",
    "password": getpass()
}
devices = [cisco1, cisco2]
commands = ["show ip int brief","showint desc"]
for device in devices:
    net_connect = ConnectHandler(**device)
    for command in commands:
        output = net_connect.send_command(command)
        print(output)

    net_connect.disconnect()