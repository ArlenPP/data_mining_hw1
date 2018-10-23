import function as fu
import fp_growth_fun as fp
from config import config
import datetime


if __name__ == '__main__':
    before = datetime.datetime.now()
    data= 'stocks'
    f = open(config['result_path'] + "FP_" + data, newline='\n', mode='w')

    cond_dict = {}
    set_frq = {}
    tran_log_list = fu.read_csv(config['dataset_path']+data+'.csv')
    log_set = fu.list_get_set(tran_log_list) 
    min_sup = fu.decide_min_sup(tran_log_list, f)
    
    # count log_set frq
    set_frq = fp.count_frq_log_set(tran_log_list, log_set)
    # sort tran_log_list by log_set frq
    fp.sort_tran_log_frq(tran_log_list, set_frq, min_sup)
    # create FP tree
    fpTree = fp.createTree(tran_log_list)
    # fpTree.disp() 
    # count the support of candidate
    
    output_dict = {}
    ## create a dict that key is item and value is the node(item) in tree 
    header_table = {}
    fp.create_header_table(header_table, set_frq.keys(), fpTree)
    ## create subpattern base
    sorted_list = [(k, set_frq[k]) for k in sorted(set_frq, key=set_frq.get, reverse=False)]
    for item in sorted_list:
        # 從排序過的item 和 頻率的 list中開始收尋，從頻率最低的開始
        if item[1] < min_sup:
            continue
        fp.find_cond_and_count(item[0], header_table, min_sup, output_dict)
    output_dict = fu.sort_dict_keys(output_dict) 
    for key, value in output_dict.items():
        fu.write_report_cond_num(f, key, value)
    after = datetime.datetime.now()
    s = "執行時間(分): " + str((after - before).total_seconds() / 60)
    fu.write_report(f, s)
    
    
