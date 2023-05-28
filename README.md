# Devasc_Skills_JV

## Lab 1 - Python Experiments

### 1.1 Install different tools/packages on Ubuntu DEVASC-LABVM
- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE

#### Task preparation and implementation.

##### Python3:
Pre installed in de devasc machine
Update met: 
`sudo apt update`

##### pip:
Install met:
`sudo apt install python3-pip`

##### Visual studio code:
Pre-installed op de Devasc-machine
Python extension downloaden/updaten met de GUI

##### Jupyter:
Install met:
```
pip install jupyterlab
pip install notebook
```

##### Python idle:
Install met:
`sudo apt install idle3`

#### Task Troubleshooting.
Voor fouten te voorkomen zijn deze twee commandos gebruikt.
```
sudo apt update
sudo apt upgrade
```

#### Task Verification.

##### Python3:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%201.png)

##### Pip:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%202.png)

##### Visual studio code:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%203.png)

##### Jupyter notebook:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%204.png)

##### Python Idle:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%205.png)


### 1.2 Run geopy and timedate Python Scipts on the DEVASC-LABVM using the tools above (1.1):

#### Task preparation and implementation.

download python scripts van de volgende link:
https://github.com/wleppens/PythonExperiments/tree/main/mixed
- timedate.py
- geopy-geocoders_location.py
- location.py

##### timedate.py:
commando voor repositories en dependencies:
`pip install datetime`

##### geopy-geocoders_location.py:
commando's voor repositories en dependencies:
```
pip install geopy
pip install folium
pip install nominatim
```
##### location.py:
Dezelfde dependencies als vorig script

#### Task Troubleshooting.
/

#### Task Verification.

##### timedate.py:
script:
![import-datetime.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/import-datetime.py)

##### Visual studio code:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%206.png)

##### Python3:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%207.png)

##### Python idle:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%208.png)

##### Jupyter:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%209.png)

##### geopy-geocoders_location.py:
script:
![geopy-geocoders_location.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Geopy-geocoders_location.py)

##### Visual studio code:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%2010.png)

##### Python3:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%2011.png)

##### Python idle:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%2012.png)

##### Jupyter:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%2013.png)

##### location.py:
script:
![location.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/location.py)

##### Visual studio code:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%2014.png)

##### Python3:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%2015.png)

##### Python idle:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%2016.png)

##### Jupyter:
![Lab 1 Python Experiments](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%201%20-%20Python%20Experiments/Lab%201%20screen%2017.png)

## Lab 2 - Explore Rest APIs With API Simulator And Postman.

### Part 1: Explore API Documentation Using the API Simulator.

#### Task preparation and implementation.
Surf naar: http://library.demo.local/

##### GET /books.
API request voor de lijst van boeken op te halen

##### POST /LoginViaBasic
inloggen voor de rest te kunnen doen

##### POST /books
Deze word gedaan voor een book te adden naar de website.
Verander de value
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%203.png)

##### GET /books/{id}
Een get voor een specifiek boek te opvragen.

##### DELETE /books/{id}
Delete een book uit de lijst.

#### Task Troubleshooting.
/

#### Task Verification.

##### GET /books.
![Lab 2 - Explore rest APIs with API-simulator and postman]([https://github.com/ViltersJ/Devasc_Skills_JV/tree/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%201.png)
curl commando `curl -X GET "http://library.demo.local/api/v1/books" -H "accept: application/json"`
##### POST /LoginViaBasic
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%202.png)
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%204.png)
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%205.png)

##### POST /books
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%206.png)
curl voor 5de boek `curl -X POST "http://library.demo.local/api/v1/books" -H "accept: application/json" -H "X-API-KEY: cisco|Ujk15vEJPGys6ZxkKpDCCnMaKH5L5miN5h1Sh1Qq2B8" -H "Content-Type: application/json" -d "{ \"id\": 5, \"title\": \"31 Days Before Your CCNA Exam\", \"author\": \"Allan Johnson\"}"`

##### GET /books/{id}
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%207.png)
curl `curl -X GET "http://library.demo.local/api/v1/books/4" -H "accept: application/json"`

