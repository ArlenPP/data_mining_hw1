from commonfunctions import *
def combination(data, r, start, k, bag, itemsets):
    if(k == r):
        itemsets.append(bag[:])
        return
    for i in range(start, len(data)):
        bag[k] = data[i]
        combination(data, r, i + 1, k + 1, bag, itemsets)
def generate_itemsets(items, num):
    itemsets = []
    combination(items, num, 0, 0, [''] * num, itemsets)
    return itemsets
def exclude(itemsets, target):
    itemsets_exclude = itemsets[:]
    if target == []:
        return itemsets_exclude
    delete_list = []
    for i in range(0, len(itemsets_exclude)):
        for j in range(0, len(target)):
            if set(target[j]).issubset(set(itemsets_exclude[i])):
                delete_list.append(i)
                break
    for index in sorted(delete_list, reverse=True):
        del itemsets_exclude[index]
    return itemsets_exclude
def itemsets_union(itemsets):
    u = set()
    for itemset in itemsets:
        u = u.union(set(itemset))
    return list(u)
file_name = 'data.csv'
threshold = 2
rows = read_csv_file(file_name)
all_items = get_all_items(rows)
exclude_target = []
for i in range(1, len(all_items) + 1):
    #print('i =', i)
    #print('all items =', all_items)
    itemsets_c = generate_itemsets(all_items, i)
    itemsets_c = exclude(itemsets_c, exclude_target)
    #print('C =', itemsets_c)
    num = search_num(itemsets_c, rows)
    itemsets_l = []
    #exclude_target = []
    for j in range(0, len(itemsets_c)):
        if num[j] < threshold:
            exclude_target.append(itemsets_c[j])
        else:
            itemsets_l.append(itemsets_c[j])
            print(itemsets_c[j], ':', num[j])
    #print('L =', itemsets_l)
    #print('exclude =', exclude_target)
    all_items = itemsets_union(itemsets_l)
    if len(all_items) < i:
        break
