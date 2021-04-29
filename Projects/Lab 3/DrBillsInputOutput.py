#----------------------------------------------------------------------
# Dr. Bill's Input/Output library
#----------------------------------------------------------------------

from tkinter import *
from tkinter import filedialog, simpledialog, messagebox, colorchooser

root = Tk()             # Initialize Tk, but...
root.withdraw()         # ...hide the GUI window.

MyFileMask = [("All Files", "*.*"), ("Text Files", "*.txt")]

#----------------------------------------------------------------------

def pickAFolder(MyTitle="Pick A Folder"):
    return filedialog.askdirectory(initialdir="", title=MyTitle)
                                            
#----------------------------------------------------------------------

def pickAFile(MyTitle="Pick A File"):
    return filedialog.askopenfilename(initialdir="", title=MyTitle, filetypes=MyFileMask)

#----------------------------------------------------------------------

def saveAFile(MyTitle="Save A File", MyDefaultExtension=".txt", MyInitialFile="Default"):
    return filedialog.asksaveasfilename(initialdir="",              \
                                        title=MyTitle,              \
                                        filetypes=MyFileMask,       \
                                        initialfile=MyInitialFile,  \
                                        defaultextension=MyDefaultExtension)

#----------------------------------------------------------------------

def requestString(Message=""):
    return simpledialog.askstring("INPUT STRING",Message)

#----------------------------------------------------------------------

def requestIntegerInRange(Message="", MyLowValue=0, MyHighValue=100):
    Caption = "ENTER INTEGER [" + str(MyLowValue) + "..." + str(MyHighValue) + "]"
    Result = simpledialog.askinteger(Caption, Message, minvalue=MyLowValue, maxvalue=MyHighValue) 
    while (Result != None) and ((Result < MyLowValue) or (Result > MyHighValue)):
        Result = simpledialog.askinteger(Caption, Message, minvalue=MyLowValue, maxvalue=MyHighValue)
    return Result

#----------------------------------------------------------------------
    
def requestFloatInRange(Message="", MyLowValue=0.0, MyHighValue=100.0):
    Caption = "ENTER FLOAT [" + str(MyLowValue) + "..." + str(MyHighValue) + "]"
    Result = simpledialog.askfloat(Caption, Message, minvalue=MyLowValue, maxvalue=MyHighValue) 
    while (Result != None) and ((Result < MyLowValue) or (Result > MyHighValue)):
        Result = simpledialog.askfloat(Caption, Message, minvalue=MyLowValue, maxvalue=MyHighValue)
    return Result

#----------------------------------------------------------------------
    
def showWarning(Message=""):
    messagebox.showwarning("WARNING",Message)
    return

#----------------------------------------------------------------------
    
def showError(Message=""):
    messagebox.showerror("ERROR",Message)
    return

#----------------------------------------------------------------------
    
def showInformation(Message=""):
    messagebox.showinfo("INFORMATION",Message)
    return

#----------------------------------------------------------------------
    
def pickAColor(MyInitialColor=(0,0,0)):
    RGB, HTML = colorchooser.askcolor(initialcolor=MyInitialColor)
    return [[int(X) for X in RGB], HTML.upper()]

#----------------------------------------------------------------------
    
