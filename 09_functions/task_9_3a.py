# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_filename):
	'''
	написать потом
	'''
	access_dict={}
	trunk_dict={}
	vlan=0
	with open(config_filename) as src:
	  for line in src:
		  #print('its ok 2')
		  access_port= False
		  vlan_1_access=False
		  if 'Ethernet' in line:
			  interface=line.split()[1]
			  print(interface)
			  print(vlan)			  			  
		  elif 'mode access' in line and access_port:
			  vlan_1_access = True
		  elif 'access vlan' in line:
			  vlan=line.split()[3]
			  vlan=int(line.split()[3]) 
			  print(vlan)
			  access_dict[interface]=vlan
			  vlan=0
			  access_port= True
		  
		  elif 'allowed vlan' in line:		  
			  vlans=line.split()[4].split(',')
			  for i in range(len(vlans)):
			    vlans[i]=int(vlans[i])
			  print(vlans)
			  trunk_dict[interface]=vlans
			  
			  
		  else:
			  if vlan_1_access and not vlan:
				  access_dict[interface]=1
			  else:
				  continue
		#sorted(access_dict)
		#sorted(trunk_dict)
		
	dict(sorted(access_dict.items(), key=lambda x: x[0]))
	dict(sorted(trunk_dict.items(), key=lambda x: x[0]))
	return (access_dict,trunk_dict)

print(get_int_vlan_map('config_sw2.txt'))
