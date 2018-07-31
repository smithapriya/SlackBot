import requests

api_url = 'https://icanhazdadjoke.com/slack'
api_joke = requests.get(url=api_url)


def get_joke():
	joke_dict = api_joke.json()
	joke_text = joke_dict['attachments'][0]['fallback']
	return joke_text



