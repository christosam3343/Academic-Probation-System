import driverHelper as DriverHelper
import gui as Gui
from tkinter import messagebox



def genReport():
    if Gui.guiObj.getYear() == "":
        messagebox.showinfo(title="Error", message="You must enter a year")
        return

    DriverHelper.generateReport(Gui.guiObj.getGpa(), Gui.guiObj.getYear())
    Gui.guiObj.yearInput.delete(0, Gui.tk.END)
    Gui.guiObj.gpaInput.delete(0, Gui.tk.END)
