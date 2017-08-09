#!/usr/bin/python3
import time

NAMES_FILE = 'names.txt'

def main():
    f = open(NAMES_FILE)
    total_time = 0
    names_list = []
    names_dict = {}
    names_set = set()
    for l in f:
        l = l.rstrip().split(',')
        name = l[1]
        start = time.time()
        #if name not in names_list:
        #    names_list.append(name)    
        #if name not in names_dict:
        #    names_dict[name] = True
        #    names_list.append(name)
        if name not in names_set:
            names_set.add(name)
            names_list.append(name)
        elapsed = time.time() - start
        #print('Lookup for {} took {}s'.format(name, elapsed))
        total_time += elapsed
        
    f.close()
    print('{} unique names were read in {}s'.format(len(names_list), total_time))
    
    
main()