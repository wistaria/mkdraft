import getpass, imaplib, sys

if len(sys.argv) != 2:
    print("usage: {} user".format(sys.argv[0]))
    sys.exit(1)

server = 'imap.gmail.com'
user = sys.argv[1]
print("server: {}".format(server))
print("user: {}".format(user))
passwd = getpass.getpass()

m = imaplib.IMAP4_SSL(server, '993')
m.login(user, passwd)
type, data = m.list()
for d in data:
    d = d.decode('utf-8').split(' "/" ')
    if d[0] == '(\\Drafts \\HasNoChildren)':
        print("draft folder: {}".format(d[1].strip('"')))
m.logout()
