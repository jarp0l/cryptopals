"""This script scrapes the frequency data of English letters from the wikipedia article 'Letter frequency'.
"""

import json
import requests
import string
import pandas as pd

URI = "https://en.wikipedia.org/wiki/Letter_frequency"
lwrcase_letters = string.ascii_lowercase
frequency_dict = {}

response = requests.get(URI)

pd_list = pd.read_html(response.text)
df_list = pd_list[3]
df_dict = df_list.to_dict()

letters = df_dict["Letter"]
frequencies = df_dict["English"]

for i in range(len(letters)):
    if letters[i] in lwrcase_letters:
        frequency_dict[letters[i]] = frequencies[i].replace("%", "")

with open("letter_frequency.json", "w") as f:
    json.dump(frequency_dict, f, indent=4)
