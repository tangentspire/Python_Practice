import itertools
import operator
import csv

# Note SECOND CHOICE IN RANK IS DEPENDENT ON FIRST CHOICE, CANNOT HAVE TOP1 = 5
# and TOP2 = 1 need to create logic to create the list only if the second rank
# is equal or less than the first rank
Top_1 = list(range(1, 6))
Top_2 = list(range(1, 6))
Mid_1 = list(range(6, 16))
Mid_2 = list(range(6, 16))
Bot_1 = list(range(16, 31))
Bot_2 = list(range(16, 31))

Combos = itertools.product(Top_1, Top_2, Mid_1, Mid_2, Bot_1, Bot_2)



with open('Combos.csv', 'w') as out:
        csv_out = csv.writer(out)
       # csv_out.writerow(['Combo'])
        for row in Combos:
            csv_out.writerow(row)

