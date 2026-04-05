import requests
from datetime import datetime

# ----------- TASK 1: FILE WORK ----------- #

def manage_notes():
    file_name = "python_notes.txt"

    # writing basic topics (simple file handling practice)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
        f.write("Topic 2: Lists are ordered and mutable.\n")
        f.write("Topic 3: Dictionaries store key-value pairs.\n")
        f.write("Topic 4: Loops automate repetitive tasks.\n")
        f.write("Topic 5: Exception handling prevents crashes.\n")

    print("Notes likh diye bhai 👍")

    # adding few more lines
    with open(file_name, "a", encoding="utf-8") as f:
        f.write("Topic 6: APIs let us fetch real world data.\n")
        f.write("Topic 7: Logging helps track issues.\n")

    print("Thoda aur content add kar diya")

    # reading back
    with open(file_name, "r", encoding="utf-8") as f:
        all_lines = f.readlines()

    print("\nReading file:\n")
    for i, line in enumerate(all_lines, 1):
        print(f"{i}. {line.strip()}")

    print(f"\nTotal lines: {len(all_lines)}")

    # search feature
    word = input("\nKuch search karna hai?: ").lower()
    found = False

    for line in all_lines:
        if word in line.lower():
            print("Mil gaya ->", line.strip())
            found = True

    if not found:
        print("Kuch nahi mila 😅")


# ----------- TASK 2: API ----------- #

BASE = "https://dummyjson.com/products"

def get_products():
    try:
        res = requests.get(f"{BASE}?limit=20", timeout=5)

        if res.status_code == 200:
            data = res.json()["products"]

            print("\nProducts list:\n")
            for p in data:
                print(f"{p['id']} | {p['title']} | {p['price']} | {p['rating']}")

            return data
        else:
            print("Data fetch nahi hua")

    except requests.exceptions.ConnectionError:
        print("Internet problem bro")
    except requests.exceptions.Timeout:
        print("Timeout ho gaya")
    except Exception as e:
        print("Unexpected:", e)

    return []


def filter_sort(products):
    result = []

    for item in products:
        if item["rating"] >= 4