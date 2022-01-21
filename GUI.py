from tkinter import *
from Demo import *
import datetime
from Demo import get_storage_info, get_old_files, get_file_size 
from PIL import ImageTk, Image

root = Tk()
root.title('Google Drive Space Saver App')
root.iconbitmap('./images/hnet.com-image.ico')
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

# second page oh
drive_info = get_storage_info()
second_prompt = Label(root, text=drive_info)
second_prompt_1 = Label(root, text="Do you still need the file {0}?? It takes up {1} of your space!! ".format(random_file_name,  random_file_storage))

def backup_and_third():
    global random_file
    global random_file_storage
    Buttons.back_up(random_file)
    message = "Congrats!!You have backed up and saved {0} of your space!! ".format(random_file_storage)
    third_screen(message)


def keep_and_third():
    global random_file
    global random_file_storage
    global second_prompt
    print(type(second_prompt))
    Buttons.keep_file(random_file)
    message = "You could have saved {0} of your space!! Don't give up! Let's keep checking for more unused files.".format(random_file_storage)
    third_screen(message)
    


def del_and_third():
    global random_file
    global random_file_storage
    Buttons.delete_file(random_file)
    message = "Congrats!!You have saved {0} of your space!! ".format(random_file_storage)
    third_screen(message)




# buttons
keep_button = Button(root, text="Keep File!", command=keep_and_third, padx=50, pady=25, fg='blue', bg='#ff0077')

delete_button = Button(root, text="Delete File!", command=del_and_third, padx=50, pady=25, fg='blue', bg='#ff0077')

backup_button = Button(root, text="Back Up File!", command=backup_and_third, padx=50, pady=25, fg='blue', bg='#ff0077')

# third page oh!
third_prompt = Label(root, text=drive_info )
third_prompt_1 = Label(root, text="")
button_quit = Button(root, text="Exit Program!", command=root.quit, padx=50, pady=25, fg='blue', bg='#ff0077')



def second_screen():
    """Display the second Screen 
    """
    global random_file
    global random_file_id 
    global random_file_name 
    global random_file_mimeType 
    # get random file size
    global random_file_storage  
    # probably display the second screen
    first_prompt.grid_forget()
    start_button.grid_forget()
    # forget the third page 
    third_prompt.grid_forget()
    third_prompt_1.grid_forget()
    start_button.grid_forget()
    button_quit.grid_forget()
    # display the second screen info
    global second_prompt
    global second_prompt_1
    global keep_button
    global delete_button
    global backup_button

    drive_info = get_storage_info()
    second_prompt_1.configure(text="Do you still need the file {0}?? It takes up {1} of your space!! ".format(random_file_name,  random_file_storage)) 

    second_prompt.grid(row=3, column=2)
    second_prompt_1.grid(row=5, column=2)
    keep_button.grid(row=6, column=1)
    delete_button.grid(row=6, column=2)
    
    # second_prompt = Label(root, text=drive_info).grid(row=3, column=2)
    # second_prompt_1 = Label(root, text="Do you still need the file {0}?? It takes up {1} of your space!! ".format(random_file_name,  random_file_storage)).grid(row=5, column=2)

    # keep_button = Button(root, text="Keep File!", command=keep_and_third, padx=50, pady=25, fg='blue', bg='#ff0077').grid(row=6, column=1)
    
    # delete_button = Button(root, text="Delete File!", command=del_and_third, padx=50, pady=25, fg='blue', bg='#ff0077').grid(row=6, column=2)

    # backup_button = Button(root, text="Back Up File!", command=backup_and_third, padx=50, pady=25, fg='blue', bg='#ff0077').grid(row=6, column=3)


def third_screen(msg: str):
    """Load the last screen 
    """
    global random_file
    global random_file_id 
    global random_file_name 
    global random_file_mimeType 
    # get random file size
    global random_file_storage 

    global second_prompt
    global second_prompt_1
    global keep_button
    global delete_button
    global backup_button
    global start_button

    second_prompt.grid_forget()
    second_prompt_1.grid_forget()
    keep_button.grid_forget()
    delete_button.grid_forget()
    backup_button.grid_forget()

    drive_info = get_storage_info()
    third_prompt.grid(row=3, column=2)
    third_prompt_1.configure(text=msg).grid(row=4, column=2)
    start_button.grid(row=5, column=2)
    button_quit.grid(row=5, column=3)


def run_start_up_functions():
    """
    THis function switches to the next info
    """
    global random_file
    global random_file_id 
    global random_file_name 
    global random_file_mimeType 
    # get random file size
    global random_file_storage                                                           
    # get a date. one year back.
    d_ate = datetime.datetime.now() - datetime.timedelta(days=1*365)
    d_ate =str(d_ate.date())
    # get random file too. 
    random_file = get_old_files(d_ate)
    while random_file == None:
        d_ate = datetime.datetime.now() - datetime.timedelta(days=1)
        d_ate =str(d_ate.date())
        random_file = get_old_files(d_ate)
    random_file_id = random_file['id']
    random_file_name = random_file['name']
    random_file_mimeType = random_file['mimeType']
    # get random file size
    random_file_storage = get_file_size(random_file_id)
    second_screen()




# icon
gdss_img = ImageTk.PhotoImage(Image.open("./images/Google Drive Space Saver128.png"))
gdss_real_img = Label(image=gdss_img).grid(row=1, column=2)

# words 2 lines
gdss_name = Label(root, text="Google Drive Space Saver!")
gdss_name.grid(row=2, column=2)

first_prompt = Label(root, text="A python App that works with Google Drive API to help you save your Drive Space, by helpin g you decide which files you need and do not need!")
first_prompt.grid(row=3, column=2)

# button
# this button might just run the function that changes pages. 
start_button = Button(root, text="Click Here to Start GDSS!", command=run_start_up_functions, padx=50, pady=25, fg='blue', bg='#ff0077')
start_button.grid(row=5, column=2)


root.mainloop()