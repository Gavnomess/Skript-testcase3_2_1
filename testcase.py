#import apsw
import string
import subprocess



def precondition(): # создание предварительных настроек

#process = subprocess.Popen('cd /tmp', shell=True)
    process = subprocess.call('mkdir /tmp/dir_wr', shell=True)
    process = subprocess.call('mkdir /tmp/dir_read', shell=True)
    process = subprocess.call('mkdir /tmp/dir_exec', shell=True)
    process = subprocess.call('mkdir /tmp/dir_wr_read', shell=True)

    process = subprocess.call('chmod 330 /tmp/dir_wr/', shell=True)
    process = subprocess.call('chmod 440 /tmp/dir_read/', shell=True)
    process = subprocess.call('chmod 660 /tmp/dir_wr_read/', shell=True)
    process = subprocess.call('chmod 110 /tmp/dir_exec/', shell=True)

    process = subprocess.call('ls -l /tmp/', shell=True)

    process = subprocess.call('mkdir /tmp/tst_fldr/', shell=True)

    process = subprocess.call('touch /tmp/tst_fldr/read_only.txt', shell=True)
    process = subprocess.call('touch /tmp/tst_fldr/write_only.txt', shell=True)
    process = subprocess.call('touch /tmp/tst_fldr/exec_only.sh', shell=True)
    process = subprocess.call('touch /tmp/tst_fldr/rw.txt', shell=True)

    process = subprocess.call('chmod 440 /tmp/tst_fldr/read_only.txt', shell=True)
    process = subprocess.call('chmod 220 /tmp/tst_fldr/write_only.txt', shell=True)
    process = subprocess.call('chmod 660 /tmp/tst_fldr/rw.txt', shell=True)
    process = subprocess.call('chmod 550 /tmp/tst_fldr/exec_only.sh', shell=True)

    process = subprocess.call('ls -l /tmp/tst_fldr/', shell=True)
    print "Начальные настройки выполнены"
    return()

def test_1():  #Тест а
    
    process = subprocess.call('exit', shell=True)
# пользователями ivanov и petrov просмотреть содержимое файлов в каталоге tst_fldr
    process = subprocess.call('cat /tmp/tst_fldr/read_only.txt', shell=True)
    process = subprocess.call('cat /tmp/tst_fldr/rw.txt', shell=True)
    process = subprocess.call('cat /tmp/tst_fldr/write_only.txt', shell=True)
    process = subprocess.call('cat /tmp/tst_fldr/exec_only.sh', shell=True)
# пользователями ivanov и petrov записать текст в файлы каталога  tst_fldr:
    process = subprocess.call("echo 'txt' > /tmp/tst_fldr/read_only.txt", shell=True)
    process = subprocess.call("echo 'txt' > /tmp/tst_fldr/rw.txt", shell=True)
    process = subprocess.call("echo 'txt' > /tmp/tst_fldr/write_only.txt", shell=True)
    process = subprocess.call("echo 'txt' > /tmp/tst_fldr/exec_only.sh", shell=True)
# пользователями ivanov и petrov выполнить файлы каталога  tst_fldr:
    process = subprocess.call('/tmp/tst_fldr/exec_only.sh', shell=True)
    process = subprocess.call('/tmp/tst_fldr/rw.txt', shell=True)
    process = subprocess.call('/tmp/tst_fldr/write_only.txt', shell=True)
    process = subprocess.call('/tmp/tst_fldr/read_only.txt', shell=True)
    print "Тест а - выполнен"
    return()

