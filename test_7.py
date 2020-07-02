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