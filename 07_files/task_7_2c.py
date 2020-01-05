# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv 
filename=argv[1]
destfilename=argv[2]

with open(filename) as src, open(destfilename,'w') as dest:
    for line in src:
        if line.startswith('!'):
            pass
        else:
            for i in range(len(ignore)):
                if ignore[i] in line:
                    break
            else:
                dest.write(line)	 
