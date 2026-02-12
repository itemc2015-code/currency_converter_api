import requests

url = "https://api.api-ninjas.com/v1/zipcode?zip=90210"
headers = {"X-Api-Key":"ncD8IQIlBbjtBhAw7m8WiJNBwXBmtqCVY0CXggIw"}

result = requests.get(url,headers=headers)

print(result.json())
print(result.status_code)