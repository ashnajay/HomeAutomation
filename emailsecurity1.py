# Import necessary elements
import time
import smtplib
import MySQLdb as db

from email.mime.text import MIMEText

# Connect to database (credentials censored)
mycon=db.connect(host="localhost",user="*****",passwd="*******",db="HomeAutoMation")
cursor=mycon.cursor()

# Execute query (below line is actual query used but to ensure there is at least one result, the uncommented query uses a fixed time)
# cursor.execute("select LogDetails from SecurityLogs where LogDetails like '%Door OPENED% and LogTime>DATE_ADD(NOW(), interval -1 minute")
cursor.execute("select LogDetails from SecurityLogs where LogDetails like '%Door OPENED%' and LogTime='2022-02-10 06:57:46'")
data=cursor.fetchall()
count=cursor.rowcount

# Loop through each row in resulting table
for row in data:
        door=row[0]
        doorname=door[3:-7]

        sql = "select Location from Door where DoorName='" + doorname + "'" # Query for getting door locations
        cursor.execute(sql)
        dataDoors=cursor.fetchall()

        # Create message that consists of door location
        for rowDoors in dataDoors:
                message=rowDoors[0]

        # Set up mail transfer protocol
        smtpserver=smtplib.SMTP('smtp.gmail.com',587)
        smtpserver.starttls()

        # Input email credentials
        smtpserver.login("yourEmail@gmail.com","yourPassword")

        # Generate email content
        pMsg="The " + message + " Has Been Opened"
        emailmsg = MIMEText(pMsg)
        emailmsg['Subject'] = 'Alert!!'
        emailmsg['From'] = 'yourEmail@gmail.com'
        emailmsg['To'] = 'yourEmail@gmail.com'

        # Send email
        smtpserver.sendmail('yourEmail@gmail.com','yourEmail@gmail.com',emailmsg.as_string())
