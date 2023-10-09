sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Zadej kód součástky: ")

if kod_soucastky in sklad:
    pocet_kusu = int(input(f"Zadej množství: "))

    if pocet_kusu <= sklad[kod_soucastky]:
        
        print(f"Poptávku lze uspokojit v plné výši")
        sklad[kod_soucastky] -= pocet_kusu
    else:
        print(f"Lze prodat pouze omezené množství kusů")
        del sklad[kod_soucastky]
else:
    print("Součástka není skladem.")



    