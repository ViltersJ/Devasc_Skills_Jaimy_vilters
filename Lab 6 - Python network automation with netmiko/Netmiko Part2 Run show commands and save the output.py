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

show_commands = ["show interface desc", "show ip interface brief"]
for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()

    print(f"Device: {device['host']}")
    for command in show_commands:
        output = connection.send_command(command)
        print(output)
        print()

        
        filename = f"{device['host']}_output.txt"
        with open(filename, "a") as file:
            file.write(output)
            file.write("\n")

    connection.disconnect()