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

def execute_script(device):
    connection = ConnectHandler(**device)
    print(f"Connected to {device['host']}!")
    connection.disconnect()
    print(f"Disconnected from {device['host']}!")

for device in devices:
    execute_script(device)
