import requests
contents = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=44e454e02934405090ff7335164bbd3c")

print (contents.text)