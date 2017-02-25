from fetch_tweets import *

import Tkinter
from Tkinter import *
import tkMessageBox

class MyTwitterGUI:
        
    def __init__(self, master):
        self.master = master
        master.title("Fetch my tweets")
        
        self.tweets={"Refresh to See..": "Null"}

        self.greet_button = Button(master, text="Refresh", command=self.greet)
        self.greet_button.pack()
        
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox = Listbox(master, yscrollcommand=scrollbar.set)
        for tweet in self.tweets:
            self.listbox.insert(END, tweet)
        self.listbox.pack(expand=YES,fill=BOTH)
        self.listbox.bind('<Double-1>', self.clickme)
        scrollbar.config(command=self.listbox.yview)
        
    def clickme(self,event):
        widget = event.widget
        selection=widget.curselection()
        selected = widget.get(selection[0])
        id = [key for key, value in self.tweets.iteritems() if value == selected][0]
        tkMessageBox.showinfo("Tweet Details", "Go to "+"https://api.twitter.com/1/statuses/oembed.json?id="+id+ " to download json file")

    def greet(self):
        myList= TweetList()
        self.tweets= myList.filterTweet(query = '%23custserve')
        self.listbox.delete(0,END)
        for tweet in list(self.tweets.values()):
            self.listbox.insert(END, tweet)

if __name__ == '__main__' :

    root = Tk()
    root.geometry("700x300")
    my_gui = MyTwitterGUI(root)
    root.mainloop()