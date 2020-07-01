# coding: utf8
#print sys.path
#sys.path.append('/home/123/project_python')
import sourcetestcase
import string
import subprocess
import pyautogui
import time
import sys

#import source_testcase3_2_1

indexlist = 0

loop = True
while loop == True:
    print '==================================================='
    print                  'Тест кейсы'
    print '==================================================='
    print '               ВЫБОР ДЕЙСТВИЙ'
    print '==================================================='
    print ' 1 - Запуск тест кейса 3.2.1 (Дискреционное управление доступом — общий механизм)'
    print ' 2 - Выход'
    print '==================================================='
    response = raw_input('Введите цифру')
    if response == '1': # 
        sourcetestcase.testcase3_2_1(indexlist)
        for indexlist in sourcetestcase.Output_tests:
            print indexlist.encode('utf-8')
        print '\033[32mВсе тесты закончены\033[0m'
    elif response == '2': # Выход
        loop = False
        print 'Тест закончен'        
    elif (response != '1') and (response != '2'):
        print 'Неизвестная команда'
        