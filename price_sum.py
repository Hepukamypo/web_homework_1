import csv

adult_sum = 0
pensioner_sum = 0
child_sum = 0

with open('products.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем заголовок

    for row in reader:
        adult_sum+=float(row[1])
        pensioner_sum+=float(row[2])
        child_sum+=float(row[3])

print(f'{adult_sum:.2f} {pensioner_sum:.2f} {child_sum:.2f}')