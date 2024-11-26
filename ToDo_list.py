# Todolist project
import json
import os


def printMenu():
    pass


to_do_list = []


def add_task(to_do_list):
    new_task = input("Write a new task you want to add.. ")
    if new_task in to_do_list:
        print("The task is already on your list")
        add_to_list = input("Would you like to add the task anyway? (y\n)")
        if add_to_list.lower != "y" or add_to_list.lower != "yes":
            return
        to_do_list.append(new_task)
        print("The task has been added successfully  ")
