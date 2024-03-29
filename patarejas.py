"""Ši programa patars ką veikti kai nėra ką veikti.
Bus galima pasirinkti iš atitinkamų kategorijų kurios turės veiklas"""

import random
import time

# VEIKLU IR KATEGORIJU DICTIONARIES

main_kategorijos = {
    1: 'Pramogos',
    2: 'Mokslai',
    3: 'Namų ruoša',
    4: 'Sportas',
    5: 'Valgis',
    6: 'Skaitymas (knygos stiliai)',
}

# MAIN KATEGORIJOS NR. 1 SUBKATEGORIJOS

pramogu_kategorijos = {
    1: 'Pasiziurek YouTube',
    2: 'Pasiziurek filma',
    3: 'Paieskok naujos muzikos',
    4: 'Pasivaikščiok',
    5: 'Pavazinek dviraciu'
}

# MAIN KATEGORIJOS NR. 2 SUBKATEGORIJOS

mokslu_kategorijos = {
    1: 'UDEMY',
    2: 'Mokomoji knyga',
    3: 'Gitaros akordai',
    4: 'Dualingo (kalbos mokymasis)',
    5: 'Pasimokyti sudėti rubiko kubą',
}

# MAIN KATEGORIJOS NR. 3 SUBKATEGORIJOS

namu_ruosos_kategorijos = {
    1: 'Išsiurbliuoti namus',
    2: 'Su drėgnu išvalyti grindis',
    3: 'Sutvarkyti seniai tvarkytą spintelę/komodą',
    4: 'Nusivalyti techniką',
    5: 'Placeholder',
}

# MAIN KATEGORIJOS NR. 4 SUBKATEGORIJOS

sporto_kategorijos = {
    1: 'Pavažinėk dviračiu',
    2: "Eik į Gym'ą",
    3: 'Atsispaudimai + atsilenkimai + planking + pritūpimai',
    4: 'Tampymosi pratimai',
    5: 'Placeholder'
}

# MAIN KATEGORIJOS NR. 5 SUBKATEGORIJOS

valgio_kategorijos = {
    1: 'Pasigaminti tai ko paprastai negaminu',
    2: 'Pasidaryti matės',
    3: 'Placeholder',
    4: 'Placeholder',
    5: 'Placeholder',
}

# MAIN KATEGORIJOS NR. 6 SUBKATEGORIJOS
# PAGALVOTI APIE GALIMYBĘ APJUNGTI ŽINIŲ PATARĖJĄ SU

################## IDEA: NESTED DICTIONARIES??? #############################

skaitymo_stiliu_kategorijos = {
    1: 'Skirk 15 min pagrindiniam puslapiui (https://www.15min.lt/)',
    2: 'Programa "Žinių patarėjas" (pasiūlo naujienų temą)',
    3: 'Knyga (rinkis mane ir parodysiu žanrus)',
    4: 'IT websites (https://www.computerworld.com/news/)',
    5: 'Ethical hacking info',
}

skaitymas_knygos = {
    1: 'Psychology',
    2: 'Cryptocurrency',
    3: 'Ethical hacking',
    4: 'Anonimity',
    5: 'Philosophy',
    6: 'Fantasy',
}

# LOGIKA (LOOPAS)

print('''SVEIKI SVEIKI, PATARSIME KA VEIKTI KAI NERA KA VEIKTI''')
time.sleep(1)
input('SPAUSKITE ENTER, KAD PAMATYTUMĖT KATEGORIJAS')
print()

for numeris, veikla in main_kategorijos.items():
    print(f"{numeris}: {veikla}")
    time.sleep(random.uniform(0.1, 0.5))

print()
time.sleep(1.5)
kategorijos_pasirinkimas = input("Įveskite skaičių ir spauskite enter\n")

if int(kategorijos_pasirinkimas) == 1:
    print()
    for numeris, veikla in pramogu_kategorijos.items():
        print(f"{numeris}: {veikla}")
        time.sleep(random.uniform(0.1, 0.5))

    print()
    time.sleep(1)

elif int(kategorijos_pasirinkimas) == 2:
    print()
    for numeris, veikla in mokslu_kategorijos.items():
        print(f"{numeris}: {veikla}")
        time.sleep(random.uniform(0.1, 0.5))

elif int(kategorijos_pasirinkimas) == 3:
    print()
    for numeris, veikla in namu_ruosos_kategorijos.items():
        print(f"{numeris}: {veikla}")
        time.sleep(random.uniform(0.1, 0.5))

elif int(kategorijos_pasirinkimas) == 4:
    print()
    for numeris, veikla in sporto_kategorijos.items():
        print(f"{numeris}: {veikla}")
        time.sleep(random.uniform(0.1, 0.5))

elif int(kategorijos_pasirinkimas) == 5:
    print()
    for numeris, veikla in valgio_kategorijos.items():
        print(f"{numeris}: {veikla}")
        time.sleep(random.uniform(0.1, 0.5))

elif int(kategorijos_pasirinkimas) == 6:
    print()
    for numeris, veikla in skaitymo_stiliu_kategorijos.items():
        print(f"{numeris}: {veikla}")
        time.sleep(random.uniform(0.1, 0.5))

kategorijos_tinkamumas = input("AR NORITE, KAD PROGRAMA ATSITIKTINAI PARINKTŲ VEIKLĄ IŠ ŠIOS KATEGORIJOS?\n"
                               "ĮRAŠYKITE T(TAIP) ARBA N(NE)\n")
