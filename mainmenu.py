import tkinter as tk

def show_frame(frame):
    frame.tkraise()
def disable_event():
    pass

window = tk.Tk()
window.title('Program Automated Caption')
window.geometry('640x480')
window.resizable(0,0)
window.protocol("WM_DELETE_WINDOW", disable_event)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)


for frame in (frame1, frame2):
    frame.grid(row=0,column=0,sticky='nsew')

#==================Frame 1 code
frame1_title=  tk.Label(frame1, text='Selamat datang di menu Program, \ntekan tombol dibawah untuk memulai', font='times 20', bg='#d4ff85')
frame1_title.pack(fill='both', expand=True)


frame1_btn = tk.Button(frame1, text='Jalankan Program',command=lambda:window.destroy())
frame1_btn.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
frame1_btn.pack(fill='x', ipady=15)


frame1_btn = tk.Button(frame1, text='Tentang Program ',command=lambda:show_frame(frame2))
frame1_btn.pack(fill='x', ipady=15)

frame1_btn = tk.Button(frame1, text='Exit Program ',command=exit)
frame1_btn.pack(fill='x', ipady=15)



#==================Frame 2 code

frame2_title=  tk.Label(frame2, text='Automated Caption Generator adalah program untuk membuat caption berdasarkan gambar yang dipilih.\n Model akan berusaha menebak caption berdasarkan fitur-fitur pada gambar.', font='times 12', bg='#d4ff85')
frame2_title.pack(fill='both', expand=True)

frame2_btn = tk.Button(frame2, text='Kembali',command=lambda:show_frame(frame1))
frame2_btn.pack(fill='x', ipady=15)

show_frame(frame1)

window.mainloop()

import mainprogram