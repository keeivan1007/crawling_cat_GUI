def image_load():#圖片載入
    import tkinter as tk
    from PIL import Image, ImageTk  # pillow 模块

    root=tk.Tk() 
    s=r'cat.jpg' # jpg圖片名跟路徑
    im=Image.open(s)
    tkimg=ImageTk.PhotoImage(im) #執行此函數前 Tk必須先實例化
    l=tk.Label(root,image=tkimg)
    l.pack()

    label =tk.Label(root,text="開始執行：喵咪載圖程式")
    label.pack()
    #label.place( height=100, width=100)

    root.mainloop()



def image_area():
    #視窗區塊
    import tkinter as tk
    win = tk.Tk()
    frame1 = tk.Frame(win)
    frame1.pack()
    label1 = tk.Label(frame1,text="標籤一")
    entry1 =tk.Entry(frame1)
    label1.grid(row=0,column=0)
    entry1.grid(row=0,column=1)

    frame2 = tk.Frame(win)
    frame2.pack()
    button1 =tk.Button(frame2,text="確定")
    button2 =tk.Button(frame2,text="取消")
    button1.grid(row=0,column=0)
    button2.grid(row=0,column=1)
    win.mainloop()




def choose(): #複選題
    global choice, ball
    str = "你喜歡的球類運動："
    for i in range(0,len(choice)):
        if (choice[i].get() == 1):
            str = str + ball[i] + " "
            msg.set(str)
            
    import tkinter as tk

    win = tk.Tk()
    choice = []
    ball = ["足球","籃球","棒球"]
    msg = tk.StringVar()
    label =tk.Label(win,text="選擇喜歡的球類運動：")
    label.pack()
    for i in range(0,len(ball)):
        tem = tk.IntVar()
        choice.append(tem)
        item = tk.Checkbutton(win,text=ball[i],variable=choice[i],command=choose)
        item.pack()
    lblmsg = tk.Label(win,fg="red",textvariable=msg)
    lblmsg.pack()
    win.mainloop()

#單選題
def choose():
    msg.set("你最喜歡的球類運動："+choice.get())
    
    import tkinter as tk

    win = tk.Tk()
    choice = tk.StringVar()
    msg = tk.StringVar()
    label = tk.Label(win,text="選擇最喜歡的球類運動")
    label.pack()
    item1 = tk.Radiobutton(win,text="足球",value="足球",variable=choice,command=choose)
    item1.pack()
    item2 = tk.Radiobutton(win,text="籃球",value="籃球",variable=choice,command=choose)
    item2.pack()
    item3 = tk.Radiobutton(win,text="棒球",value="棒球",variable=choice,command=choose)
    item3.pack()

    lblmsg = tk.Label(win,fg="red",textvariable=msg)
    lblmsg.pack()
    item1.select()
    choose()
    win.mainloop()