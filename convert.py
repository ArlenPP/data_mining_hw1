from commonfunctions import *
file_name = 'BreadBasket_DMS.csv'
rows = read_csv_file(file_name)
converted = []
for i in range(1, len(rows)):
    #print(converted)
    t = int(rows[i][2])
    if t > len(converted):
        converted.append([])
        converted[len(converted)-1].append(rows[i][3])
    else:
        if not rows[i][3] in converted[t-1]:
            converted[t-1].append(rows[i][3])

with open('stocks.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(converted)
