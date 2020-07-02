def test_8():  #Тест з

# Сменить владельца каталогов  dir_exec,  dir_read. dir_wr,  dir_wr_read назначив новым владельцем пользователя root и назначив группу владельца audio:
    process = subprocess.check_call('sudo chown root:audio /tmp/dir_exec/', shell=True)
    process = subprocess.check_call('sudo chown root:audio /tmp/dir_read/', shell=True)
    process = subprocess.check_call('sudo chown root:audio /tmp/dir_wr/', shell=True)
    process = subprocess.check_call('sudo chown root:audio /tmp/dir_wr_read/', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.check_call('ls -l /tmp/', shell=True)
    print "Тест з - выполнен" 
    return()