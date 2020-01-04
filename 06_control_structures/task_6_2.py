# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ipaddress=input ('Введите IP адрес в формате хх.хх.хх.хх : ')
byte1_dec=int(ipaddress.split('.')[0])

if byte1_dec > 0 and byte1_dec <= 223:
 print('unicast')
elif (byte1_dec >= 224) and (byte1_dec <= 239):
 print('multicast')
elif ipaddress== '255.255.255.255':
 print('local broadcast')
elif ipaddress== '0.0.0.0':
 print('unassigned')
else: 
 print('unused')
	
