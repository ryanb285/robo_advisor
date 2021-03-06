import os
from dotenv import load_dotenv
import requests

load_dotenv()

#https://github.com/prof-rossetti/intro-to-python/blob/main/projects/robo-advisor/README.md
#^ link to requirements

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


#this exit is here because the while True loop is breaking
#check to see if we're trying to make conditions false in a true loop, like an idiot

while True:
    symbol = input("Please select a valid ticker: ")
    if len(symbol) > 6:
        print("Not a valid ticker")
    elif not symbol.isalpha():
        print("Not a valid ticker")
    else:
        break

print(symbol)
exit()

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

response = requests.get(request_url)


print(type(response))

exit()

print(response.text)


# we may need to set up a list of valid tickers and do data vlaidation in a while loop like groceries


#will need to handle errors

#will need to convert the string to a nested dictionary 2h11 @ class 7 

