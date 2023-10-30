tiket_total = int(input("Введите количество билетов к приобретению: "))
print(tiket_total)
count = 0
for i in range(tiket_total):
    age = int(input(f"Введите возраст посетителя для {i+1} билета: "))
    if age >= 25:
        count+=1390
    elif age >= 18:
        count+=990
    else:
        count+=0
if tiket_total > 3:
    print("Стоимость Ваших билетов составляет ", count*0.9)
else:
    print(count)