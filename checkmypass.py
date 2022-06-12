import requests #this module allows making a request.

url = 'https://api.pwnedpasswords.com/range/' '+password' 
res = requests.get(url)
print(res)
