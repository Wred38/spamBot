import time, pyautogui, pyperclip
import tkinter as tk



Window = tk.Tk()  
Window.geometry('350x243')
Window.title('Spam bot')
Window.resizable(False, False)





scrollbar = tk.Scrollbar(Window)
scrollbar.pack(side = 'right', fill = 'y' )

running = False
i = 2.0



    
def spamCopy():
    Window.clipboard_clear()
    Window.clipboard_append(entry.get())
    if running:
        #time.sleep(i)
        pyautogui.write(pyperclip.paste())
        pyautogui.press('ENTER')
    Window.after(int(i*1000), spamCopy)
    
    

def start():
    entry.config(state = 'readonly')
    global running
    running = True
    

def stop():
    entry.config(state = 'normal')
    global running
    running = False


def timeUp():
    global i
    if i >= 2:
        i += 1
    elif i >= 1:
        i += 0.5
    elif i < 1:
        i += 0.1
    currenttime.config(text = 'Current time between msgs: ' + str(round(i, 2)) + ' second(s).')

def timeDown():
    global i
    if i < 0.2:
        i == 0.1
    elif i > 2:
        i -= 1
    elif i <= 1:
        i -= 0.1
    elif i <= 2:
        i -= 0.5
    currenttime.config(text = 'Current time between msgs: ' + str(round(i, 2)) + ' second(s).')



typespam = tk.Label(Window,
                    text = 'Type spam:')
typespam.pack()





entry = tk.Entry(Window,
                 bg = 'light gray',
                 xscrollcommand = scrollbar.set)
entry.pack()

scrollbar.config(command = entry.xview)




                       



currenttime = tk.Label(Window,
                      text = 'Current time between msgs: ' + str(i) + ' second(s).')
currenttime.pack()



timedown = tk.Button(Window,
                     text = 'Time down',
                     fg = 'blue',
                     width = 10,
                     height = 10,
                     command = timeDown)
timedown.pack(side = 'left')

timeup = tk.Button(Window,
                   text = 'Time up',
                   fg = 'blue',
                   width = 10,
                   height = 10,
                   command = timeUp)
timeup.pack(side = 'left')


startbutton = tk.Button(Window,
                   text = 'Start',
                   fg = 'green',
                   width = 15,
                   height = 5,
                   command = start)  
startbutton.pack()


stopbutton = tk.Button(Window,
                       text = 'Stop',
                       fg = 'red',
                       width = 15,
                       height = 5,
                       command = stop)
stopbutton.pack()



  
Window.after(100, spamCopy)
Window.mainloop()
