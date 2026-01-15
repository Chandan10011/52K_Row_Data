import csv
import random
import string

ROWS = 5_200_000   # 52 lakh rows (50 lakh se zyada)

first_names = [
    "Rahul","Amit","Neha","Pooja","Rohit","Ankit","Suman","Priya",
    "Deepak","Kiran","Ravi","Nisha","Aakash","Komal","Vikas"
]

last_names = [
    "Sharma","Verma","Singh","Gupta","Kumar","Yadav",
    "Mishra","Patel","Jain","Agarwal","Mehta","Bansal"
]

cities = ["Delhi","Mumbai","Pune","Bangalore","Chennai","Kolkata","Jaipur"]
products = ["Laptop","Mouse","Keyboard","Monitor","Mobile","Tablet"]

with open("power_query_50_lakh_plus.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # Header
    writer.writerow([
        "ID","First_Name","Last_Name","Full_Name",
        "City","Product","Quantity","Price","Remarks"
    ])

    for i in range(1, ROWS + 1):
        fn = random.choice(first_names)
        ln = random.choice(last_names)
        full = fn + " " + ln
        city = random.choice(cities)
        product = random.choice(products)
        qty = random.randint(1, 10)
        price = random.randint(500, 75000)

        # Long text → file size badhe
        remarks = ''.join(random.choices(string.ascii_letters + string.digits, k=60))

        writer.writerow([i, fn, ln, full, city, product, qty, price, remarks])

print("50 Lakh+ rows CSV file created successfully")
