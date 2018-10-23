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

# def set_get_combinations(log_set):
#     cand_arr = []
#     count_arr = []
#     # start from 0 to len -1
#     for n in range(len(log_set)):
#         n = n + 1
#         tmp = list(combinations(log_set, n))

#         for i in tmp:
#             i = list(i)
#             cand_arr.append(i)
#             count_arr.append(0)

#     return cand_arr, count_arr

# def count_condidate(cand_arr, count_arr, tran_log_list):
#     for log in tran_log_list:
#        for idx, candidate in enumerate(cand_arr):
#             if(set(log).issubset(set(candidate))):
#                 count_arr[idx] += 1

# def print_min_support(cand_arr, count_arr, min_sup):
#     for idx, num in enumerate(count_arr):
#         if (num >= min_sup):
#             print("condidate: " + str(cand_arr[idx]) + "count = " + str(count_arr[idx]))

def force_counter(tran_log_list, log_set, min_sup, f):
    cond_dict = {}
    cond_dict['min_sup']: min_sup
    # 找出所有可能的condidate 從c1 ~ c len
    for n in range(len(log_set)):
        n = n + 1
        tmp = list(combinations(log_set, n))
        tmp.sort()
        print("N = %d Len = %d" % (n, len(tmp)))
        for cond in tmp:
            tmp_cond = list(cond)
            tmp_cond.sort()
            count = count_cond_sup(cond, tran_log_list)
            if count >= min_sup:
                s = "condidate: " + str(tmp_cond) + ", and count = " + str(count)
                write_report(f, s)
                cond_dict[str(tmp_cond)]: count
    return cond_dict

def decide_min_sup(tran_log, f):
    min_sup = len(tran_log)*config['min_sup']
    s = ("min_sup = %d" % min_sup)
    write_report(f, s)
    print (s)
    return min_sup

def write_report(file, msg):
    file.write(msg)
    file.write('\n')

def count_cond_sup(cond, tran_log):
    log_set = []
    cond_set = set(cond)
    count = 0
    for log in tran_log:
        log_set.append(set(log))
    for log in log_set:
        if cond_set.issubset(log):
            count += 1
    return count
    
