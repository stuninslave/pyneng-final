# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
dict1={}
with open('CAM_table.txt') as src:
	for line in src:
		if '/' in line:
			list1=line.rstrip().split()
			list1.pop(-2)
			#dict1[int(list1[0])]=line.rstrip()
			dict1.setdefault(int(list1[0]),[])
			dict1[int(list1[0])].append(list1)
			dict2=sorted(dict1)
	
vlannumber=int(input('Введите номер VLAN :'))

for key in dict1:
	for i in range(len(dict1[key])):
				column1=dict1[key][i][0]
				column2=dict1[key][i][1]
				column3=dict1[key][i][2]
				if key == vlannumber:
					print('{0:<8} {1:<20} {2:<8}'.format(column1,column2,column3))

		
		
