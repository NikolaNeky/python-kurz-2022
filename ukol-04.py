#Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

#Tvůj program bude obsahovat dvě funkce:

#První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. 
#Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
#Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

#Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. 
#Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

#Tipy:

#Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
#Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".

""" 
#ověří, že číslo má správný formát
def funkce_1():
    platne = True
    # nejaky vyraz co overi ze je cislo platne nebo ne
    return platne

#vrati kolik zpráva bude stát
def funkce_2():
    cena = 1
    # nejaky vypocet
    return cena

## Samotny kod a ovlani funkci
# input od uzivatele na telefoni cislo
# podminka
# pokud funkce_1(tel_cislo) vrati True tak uvnitr se zeptat na text a avolad funkce_2(text) pro zjisteni ceny
# pokud nevrati True tak v else muze byt nejaky prin na nespravny format """


#funkce_1
def nine_digit(number):
    nine_digit = len(str(number)) == 9
    return nine_digit


def thirteen_digit(number):
    thirteen_digit = len(str(number)) == 13
    return thirteen_digit

#funkce_2
def funkce_2(message):
    cena = 3
    letters = len(str(message))
    konecna_cena = letters * cena
    return konecna_cena



number = input("Zadej číslo: ")

if nine_digit(number) or thirteen_digit(number):
    Valid = True
    message = input("Text zprávy: ")
    konecna_cena = funkce_2(message)
    print(konecna_cena) #já fakt nevím, co s tím :)...



else:
    Valid = False
    print(F"Toto číslo je nesprávné.")





    


