import pyshorteners
import tkinter as tk
import os
def addToClipBoard():
    command = 'echo ' + short_url.strip() + '| clip'
    os.system(command)
    lbs=tk.Label(master,text="Shorted URL has been Copyied to clipboard!",fg="yellow",bg="black",font=("Verdana",8,"bold")).place(x=10,y=150)

def clear():
    tx.delete("1.0","end")

def shortner():
    #url=input("Please enter the Url of ")
    url=text.get()
    print("your typed url is ",url)
    s=pyshorteners.Shortener()
    print("your Shortned Url is -> ",s.tinyurl.short(url))
    global short_url
    short_url=s.tinyurl.short(url)
    #lb=tk.Label(master,text=short_url,bg="white",fg="black",font=font).place(x=50,y=200)
    bt2=tk.Button(master,text="Copy to Clipboard",fg="yellow",bg="black",command=addToClipBoard).place(x=100,y=110)
    global tx
    tx=tk.Text(master)
    tx.place(x=50,y=80,height=20,width=200)
    clear()
    tx.insert(tk.END,short_url)


def disp():
    global master
    master=tk.Tk()
    master.title("URL Shortner Python app")
    master.geometry("300x180")
    master.configure(bg="black")
    global font
    font=("Verdana",10,"bold")


    url=tk.Label(master,text="Enter url",fg="yellow",bg="black",font=font).place(x=10,y=10)
    global text
    text=tk.Entry(master,text="enter text",fg="black",bg="white",font=font)
    text.place(x=80,y=10)
    bt=tk.Button(master,text="click to Short Url",fg="yellow",bg="black",command=shortner).place(x=100,y=40)

    master.mainloop()


if __name__ == "__main__":
    disp()
    
