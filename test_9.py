def test_9():  #Тест и

    process = subprocess.Popen('logname', shell=True,
                                   stdout = subprocess.PIPE, 
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    username = process.communicate()
    username = [line.rstrip() for line in username]
# Пользователем ivanov создать файл:
    process = subprocess.check_call('touch /tmp/ivanov.file', shell=True)
# Назначить ему права с полным доступом для всех пользователей и дополнительным атрибутом Sticky bit:    
    process = subprocess.check_call('chmod 1777 /tmp/ivanov.file', shell=True)
# Пользователем root сменить группу владельца файла на общедоступную для пользователей ivanov и petrov:    
    process = subprocess.check_call('sudo chown '+username[0]+':audio /tmp/ivanov.file', shell=True)
# Проверить правильность назначенных прав:
    process = subprocess.check_call('ls -l /tmp/', shell=True)
# Пользователем ivanov удалить  файл ivanov.file:
    process = subprocess.check_call('rm -f /tmp/ivanov.file', shell=True)
    print "Тест и - выполнен"
    return()