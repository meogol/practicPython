from tkinter import *
from tkinter import filedialog as fd

from ViewModel import ViewModel


class View(Frame):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.vm = ViewModel()

    def init_ui(self):
        self.master.title("Lungo-Vision")
        self.pack(fill=BOTH, expand=True)

        def open_dialog(event):
            name = fd.askopenfilename()
            if name == '':
                return

            self.vm.input_of_image(name)

            canvas.image = self.vm.get_image()
            canvas.create_image(0, 0, image=canvas.image, anchor='nw')

        imgHolder = Frame(self, bg='#BBAEC8', highlightbackground='black', highlightthickness=1)
        imgHolder.place(relx=0.05, rely=0.125, relwidth=0.5, relheight=0.8)

        canvas = Canvas(imgHolder, height=600, width=600)
        canvas.pack()

        textHolder = Frame(self, bg='white', highlightbackground='black', highlightthickness=1)
        textHolder.place(relx=0.6, rely=0.525, relwidth=0.35, relheight=0.4)

        textField = Label(textHolder, text='Ожидаем начала анализа', bg='white', justify=LEFT)
        textField.pack(side=TOP)
        textField.grid(row=0, column=0)

        btnHolder = Frame(self)
        btnHolder.place(relx=0.6, rely=0.32, relwidth=0.35, relheight=0.2)

        analyzisBtn = Button(btnHolder, text='Анализировать', bg='#CEC3D4', relief=GROOVE, height=2)
        analyzisBtn.pack(fill=X, side=BOTTOM)

        downloadImg = Button(btnHolder, text='Загрузить рентген снимок', fg='white', bg='#7E4160', relief=GROOVE,
                             height=2)
        downloadImg.pack(pady=10, side=BOTTOM, fill=X)
        downloadImg.bind('<Button-1>', open_dialog)


def main():
    root = Tk()
    root.geometry("600x600")
    root.resizable(width=True, height=True)
    root.minsize(width=800, height=600)
    app = View()
    root.mainloop()


if __name__ == '__main__':
    main()