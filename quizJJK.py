# Stil 3 spørgsmål om JJk

import sys
print('Er du klar til en quiz om JJK?')

svar = input('>')

if svar == 'ja' or svar == 'Ja':
    print('Ok så lad os komme igang!')
else:
    sys.exit()


print('1. Spørgssmål. Hvilken ny ability fik Gojo Satarou efter han blandet blå og rød sammen i hans limitless technique')

answer_1 = input('>')

if answer_1 == 'Hollow hpurple' or answer_1 == 'hollow purple':
    print('Korrekt!')

else:
    print('Forkert!')

print('2. Spørgsmål. Hvilken cursed ability havde Geto der tillod ham at sluge cursed spirits og dermed få evnen til at kontrollere dem og bruge dem i battle')

answer_2 = input('>')

if answer_2 == 'Cursed manipulation' or answer_2 == 'cursed manipulation':
    print('Korrekt!')

else:
    print('Forkert!')

print('3. Spørgsmål. Hvad var det der gjorde at Toji blev meget stærk, men mistede sin cursed ability? a) Heavenly pact b) Sukuna finger c) Ten shadow technique')

answer_3 = input('>')

if answer_3 == 'a' or answer_3 == 'A':
    print('Korrekt!')

else:
    print('Forkert!')

print('Det var alt for denne quiz, tak for deltagelsen:)')
