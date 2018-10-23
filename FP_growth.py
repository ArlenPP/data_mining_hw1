import function as fu
import fp_growth_fun as fp
from config import config


if __name__ == '__main__':
    data= 'test_data'
    f = open(config['result_path'] + "FP_" + data, newline='\n', mode='w')

    cond_dict = {}
    set_frq = {}
    tran_log_list = fu.read_csv(config['dataset_path']+data+'.csv')
    log_set = fu.list_get_set(tran_log_list) 
    
    # count log_set frq
    set_frq = fp.count_frq_log_set(tran_log_list, log_set)
    # sort tran_log_list by log_set frq
    fp.sort_tran_log_frq(tran_log_list, set_frq)
    # create FP tree
    fpTree = fp.createTree(tran_log_list)
    fpTree.disp()
    # count the support of candidate
