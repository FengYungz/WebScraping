import requests
session = requests.Session()
print(session.cookies.get_dict())
{}
response = session.get('http://localhost:3000/')
print(session.cookies.get_dict())