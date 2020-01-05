# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
	'''
    intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
    trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)

    Функция возвращает список команд с конфигурацией на основе указанных 
    портов intf_vlan_mapping и шаблона комманд trunk_template. 
	'''
	config_dict={}
	config_file=[]
	for intf_name,intf_vlan_list in intf_vlan_mapping.items():
		config_dict[intf_name]=[]
		for command in trunk_template:
			if command.endswith('allowed vlan'):
				config_dict[intf_name].append('{} {}'.format(command,','.join(str(x) for x in intf_vlan_list)))								
			else:
				config_dict[intf_name].append(('{}'.format(command)))				
	return config_dict
	
print(generate_trunk_config(trunk_config,trunk_mode_template))
