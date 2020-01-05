# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_filename):
	'''
	написать потом
	'''
	access_dict={}
	trunk_dict={}
	
	with open(config_filename) as src:
	  for line in src:
		  #print('its ok 2')
		  if 'Ethernet' in line:
			  interface=line.split()[1]
			  print(interface)			  
		  elif 'access vlan' in line:
			  vlan=line.split()[3]
			  vlan=int(line.split()[3]) 
			  print(vlan)
			  access_dict[interface]=vlan
			  
		  elif 'allowed vlan' in line:		  
			  vlans=line.split()[4].split(',')
			  for i in range(len(vlans)):
			    vlans[i]=int(vlans[i])
			  print(vlans)
			  trunk_dict[interface]=vlans
			  
		  else:
			  continue
		#sorted(access_dict)
		#sorted(trunk_dict)
		
	dict(sorted(access_dict.items(), key=lambda x: x[0]))
	dict(sorted(trunk_dict.items(), key=lambda x: x[0]))
	return (access_dict,trunk_dict)

print(get_int_vlan_map('config_sw1.txt'))
