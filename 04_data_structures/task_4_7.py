# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
octet1=mac.split(':')[0]
octet2=mac.split(':')[1]
octet3=mac.split(':')[2]
mac='0x'+octet1+octet2+octet3
mac_int = int(mac, 16)
mac_bin=str(bin(mac_int))
print (mac_bin[2:])
