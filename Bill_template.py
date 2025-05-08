name = "Anush"
phone = "9182"
date = "19"
time = "9"

bill = f"""
================================================================
                      TAX INVOICE
                      -----------

                   POKHARA COSMETICS
                  Matepani-12, Pokhara
                  -------------------

Date: {date}                           Time: {time}
Name: Anush Gurung                     Phone: 98111111
================================================================
"""

header = """
================================================================
|  SN  |        Name        | Free Items | Qty  | Rate | Total |
================================================================
"""

item_template = """\
|  {sn:^3} | {name:<18} |    {free:^6} | {qty:^4} | {rate:^4} | {total:^6} |
-----------------------------------------------------------------
"""

print(bill)
print(header)

items = [
    {"sn": "1", "name": "Bound Shampoo", "free": "1", "qty": "12", "rate": "12", "total": "100"},
    {"sn": "2", "name": "Hair Conditioner", "free": "0", "qty": "1", "rate": "25", "total": "25"},
    {"sn": "3", "name": "Face Cream", "free": "1", "qty": "2", "rate": "15", "total": "30"}
]

for item in items:
    print(item_template.format(**item))

print("\n" + " " * 40 + "Grand Total: ₹155")
print("\n" + "Thank you for your purchase!".center(64))
print("=" * 64)