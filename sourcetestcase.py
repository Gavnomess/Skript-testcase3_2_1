# coding: utf8
import string
import subprocess
import pyautogui
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

Dir_and_files = ('/tmp/dir_wr','/tmp/dir_read','/tmp/dir_exec','/tmp/dir_wr_read','/tmp/tst_fldr/',
                 '/tmp/tst_fldr/read_only.txt', '/tmp/tst_fldr/write_only.txt',
                 '/tmp/tst_fldr/exec_only.sh', '/tmp/tst_fldr/rw.txt')
Output_tests = []
#global index_list 




def precondition(index_list): # создание предварительных настроек

# удаление каталогов 
    process = subprocess.call('sudo rm -fr /tmp/dir_wr/', shell=True)
    process = subprocess.call('sudo rm -fr /tmp/dir_read/', shell=True)
    process = subprocess.call('sudo rm -fr /tmp/dir_wr_read/', shell=True)
    process = subprocess.call('sudo rm -fr /tmp/dir_exec/', shell=True)
    process = subprocess.call('sudo rm -fr /tmp/tst_fldr/', shell=True)

    process = subprocess.check_call('sudo mkdir /tmp/dir_wr', shell=True)
    if process == 0:
        Output_tests.append('Создание директории '+Dir_and_files[0]+ "\033[32m прошло успешно\033[0m")
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo mkdir /tmp/dir_read', shell=True)
    if process == 0:
        Output_tests.append('Создание директории '+Dir_and_files[1]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo mkdir /tmp/dir_exec', shell=True)
    if process == 0: 
        Output_tests.append('Создание директории '+Dir_and_files[2]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo mkdir /tmp/dir_wr_read', shell=True)
    if process == 0:
        Output_tests.append('Создание директории '+Dir_and_files[3]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

# Создание прав на изменение каталога ##########################################################

    process = subprocess.check_call('sudo chmod 330 /tmp/dir_wr/', shell=True)
    if process == 0:
        Output_tests.append('Изменение прав для каталога '+Dir_and_files[0]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo chmod 440 /tmp/dir_read/', shell=True)
    if process == 0:
        Output_tests.append('Изменение прав для каталога '+Dir_and_files[1]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo chmod 660 /tmp/dir_wr_read/', shell=True)
    if process == 0:
        Output_tests.append('Изменение прав для каталога '+Dir_and_files[2]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1
    process = subprocess.check_call('sudo chmod 110 /tmp/dir_exec/', shell=True)
    if process == 0:
        Output_tests.append('Изменение прав для каталога '+Dir_and_files[3]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1
# Просмотреть права созданных каталогов:
    process = subprocess.check_call('sudo ls -l /tmp/', shell=True)

#Создать тестовый каталог  tst_fldr и в нем 4 файла:
    process = subprocess.check_call('sudo mkdir /tmp/tst_fldr/', shell=True)
    if process == 0:
        Output_tests.append('Создание директории '+Dir_and_files[4]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo touch /tmp/tst_fldr/read_only.txt', shell=True)
    if process == 0:    
        Output_tests.append('Создание файла '+Dir_and_files[5]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo touch /tmp/tst_fldr/write_only.txt', shell=True)
    if process == 0:    
        Output_tests.append('Создание файла '+Dir_and_files[6]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo touch /tmp/tst_fldr/exec_only.sh', shell=True)
    if process == 0:    
        Output_tests.append('Создание файла '+Dir_and_files[7]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo touch /tmp/tst_fldr/rw.txt', shell=True)
    if process == 0:    
        Output_tests.append('Создание файла '+Dir_and_files[8]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

# Создание прав на изменение файлов ##########################################################
    process = subprocess.check_call('sudo chmod 440 /tmp/tst_fldr/read_only.txt', shell=True)
    if process == 0:    
        Output_tests.append('Изменение прав для файла '+Dir_and_files[5]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo chmod 220 /tmp/tst_fldr/write_only.txt', shell=True)
    if process == 0:    
        Output_tests.append('Изменение прав для файла '+Dir_and_files[6]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo chmod 660 /tmp/tst_fldr/rw.txt', shell=True)
    if process == 0:
        Output_tests.append('Изменение прав для файла '+Dir_and_files[8]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1

    process = subprocess.check_call('sudo chmod 550 /tmp/tst_fldr/exec_only.sh', shell=True)
    if process == 0:
        Output_tests.append('Изменение прав для файла '+Dir_and_files[7]+'\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1
# Просмотреть права созданных файлов:        
    process = subprocess.check_call('sudo ls -l /tmp/tst_fldr/', shell=True)

    print "Начальные настройки выполнены"
    Output_tests.append("\033[32mНачальные настройки выполнены\033[0m")
    index_list +=1
    return(index_list)

def test_1(index_list, condition_tests):  #Тест а

# пользователями ivanov и petrov просмотреть содержимое файлов в каталоге tst_fldr
    process = subprocess.Popen("cat /tmp/tst_fldr/read_only.txt", shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='cat: /tmp/tst_fldr/read_only.txt: Отказано в доступе\n':
            status2 = 'cat: /tmp/tst_fldr/read_only.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m') 
    elif condition_tests == 2:
        if status1 == '' and status2 == '':
            Output_tests.append('Считывание файла /tmp/tst_fldr/read_only.txt\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1 
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')

    process = subprocess.Popen('cat /tmp/tst_fldr/rw.txt', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='cat: /tmp/tst_fldr/rw.txt: Отказано в доступе\n':
            status2 =='cat: /tmp/tst_fldr/rw.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status1 == '' and status2 == '':
            Output_tests.append('Считывание файла /tmp/tst_fldr/rw.txt\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1 
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')

    process = subprocess.Popen('cat /tmp/tst_fldr/write_only.txt', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='cat: /tmp/tst_fldr/write_only.txt: Отказано в доступе\n':
            status2 =='cat: /tmp/tst_fldr/write_only.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status2 =='cat: /tmp/tst_fldr/write_only.txt: Отказано в доступе\n':
            status2 =='cat: /tmp/tst_fldr/write_only.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')

    process = subprocess.Popen('cat /tmp/tst_fldr/exec_only.sh', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='cat: /tmp/tst_fldr/exec_only.sh: Отказано в доступе\n':
            status2 =='cat: /tmp/tst_fldr/exec_only.sh: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status1 == '' and status2 == '':
            Output_tests.append('Считывание файла /tmp/tst_fldr/exec_only.sh\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1 
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')       

# пользователями ivanov и petrov записать текст в файлы каталога  tst_fldr:
    process = subprocess.Popen("echo 'txt' > /tmp/tst_fldr/read_only.txt", shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='/bin/sh: /tmp/tst_fldr/read_only.txt: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/read_only.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status2 =='/bin/sh: /tmp/tst_fldr/read_only.txt: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/read_only.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')

    process = subprocess.Popen("echo 'txt' > /tmp/tst_fldr/rw.txt", shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='/bin/sh: /tmp/tst_fldr/rw.txt: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/rw.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status1 == '' and status2 == '':
            Output_tests.append('Запись в файл /tmp/tst_fldr/rw.txt\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1 
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
       
    process = subprocess.Popen("echo 'txt' > /tmp/tst_fldr/write_only.txt", shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='/bin/sh: /tmp/tst_fldr/write_only.txt: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/write_only.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status1 == '' and status2 == '':
            Output_tests.append('Запись в файл /tmp/tst_fldr/write_only.txt\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1 
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')

    process = subprocess.Popen("echo 'txt' > /tmp/tst_fldr/exec_only.sh", shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='/bin/sh: /tmp/tst_fldr/exec_only.sh: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/exec_only.sh: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status2 =='/bin/sh: /tmp/tst_fldr/exec_only.sh: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/exec_only.sh: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')

# пользователями ivanov и petrov выполнить файлы каталога  tst_fldr:
    process = subprocess.Popen('/tmp/tst_fldr/exec_only.sh', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='/bin/sh: /tmp/tst_fldr/exec_only.sh: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/exec_only.sh: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status1 == '' and status2 == '':
            Output_tests.append('Запуск файла /tmp/tst_fldr/exec_only.sh\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1 
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')

    process = subprocess.Popen('/tmp/tst_fldr/rw.txt', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='/bin/sh: /tmp/tst_fldr/rw.txt: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/rw.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status2 =='/bin/sh: /tmp/tst_fldr/rw.txt: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/rw.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
 
    process = subprocess.Popen('/tmp/tst_fldr/write_only.txt', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='/bin/sh: /tmp/tst_fldr/write_only.txt: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/write_only.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status2 =='/bin/sh: /tmp/tst_fldr/write_only.txt: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/write_only.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')

    process = subprocess.Popen('/tmp/tst_fldr/read_only.txt', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    status1,status2 = process.communicate()
    if condition_tests == 1:
        if status2 =='/bin/sh: /tmp/tst_fldr/read_only.txt: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/read_only.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
    elif condition_tests == 2:
        if status2 =='/bin/sh: /tmp/tst_fldr/read_only.txt: Отказано в доступе\n':
            status2 =='/bin/sh: /tmp/tst_fldr/read_only.txt: Отказано в доступе'
            Output_tests.append(status2+'\033[32m - Успех\033[0m')
            print Output_tests[index_list].encode('utf-8')
            index_list +=1
        else:
            print status2
            raise ValueError('\033[31m'+status2+' -не соответсвует ожиданиям!\033[0m')
                
    print "Тест а - выполнен"
    Output_tests.append("\033[32mТест а - выполнен\033[0m")
    index_list +=1
    return(index_list)

def test_2(index_list, condition_tests):  #Тест б
    process = subprocess.Popen('logname', shell=True,stdout = subprocess.PIPE, stdin = subprocess.PIPE,stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
    #process = subprocess.check_call('sudo -i', shell=True)
# Пользователем root назначить владельцем каталога tst_fldr и всех файлов в нем пользователя ivanov:  
    process = subprocess.check_call('sudo chown -R '+username[0]+' /tmp/tst_fldr/', shell=True)
    if process == 0:
        Output_tests.append('Изменение прав для каталога /tmp/tst_fldr/\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1
# Проверить правильность назначенных прав:   
    process = subprocess.check_call('ls -l /tmp/tst_fldr/', shell=True)
# Владельцем всех созданных файлов является пользователь ivanov.
# Пользователями ivanov и petrov повторить попытки чтения, записи, запуска файлов в каталоге tst_fldr
    condition_tests = 2
    index_list = test_1(index_list, condition_tests)
    print "Тест б - выполнен"
    Output_tests.append("\033[32mТест б - выполнен\033[0m")
    index_list +=1
    return(index_list)

def test_3():  #Тест в
    process = subprocess.Popen('logname', shell=True,
                                   stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
    #process = subprocess.check_call('sudo -i', shell=True)
# Пользователем root назначить владельцем каталога tst_fldr и всех файлов в нем пользователя root, группой владельца назначить ivanov:
    process = subprocess.check_call('sudo chown -R root:'+username[0]+' /tmp/tst_fldr/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.check_call('ls -l /tmp/tst_fldr/', shell=True)
# Пользователями ivanov и petrov повторить попытки чтения, записи, запуска файлов в каталоге tst_fldr.    
    test_1()
    print "Тест в - выполнен"
    return()

def test_4():  #Тест г

    process = subprocess.Popen('logname', shell=True,
                                   stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
# Добавить пользователей ivanov и petrov в группу audio:
    process = subprocess.check_call('sudo usermod -a -G audio '+username[0], shell=True)
# Пользователем root назначить владельцем каталога tst_fldr и всех файлов в нем пользователя root, группой владельца назначить audio:
    process = subprocess.check_call('sudo chown -R root:audio /tmp/tst_fldr/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.check_call('ls -l /tmp/tst_fldr/', shell=True)  
# Для применения назначенных групп завершить текущие сеансы пользователей ivanov и petrov. 
# Начать новые сеансы от имени  пользователей ivanov и petrov
    process = subprocess.check_call('exit', shell=True)
# Убедиться, что новая группа доступна пользователю:
    process = subprocess.check_call('id', shell=True)
# Пользователями ivanov и petrov повторить попытки чтения, записи, запуска файлов в каталоге tst_fldr.
    test_1()
    print "Тест г - выполнен"     
    return()

def test_5():  #Тест д

# Пользователями ivanov и petrov просмотреть содержимое каталогов:
    process = subprocess.check_call('ls -l /tmp/dir_exec/', shell=True) 
    process = subprocess.check_call('ls -l /tmp/dir_read/', shell=True)
    process = subprocess.check_call('ls -l /tmp/dir_wr/', shell=True)
    process = subprocess.check_call('ls -l /tmp/dir_wr_read/', shell=True)
# Пользователями ivanov и petrov в каждом каталоге создать файл test.txt:
    process = subprocess.check_call('touch /tmp/dir_exec/test.txt', shell=True)
    process = subprocess.check_call('touch /tmp/dir_read/test.txt', shell=True)
    process = subprocess.check_call('touch /tmp/dir_wr/test.txt', shell=True)
    process = subprocess.check_call('touch /tmp/dir_wr_read/test.txt', shell=True)
# Пользователями ivanov и petrov сменить текущий каталог:
    process = subprocess.check_call('cd /tmp/dir_exec/', shell=True)
    process = subprocess.check_call('cd /tmp/dir_read/', shell=True)
    process = subprocess.check_call('cd /tmp/dir_wr/', shell=True)
    process = subprocess.check_call('cd /tmp/dir_wr_read/', shell=True)
    print "Тест д - выполнен"
    return()

def test_6():  #Тест е

    process = subprocess.Popen('logname', shell=True,
                                   stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
# Сменить владельца каталогов  dir_exec,  dir_read. dir_wr,  dir_wr_read назначив новым владельцем пользователя ivanov:    
    process = subprocess.check_call('sudo chown '+username[0]+' /tmp/dir_exec/', shell=True)
    process = subprocess.check_call('sudo chown '+username[0]+' /tmp/dir_read/', shell=True)
    process = subprocess.check_call('sudo chown '+username[0]+' /tmp/dir_wr/', shell=True)
    process = subprocess.check_call('sudo chown '+username[0]+' /tmp/dir_wr_read/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.check_call('ls -l /tmp/', shell=True)  
# Пользователями ivanov и petrov просмотреть содержимое каталогов, в каждом каталоге создать файл test.txt,  сменить текущий каталог.
    process = subprocess.check_call('touch /tmp/dir_exec/test.txt', shell=True)
    process = subprocess.check_call('touch /tmp/dir_read/test.txt', shell=True)
    process = subprocess.check_call('touch /tmp/dir_wr/test.txt', shell=True)
    process = subprocess.check_call('touch /tmp/dir_wr_read/test.txt', shell=True)

    process = subprocess.check_call('cd /home', shell=True)
    print "Тест е - выполнен"
    return()

def test_7():  #Тест ж

    process = subprocess.Popen('logname', shell=True,
                                   stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
# Сменить владельца каталогов  dir_exec,  dir_read. dir_wr,  dir_wr_read назначив новым владельцем пользователя root и назначив группу владельца ivanov:
    process = subprocess.check_call('sudo chown '+username[0]+' /tmp/dir_exec/', shell=True)
    process = subprocess.check_call('sudo chown '+username[0]+' /tmp/dir_read/', shell=True)
    process = subprocess.check_call('sudo chown '+username[0]+' /tmp/dir_wr/', shell=True)
    process = subprocess.check_call('sudo chown '+username[0]+' /tmp/dir_wr_read/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.check_call('ls -l /tmp/', shell=True)
    print "Тест ж - выполнен"    
    return()

def test_8():  #Тест з

# Сменить владельца каталогов  dir_exec,  dir_read. dir_wr,  dir_wr_read назначив новым владельцем пользователя root и назначив группу владельца audio:
    process = subprocess.check_call('sudo chown root:audio /tmp/dir_exec/', shell=True)
    process = subprocess.check_call('sudo chown root:audio /tmp/dir_read/', shell=True)
    process = subprocess.check_call('sudo chown root:audio /tmp/dir_wr/', shell=True)
    process = subprocess.check_call('sudo chown root:audio /tmp/dir_wr_read/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.check_call('ls -l /tmp/', shell=True)
    print "Тест з - выполнен" 
    return()

def test_9():  #Тест и

    process = subprocess.Popen('logname', shell=True,
                                   stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
# Пользователем ivanov создать файл:
    process = subprocess.check_call('touch /tmp/ivanov.file', shell=True)
# Назначить ему права с полным доступом для всех пользователей и дополнительным атрибутом Sticky bit:    
    process = subprocess.check_call('chmod 1777 /tmp/ivanov.file', shell=True)
# Пользователем root сменить группу владельца файла на общедоступную для пользователей ivanov и petrov:    
    process = subprocess.check_call('sudo chown '+username[0]+':audio /tmp/ivanov.file', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.check_call('ls -l /tmp/', shell=True)
# Пользователем ivanov удалить  файл ivanov.file:
    process = subprocess.check_call('rm -f /tmp/ivanov.file', shell=True)
    print "Тест и - выполнен"
    return()

def testcase3_2_1 (self): #Тест кейс 3.2.1
    condition_tests = 1

    index_list = precondition(self)

    index_list = test_1(index_list, condition_tests)

    index_list = test_2(index_list, condition_tests)

    return()

    
"""    
    
    test_3()
 
    test_4()
    
    test_5()
     
    test_6()
    
    test_7()
     
    test_8()
     
    test_9()
"""
    

