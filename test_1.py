# coding: utf8
import string
import subprocess
import pyautogui
import time
import sys
#from pre_condition import Output_tests

reload(sys)
sys.setdefaultencoding('utf-8')


#global index_list 






def test_1(index_list, condition_tests, Output_tests):  #Тест а

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
        if status2 == '':
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
        if status2 == '':
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
        if status2 == '':
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
