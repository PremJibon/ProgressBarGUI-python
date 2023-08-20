from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 10
    download = 0
    while(download < GB):
        time.sleep(1)
        bar['value']+=10
        download+=1
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+"GB Completed")
        window.update_idletasks()

window = Tk()
window.title("Progress Bar Model")

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)


percent= StringVar()
percentLabel = Label(window,textvariable=percent).pack()

text = StringVar()
textLabel = Label(window,textvariable=text).pack()

button = Button(window,text='Download',command=start).pack()

window.mainloop()
