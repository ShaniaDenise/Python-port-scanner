import socket
import datetime

scn_fl = open("YourScanHere.txt", "w")
scn_fl.write("Shania's Port Scanner \n")

user_input = input("Type host here:")

host_ip = socket.gethostbyname(user_input)

starttime = datetime.datetime.now()
scn_fl.write("Started scan at: " + str(starttime) + "\n \n")


i = 1025

while i <=1025:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con = s.connect_ex((host_ip, i))
    print(str(con) + "" + str(i))
    if con == 0:
        print("port {} is open".format(i))
        scn_fl.write("Port {} is open".format(i))
    if con == 10013:
        print("Permission is denied")
    if con == 8:
        print("Insufficient memory")
    if con == 10022:
        print("Bad address")
    else:
        print("this port is closed")

    i += 1
    endtime = datetime.datetime.now()
    scn_fl.write(" Finished scan at: " + str(endtime) + "\n \n")



    totaltime = endtime - starttime


timelist = str(totaltime).split(":")
float(timelist[-1])
print("This scan took {:.4} seconds".format(timelist[-1]))

scn_fl.close()


