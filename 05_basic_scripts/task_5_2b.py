# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

network=argv[1]
netmask=argv[2]

# start ip calculating block
#
#prefixlength=input(' Введите IP подсеть в формате prefix/lenght: ')
#prefix=prefixlength.split('/')[0]
prefix=network
ip_octet1=int(prefix.split('.')[0])
ip_octet2=int(prefix.split('.')[1])
ip_octet3=int(prefix.split('.')[2])
ip_octet4=int(prefix.split('.')[3])
#length=int(prefixlength.split('/')[1])
length=int(netmask)
"""
print (network)
print (prefix)
print (length)
print (netmask)
"""

ip_binary_string1= str(bin(ip_octet1))[2:]
ip_binary_octet1='0'*(8-len(ip_binary_string1))+ip_binary_string1

ip_binary_string2= str(bin(ip_octet2))[2:]
ip_binary_octet2='0'*(8-len(ip_binary_string2))+ip_binary_string2

ip_binary_string3= str(bin(ip_octet3))[2:]
ip_binary_octet3='0'*(8-len(ip_binary_string3))+ip_binary_string3

ip_binary_string4= str(bin(ip_octet4))[2:]
ip_binary_octet4='0'*(8-len(ip_binary_string4))+ip_binary_string4

ip_binary_octets=ip_binary_octet1+ip_binary_octet2+ip_binary_octet3+ip_binary_octet4 # IP binary
ip_binary_octets_stripped=ip_binary_octets[:length]+'0'*(32-length) #subnet binary

subnet_octet1_bin=ip_binary_octets_stripped[0:8]
subnet_octet2_bin=ip_binary_octets_stripped[8:16]
subnet_octet3_bin=ip_binary_octets_stripped[16:24]
subnet_octet4_bin=ip_binary_octets_stripped[24:32]
subnet_octet1_int=int(subnet_octet1_bin,2)
subnet_octet2_int=int(subnet_octet2_bin,2)
subnet_octet3_int=int(subnet_octet3_bin,2)
subnet_octet4_int=int(subnet_octet4_bin,2)
#print (ip_binary_string)
#print (ip_binary_octet1)
#print (ip_binary_octet2)
#print (ip_binary_octet3)
#print (ip_binary_octet4)

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

print(network_template.format(subnet_octet1_int,subnet_octet2_int,subnet_octet3_int,subnet_octet4_int))
print(mask_template.format(length,octet1_int,octet2_int,octet3_int,octet4_int))



