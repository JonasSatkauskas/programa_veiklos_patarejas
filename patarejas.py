"""Ši programa patars ką veikti kai nėra ką veikti.
Bus galima pasirinkti iš atitinkamų kategorijų kurios turės veiklas"""

import random
import time

# VEIKLU IR KATEGORIJU DICTIONARIES

# SIS SARASAS VISADA BUS RODOMAS PIRMAS

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

# LOGIKA

print('''SVEIKI SVEIKI, PATARSIME KA VEIKTI KAI NERA KA VEIKTI''')
time.sleep(1.5)
input('SPAUSKITE ENTER, KAD ISSIRINKTUMETE IS KATEGORIJU')

z = 1
for i in main_kategorijos.values():
    print(f'{z}. {i}')
    time.sleep(0.2)
    z += 1

