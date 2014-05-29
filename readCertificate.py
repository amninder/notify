f = open('Certificates.pem','r')
string = ""
while 1:
    line = f.readline()
    if not line:break
    string += line

f.close()


print string