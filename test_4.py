# coding: utf8
import string
import subprocess
import pyautogui
import time
import sys
from test_1 import test_1

reload(sys)
sys.setdefaultencoding('utf-8')




def test_4(index_list, condition_tests, Output_tests):  #Тест г
    process = subprocess.Popen('logname', shell=True,
                                   stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
# Добавить пользователей ivanov и petrov в группу audio:
    process = subprocess.check_call('sudo usermod -a -G audio ivanov', shell=True)
    if process == 0:
        Output_tests.append('Добавление пользователя ivanov в группу audio\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1
# Пользователем root назначить владельцем каталога tst_fldr и всех файлов в нем пользователя root, группой владельца назначить audio:
    process = subprocess.check_call('sudo chown -R root:audio /tmp/tst_fldr/', shell=True)
    if process == 0:
        Output_tests.append('Изменение прав для каталога /tmp/tst_fldr/\033[32m прошло успешно\033[0m')
        print Output_tests[index_list].encode('utf-8')
        index_list +=1
# Проверить правильность назначенных прав:
    process = subprocess.check_call('ls -l /tmp/tst_fldr/', shell=True)  
# Для применения назначенных групп завершить текущие сеансы пользователей ivanov и petrov. 
# Начать новые сеансы от имени  пользователей ivanov и petrov
    #process = subprocess.check_call('/bin/sh', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)

    #process = subprocess.check_call('sudo su ivanov', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)

    #sudo su ivanov -c /bin/sh
    process = subprocess.check_call('/usr/bin/gnome-terminal', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    time.sleep(1)
    pyautogui.PAUSE = 0.5
    pyautogui.write('sudo su ivanov')
    pyautogui.PAUSE =0.5
    process = pyautogui.press('Enter')
    pyautogui.PAUSE = 0.5
    pyautogui.write('id')
    pyautogui.PAUSE =0.5
    pyautogui.press('Enter')



    process1 = subprocess.Popen('id', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)

    """
    process = subprocess.Popen(' sudo su ivanov', shell=True,
                                stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    process1=process.communicate()
    print process1
    process1 = subprocess.Popen('id', shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
    process2=process1.communicate()
    print process2[0].encode('utf-8')
    process.wait()
    """
    #time.sleep(8)

    """
# Пользователями ivanov и petrov повторить попытки чтения, записи, запуска файлов в каталоге tst_fldr.
    condition_tests = 2
    index_list = test_1(index_list, condition_tests, Output_tests)
    print "Тест г - выполнен"
    Output_tests.append("\033[32mТест г - выполнен\033[0m")
    index_list +=1  
    """   
    return()