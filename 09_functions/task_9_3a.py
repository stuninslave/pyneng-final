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

def _parse_interfaces(config_filename):
    interfaces = []
    name = ''
    mode = ''
    access_vlan = None
    trunk_encapsulation = None
    trunk_allowed_vlan = None
    duplex = 'auto'
    in_config = False
    with open(config_filename) as src:
        for line in src:
            if line.strip().startswith('interface'):
                in_config = True
                name = line.split('interface')[-1].strip()
            if not in_config:
                continue
            elif line.strip().startswith('switchport mode') and in_config:
                mode = line.split('switchport mode')[-1].strip()
            elif line.strip().startswith('switchport access vlan') and in_config:
                access_vlan = int(line.split('switchport access vlan')[-1].strip())
            elif line.strip().startswith('switchport trunk encapsulation') and in_config:
                trunk_encapsulation = line.split('switchport trunk encapsulation')[-1].strip()
            elif line.strip().startswith('switchport trunk allowed vlan') and in_config:
                trunk_allowed_vlan = [
                    int(item)
                    for item in
                    line.split('switchport trunk allowed vlan')[-1].strip().split(',')
                ]
            elif line.strip().startswith('duplex') and in_config:
                duplex = line.split('duplex')[-1].strip()
            elif line.strip().startswith('!') and in_config:
                in_config = False
                interfaces.append(
                    {
                        'name': name,
                        'mode': mode,
                        'access_vlan': access_vlan,
                        'trunk_encapsulation': trunk_encapsulation,
                        'trunk_allowed_vlan': trunk_allowed_vlan,
                        'duplex': duplex
                    }
                )
                name = ''
                mode = ''
                access_vlan = None
                trunk_encapsulation = None
                trunk_allowed_vlan = None
                duplex = 'auto'
    return interfaces


def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    interfaces = _parse_interfaces(config_filename)
    for interface in interfaces:
        key = interface['name']
        if interface['mode'] == 'access':
            vlan = interface['access_vlan']
            if vlan == None:
				vlan=1
            access_dict[key] = vlan
        elif interface['mode'] == 'trunk':
            vlan = interface['trunk_allowed_vlan']
            trunk_dict[key] = vlan
    return access_dict, trunk_dict

print(get_int_vlan_map('config_sw2.txt'))




