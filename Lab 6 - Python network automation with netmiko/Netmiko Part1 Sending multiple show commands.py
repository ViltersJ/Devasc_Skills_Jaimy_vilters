from netmiko import ConnectHandler
from getpass import getpass

cisco1 = { 
    "device_type": "cisco_ios",
    "host": "172.16.9.7",
    "username": "cisco",
    "password": getpass()
}
command = "show ip int brief"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

command2 = "show ip arp"

with ConnectHandler(**cisco1) as net_connect:
    output2 = net_connect.send_command(command2)

print(output)
print(output2)