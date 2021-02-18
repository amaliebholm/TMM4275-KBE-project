import requests

#the required first parameter of the 'get' method is the 'url':
url = 'http://127.0.0.1:4321/setSize'
x = requests.post(url, data = 'a=1111&b=1234&c=1500&d=1600')

#print the response text (the content of the requested file):
print(x.text)
