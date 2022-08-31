#we can use a database if we want
#from app import db 
from flask import flash
import pandas as pd


class Printer(object):

    def show_string(self, text):
        if text == '':
            flash("You didn't enter any text to flash")
        else:
            flash(text + "!!!")


class User(self):

    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email
        self.database=pd.DataFrame([id,email,username,password], columns=['Users'])

    def save(self):
        """
        save in the database
        """
        self.database.update()
        return True


    def delete(self,index: int):
        """
        delete from database
        """
        self.database.drop(labels=index, axis=0)
        return True


