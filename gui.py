import tkinter as tk
import guiHelper as GuiHelper

guiObj = 0
     
class Gui:

    window = tk.Tk()
    yearInput = 0
    gpaInput = 0

    def createGui(self):
        try:
            Gui.window.title("Academic Probation Alert")
            Gui.window.protocol("WM_DELETE_WINDOW") 
            Gui.window.resizable(0, 0)
            menu = tk.Menu(self.window)
            Gui.window.config(menu=menu)
            Gui.window.geometry("460x200")
            Gui.window.configure(bg="#323232")
            Gui.window.columnconfigure(0, weight=2)
            Gui.window.columnconfigure(1, weight=1)
            Gui.window.columnconfigure(2, weight=1)
            Gui.window.columnconfigure(3, weight=1)

            l1 = tk.Label(self.window, text='University Of Technology')
            l1.grid(row=0, column=0, columnspan=2)
            l1.configure(bg="#323232")
            l1.configure(fg="#e5e7e9")
            l1.configure(font=('Arial', 25, "bold"))
            l1.configure(anchor="center", justify='center')

            l2 = tk.Label(self.window, text='Academic Probation Alert GPA Report')
            l2.grid(row=1, column=0, columnspan=2)
            l2.configure(bg="#323232")
            l2.configure(fg="#e5e7e9")
            l2.configure(font=('Arial', 15,))
            l2.configure(anchor="center", justify='center')

            space = tk.Label(self.window, text='')
            space.grid(row=2, column=1)
            space.configure(bg="#323232")

            yearLabel = tk.Label(self.window, text='Year')
            yearLabel.grid(row=3, column=0)
            yearLabel.configure(bg="#323232")
            yearLabel.configure(fg="#e5e7e9")
            yearLabel.configure(font=("bold"))
            yearLabel.configure(anchor="e", justify='right')
            yearText = tk.Entry(self.window, width=45)
            yearText.grid(row=3, column=1, sticky="w")
            yearText.configure(bg="#474747")
            yearText.configure(fg="#e5e7e9")
            yearText.configure(highlightthickness = 1, highlightbackground = "#8a8a8a", borderwidth=0)
            yearText.configure(insertbackground='white')
            Gui.yearInput = yearText

            gpaLabel = tk.Label(self.window, text='GPA')
            gpaLabel.grid(row=4, column=0)
            gpaLabel.configure(bg="#323232")
            gpaLabel.configure(fg="#e5e7e9")
            gpaLabel.configure(font=("bold"))
            gpaLabel.configure(anchor="e", justify='right')
            gpaText = tk.Entry(self.window, width=45)
            gpaText.grid(row=4, column=1, sticky="w")
            gpaText.configure(bg="#474747")
            gpaText.configure(fg="#e5e7e9")
            gpaText.configure(highlightthickness = 1, highlightbackground = "#8a8a8a", borderwidth=0)
            gpaText.configure(insertbackground='white')
            Gui.gpaInput = gpaText

            space1 = tk.Label(self.window, text='')
            space1.grid(row=5, column=1)
            space1.configure(bg="#323232")

            genReport = tk.Button(self.window, text='Generate Report', width=15, command=GuiHelper.genReport)
            genReport.grid(row=6, column=0, columnspan=2)
            genReport.configure(bg="#e5e7e9")
            genReport.configure(font=('Arial', 9, "bold"))
            genReport.configure(highlightthickness = 1, borderwidth=0) 
        except Exception as e:
            print("error creating GUI")

        tk.mainloop()

        




    def getGpa(self):

        if self.gpaInput.get() == "":
            return 2.2
        else:
            return self.gpaInput.get()
    
    def getYear(self):
        return self.yearInput.get()