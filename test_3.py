# coding: utf8
import string
import subprocess
import pyautogui
import time
import sys
from test_1 import test_1

reload(sys)
sys.setdefaultencoding('utf-8')



def test_3(index_list, condition_tests, Output_tests):  #Тест в
    process = subprocess.Popen('logname', shell=True,
                                   stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
    #process = subprocess.check_call('sudo -i', shell=True)
# Пользователем root назначить владельцем каталога tst_fldr и всех файлов в нем пользователя root, группой владельца назначить ivanov:
    process = subprocess.check_call('sudo chown -R root:'+username[0]+' /tmp/tst_fldr/', shell=True)
    if process == 0:
        Output_tests.append('Изменение прав для каталога /tmp/tst_fldr/\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1
# Проверить правильность назначенных прав:
    process = subprocess.check_call('ls -l /tmp/tst_fldr/', shell=True)
# Пользователями ivanov и petrov повторить попытки чтения, записи, запуска файлов в каталоге tst_fldr.    
    
    condition_tests = 2
    index_list = test_1(index_list, condition_tests, Output_tests)
    print "Тест в - выполнен"
    Output_tests.append("\033[32mТест в - выполнен\033[0m")
    index_list +=1
    return(index_list)