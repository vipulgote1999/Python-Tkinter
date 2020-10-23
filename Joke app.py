import tkinter as tk
import pyjokes
master=tk.Tk()
master.geometry("400x300")
master.configure(bg="blue")
master.title("Jokes Game In python")

def joke():
    global joke
    joke=pyjokes.get_joke()
    clear()
    T.insert(tk.END,joke)

def clear():
    T.delete("1.0","end")

T=tk.Text(master)
T.place(x=5,y=5,height=80,width=290)
b=tk.Button(master,text="joke",fg="white",bg="red",command=joke)
b.place(x=35,y=100,height=50,width=100)
b2=tk.Button(master,text="clear",fg="white",bg="red",command=clear)
b2.place(x=180,y=100,height=50,width=100)

master.mainloop()