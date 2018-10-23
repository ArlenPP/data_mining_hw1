import function as fu
from config import config

if __name__ == '__main__':
    cond_dict = {}
    set_decreas = []
    tran_log_list = fu.read_csv(config['dataset_path']+'stocks.csv')
    log_set = fu.list_get_set(tran_log_list) 
    set_decreas = fu.FP_growth_step1(tran_log_list, log_set)
    # for k, v in set_decreas:
    #     print(k, v)