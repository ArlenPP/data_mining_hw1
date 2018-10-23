import csv
from config import config
import function as fu

if __name__ == '__main__':
    cond_dict = {}
    tran_log_list = fu.read_csv(config['dataset_path']+'stocks.csv')
    log_set = fu.list_get_set(tran_log_list)    
    min_sup = fu.decide_min_sup(tran_log_list)
    cond_dict = fu.force_counter(tran_log_list, log_set, min_sup)

