from newsdataapi import NewsDataApiClient
from tkinter import *

from tkinter import scrolledtext


# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey="NewsDataAPI")

# You can pass empty or with request parameters {ex. (country = "us")}

response = api.news_api(
    language="bg, en", category="business, technology, top, entertainment")

data = response["results"]

window = Tk()

window.title("NewsCollection app")

window.geometry('800x600')

txt = scrolledtext.ScrolledText(window, width=50, height=60)

txt.insert(INSERT, data[0]["title"] + "\n" + data[0]["description"] + "\n" + data[0]["link"]+"\n"+"\n"+data[1]["title"] + "\n" +
           data[1]["description"] + "\n" + data[1]["link"]+"\n"+"\n"+data[2]["title"] + "\n" + data[2]["description"] + "\n" + data[2]["link"]+"\n"+"\n"+data[3]["title"] + "\n" + data[3]["description"] + "\n" + data[3]["link"]+"\n"+"\n"+data[4]["title"] + "\n" + data[4]["description"] + "\n" + data[4]["link"])

txt.grid(column=0, row=0)

exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.grid(column=0, row=1)

window.attributes('-fullscreen', True)

window.mainloop()