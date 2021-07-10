from tkinter import * 
import tkinter.messagebox
from covid import Covid
from prettytable import PrettyTable

class AppCovid():
    def __init__(self, root) -> None:
        self.root = root 
        self.root.title("Statistik Covid-19")

        canvas = Canvas(root, width=600, height=590)
        canvas.grid(columnspan=5, rowspan=5)

        #image 
        gambar = PhotoImage(file="logo1n.png")
        gambarLabel = Label(image=gambar,  )
        gambarLabel.image = gambar
        gambarLabel.grid(row=0, column=2)

        #var 
        result = StringVar()
        resultCovid = StringVar()

        #intruksi 
        intruksi = Label(root, text="Masukan Nama Negara", font=("Avenir",13, "bold"))
        intruksi.grid(row=1, column=2)

        #textbox
        def TextBOX(item):
            self.textBox = Text(root, height=20, width=50 )
            self.textBox.insert(1.0, item)
            self.textBox.tag_configure("left",)
            self.textBox.tag_add("left", 1.0, "end")
            self.textBox.place(x=108, y=550)

        
        #func
        def iReset():
            result.set("")
            return
        
        def iExit():
            Exit = tkinter.messagebox.askyesno(
                "Statistik Covid-19", "Kamu Yakin Mau Keluar ?")
            if Exit > 0:
                root.destroy()
                return
        def countryOnly():
            item = result.get()

            if item.isascii():

                # item 
                covid = Covid(source="worldometers")
                data = covid.get_data()
                country = covid.get_status_by_country_name(item)

                myTable = PrettyTable(["Covid Statistik", "total"])

                for key, value in country.items():
                    myTable.add_row([key, value])
                
                print(myTable)

        #Entry
        self.nameCountry = Entry(root, 
            textvariable=result, 
            width=25)
        self.nameCountry.grid(row=2, column=2 )

        #Button Sumbit 
        self.btnSumbit = Button(root, text="Sumbit",
         command= countryOnly,
            font=("Avenir", 10))
        self.btnSumbit.place(x=198, y=500)

        #Button exit
        self.btnExit = Button(root, text="Exit", 
        command=iExit,
            font=("Avenir", 10))
        self.btnExit.place(x=350, y=500)

        # Button Reset 
        self.ResetButton = Button(root, text="Reset",
            command=iReset,
            font=("Avenir", 10))
        self.ResetButton.place(x=280, y=500)

if __name__ == "__main__":
    root = Tk()
    App = AppCovid(root)
    root.mainloop()