import csv
from config import config
from itertools import combinations

# return 二維array,每個element是一個transition log(裡面要在以逗點分開)
def read_csv(csv_file_path):
    # open csv file
    with open(csv_file_path, newline='') as f:
        # 讀取每一行的csv檔案內容
        rows = csv.reader(f)
        tmp_arr = []
        for row in rows:
            tmp_arr.append(row)
        return tmp_arr

# 傳入所有transition 的二維array回傳他的set
def list_get_set(tran_log_list):
    tmp_arr = []
    for tran in tran_log_list:
        tmp_arr.extend(tran)
    return set(tmp_arr)

def set_get_combinations(log_set):
    cand_arr = []
    count_arr = []
    # start from 0 to len -1
    for n in range(len(log_set)):
        n = n + 1
        tmp = list(combinations(log_set, n))

        for i in tmp:
            i = list(i)
            cand_arr.append(i)
            count_arr.append(0)

    return cand_arr, count_arr

def count_condidate(cand_arr, count_arr, tran_log_list):
    for log in tran_log_list:
       for idx, candidate in enumerate(cand_arr):
            if(set(log).issubset(set(candidate))):
                count_arr[idx] += 1

def print_min_support(cand_arr, count_arr, min_sup):
    for idx, num in enumerate(count_arr):
        if (num >= min_sup):
            print("condidate: " + str(cand_arr[idx]) + "count = " + str(count_arr[idx]))

def force_counter(tran_log_list, log_set, min_sup):
    cond_dict = {}
    cond_dict['min_sup']: min_sup
    for n in range(len(log_set)):
        n = n + 1
        tmp = list(combinations(log_set, n))
        tmp.sort()
        for cond in tmp:
            count = 0
            tmp_cond = list(cond)
            tmp_cond.sort()
            for log in tran_log_list:
                if set(tmp_cond).issubset(set(log)):
                    count += 1
            if count >= min_sup:
                print("condidate: " + str(tmp_cond) + ", and count = " + str(count))
                cond_dict[str(tmp_cond)]: count
    return cond_dict

def decide_min_sup(tran_log):
    min_sup = len(tran_log)*config['min_sup']
    print ("min_sup = %d" % min_sup)
    return min_sup
