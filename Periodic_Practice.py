from tkinter import *

root = Tk()
table = Frame(root, width=100, height=100)
table.pack()

table.winfo_geometry("250x200+X+Y")

rows = 7
cols = 18
atomic_num = 1
new_col = 0
for i in range(rows):
    #new_col = 1
    for ii in range(cols):
        New_Button = Button(table, text= atomic_num, width = 5, height = 5, fg="red")
       # print(i, " ", ii)
        # if new_col == 1:
        #     New_Button.pack(side= LEFT)
        # else:
        #     New_Button.pack(side= TOP)
        # new_col = 0
        New_Button.grid(row = i, column = ii)
        atomic_num+=1

root.mainloop()