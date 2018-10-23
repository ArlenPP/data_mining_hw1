import csv
import config
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
