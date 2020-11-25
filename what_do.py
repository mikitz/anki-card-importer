file = open('what_do.txt', mode = 'r')
what_do = file.read()
file.close()
if what_do == 'listening':
    print("Listening Today")
    f = open('what_do.txt', 'w+')
    f.write('reading')
    f.close()
elif what_do == 'reading':
    print("Reading Today")
    f = open('what_do.txt', 'w+')
    f.write('listening')
    f.close()
else:
    pass