import speedtest
import tkinter as tk
from tkinter import messagebox

def testing():
    st=speedtest.Speedtest()
    print("your Downlode speed is :",st.download()//10**6,"Mbps")
    print("your uplode speed is :",st.upload()//10**6,"Mbps")
    print("your ping speed is :",st.results.ping,"ms")


def do_something():
    messagebox.showinfo("confirmation",'''speed Test Starting......
                        it may take upto 1 min ''')
    print("speed Test Starting please wait it may take upto 1 min")

    d.configure(text=str(st.download()//10**6)+"Mbps")
    u.configure(text=str(st.upload()//10**6)+"Mbps")
    p.configure(text=str(int(st.results.ping))+" ms")
    l.configure(text="Speed Test")
    
def design():
    master1=tk.Tk()
    master1.geometry("400x350")
    master1.configure(bg="black")
    
    font=("Verdana",15,"bold")
    global d,u,p,l
    dspeed=tk.Label(master=master1,text="Downlode speed",fg="orange",bg="black",font=font).place(x=10,y=10)
    d=tk.Label(master=master1,text="0 Mbps",fg="orange",bg="black",font=font)
    d.place(x=250,y=10)
    
    uspeed=tk.Label(master=master1,text="Uplode speed",fg="orange",bg="black",font=font).place(x=10,y=50)
    u=tk.Label(master=master1,text="0 Mbps",fg="orange",bg="black",font=font)
    u.place(x=250,y=50)

    ping=tk.Label(master=master1,text="Ping",fg="orange",bg="black",font=font).place(x=10,y=90)
    p=tk.Label(master=master1,text="0 ms",fg="orange",bg="black",font=font)
    p.place(x=250,y=90)

    l=tk.Label(master=master1,text="Click here to run Speed Test",bg="black",fg="orange",font=font)
    l.place(x=50,y=250)
    
    b1=tk.Button(master=master1,text="Speed Test",fg="orange",bg="black",command=do_something).place(x=50,y=300,height=40,width=300)
    master1.mainloop()


if __name__ == "__main__":
    st=speedtest.Speedtest()
    #testing()
    design()
