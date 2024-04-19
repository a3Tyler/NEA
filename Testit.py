#This file contains the code for TestIt! (my NEA project)

#Import key functions
import tkinter
from tkinter import Tk, Label, Entry, Button

#Create a title
Title = Tk()
Title.title("TestIt!")

#New subroutine called 'Welcome'
def Welcome():
    txtWelcome_title = tkinter.label(text = "Welcome to TestIt!")