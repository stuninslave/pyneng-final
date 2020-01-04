# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ipaddress_correct= False
ipaddress=input ('Введите IP адрес в формате хх.хх.хх.хх : ')
while not ipaddress_correct:
      try:
       byte1_dec=int(ipaddress.split('.')[0])
       byte2_dec=int(ipaddress.split('.')[1])
       byte3_dec=int(ipaddress.split('.')[2])
       byte4_dec=int(ipaddress.split('.')[3])      
      except:
       print('неверный ip address')
      if (byte1_dec >=0 and byte1_dec <=255 and byte2_dec >=0 and byte2_dec <=255 and byte3_dec >=0 and byte3_dec <=255 and byte4_dec >=0 and byte4_dec <=255 and len(ipaddress.split('.')))==4:
         ipaddress_correct = True         
      else:
         ipaddress=input ('Введите  корректный IP адрес в формате хх.хх.хх.хх : ')


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

