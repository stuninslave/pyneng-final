# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
# start ip calculating block
#
prefixlength=input(' Введите IP подсеть в формате prefix/lenght: ')
prefix=prefixlength.split('/')[0]
ip_octet1=int(prefix.split('.')[0])
ip_octet2=int(prefix.split('.')[1])
ip_octet3=int(prefix.split('.')[2])
ip_octet4=int(prefix.split('.')[3])
length=int(prefixlength.split('/')[1])

#end ip calculating block
#
# start mask calculating block
mask_binary='1'*length+'0'*(32-length)
octet1_binary=mask_binary[0:8]
octet2_binary=mask_binary[8:16]
octet3_binary=mask_binary[16:24]
octet4_binary=mask_binary[24:32]

octet1_int=int(octet1_binary,2)
octet2_int=int(octet2_binary,2)
octet3_int=int(octet3_binary,2)
octet4_int=int(octet4_binary,2)

#end calculating block

# test print (octet1,octet2,octet3,octet4)
#test print (octet1_int,octet2_int,octet3_int,octet4_int)

#start output template block

network_template='''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

mask_template='''
Mask:
/{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:08b} {2:08b} {3:08b} {4:08b}
'''
#end ouput template block

print(network_template.format(ip_octet1,ip_octet2,ip_octet3,ip_octet4))
print(mask_template.format(length,octet1_int,octet2_int,octet3_int,octet4_int))


