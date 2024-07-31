from tkinter import *
from tkinter import filedialog

a= Tk()
a.title("Notepad")
a.geometry("500x600")


def closeapp():
    a.destroy()

def open_file():
    file=filedialog.askopenfile(mode="r",defaultextension="txt",filetypes=[("Text file",".txt"),("All Files",".*.*")])
    if file is not None:
        Text_area.delete("1.0",END)
        Text_area.insert("1.0",file.read())
        file.close()

def save_file():
    file=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=[("text file",".txt"),("All Files","*.*")])
    if file is not None:
        file.write(Text_area.get("1.0",END))
        file.close()

def create_new_file():
    Text_area.delete("1.0",END)
def copy_selected_text():
    try:
        selected_text=Text_area.get(SEL_FIRST,SEL_LAST)
        a.clipboard_clear()
        a.clipboard_append(selected_text)
    except TclError:
        pass
def paste_text():
    try:
        text =a.clipboard_get()
        Text_area.insert("insert",text)
    except TclError:
        pass

def cut_selected_text():
    try:
        copy_selected_text()
        Text_area.delete(SEL_FIRST,SEL_LAST)
    except TclError:
        pass




menulist=Menu(a)

filemenu=Menu(menulist,tearoff=0)
menulist.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New File",command=create_new_file)
filemenu.add_separator()
filemenu.add_command(label="Open file",command=open_file)
filemenu.add_command(label="Open Folder")
filemenu.add_separator()
filemenu.add_command(label="Save",command=save_file)
filemenu.add_command(label="Exit",command=closeapp)

editmenu=Menu(menulist,tearoff=False)
menulist.add_cascade(label="Edit",menu=editmenu)    
editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_separator()
editmenu.add_command(label="Cut",command=cut_selected_text)
editmenu.add_command(label="copy",command=copy_selected_text)
editmenu.add_command(label="Paste",command=paste_text)
a.config(menu=menulist)



Text_area= Text(a)
Text_area.pack(fill=BOTH, expand=1)




a.mainloop()