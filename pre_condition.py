# coding: utf8
import string
import subprocess
import pyautogui
import time
import sys
from test_1 import test_1
from test_2 import test_2
from test_3 import test_3
from test_4 import test_4
"""
from test_5 import test_5
from test_6 import test_6
from test_7 import test_7
from test_8 import test_8
from test_9 import test_9
"""

reload(sys)
sys.setdefaultencoding('utf-8')

Dir_and_files = ('/tmp/dir_wr','/tmp/dir_read','/tmp/dir_exec','/tmp/dir_wr_read','/tmp/tst_fldr/',
                 '/tmp/tst_fldr/read_only.txt', '/tmp/tst_fldr/write_only.txt',
                 '/tmp/tst_fldr/exec_only.sh', '/tmp/tst_fldr/rw.txt')
Output_tests = []

def precondition(index_list): # создание предварительных настроек

# удаление каталогов 
    process = subprocess.call('sudo rm -fr /tmp/dir_wr/', shell=True)
    process = subprocess.call('sudo rm -fr /tmp/dir_read/', shell=True)
    process = subprocess.call('sudo rm -fr /tmp/dir_wr_read/', shell=True)
    process = subprocess.call('sudo rm -fr /tmp/dir_exec/', shell=True)
    process = subprocess.call('sudo rm -fr /tmp/tst_fldr/', shell=True)
# создание пользователя ivanov
    process = subprocess.call('sudo pkill -9 -u ivanov', shell=True)
    process = subprocess.call('sudo userdel -fr ivanov', shell=True)
    process = subprocess.call('sudo useradd ivanov', shell=True)

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




def testcase3_2_1 (self): #Тест кейс 3.2.1
    condition_tests = 1
    index_list = precondition(self)
    index_list = test_1(index_list, condition_tests, Output_tests)
    index_list = test_2(index_list, condition_tests, Output_tests)
    index_list = test_3(index_list, condition_tests, Output_tests)
    index_list = test_4(index_list, condition_tests, Output_tests)
    return()
"""
    test_5()
     
    test_6()
    
    test_7()
     
    test_8()
     
    test_9()
"""    

    
