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
        sourcetestcase.testcase3_2_1(sourcetestcase.index_list)
        for sourcetestcase.index_list in sourcetestcase.Output_tests:
            print sourcetestcase.index_list.encode('utf-8')
        print 'Все тесты закончены'
    elif response == '2': # Выход
        loop = False
        print 'Тест закончен'        
    elif (response != '1') and (response != '2'):
        print 'Неизвестная команда'
        