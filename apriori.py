import function as fu
import fp_growth_fun as fp
import apriori_function as ap
from config import config
import datetime

if __name__ == '__main__':
    before = datetime.datetime.now()
    data = 'data.ntrans_10.nitems_0.01.tlen_5'
    f = open(config['result_path'] + "apriori_" + data, newline='\n', mode='w')

    # init and prepare data
    cond_dict = {}
    tran_log_list = fu.read_csv(config['dataset_path']+data+'.csv')
    log_set = fu.list_get_set(tran_log_list)
    min_sup = fu.decide_min_sup(tran_log_list, f)
    # min_sup = 2
    # apriori
    log_set = list(log_set)
    C1 = []
    for log in log_set:
        tmp_set = set()
        tmp_set.add(log)
        C1.append(tmp_set)
    ap.scan_cond_set(tran_log_list, C1, min_sup, cond_dict)

    output_dict = fu.sort_dict_keys(cond_dict)
    for key, value in output_dict.items():
        fu.write_report_cond_num(f, key, value)

    after = datetime.datetime.now()
    s = "執行時間(分): " + str((after - before).total_seconds() / 60)
    fu.write_report(f, s)
    
