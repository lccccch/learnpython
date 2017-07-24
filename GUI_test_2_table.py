from Tkinter import *
from Tkinter import Tk
import sys
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        self.t=master
        self.createWidgets()
        self.lock1=0
        self.lock2=0
    def createWidgets(self):
        self.tb=Tk.Notebook(self,height=200,width=300)
        self.tree = Tk.Treeview(self)
        ysb = Tk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = Tk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text='Path', anchor='w')
        path=['��ҳ','ע��']
        root_node = self.tree.insert('', 'end', text='����', open=True)
        self.process_directory(root_node, path)
        #����һ��grid
        self.tree.grid(row=0, column=0,sticky='n')
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        self.tb.grid(row=0,column=2)
        self.grid()
        self.tree.bind('<<TreeviewSelect>>',self.func)
    def process_directory(self, parent, path):
        #����·���µ���Ŀ¼
        for p in path:
            oid = self.tree.insert(parent, 'end', text=p, open=False)
    def func(self,event):
        #���ض���ΪTuple
        select=self.tree.selection()
        select=select[0]
        if select=='I002' and self.lock1==0:
            lable=Label(text='��ӭ��½��',fg='black')
            self.tb.add(lable,text='��ҳ')
            self.lock1=1
        if select=='I003' and self.lock2==0:
            self.child=Frame(self.t)
            self.name=StringVar()
            self.name.set('����')
            self.psw=StringVar()
            self.psw.set('����')
            lb=Label(self.child,text='�û���',fg='black')
            lb.grid(row=0,column=0,pady=15,padx=10,sticky='se')
            name=Entry(self.child)
            name['textvariable']=self.name
            name.grid(row=0,column=1)
            la=Label(self.child,text='����',fg='black')
            la.grid(row=1,column=0,padx=10,sticky='se')
            psw=Entry(self.child)
            psw['textvariable']=self.psw
            psw.grid(row=1,column=1)
            style=Tk.Style()
            style.map("C.TButton",foreground=[('pressed', 'red'), ('active', 'blue')],
            background=[('pressed', '!disabled', 'black'), ('active', 'white')])
            btn1=Tk.Button(self.child,text='�ύ',style='C.TButton',command=self.submit)
            btn2=Tk.Button(self.child,text='����',style='C.TButton',command=self.reset)
            btn1.grid(row=2,column=0,pady=10,padx=10,sticky='e')
            btn2.grid(row=2,column=1)
            self.tb.add(self.child,text='�޸�����')
            self.lock2=1
    def submit(self):
        fp=open('1.txt','w')
        if self.name.get()!='':
            fp.writelines(self.name.get()+'\n')
        if self.psw.get()!='':
            fp.writelines(self.psw.get())
        fp.close()
    def reset(self):
        self.name.set('')
        self.psw.set('')
root=Tk()
app=Application(root)
app.mainloop()