##### DELETE /books/{id}
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/lab%202%20screen%208.png)
curl `curl -X DELETE "http://library.demo.local/api/v1/books/5" -H "accept: application/json" -H "X-API-KEY: cisco|Ujk15vEJPGys6ZxkKpDCCnMaKH5L5miN5h1Sh1Qq2B8"`


### Part 2: Use Postman to Make API Calls to the API Simulator.

#### Task preparation and implementation.
Open postman en herhaal de stappen hierboven.

##### POST loginviabasic
Vul de authority tab in als volgt.
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2010.png)
Dit geeft alweer de token die nodig is voor de rest te kunnen uitvoeren.

##### POST books
Vul de authorization tab in type API key:
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2012.png)
De code die als input wordt gestuurd verandert iets:
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20Screen%2013.png)

##### GET /books
We kunnen deze ook sorten op auteur als volgt:
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2015.png)

#### Task Troubleshooting.
/

#### Task Verification.

##### GET books
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%209.png)

##### POST loginviabasic
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2011.png)

##### POST books
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2014.png)

##### GET /books
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2016.png)

### Part 3: Use Python to Add 100 Books to the API Simulator.

#### Task preparation and implementation.
Voor dit onderdeel is er een script geschreven.
![add100RandomBooks.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/add100RandomBooks.py)
Voor delen te snappen van dit script zijn er kleine opdrachten uitgevoerd.
Voor faker ziet dit er als volgt uit.
```
python3
from faker import Faker
fake = Faker()
print('My name is {}.'.format(fake.name()))
print('My name is {0} and i wrote {1} ({2})'.format(fake.name(),fake.catch_phrase(),fake.isbn13()))
```
De for loop:
```
for i in range (10):
    print(fake.name())
```
Dit zal 10 namen genereren.
Run het script

#### Task Troubleshooting.
Voor de faker commandos was er een probleem de variabelen moesten gezocht worden.
`fake.`
Als je twee keer tabt krijg je de volgende output:
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2019.png)
Hiervoor zijn:
```
fake.catch_phrase()
fake.isbn13()
fake.name()
```
gebruikt
#### Task Verification.

Faker: 

![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2017.png)

For loop:

![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2018.png)

Script run:

![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2020.png)
![Lab 2 - Explore rest APIs with API-simulator and postman](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Lab%202%20screen%2021.png)


## Lab 3 - Python Review - Development tools and Classes.

### Part 1: Python Programming Review Cisco DEVNET 1.3.3

#### Task preparation and implementation.

Versie verification `python3 -v`

Interpreter: `python3`

Hello world script: 
![script Hello world.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Hello-world.py)

Personal info script:
![Script personalinfo.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/personal-info.py)

If script:
![if-vlan.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/if-vlan.py)

Elif script:
![if-acl.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/if-acl.py)

For script:
![for script](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/for.py)

While script:
![while script](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/while.py)

File-access:
![file-access script](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/file-access.py)

#### Task Troubleshooting.
/
#### Task Verification.

Gebruik de interpreter als calculator:
```
python3
2+3
10-4
2*4
20/5
3**2
```
![Lab 3 - Python review - Development tools and classes](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Lab%203%20screen%201.png)

Hello world:
![Lab 3 - Python review - Development tools and classes](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Lab%203%20screen%202.png)

Types:
```
int
float
str
bool
```

List:
`testlijst=["1", "2", "3"]`

personalinfo script:
![Lab 3 - Python review - Development tools and classes](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Lab%203%20screen%203.png)

if-vlan script:
![Lab 3 - Python review - Development tools and classes](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Lab%203%20screen%204.png)

elif script:
![Lab 3 - Python review - Development tools and classes](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Lab%203%20screen%205.png)

for script:
![Lab 3 - Python review - Development tools and classes](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Lab%203%20screen%206.png)

while script:
![Lab 3 - Python review - Development tools and classes](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Lab%203%20screen%207.png)

file-access script:
![Lab 3 - Python review - Development tools and classes](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/Lab%203%20screen%208.png)

### Part 2: Explore Python Development Tools Cisco DEVNET 3.1.12

#### Task preparation and implementation.
Versie verification: `python3 -v`

Check huidige paketten en de versie ervan installed: 
```
cd /labs/devnet-src/python
python3 -m pip freeze
python3 -m pip freeze | grep requests
```

#### Task Troubleshooting.
/
#### Task Verification.

