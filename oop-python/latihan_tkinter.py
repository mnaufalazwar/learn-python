import tkinter

main_window = tkinter.Tk()

print(main_window.__dict__)

tombol1 = tkinter.Button(main_window, text = "tombol1")

tombol1.pack()

main_window.mainloop()
