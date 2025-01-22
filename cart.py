# Ühenda andmetega
# Kasutaja sisestab otsitava
# Kuvab otsitavad põhiandmed (2-3tk)

import json


with open('carts.json', 'r', encoding='utf-8') as file:
    carts = json.load(file)

print(carts)