Starten van een virtual environment packages checken en installen vervolgens envi sluiten:
```
cd /labs/devnet-src/python
source devfun/bin/activate
pip3 freeze
pip3 install requests
pip3 freeze
deactivate
```
Een environment sharen en nieuwe aanmaken aan de hand van de share:
```
cd /labs/devnet-src/python
source devfun/bin/activate
pip3 freeze > requirements.txt
deactivate
```
```
python3 -m venv nieuweenvi
source nieuweenvi/bin/activate
pip3 install -r requirements.txt
pip3 freeze
deactivate
```

### Part 3: Explore Python Classes cisco DEVNET 3.4.6

#### Task preparation and implementation.

definieer een functie.

definieer een class met methods.

#### Task Troubleshooting.
/
#### Task Verification.

functie: !["mycity.py"](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/myCity.py)

method script:!["myLocation.py"](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%203%20-%20Python%20review%20-%20Development%20tools%20and%20classes/myLocation.py)

## Lab 4 - Network Infrastructure and troubleshooting.

#### Task preparation and implementation.

##### 1.	Install, configure and test the network infrastructure based on the network drawing.
![Lab 4 - Network infrastructure and troubleshooting](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/Lab%204%20screen%201.png)

##### 2.	Proactively determine what is needed to ensure the continuity of the system and network infrastructure.
HSRP is geconfigureerd voor redundantie te kunnen opbouwen. Dit voorziet scalability.
Commandos:
```
interface g0/0.10
description Management vlan subinterface
encapsulation dot1q 10
ip address 172.16.9.4 255.255.255.240
standby version 2
standby 10 ip 172.16.9.1
standby 10 priority 150
exit
interface g0/0.40
description Data vlan subinterface
encapsulation dot1q 40
ip address 172.16.9.52 255.255.255.240
standby version 2
standby 40 ip 172.16.9.49
standby 40 priority 150
exit
```

Domain commando: `ip domain name pxl.be`

##### 3.	Apply best practices to configuration and network security.
VLANS best practice segmentatie op switch.
Commandos switch:
```
vlan 10
name "Management Segment Student Rack 09"
exit
vlan 40
name "Data Users Segment Student Rack 09"
exit
vlan 99
name native
exit
```

SSH 2.0.
Commandos:
```
crypto key generate rsa 1024
ip ssh version 2
username cisco password class
```

Alle ongebruikte poorten zijn gesloten met het commando: `no shutdown`.

Op user ports is het commando `switchport port-security mac-address sticky` gebruikt.


##### 4.	Draw up an IP plan and document your solution.

| DEVICE          | INTERFACE   | IP            | VLAN |
|-----------------|-------------|---------------|------|
| LAB-RA09-C-R03  | G0/0.10     | 172.16.9.4    | 10   |
|                 | G0/0.10HSRP | 172.16.9.1    | 10   |
|                 | G0/0.40     | 172.16.9.52   | 40   |
|                 | G0/0.40HSRP | 172.16.9.49   | 40   |
|                 | G0/1        | 10.199.66.109 | /    |
| LAB-RA09-A-SW03 | VLAN10      | 172.16.9.7    | 10   |

##### 5.	Make sure you can backup and restore device configuration from a backup environment.
Router eerst.
Commandos:
```
en
conf t
interface g0/1
ip address 10.199.66.109 255.255.255.224
no shutdown
exit
ip route 0.0.0.0 0.0.0.0 10.199.66.100
copy tftp: running-config
10.199.64.134
lab-ra09-c-r03-confg
interface g0/1
no shutdown
interface g0/0
no shutdown
```
Switch second
Commandos:
```
en
conf t
vlan 10
name "Management Segment Student Rack 09"
exit
interface vlan 10
description "Management Segment Student Rack 09"
ip address 172.16.9.7 255.255.255.240
no shutdown
exit
ip default-gateway 172.16.9.1
interface g0/1
switchport mode trunk
switchport trunk allowed vlan 10
switchport trunk native vlan 99
no shutdown
exit
copy tftp: running-config
10.199.64.134
lab-ra09-c-r03-confg
```

#### Task Troubleshooting.

Probleem 1: We konden niet connecten met de switch van de leerkracht.

