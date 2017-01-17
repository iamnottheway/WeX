

try:
	from tkinter import *
except IOError:
	from Tkinter import *
	print("Importing from python2")


class UI_Class(object):

	def __init__(self,master):
		self.master = master
		self.master.title("Heizenberg")
		self.master.geometry("450x600+400+100")
		self.master.config(bg = '#ffffff')
		self.master.resizable(0,0)
		self.Add_Widgets()

	def Add_Widgets(self):

		"""

		This class  method adds UI to the add.

		contains the eye-catching UI :P 

		self.addNavigationBar creates a display navigation bar to dispplay the app name

		"""

		self.addNavigationBar = Frame(self.master,width = 450,height = 75,bg = "#333")
		self.addNavigationBar.grid(column = 1,row = 1)

		self.appNameStylized = Label(self.master,bg = "#333",text = "Heizenberg",font = ("Laksaman",18),fg = "#31d647")
		self.appNameStylized.grid(column = 1,row = 1,padx = 0,pady = 0,ipadx = 20,ipady = 10,sticky = W+S+N)

		self.displayTextBox = Text(self.master,bg = "#ffffff",font = ("Arial",12),fg = "#31b5d6",bd = 0,highlightbackground = '#ffffff',\
			state = DISABLED,cursor = 'arrow')
		self.displayTextBox.grid(column = 1,row = 2)

		self.searchBox = Entry(self.master, width = 30,bd = 0,highlightbackground = '#31b5d6',highlightcolor = "#31b5d6",font = ("Laksaman",10),fg = "#333")
		self.searchBox.grid(column = 1,row = 3,padx = 10,pady = 10,ipadx = 10,ipady = 10,sticky = W)

		self.searchButton = Button(self.master,text = "Send",width = 10,height = 3,bd = 0,bg = "#3191d6",activebackground = "#31b5d6",\
			fg = "white",activeforeground = "white",cursor = 'hand2',command = self.Process_Input)
		self.searchButton.grid(column = 1,row = 3,padx = 1,pady = 3)

	def Process_Input(self):
		self.textInput = self.searchBox.get() # store (the input text to check if the string is empty
		if self.textInput == " " or None:
			""" If the input is empty, it does nothing"""
			pass
		else:
			""" If there is something as input, displays it in the displayBox"""
			self.textInput +='\n'
			self.displayTextBox.insert(END,self.textInput)





def main():
	app = Tk()
	Win = UI_Class(app)
	app.mainloop()


if __name__ == '__main__':
	main()