# Ühenda andmetega
# Kasutaja sisestab otsitava
# Kuvab otsitavad põhiandmed (2-3tk)



import json
import requests

url = "https://dummyjson.com/carts"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
otsitav = input("Sisesta otsitav toote nimi: ").lower()
results = []
for cart in data['carts']:
    for product in cart['products']:
        if otsitav in product['title'].lower():
            results.append({
                "Title": product['title'],
                "Price": product['price'],
                "Quantity": product['quantity']
            })
            
if results:
    print("\nLeitud tulemused:")
    for result in results[:3]:
        print(f"Toote nimi: {result['Title']}")
        print(f"Hind: {result['Price']} €")
        print(f"Kogus: {result['Quantity']}")
else:
    print("Tulemusi ei leitud.")

