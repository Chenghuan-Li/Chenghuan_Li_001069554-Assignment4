# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from socket import socket,AF_INET, SOCK_STREAM
s = socket(AF_INET,SOCK_STREAM)
server = ('127.0.0.1',8888)
s.connect(server)
data = s.recv(1024)
print("received",data,"from")
str1 = "HELLO li.chenghu\n"
s.send(str1.encode())
done = True
while done:
    data = s.recv(1024)
    data2 = data.decode()
    print(data2)
    if data2[0] == "M":
        data = data2.replace('\n', '').replace('\r', '')
        num1 = int(data2.split()[1])
        num2 = int(data2.split()[3])
        oper = data2.split()[2]
        if(oper == "+"):
            str2="ANSWER "+str(num1+num2)+"\n"
            print(str2)
            s.send(str2.encode())
        elif(oper == "-"):
            str2 = "ANSWER " + str(num1 - num2) + "\n"
            print(str2)
            s.send(str2.encode())
        elif(oper == "*"):
            str2 = "ANSWER " + str(num1 * num2) + "\n"
            print(str2)
            s.send(str2.encode())
        else:
            str2 = "ANSWER " + str(int(num1 / num2)) + "\n"
            print(str2)
            s.send(str2.encode())
    else:
        print(data2)
        done = False
        s.close()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/