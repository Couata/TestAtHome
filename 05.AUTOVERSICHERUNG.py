#assurence voiture

kw = 0
prix_voiture = 0
kasko = 0
dieb = 0
feuer = 0

#---------------------------------------- variables-------------------------------------------

kw = int(input("\n Was ist die Leistung des Wagens in KW? (max.: 300KW) "))
prix_voiture = int(input("\n Was ist der Katalogwert des Wagens in €? (max.: 60.000€) "))
if kw <= 300 and prix_voiture <= 60000:
    kasko = input("\n Wollen sie ein Kaskoversicherung? Ja oder neim? ")
    dieb = input("\n Wollen sie eine Diebstahlversicherung? Ja oder nein? ")
    feuer = input("\n Wollen sie eine Feuerversicherung? Ja oder nein? ")
else:
    print("Die maximalen Anzahlen wurden nicht respektiert! Versuch nochmal.")
#prix
kwp = 0
kaskop = 0
diebp = 0
feuerp = 0

taxe = 0
prix = 0


#-------------------------------------- calcule ----------------------------------------------

#Hauptpflicht
if kw <= 52:
    kwp = 110 + kw * 7.50
elif 53 <= kw <= 184:
    kwp = 110 + 52 * 7.5 + (kw - 52) * 2.20
else: 
    kwp = 110 + 132 * 2.20 + 52 * 7.50

#Kaskoversicherung
if kasko == "Ja" or "ja":
    kaskop = 50 + prix_voiture * 0.03
else:
    kaskop = 0

#Diebstahlversicherung
if dieb == "Ja" or "ja":
    diebp = prix_voiture * 0.006
else:
    diebp = 0

#Feuer
if feuer == "Ja" or "ja":
    feuerp = prix_voiture * 0.003
else:
    feuerp = 0
    

#Steuern
taxe = kwp * 0.27 + (kaskop + diebp + feuerp) * 0.17
#Prix totale
prix = kwp + kaskop + diebp + feuerp + taxe

#------------------------------------------- affichage ----------------------------------------------
if kw <= 300 and prix_voiture <= 16000:
    print(f"Rechnung: \n\
        ------------------------------------------------------------------\n\
        \t Hauptpflicht          : {round(kwp , 2)}€ \n\
        \t Kaskoversicherung     : {round(kaskop , 2)}€ \n\
        \t Diebstahlversicherung : {round(diebp , 2)} € \n\
        \t Feuerversicherung     : {round(feuerp , 2)}€\n\
        \t Steuern               : {round(taxe , 2)}€ \n\
        -------------------------------------------------------------------\n\
        \t Preis                 : {round(prix , 2)}€")

else:
    None