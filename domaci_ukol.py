import requests
import json
import sys

response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10")

#transform to python
data = response.json()

#checking number of facts
print(len(data))

facts = []
number = 1

#creating numbered list of facts
for entry in data:
    fact = entry["text"]
    numbered = f"{number}. {fact}"
    facts.append(numbered)
    number += 1

#creating json file
with open("kocici_fakta.json", mode="w", encoding="utf-8") as output_file:
    json.dump(facts, output_file, ensure_ascii=False, indent=4)

#timeout
try:
    response_fast = requests.get("https://cat-fact.herokuapp.com/facts//random?animal_type=cat&amount=10", timeout = 0.001)
except TimeoutError:
    print("Jsi příliš nedočkavý!") #nevím, proč mi nefunguje ta TimeoutError, ale ošetřila jsem Exception
except Exception as err:
    print(f"Něco se pokazilo: {err}.")