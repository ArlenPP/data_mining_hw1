import csv
from config import config
import function as fu

if __name__ == '__main__':
    tran_log_list = fu.read_csv(config['dataset_path']+'stocks.csv')
    tran_set = fu.list_get_set(tran_log_list)    
    cand_arr, count_arr =  fu.set_get_combinations(tran_set)
    fu.count_condidate(cand_arr, count_arr, tran_log_list)
    min_sup = len(tran_log_list)*config['min_sup']
    fu.print_min_support(cand_arr, count_arr, min_sup)

