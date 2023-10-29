import subprocess
import os
import tkinter as tk
from tkinter import filedialog

def select_directory(link):
    directory = filedialog.askdirectory()
    if directory:
        execute_git_commands(directory, link)

def execute_git_commands(directory, link=None):
    git_commands = [
        'git init',
        'git branch -M main',
        'git acm "chunks"',
        'git remote add origin {0}'.format(link),
        'git push -u origin main'
    ]

    # Change the current working directory to the selected directory
    if directory:
        os.chdir(directory)

    for command in git_commands:
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {command}")
            print(f"Error message: {e.stderr.decode()}")
            break

# Create a simple Tkinter GUI
link = input("Enter the link: ")
select_directory(link)
