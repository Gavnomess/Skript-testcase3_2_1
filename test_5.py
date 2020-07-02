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