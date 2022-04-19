import time
from drawing import draw_numbers

name = input('Jak masz na imie? ')
print(f'Witaj {name}')
time.sleep(1)
print('Wypisz swoich 6 szczęsliwych cyfr od 1 do 49')
my_numbers = set()
LOOP = 1

while len(my_numbers) <= 5:
    my_numbers.add(int(input(f'Wpisz numerek {LOOP}:   ')))
    LOOP += 1

print(f'Twoje numery to {my_numbers}')

print('---' * 30)
print('Następuje losowanie liczb')
print('---' * 30)
time.sleep(1)

losowane_liczby = {}
NR_LOSOWANIA = 0
t_start = time.process_time()
while my_numbers != losowane_liczby:
    losowane_liczby = draw_numbers()
    NR_LOSOWANIA += 1

t_end = time.process_time()

KOSZT = NR_LOSOWANIA * 3
print(name)
print(f'Wygrałeś w {NR_LOSOWANIA:,} losowaniu')
print(f'Twoje liczby to: {my_numbers}')
print(f'Całkowity koszt zakładów: {KOSZT:,} PLN')
print(f'Ilość tygodni: {NR_LOSOWANIA / 4:,}')
print(f'Ilość lat: {int(NR_LOSOWANIA / 4 / 12):,}')
print(f'Czas wykonania obliczeń: {t_end - t_start}')
