###################################
#    Created on Aug 9, 2015
#
#    @author: Grant Mercer
#
###################################
from Tkconstants import FLAT, RIGHT, LEFT
import collections
import tkFileDialog
import tkMessageBox
from Tkinter import *

class PropertyDialog(Toplevel):
    def __init__(self, root, string):
        Toplevel.__init__(self)
        self.wm_overrideredirect(1)
        self.\
             geometry('+%d+%d' %
                      (root.winfo_pointerx() - 60,
                       root.winfo_pointery()))
        try:
            self.tk.call('::Tk::unsupported::MacWindowStyle',
                                         'style', self._w,
                                         'help', 'noActivates')
        except TclError:
            pass
        window_frame = Frame(self)
        window_frame.pack(side=TOP, fill=BOTH, expand=True)
        exit_frame = Frame(window_frame, background='#ffffe0')
        exit_frame.pack(side=TOP, fill=X, expand=True)
        button = Button(exit_frame, text='x', width=3, command=self.free,
               background='#ffffe0', highlightthickness=0, relief=FLAT)
        button.pack(side=RIGHT)
        text_frame = Frame(window_frame)
        text_frame.pack(side=TOP, fill=BOTH, expand=True)
        label = Label(text_frame, text=string, justify=LEFT,
                      background='#ffffe0',
                      font=('tahoma', '8', 'normal'))
        label.pack(ipadx=1)

    def free(self):
        self.destroy()

def create():
    t = PropertyDialog(root, 'this')
    return

root = Tk()

Button(root, text='create', command=create).pack()

root.mainloop()