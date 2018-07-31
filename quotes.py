import requests

api_url = 'http://quotes.rest/qod.json?category=life'
api_quote = requests.get(url=api_url)


def get_quote():
	quote_dict = api_quote.json()
	quote_text = quote_dict['contents']['quotes'][0]['quote']
	return quote_text