def test_2():  #Тест б
    process = subprocess.Popen('logname', shell=True,
                                   stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
    #process = subprocess.call('sudo -i', shell=True)
# Пользователем root назначить владельцем каталога tst_fldr и всех файлов в нем пользователя ivanov:  
    process = subprocess.call('sudo chown -R '+username[0]+' /tmp/tst_fldr/', shell=True)
# Проверить правильность назначенных прав:   
    process = subprocess.call('ls -l /tmp/tst_fldr/', shell=True)
# Владельцем всех созданных файлов является пользователь ivanov.
# Пользователями ivanov и petrov повторить попытки чтения, записи, запуска файлов в каталоге tst_fldr
    #process = subprocess.call('exit', shell=True)
    test_1()
    print "Тест б - выполнен"
    return()

def test_3():  #Тест в
    process = subprocess.Popen('logname', shell=True,
                                   stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
    #process = subprocess.call('sudo -i', shell=True)
# Пользователем root назначить владельцем каталога tst_fldr и всех файлов в нем пользователя root, группой владельца назначить ivanov:
    process = subprocess.call('sudo chown -R root:'+username[0]+' /tmp/tst_fldr/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.call('ls -l /tmp/tst_fldr/', shell=True)
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
    process = subprocess.call('sudo usermod -a -G audio '+username[0], shell=True)
# Пользователем root назначить владельцем каталога tst_fldr и всех файлов в нем пользователя root, группой владельца назначить audio:
    process = subprocess.call('sudo chown -R root:audio /tmp/tst_fldr/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.call('ls -l /tmp/tst_fldr/', shell=True)  
# Для применения назначенных групп завершить текущие сеансы пользователей ivanov и petrov. 
# Начать новые сеансы от имени  пользователей ivanov и petrov
    process = subprocess.call('exit', shell=True)
# Убедиться, что новая группа доступна пользователю:
    process = subprocess.call('id', shell=True)
# Пользователями ivanov и petrov повторить попытки чтения, записи, запуска файлов в каталоге tst_fldr.
    test_1()
    print "Тест г - выполнен"     
    return()

def test_5():  #Тест д

# Пользователями ivanov и petrov просмотреть содержимое каталогов:
    process = subprocess.call('ls -l /tmp/dir_exec/', shell=True) 
    process = subprocess.call('ls -l /tmp/dir_read/', shell=True)
    process = subprocess.call('ls -l /tmp/dir_wr/', shell=True)
    process = subprocess.call('ls -l /tmp/dir_wr_read/', shell=True)
# Пользователями ivanov и petrov в каждом каталоге создать файл test.txt:
    process = subprocess.call('touch /tmp/dir_exec/test.txt', shell=True)
    process = subprocess.call('touch /tmp/dir_read/test.txt', shell=True)
    process = subprocess.call('touch /tmp/dir_wr/test.txt', shell=True)
    process = subprocess.call('touch /tmp/dir_wr_read/test.txt', shell=True)
# Пользователями ivanov и petrov сменить текущий каталог:
    process = subprocess.call('cd /tmp/dir_exec/', shell=True)
    process = subprocess.call('cd /tmp/dir_read/', shell=True)
    process = subprocess.call('cd /tmp/dir_wr/', shell=True)
    process = subprocess.call('cd /tmp/dir_wr_read/', shell=True)
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
    process = subprocess.call('sudo chown '+username[0]+' /tmp/dir_exec/', shell=True)
    process = subprocess.call('sudo chown '+username[0]+' /tmp/dir_read/', shell=True)
    process = subprocess.call('sudo chown '+username[0]+' /tmp/dir_wr/', shell=True)
    process = subprocess.call('sudo chown '+username[0]+' /tmp/dir_wr_read/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.call('ls -l /tmp/', shell=True)  
# Пользователями ivanov и petrov просмотреть содержимое каталогов, в каждом каталоге создать файл test.txt,  сменить текущий каталог.
    process = subprocess.call('touch /tmp/dir_exec/test.txt', shell=True)
    process = subprocess.call('touch /tmp/dir_read/test.txt', shell=True)
    process = subprocess.call('touch /tmp/dir_wr/test.txt', shell=True)
    process = subprocess.call('touch /tmp/dir_wr_read/test.txt', shell=True)

    process = subprocess.call('cd /home', shell=True)
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
    process = subprocess.call('sudo chown '+username[0]+' /tmp/dir_exec/', shell=True)
    process = subprocess.call('sudo chown '+username[0]+' /tmp/dir_read/', shell=True)
    process = subprocess.call('sudo chown '+username[0]+' /tmp/dir_wr/', shell=True)
    process = subprocess.call('sudo chown '+username[0]+' /tmp/dir_wr_read/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.call('ls -l /tmp/', shell=True)
    print "Тест ж - выполнен"    
    return()

def test_8():  #Тест з

# Сменить владельца каталогов  dir_exec,  dir_read. dir_wr,  dir_wr_read назначив новым владельцем пользователя root и назначив группу владельца audio:
    process = subprocess.call('sudo chown root:audio /tmp/dir_exec/', shell=True)
    process = subprocess.call('sudo chown root:audio /tmp/dir_read/', shell=True)
    process = subprocess.call('sudo chown root:audio /tmp/dir_wr/', shell=True)
    process = subprocess.call('sudo chown root:audio /tmp/dir_wr_read/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.call('ls -l /tmp/', shell=True)
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
    process = subprocess.call('touch /tmp/ivanov.file', shell=True)
# Назначить ему права с полным доступом для всех пользователей и дополнительным атрибутом Sticky bit:    
    process = subprocess.call('chmod 1777 /tmp/ivanov.file', shell=True)
# Пользователем root сменить группу владельца файла на общедоступную для пользователей ivanov и petrov:    
    process = subprocess.call('sudo chown '+username[0]+':audio /tmp/ivanov.file', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.call('ls -l /tmp/', shell=True)
# Пользователем ivanov удалить  файл ivanov.file:
    process = subprocess.call('rm -f /tmp/ivanov.file', shell=True)
    print "Тест и - выполнен"
    return()

def testcase3_2_1 (): #Тест кейс 3.2.1
    precondition()

    test_1()
     
    test_2()
    
    test_3()
 
    test_4()
    
    test_5()
     
    test_6()
    
    test_7()
     
    test_8()
     
    test_9()

    return()




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
        testcase3_2_1()
        print 'Все тесты закончены'
    elif response == '2': # Выход
        print 'Тест закончен'
        loop = False
            
    elif (response != '1') and (response != '2'):
        print 'Неизвестная команда'