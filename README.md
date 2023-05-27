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

## Lab 2 - Explore Rest APIs With API Simulator And Postman 

## Lab 3 - Python Review - Development tools and Classes

## Lab 4 - Network Infrastructure and troubleshooting

#### Task preparation and implementation.

##### 1.	Install, configure and test the network infrastructure based on the network drawing

##### 2.	Proactively determine what is needed to ensure the continuity of the system and network infrastructure

##### 3.	Apply best practices to configuration and network security

##### 4.	Draw up an IP plan and document your solution

##### 5.	Make sure you can backup and restore device configuration from a backup environment

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

## Lab 5 - Software Development and Design Content

## Lab 6 - Python Network automation with netmiko

## Lab 7 - YANG, NETCONFIG and RESTCONFIG
