import re
import os
import PyPDF2
import tkinter as tk
from tkinter.filedialog import askdirectory, asksaveasfilename


def open_dir():

    global dir
    dir = askdirectory()
    if not dir:
        return
  
    window.title(f"Detector de Fail - {dir}")
    
def redenumire():

    global da_nu
    
    da_nu = button2["text"]
    
    if da_nu.lower() == "da":
        button2["text"] = "Nu"
    else:
        button2["text"] = "Da"

def verificare():

    window.columnconfigure(1, minsize = 500, weight = 1)
    fr2 = tk.Frame(master = window, relief = tk.SUNKEN, bd = 2)
    afisare = tk.Text (master = fr2, height = 12)
    
    afisare.grid(row = 0, column = 0, sticky = 'ew')
    fr2.grid(row = 0, column = 1, sticky = 'nsew', padx = 3)
    
    certificate = []
    index = 0
    
    for pdfFile in os.listdir(dir):
        if ".pdf" in pdfFile:
            
           
            pdfRead = PyPDF2.PdfFileReader(dir + "/" + pdfFile)
           
            if text1.get().lower() == 'trescal':
                for i in range(1,(pdfRead.getNumPages() - 2)):
                    page = pdfRead.getPage(i)
                    pageContent = page.extractText()
                    j = pageContent.split()
                                                          
                    for x in j:
                        if x.startswith(text2.get()):
                            j = False
                    if not j:
                        certificate.append(i + 1)
                        index +=1    
                            
            if certificate:
                afisare.insert(tk.END, (text2.get() + " gasit in " + pdfFile + ", pagina: " + str(certificate) + "\n\n"))
                index = 0
                certificate.clear()
               
            if button2["text"].lower() == "nu":
                page = pdfRead.getPage(0).extractText().split()

                try:
                    os.rename(dir + "/" + pdfFile, dir + "/" + page[page.index("020337Bucharest") + 1] + '.pdf')
                except FileExistsError:
                    os.rename(dir + "/" + pdfFile, dir + "/" + page[page.index("020337Bucharest") + 1] + ' - copy.pdf')
                    
                

window = tk.Tk()
window.title("Detector de Fail")

fr1 = tk.Frame(master = window)


label1 = tk.Label(master = fr1, text = "Firma de calibrare")
text1 = tk.Entry (master = fr1, width = 50)
label2 = tk.Label(master = fr1, text = "Indicii de fail (!, !!, F, etc.)")
text2 = tk.Entry (master = fr1, width = 50)
label3 = tk.Label(master = fr1, text = "Locatie fisiere")
button1 = tk.Button (master = fr1, text = "Deschide", command = open_dir)
label4 = tk.Label(master = fr1, text = "Redenumire fisier dupa SN?")
button2 = tk.Button (master = fr1, text = "Da", command = redenumire)
button3 = tk.Button (master = fr1, text = "Verificare", command = verificare)

label1.grid(row = 0, column = 0, sticky = 'w')
text1.grid (row = 1, column = 0)
label2.grid(row = 2, column = 0, sticky = 'w')
text2.grid (row = 3, column = 0)
label3.grid(row = 4, column = 0, sticky = 'w')
button1.grid (row = 5, column = 0, sticky = 'w')
label4.grid(row = 6, column = 0, sticky = 'w')
button2.grid (row = 7, column = 0, sticky = 'w')
button3.grid (row = 8, column = 0, sticky = 'ew')
fr1.grid(row = 0, column = 0, sticky = 'nw')


window.mainloop()
