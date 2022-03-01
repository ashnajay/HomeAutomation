# HomeAutomation

## About

This is a program that uses output from ESP32 chips and MQTT protocols to log when doors
in a home are opened into a MYSQL database containing door codes and locations.

The program accesses the data within this database through the use of SQL queries and
parses the results of these queries, ultimately sending an email message to the homeowner,
alerting them of any doors that have been opened within a certain timeframe using the simple
mail transfer protocol.

A easily readable version of this program is provided in this repository, but in order to actually
execute the program, please follow the instructions below.

## To Run

In order to run this program, you must first install the terminal emulator, PuTTy. Once this is
properly installed, you must enter the following into the Host Name box: `210.18.139.72`

For the username and password needed to execute the program, I will provide you my credentials:
Username: `*****`
Password: `*****`

In addition, please go to your Chrome settings and in the **Security** tab, temporarily enable _Less
secure app access_

In the PuTTy terminal, type `cd ashna` followed by `nano emailsecurity1.py`

Once in the python file, change any instances of `yourEmail` to your email address and any instances
of `yourPassword` to your password. Then, exit the file and type `python emailsecurity1.py` in order
to run the program and check your inbox for results!
