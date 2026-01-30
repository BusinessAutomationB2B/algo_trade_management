# https://stackoverflow.com/questions/45473003/read-username-and-password-from-a-file

def get_id_password():
    f=open("/home/tester/Documents/account.txt","r")
    lines=f.readlines()
    # lines[0] is the comment line, and remember to remove '\n'
    username=lines[1]
    password=lines[2]

    # https://pythonadventures.wordpress.com/2010/10/11/chomp-functionality-in-python/
    username = username.replace('\n', '')    # remove '\n' only
    userpassword = username.replace('\n', '')    # remove '\n' only
    # print(username)
    # print(password)
    f.close()
    return(username,password)

if __name__ == '__main__':
    id,pw = get_id_password()
    print(id)
    print(pw)
    
    
