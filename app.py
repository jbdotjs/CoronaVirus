import requests

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "Replace this text with your RapidAPI key"
    }

print("Welcome to the Covid-19 Statistics Checker!!!\n")

exit=''

while exit!='n':

	country=str(input("\n Enter country's name: "))
	querystring = {"country":f"{country}"}


	response = requests.request("GET", url, headers=headers, params=querystring)
	data=response.json()

	if data['statusCode']==200:

		lastchecked=data['data']["lastChecked"]
		stats=data['data']["covid19Stats"]
		country=stats[0]["country"]
		confirmed=stats[0]["confirmed"]
		deaths=stats[0]["deaths"]
		recovered=stats[0]["recovered"]

		print(f"Last Checked: {lastchecked}")
		print(f"Country: {country}\n")
		print(f"Confirmed Cases: {confirmed}\n")
		print(f"Deaths: {deaths}\n")
		print(f"Recovered: {recovered}")

		exit=input("\n Do you want to perform another search? (y/n): ").lower()

	else:
		pass
