#
import collections
import sys

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)
User = collections.namedtuple("User", "username forename middlename surname id")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(sys.argv[0]))
        sys.exit()
   
    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forename.lower(), user.id)] = user
    print_users(users)

def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    return user

def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace("-", "").replace("'", ""))    
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames: 
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username

def print_users(users):
    namewidth = 17
    usernamewidth = 9
    linecount = 0
    usercount = 0

    for key in sorted(users):

        if linecount % 64 == 0 or linecount == 0:
            print("\n")
            print_headers(namewidth, usernamewidth)
            linecount += 2
        
        if usercount % 2 == 0:
            user2 = User
            name2 = ""
            user1 = users[key]
            initial1 = ""
            if user1.middlename:
                initial1 = " " + user1.middlename[0]
            name1 = "{0.surname}, {0.forename}{1}".format(user1, initial1)
            name1 = name1[:namewidth]
        else:
            user2 = users[key]
            initial2 = ""
            if user2.middlename:
                initial2 = " " + user2.middlename[0]
            name2 = "{0.surname}, {0.forename}{1}".format(user2, initial2)
            name2 = name2[:namewidth]

        usercount += 1
        if usercount % 2 == 0:
            print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}     {2:.<{nw}} ({3.id:4}) {3.username:{uw}}".format(name1, user1, name2, user2, nw=namewidth, uw=usernamewidth))    
        elif usercount == len(users) and usercount % 2 == 1:
            print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(name1, user1, nw=namewidth, uw=usernamewidth))    
            
        linecount += 1     

def print_headers(namewidth, usernamewidth):
    print("{0:<{nw}} {1:^6} {2:{uw}}     {0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth))
    print("{0:-<{nw}} {0:-<6} {0:-<{uw}}     {0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth))
        
main()