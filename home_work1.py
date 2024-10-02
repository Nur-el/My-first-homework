monday = float(input("введите расход за пониделник:"))
tuesday = float(input("введите расход за вторник:"))
wednesday = float(input("введите расход за среда:"))
thursday = float(input("введите расход за четверг:"))
friday = float(input("введите расход за пятница:"))
saturday = float(input("введите расход за субота:"))
sunday = float(input("введите расход за воскресение:"))


summ = monday + tuesday + wednesday + thursday + friday + saturday + sunday

print(f'общяя сумма расходов: {summ}')


average = summ / 7
average_round = round(average, 1)
print(f'Средний расход состовляет: {average_round}')


