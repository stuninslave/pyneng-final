# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route_list=ospf_route.split()
Protocol_='OSPF'
Prefix_=ospf_route_list[1]      
AD_Metric=ospf_route_list[2].strip('[]')
Next_Hop=ospf_route_list[4].strip(',')
Last_update=ospf_route_list[5].strip(',')
Outbound_Interface=ospf_route_list[6]

print("{:<20} {:<20}".format('Protocol:',Protocol_))
print("{:<20} {:<20}".format('Prefix:',Prefix_))
print("{:<20} {:<20}".format('AD/Metric:',AD_Metric))
print("{:<20} {:<20}".format('Next-Hop:',Next_Hop))
print("{:<20} {:<20}".format('Last update:',Last_update))
print("{:<20} {:<20}".format('Outbound Interface:',Outbound_Interface))
