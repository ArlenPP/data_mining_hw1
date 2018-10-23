from config import config
import function as fu
from itertools import combinations

def scan_cond_set(tran_log ,D , min_sup, output_ditc, layer=1):
    tmp_set = set()
    layer += 1
    print("N = %d Len = %d" % (layer-1, len(D)))
    if len(D) <= 1:
        return
    for cond in D:
        count = 0
        for log in tran_log:
            if cond.issubset(set(log)):
                count += 1
        if count >= min_sup:
            tmp_list = list(cond)
            tmp_list.sort()
            s = str(tmp_list)
            output_ditc[s] = count
            for cd in cond:
                tmp_set.add(cd)

    new_cond_set = list(combinations(tmp_set, layer))
    new_cond_list = []
    for s in new_cond_set:
        t_s = set()
        for i in s:
            t_s.add(i)
        new_cond_list.append(t_s)
    scan_cond_set(tran_log, new_cond_list, min_sup, output_ditc, layer)
        
