from function_finder.data.save import load_data, store_data
from function_finder.classes.class_directory import Directory
from function_finder.classes.class_function import Function
from function_finder.gui.listapp import ListApp
from function_finder.gui.update import check_for_change
from tkinter import messagebox


# runs when __main__ is run
def run():
    try:
        load_data()
        check_for_change(Directory.all[0])
        app = ListApp(Function.all)
        app.mainloop()
    finally:
        try:
            for directory in Directory.all:
                directory.refresh_modifications()

            store_data()

            print("Finished")
        except BaseException:
            messagebox.showerror(
                master=None,
                message="Something has gone terribly wrong. \n It is \
                        recommended that you close this application, delete \
                        the allfuncs file, and re-load from the beginning.")
