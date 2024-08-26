import tkinter as tk
from tkinter import filedialog
from tkinter import Tk , Text, Frame, Button
import os

class Notepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Experimental Notepad")
        self.current_path:str = None

        #Area holding the text:
        self.text_area: Text = Text(self.root , wrap='word')
        self.text_area.pack(expand=True , fill='both')

    #Button frames for Save and Load:
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        #Save Button:
        self.save_button: Button = Button(self.button_frame, text='Save',command=self.save_file , width= 10, activebackground= 'gray')
        self.save_button.pack(side=tk.LEFT)

        #Save As Button:
        self.saveAs_button: Button = Button(self.button_frame, text='Save As',command=self.saveAs_file , width= 10, activebackground= 'gray')
        self.saveAs_button.pack(side=tk.LEFT)
        
        #Load Button:
        self.load_button: Button = Button(self.button_frame, text='Load',command=self.load_file, width= 10, activebackground= 'gray')
        self.load_button.pack(side=tk.LEFT)

        #Clear Button:
        self.clear_button: Button = Button(self.button_frame, text= 'Clear All', command=self.clear_all,width=10 , activebackground='gray')
        self.clear_button.pack(side=tk.LEFT)

        self.root.protocol('WM_DELETE_WINDOW', self.Close_msg)

    def Close_msg(self)->None:
        answer = tk.messagebox.askyesno("Warning" , "Do you want to save your latest changes?")
        if answer:
            self.save_file()
        else:
            self.root.quit
        self.root.destroy()


    def save_file(self)->None:
        if self.current_path:
            with open(self.current_path, 'w') as file:
                file.write(self.text_area.get(1.0,tk.END))
            print(f"save changes to {self.current_path}")
        else:
            self.saveAs_file()


    def saveAs_file(self)-> None:
        path: str = filedialog.asksaveasfilename(defaultextension='.txt',
                                                filetypes=[('Text files' , '*.txt')],
                                                initialfile="Untitled.txt")
        if path:
            with open(path, 'w') as file:
                file.write(self.text_area.get(1.0 , tk.END))
            self.current_path = path
            print(f'File saved to: {path}')


    def load_file(self)-> None:
        path: str = filedialog.askopenfilename(defaultextension='.txt',
                                                filetypes=[('Text files' , '*.txt')])

        with open(path, 'r') as file:
            content: str = file.read()
            self.text_area.delete(1.0 , tk.END)
            self.text_area.insert(tk.INSERT , content)
        self.current_path = path
        print(f'File loaded from: {path}')


    def clear_all(self)->None:
        result = tk.messagebox.askyesno("Confirm", "Are you sure you want to clear all?")
        if result:
            self.text_area.delete(1.0, tk.END)
        else:
            return


    def Run(self)-> None:
        self.root.mainloop()



def main() -> None:
    root: Tk = tk.Tk()
    app: Notepad = Notepad(root= root)
    app.Run()


if __name__ == '__main__':
    main()