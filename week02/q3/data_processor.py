import csv
import re

def process_and_save(user_data: list):
    new_list = []
    pattern = re.compile(r'^4\d*$')

    for i in user_data:
        postal_code = str(i['address']['zipcode'])
        if pattern.match(postal_code):
            new_list.append({
                "name": i["name"],
                "email": i["email"],
                "address": i["address"]["zipcode"],
            })
    with open("data.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email","address"])
        writer.writeheader()
        writer.writerows(new_list)

    with open("data.csv", "r", encoding="utf-8") as f:
        print(f.read())





"""
user_data = [
    {
    "name": "fatemeh",
    "email": "fatemehsadat1380@gmail.com",
    "company_name": "abc",
    "postal_code": 912345,
    "phone_number": 9834567899
    },
    {
        "name": "zahra",
        "email": "abc@gmail.com",
        "company_name": "abc",
        "postal_code": 25863,
        "phone_number": 8765432101
    },
    {
        "name": "sara",
        "email": "def@gmail.com",
        "company_name": "sdf",
        "postal_code": 987452,
        "phone_number": 9182346724
    }
]"""