Oorzaak: Switchports staan standaard down.

Oplossing: De poort stond op shutdown, opgelost door `no shutdown` in te geven.

Probleem 2: Er kon geen ping of TFTP verzonden worden van de router naar de remote PC.

Oorzaak: origineel was er een routing probleem die het 10.199.66.X netwerk niet door routen.

Oplossing:  Router laten pingen via zijn subinterface dus met gebruik van VLAN ip adres.
Het commando: `ip tftp source-interface gigabitEthernet 0/0.10` 
heeft er voor gezorgd dat wij TFTP altijd vanaf ons Vlan IP adres doen.

Probleem 3: We hadden geen connectivity meer zonder dat er iets veranderd was aan onze configs.

Oorzaak: Iemand had onze kabel uitgetrokken en onze poort gebruikt.

Oplossing: Kabels gevolgd om na te gaan wie onze poort gebruikte, hierna hebben we het opgelost door onze kabel terug in te steken.

Probleem 4: Router configureert automatisch ACLs bij erase & reload.

Oorzaak: Bug door exec-timeout.

Oplossing: Exec timeout uitzetten.

#### Task Verification.
![Router config](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/lab-ra09-c-r03-confg)
![Switch config](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/lab-ra09-a-sw03-confg)

## Lab 5 - Software Development and Design Content

### Part 1: Software Version Control with Git Cisco DEVNET 3.3.11

#### Task preparation and implementation.

##### 1. Check de installatie van git
Commando: `git --version`

##### 2. Initiatie git
Commandos:
```
git config --global user.name "username"
git config --global user.email "email"
cd Devasc-Skills (map waar de repository moet gemaakt worden)
git init
```

##### 3. Staging en committing een file in de repository
Commandos:
```
echo test > test.txt
git add test.txt
git commit -m "message zoals added screenshot"
```

##### 4.	File aanpassen en de verandering tracken.
Commandos:
```
echo "voorbeeld tekst" >> test.txt
git add test.txt
git commit -m "added a line"
```

##### 5.	Branches en merging
Commandos:
```
git branch 'branchname'
git checkout 'branchname'
git merge 'branchname'
got brand -d 'branchname' (delete branch)
```
##### 6.	Integreren van git met GitHub
Commandos:
```
git remode add origin "hyperlink naar online repository"
git push remote origin master
```
na het laatste commando geef je de username van github en personal access token.

#### Task Troubleshooting.

git push werkt niet meer met password.
Hiervoor is nu een Personal Acces token nodig

#### Task Verification.
![Lab 5 - Software development and design content](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/Lab%205%20screen%201.png)
Deze git

### Part 2: Create a Python Unit Test Cisco DEVNET 3.5.7
/

### Part 3: Parse Different Data Types with Python Cisco DEVNET 3.6.6

#### Task preparation and implementation.

##### Parse XML in python.
script:
![parsexml.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/parsexml.py)

##### Parse JSON in python
script:
![parsejson.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/parsejson.py)

##### Parse YAML in python
script:
![parseyaml.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/parseyaml.py)

#### Task Troubleshooting.
/

#### Task Verification.

##### XML
![Lab 5 - Software development and design content](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/Lab%205%20screen%202.png)

##### JSON
![Lab 5 - Software development and design content](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/Lab%205%20screen%203.png)

##### YAML
![Lab 5 - Software development and design content](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/Lab%205%20screen%204.png)

## Lab 6 - Python Network automation with netmiko

### Part 1: connecting to a single iOS device

#### Task preparation and implementation.

Schrijf een script voor single show command.

Schrijf een script voor multiple show commands.

Schrijf een script voor multiple configuration commands to a single device.

#### Task Troubleshooting.

Er was een probleem met authenticatie.
Hier is er voor elk script een nieuwe module gedownload genaamd getpass.

#### Task Verification.

![Single show](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20Part1%20Sending%20single%20show%20command.py)

![Multiple show](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20Part1%20Sending%20multiple%20show%20commands.py)

![Multiple config](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20Part1%20Send%20multiple%20configuration%20commands%20to%20a%20single%20device.py)

### Part 2: Connect to multiple IOS devices.

#### Task preparation and implementation.

Schrijf een send show commands to multiple devices.

Schrijf een send configuration commands to multiple devices.

