bill_thickness = 0.11 * 0.001 # Meter (0.11 mm)
sears_height = 442 # Höhe (Meter)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Anzahl der Tage', day)
print('Anzahl der Geldscheine', num_bills)
print('Endhöhe', num_bills * bill_thickness)
