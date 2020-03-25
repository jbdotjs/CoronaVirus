
import requests 
from datetime import datetime

print("Welcome to the Covid-19 Statistics Checker & Mailer !!!\n")

country=str(input("\n Enter country's name: "))

url = "https://covid-19-data.p.rapidapi.com/country"
headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "enter your xrapid api key here"
    }
querystring = {"format":"json","name":f"{country}"}

url2 = "https://covid-19-data.p.rapidapi.com/totals"

querystring2 = {"format":"json"}

headers2 = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "enter your xrapid api key here"
    }


response = requests.request("GET", url, headers=headers, params=querystring)
data=response.json()

response2 = requests.request("GET", url2, headers=headers2, params=querystring2)
data2=response2.json()

#extracting data from json

if response.status_code==200:

	lastchecked=datetime.now()
	country=data[0]["country"]
	confirmed=data[0]["confirmed"]
	deaths=data[0]["deaths"]
	recovered=data[0]["recovered"]

	print(f"Last Checked: {lastchecked}")
	print(f"Country: {country}\n")
	print(f"Confirmed Cases: {confirmed}\n")
	print(f"Deaths: {deaths}\n")
	print(f"Recovered: {recovered}")


else:
	print('status code of 1st api is not 200')

if response2.status_code==200:
	total_cases=data2[0]['confirmed']
	total_recovered=data2[0]['recovered']
	total_deaths=data2[0]['deaths']

else:
	print('2nd api is not working')


# Sending mail through Simple Mail Transfer Protocol (SMTP) 

import smtplib

gmail_user = "sender@gmail.com"
gmail_password = 'password'


sent_from = "sender@gmail.com"
to = ["receiver1@gmail.com", "receiver2@gmail.com", "receiver3@gmail.com"]


email_text = f"""

Time of checking: {lastchecked}
Country: {country}

Confirmed Cases: {confirmed}

Deaths: {deaths}

Recovered: {recovered}

World Summary: 

Total Cases= {total_cases}
Total Deaths= {total_deaths}
Total Recovered= {total_recovered}

Important: There is currently no vaccine to prevent coronavirus disease (COVID-19). 

You can protect yourself and help prevent spreading the virus to others if you: 

Do: 
1. Wash your hands regularly for 20 seconds, with soap and water or alcohol-based hand rub 
2. Cover your nose and mouth with a disposable tissue or flexed elbow when you cough or sneeze 
3. Avoid close contact (1 meter or 3 feet) with people who are unwell 
4. Stay home and self-isolate from others in the household if you feel unwell 

Don't: 
1. Touch your eyes, nose, or mouth if your hands are not clean

Mild Symptoms:
1. Tummy ache  
2. Eye infections and loss of taste and smell  
3. Brain fog 
4. Fatigue

Source: https://www.thesun.co.uk/news/11240984/4-mild-symptoms-coronavirus-not-ignore/


Stay Safe and Pray for humanity.


Do not reply to this email. Stats provided by JB Talha Khan.

"""

try:
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(gmail_user, gmail_password)
	server.sendmail(sent_from, to, email_text)
	server.close()

	print( 'Email sent!')


except:
	print ('Something went wrong...')
