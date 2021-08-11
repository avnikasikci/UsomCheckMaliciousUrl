from tkinter import * # thkinter bütün methodlarını ekle
import datetime # log için grekli


def run_check():
    file = open("usom.txt", "r")  # r read file
    content = file.read()
    file.close()
    ip = entry1.get()
    today = datetime.datetime.now()
    if (str(ip)) in content:
        file = open("log.txt", "a")#append mode
        logStr = str(ip) + " " + "malicius\n Date:" + str(today) + "\n"
        file.write(logStr)
        file.close()
        v.set("Malicius Ip")
    else:
        file = open("log.txt", "a")
        logStr = str(ip) + " " + "not malicius\n Date:" + str(today) + "\n"
        file.write(logStr)
        file.close()
        v.set("Not Malicius İp")

top=Tk()
top.title("Usom Check Ip")
ButtonCheck=Button(top,text="Check",command=run_check)
ButtonCheck.place(x=50,y=50)
ButtonCheck.pack()
label1=Label(top,text="Please, input check ip: ")
label1.place(x=50,y=80)
label1.pack()
entry1=Entry(top)
entry1.place(x=50,y=90)
entry1.pack()
v=StringVar()
entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=100)
entry2.pack()
top.mainloop()


