import requests

questions = {"q1": "What is your favorite color?", "q2": "What is the unladen airspeed of a swallow?", "label": 0}

# URL = "http://ec2-18-117-121-240.us-east-2.compute.amazonaws.com:5555/add"
URL = "http://192.168.1.37:5555/predict"
# sending get request and saving the response as response object 
r = requests.post(url=URL, json=questions)
print(r.json())