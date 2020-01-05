# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv 
filename=argv[1]

with open(filename) as src:
    for line in src:
        if line.startswith('!'):
            pass
        else:
            for i in range(len(ignore)):
                if ignore[i] in line:
                    break
            else:
                print(line.rstrip())	 
		    
       		    
