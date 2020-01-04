# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

questions = {'access' : 'Введите номер VLAN: ','trunk' : 'Введите список разрешенных VLAN через запятую: '}

interface_type=input('Введите режим работы интерфейса (access/trunk): ')
interface_name=input('Введите тип и номер интерфейса: ')
vlan_list=input(questions[interface_type])


access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]


access_string='\n'.join(access_template).format(vlan_list)
trunk_string='\n'.join(trunk_template).format(vlan_list)


config_types= {'access' : access_string , 'trunk' : trunk_string} 
print('interface '+interface_name)
print(config_types[interface_type])