Schrijf een run show commands and save the output.

Schrijf een backup the device configurations.

Schrijf een configure a subset of Interfaces.

Schrijf een send device configuration using an external file.

Schrijf een connect using a Python Dictionary.

Schrijf een execute a script with a Function or classes.

Schrijf een execute a script with a statements (if, ifelse, else).


#### Task Troubleshooting.

Er was een probleem met authenticatie.
Hier is er voor elk script een nieuwe module gedownload genaamd getpass.

#### Task Verification.

![show naar multiple](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20Part2%20Send%20show%20commands%20to%20multiple%20devices.py)

![config naar multiple](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20Part2%20Send%20configuration%20commands%20to%20multiple%20devices.py)

![run show en save de output](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20Part2%20Run%20show%20commands%20and%20save%20the%20output.py)

![backup device config](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20Part2%20Backup%20the%20device%20configurations.py)

![Configure a subset of Interfaces](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20Part%202%20Configure%20a%20subset%20of%20Interfaces.py)

![Send device configuration using an external file](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20Part%202%20Send%20device%20configuration%20using%20an%20external%20file.py)

![Connect using a Python Dictionary](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20Part%202%20Connect%20using%20a%20Python%20Dictionary.py)

![Execute a script with a Function or classes](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20part%202%20Execute%20a%20script%20with%20a%20Function%20or%20classes.py)

![Execute a script with a statements (if, ifelse, else)](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Netmiko%20part%202%20Execute%20a%20script%20with%20a%20statements%20(if%2C%20ifelse%2C%20else).py)


## Lab 7 - YANG, NETCONFIG and RESTCONFIG

### Part 1: Install the CSR1000v VM Cisco DEVNET 7.0.3

#### Task preparation and implementation.

Download de OVA.

Download de nieuwste ISO.

Mount de ISO in dvd drive 1 van de VM.

Doorga de installatie procedure van de CSR1000v.

#### Task Troubleshooting.

Er was een probleem met de OVA deze kwam niet met een geupdate ISO. Dit is verholpen met een geupdate ISO van de lector.

#### Task Verification.

Ping het IP van de CSR1000v vanaf de DEVASC VM:
`ping 192.168.139.128`

ssh naar de switch vanaf de DEVASC VM:
` ssh cisco@192.168.139.128 `

### Part 2: Explore YANG Models Cisco DEVNET 8.3.5

#### Task preparation and implementation.

`wget de raw ietf-interfaces.yang` van github

Ga u installatie van pyang na met: `pyang -v`
Of install het met: `pip3 install pyang --upgrade`

#### Task Troubleshooting.

/

#### Task Verification.

!["script ietf-interface.yang"](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/ietf-interfaces.yang)

### Part 3: Use NETCONF to Access an IOS XE Device cisco DEVNET 8.3.6

#### Task preparation and implementation.

Verifieer connectie door ping van DEVASC naar CSR1000v VM.
`ssh cisco@192.168.139.128`

`show platform software yang-management process` als verificatie of de netconfig daemon runt.

Als de daemon niet zou runnen:
```
conf t 
netconf-yang 
```

Open een SSH connectie naar de netconf process zelf met:
`ssh cisco@192.168.139.128 -p 830 -s netconf`

Stuur de volgende XML code naar de VM in de gestarte SSH naar de netconf.

![hello.xml](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/hello.xml)

Voor info over de interfaces kan je de volgende XML Get code sturen.

![get.xml](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/get.xml)

Voor de sessie te eindigen gebruik de volgende xml.

![close.xml](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/close.xml)

Vervolgens is er een python script gemaakt voor requests te sturen en configuratie opdrachten.

#### Task Troubleshooting.

Na de get request zal de VM reageren met een onleesbare string.

Deze onleesbare string is verholpen met pretify xml internet tool kopieer de string op “]]>]]>” na en laat deze in een leesbaar formaat zetten.

#### Task Verification.

Python script: 

![ncclient-netconf.py](https://github.com/ViltersJ/Devasc_Skills_JV/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/ncclient-netconf.py)

### Part 4: Use RESTCONF to Access an IOS XE Device cisco DEVNET 8.3.7

#### Task preparation and implementation.

#### Task Troubleshooting.

#### Task Verification.
