# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def convert_config_to_dict(config_filename):
	config_dict={}
	key_command=None
	list_of_commands=[]
	global_command=False
	to_ignore=False
	with open(config_filename) as src:
		for line in src:
			line=line.strip('\n')
			print(line)
			to_ignore=False
			for word in ignore:
				if word in line:
					to_ignore=True
			
			if line.startswith('!') or to_ignore:
				print('1.0 >>>>>line ignored')
				pass					
			#elif line.startswith(' ') and not global_command:
			#	continue	
			elif not line.startswith(' '):
				key_command=line
				print('2.0 key command='+key_command)
				global_command=True
				list_of_commands=[]
				print('3.0 global_command=true')				
			elif line.startswith(' ') and global_command:
				list_of_commands.append(line[1:])
				print('4.0 LIST OF COMMANDS\n')
				print(list_of_commands)
			
			if key_command:
				config_dict[key_command]=list_of_commands
			
	return config_dict

print(convert_config_to_dict('config_sw1.txt'))



				
