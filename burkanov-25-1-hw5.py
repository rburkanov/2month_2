data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []

for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)
# print(codes)
# print(designations)

operators = {}

for i in range(0, len(designations)):
    operators[designations[i]] = codes[i]


del operators['Katel']
del operators['Fonex']

operators['O!'] = {'0705', '0700', '0500'}
operators['Megacom'] = {'0550', '0999', '0555'}
operators['Beeline'] = {'0770', '0222', '0777'}

for i in operators:
    print(f'{i} - {operators[i]} ')

