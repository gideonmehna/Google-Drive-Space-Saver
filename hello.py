from tkinter import *
from Demo import *
import datetime
from Demo import get_storage_info, get_old_files, get_file_size 

root = Tk()
"""
We want to display our icon, then the words google space driver
saver

Then prompt the user to find out if they want to save space.
this button runs a function from our Demo.py to check for  a random file, store it in a variable that will be displayed on the next screen. 

cover enough space
"""
random_file = {}
random_file_id = ''
random_file_name = ''
random_file_mimeType = ''
# get random file size
random_file_storage = ''
def run_start_up_functions():
    # probably display the second screen
    # get a date. one year back.
    d_ate = datetime.datetime.now() - datetime.timedelta(days=1*365)
    d_ate =str(d_ate.date())
    # get random file too. 
    random_file = get_old_files(d_ate)
    random_file_id = random_file.id
    random_file_name = random_file.name
    random_file_mimeType = random_file.mimeType
    # get random file size
    random_file_storage = get_file_size(random_file_id)
    

drive_info = get_storage_info()
# icon
# words 2 lines
gdss_name = Label(root, text="Google Drive Space Saver!")
gdss_name.grid(row=1, column=2)
first_prompt = Label(root, text="A python App that works with Google Drive API to help you save your Drive Space, by helpin g you decide which files you need and do not need!")
first_prompt.grid(row=2, column=2)
# button
# this button might just run the function that changes pages. 
start_button = Button(root, text="Click Here to Start GDSS!", command=run_start_up_functions, padx=50, pady=50, fg='blue', bg='#ff0077')
start_button.grid(row=3, column=2)
"""
display the words, Here is a Random File, Do you still need this. also display the storage info. 

Then display the file's name and mimeType and storage if possible. Get the information from the display_file variable.

then display our three buttons. keep_button, delete_button, 
backup_button

each button is connected to the respective function in demo.py

and each function will pass in the file id into demo.py 's respective function. 
"""
# displaying two lines of words, the storage info and randome file info
# ########################################### change root

second_prompt = Label(root, text=get_storage_info).grid(row=1, column=2)
second_prompt_1 = Label(root, text="Do you still need the file {0} of type {1}?? It takes up {2} of your space!! ".format(random_file_name,random_file_mimeType, random_file_storage)).grid(row=2, column=2)

keep_button = Button(root, text="Keep File!", command=Buttons.keep_file(random_file), padx=50, pady=50, fg='blue', bg='#ff0077').grid(row=3, column=1)

delete_button = Button(root, text="Keep File!", command=Buttons.delete_file(random_file), padx=50, pady=50, fg='blue', bg='#ff0077').grid(row=3, column=2)

backup_button = Button(root, text="Keep File!", command=Buttons.back_up(random_file), padx=50, pady=50, fg='blue', bg='#ff0077').grid(row=3, column=3)

"""
Upon every click there is a specific message that should be passed into the next slide. 

then the space that has been freed up too. 
and the new storage info compared to the old storage info. with a congrats message if any. 

then the program should maybe close on its own. or prompt the user to run again. maybe both buttons. 
"""
# ########################################### change root

third_prompt = Label(root, text=get_storage_info).grid(row=1, column=2)
third_prompt_1 = Label(root, text="Congrats!!You have saved {2} of your space!! ".format(random_file_storage)).grid(row=2, column=2)

button_quit = Button(root, text="Exit Program!", command=root.quit, padx=50, pady=50, fg='blue', bg='#ff0077').grid(row=3, column=3)

e = Entry(root, width =50)
e.pack()
def keep_file():
    myLabel3 = Label(root, text="You have kept the file")
    myLabel3.grid(row=2,column=1)
# creating a lavel widget

myLabel2 = Label(root, text="Google Drive Space Saver!")

keep_button = Button(root, text="Keep File!", command=keep_file, padx=50, pady=50, fg='blue', bg='#ff0077')

# shoving it onto the screen 

# myLabel1.pack()
myLabel2.grid(row=1,column=1)
keep_button.grid(row=3,column=1)

root.mainloop()

"""
questions.
how do we load another page

how do we add an icon. 

"""