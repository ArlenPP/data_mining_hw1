from config import config
import function as fu
import datetime

if __name__ == '__main__':
    
    cond_dict = {}
    f = open(config['result_path'] + "force_kaggle", newline='\n', mode='w')

    tran_log_list = fu.read_csv(config['dataset_path']+'stocks.csv')
    log_set = fu.list_get_set(tran_log_list)
    min_sup = fu.decide_min_sup(tran_log_list, f)
    
    before = datetime.datetime.now()
    print("start: " + before.strftime("%H:%S:%m"))
    cond_dict = fu.force_counter(tran_log_list, log_set, min_sup, f)
    after = datetime.datetime.now()
    s = "執行時間(分): " + str((after - before).total_seconds() / 60)
    fu.write_report(f, s)
    print(s)
