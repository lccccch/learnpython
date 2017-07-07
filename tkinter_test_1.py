from Tkinter import *
class Application(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.creteWidgets()

  def createWidgets(self):
    self.helloLabel = Label(self, text='Hello, world!')
    self.helloLabel.pack()
    self.quitButton = Buffton(self, text='Quit', command=self.quir())
    self.quitButton.pack()
