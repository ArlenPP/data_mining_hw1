from config import config
import function as fu
from itertools import combinations

class treeNode:
    def __init__(self, nameItem, numOccur, parentNode):
        self.name = nameItem
        self.count = numOccur
        self.parent = parentNode
        self.child = {}
        self.nodeLink = None

    # display the tree for debug
    def disp(self, ind=1):
        print('  '*ind, self.name, ' ', self.count)
        for child in self.child.values():
            child.disp(ind+1)
def count_frq_log_set(tran_log, log_set):
    d = {}
    log_set_list = list(log_set)
    log_set_list.sort()
    for s in log_set_list:
        tmp = []
        tmp.append(s)
        count = fu.count_cond_sup(tmp, tran_log)
        d[s] = count
    # sorted_dict = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
    return d

def sort_tran_log_frq(tran_log, frq, min_sup):
    for log in tran_log:
        for item in log:
            if frq[item] < min_sup:
                log.remove(item)
        log.sort(key=lambda k: (frq[k], k), reverse=True)

def createTree(tran_log):
    fpTree = treeNode('root', 1, None)
    for log in tran_log:
        updateTree(log, fpTree)
    return fpTree

def updateTree(log, node):
    if len(log) > 0:
        item = log[0]
        if item in node.child.keys():
            node.child[item].count += 1
            log.remove(item)
            updateTree(log, node.child[item])
        else:
            node.child[item] = treeNode(item, 1, node)
            log.remove(item)
            updateTree(log, node.child[item])


def create_header_table(item_d, items, node):
    for item in items:
        tmp = []
        find_item_leaf(item, node, tmp)
        item_d[item]= tmp
        
def find_item_leaf(item, node, arr):
    if item == node.name:
        arr.append(node)
        return None
    if node.child.keys() == None:
        return None
    for child in node.child.values():
        find_item_leaf(item, child, arr)

def find_cond_and_count(item, header, min_sup, output_dict):
    tmp_dict = {}
    for node in header[item]:
        tmp = []
        frq = node.count
        ascendTree(node.parent, tmp)
        for i in range(len(tmp)+1):
            name_arr = []
            for s in list(combinations(set(tmp), i)):
                t = []
                t.append(item)
                for it in s:
                    t.append(it)
                t.sort()
                name_arr.append(t)
            for cond_name in name_arr:
                if str(cond_name) in tmp_dict.keys():
                    tmp_dict[str(cond_name)] += frq
                else:
                    tmp_dict[str(cond_name)] = frq
    for key, value in tmp_dict.items():
        if (value >= min_sup):
            output_dict[key] = value
    
def ascendTree(leafNode, prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)
