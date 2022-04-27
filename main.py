import random
from tkinter import *
import pip._vendor.requests as requests
from PIL import Image, ImageTk
from io import BytesIO
from quiz_interface import QuizInterface

# getting countries, their names and codes
api_url = "https://api.first.org/data/v1/countries"
response = requests.get(api_url)
api = response.json()
data = api["data"]
countries = []
for item in data:
    name = data[item]["country"]
    if "(" in name:
        name = name[:name.index("(")]
    countries.append({item.lower(): name})

# creating quiz interface

random.shuffle(countries)

questions = countries[:10]
codes = []
answers = []
choices = []
for question in questions:
    key = list(question.keys())
    value = list(question.values())
    codes.append(key[0])
    answers.append(value[0])
    num1 = random.randint(10, len(countries)-1)
    num2 = random.randint(10, len(countries)-1)
    while num1 == num2:
        num1 = random.randint(10, len(countries))
    choice = []
    choice.append(value[0])
    value1 = list(countries[num1].values())
    value2 = list(countries[num2].values())
    choice.append(value1[0])
    choice.append(value2[0])
    choices.append(choice)

quiz_interface = QuizInterface(codes, answers, choices)

