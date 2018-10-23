from config import config
import function as fu

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

def sort_tran_log_frq(tran_log, frq):
    for log in tran_log:
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