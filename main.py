cislo1= int(input ("zadejte prvni cislo"))
ciselo2= int(input ("zadejte druhy cislo"))

opakovat = "ano"
while opakovat == "ano":
    operace = input ("zadejte cislo co chcete udelat?")

if operace == "scitani":
    vysledek = cislo1 + ciselo2
    print(vysledek)
elif operace == "odcitanii":
    vysledek = cislo1 - ciselo2
    print(vysledek)
elif operace == "nasobeni":
    vysledek = cislo1 * ciselo2
    print(vysledek)
elif operace == "deleni":
    vysledek = cislo1 / ciselo2
    print(vysledek)
