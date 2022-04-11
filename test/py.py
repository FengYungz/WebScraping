from time import sleep
import requests

page = requests.get("https://sorteia-quiz.vercel.app/")

sleep(10)

print(page.content)