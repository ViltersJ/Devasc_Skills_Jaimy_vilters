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

for device in devices:
    connection = ConnectHandler(**device)
    print(f"Connected to {device['host']}")
    
    connection.enable()
    output = connection.send_command("show run | include hostname")
    hostname = output.split()[1]
    
    output = connection.send_command("show running-config")

    filename = f"{hostname}_config.txt"
    with open(filename, "w") as file:
        file.write(output)
    print(f"Configuration backup for {device['host']} saved as {filename}")

    connection.disconnect()
    print(f"Disconnected from {device['host']}")

