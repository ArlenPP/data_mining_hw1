import function as fu
from config import config

if __name__ == '__main__':
    cond_dict = {}
    tran_log_list = fu.read_csv(config['dataset_path']+'stocks.csv')
    log_set = fu.list_get_set(tran_log_list) 
    