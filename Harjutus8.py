#Gabriel 24.10.24
#Ülesanne 8


#Loendid ja sõnastikud
"""
telefonid={
'Mari': '5957503',
'Toomas': '5719979',
'Kertu': '5201750',
'Siim': '5580027',
'Piret': '5960799',
'Jaan': '5160415',
'Lea': '5760164',
'Mart': '5337951',
'Anni': '5004818',
'Tõnu': '5721873',
'Kai': '5811884',
'Rasmus': '5859489',
'Eva': '5039393',
'Oskar': '5635812',
'Liina': '5696114',
'Peeter': '5560756',
'Sandra': '5257415',
'Heiki': '5207248',
'Kristi': '5703338',
'Urmas': '5400549'
}
print(telefonid["Rasmus"])
telefonid["Gabriel"] = "5555555"
telefonid.pop("Kristi")
telefonid["Eva"] = "5555555"
print(telefonid)

valik=input("Otsi kontakti: ")
try:
    print(f"{valik} telefoninumber on: {telefonid[valik]}")
except:
    print(f"{valik} tel.nr pole")
"""
#Ladu
tooted = {

'piim': {'kogus': 20, 'hind': 1.19},
'küpsised': {'kogus': 20, 'hind': 4.99},
'või': {'kogus': 20, 'hind': 2.29},
'juust': {'kogus': 15, 'hind': 1.9},
'leib': {'kogus': 15, 'hind': 2.59},
'jogurt': {'kogus': 18, 'hind': 3.65},
'õunad': {'kogus': 35, 'hind': 3.15},
'apelsinid': {'kogus': 40, 'hind': 0.99},
'banaanid': {'kogus': 23, 'hind': 1.29}
}
toode = "piim"
toote_kogus = 10

if toode in tooted:
    if toote_kogus <= tooted[toode]["kogus"]:
        print("------------Arve------------")
        print(f"Toode; {toode}")
        print(f"Hind; {tooted[toode]['hind']} $")
        print(f"Kogus; {toote_kogus} tk")
        print(f"Summa; {round(toote_kogus * tooted[toode]['hind'],2)}$")
        print("------------AITÄH------------")
        tooted[toode]["kogus"] = tooted[toode]["kogus"] - toote_kogus
    else:
        print(f"Soovitud kogust pole. Meil on pakkuda {tooted[toode]['kogus']} tk")

else:
    print("ei ole")



#print(tooted["õunad"])
#print(tooted["õunad"]["hind"])
print(tooted)

      