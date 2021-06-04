from tkinter import * # tkinter is used to create GUI Applications
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess # The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
file_path = ''

def set_file_path(path):
    global file_path # set file_path as global variable
    file_path = path # uses path in open_file func

def open_file():
    path = askopenfilename(filetypes = [('Python Files','*.py')]) # Includes all filetypes with .py extension
    with open(path, 'r') as file:   # Open path in write mode
       code = file.read()   # Read from file
       editor.delete('1.0', END) # Delete any existing content in the editor
       editor.insert('1.0',code) #Insert code into the file, for user to be able to read it.
       set_file_path(path) # When opening a file we can initialise file_path gloabl variable to path in this function.


def save_as():
    if file_path == '': # If file path is empty, we ask for a file path location
        path = asksaveasfilename(filetypes = [('Python Files','*.py')]) # Includes all filetypes with .py extension.
    else: # If file has already been opened or saved
        path = file_path # We set the path to previous file path
    with open(path, 'w') as file:   # Open path in write mode
        code = editor.get('1.0', END) # Capture code from start to end in editor
        file.write(code)    # Write the captured code to file
        set_file_path(path) # When saving a file we can initialise file_path gloabl variable to path in this function.
        # This will help us to retain the path file where you are saving files and save it there.


def run():
    if file_path == '':
        save_prompt = Toplevel() # Creates pop-up
        text = Label(save_prompt, text = 'Please save your code')
        text.pack()
        return
    command = f'python {file_path}' # Creates a command of python executable process
    process = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    # Setting a process to execute a python code
    output, error = process.communicate()
    code_output.insert(END, output) # printing the output, new output will be added to end.
    code_output.insert(END, error) # printing the error, new output will be added to end.


    


compiler = Tk() # Creates a main window
compiler.title('PY-DE (Python IDE)')    #Give a name to our IDE :)

menu_bar = Menu(compiler) # Using menu fun we create a menu widget we create a menu bar on top of compiler

file_menu = Menu(menu_bar, tearoff=0) # Create a file menu on top of menu bar
file_menu.add_command(label = 'Open', command = open_file)# Calling run fun on top with label Open
file_menu.add_command(label = 'Save', command = save_as)
file_menu.add_command(label = 'Save as', command = save_as)
file_menu.add_command(label = 'Exit', command = exit) # Exits from IDE
menu_bar.add_cascade(label = 'File', menu = file_menu) # Displays Open -> File


run_bar = Menu(menu_bar, tearoff=0) # Create a run bar von top of menu bar
run_bar.add_command(label = 'Run', command = run) # Calling run fun on top
menu_bar.add_cascade(label = 'Run', menu = run_bar)

 #  Cascading menu  is a secondary menu that appears while you are holding the cursor over an item on the primary menu
compiler.config(menu = menu_bar)
editor = Text() # Widget used to show text data on python application
editor.pack()   #The Pack geometry manager packs widgets in rows or columns. 

code_output = Text(height=10)    # Text box to see code output
code_output.pack()
#We can use options like fill, expand, and side to control this geometry manager.
compiler.mainloop()


