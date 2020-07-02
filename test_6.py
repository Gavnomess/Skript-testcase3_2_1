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