#import tkinter
from tkinter import *
import tkinter.font as font
#import json
import json
# Import matplotlib
from matplotlib import pyplot as plt
# Import datetime
import datetime

####Setting up program window####
root = Tk()
root.title('Weather Chart')
root.geometry("1000x1000")
root.config(bg='#51ABA4')
myFont = font.Font(family='Comic Sans MS', size=20, weight="bold")

####Weather Graph####


def graph():
    with open('weather.json') as f:
        data = json.load(f)

# Get Weather Types
    weather = data.keys()

# Get month
    x = datetime.datetime.now()

# Get number of occurrences
    days = data.values()
    plt.bar(weather, days, .8, color=['yellow', 'gray'])

# Add Labels to graph
    plt.title(f'Weather for the Month of: {x.strftime("%B")} ', size=15)
    plt.xlabel("Weather", size=12)
    plt.ylabel("Number of Days", size=12)
    plt.grid()
    plt.show()


###Exit Button###
button_quit = Button(root, text="Exit Program", command=quit)
button_quit.pack(side=BOTTOM, pady=10)

####make weather graph button####

graph_it = Button(root, text="Graph Weather Chart",
                  compound=CENTER, command=graph)
graph_it['font'] = myFont
graph_it.pack(side=BOTTOM, pady=30)

####Functions for when weather buttons are clicked####


def sunClick():
    with open('weather.json') as f:
        data = json.load(f)
    # Record another sunny day
        data['Sunny'] += 1
        with open('weather.json', 'w') as output_file:
            json.dump(data, output_file)
    # print(data)


def cloudyClick():
    with open('weather.json') as f:
        data = json.load(f)
        # Record another cloudy day
        data['Cloudy'] += 1
        with open('weather.json', 'w') as output_file:
            json.dump(data, output_file)
    # print(data)


def foggyClick():
    with open('weather.json') as f:
        data = json.load(f)
        # Record another foggy day
        data['Foggy'] += 1
        with open('weather.json', 'w') as output_file:
            json.dump(data, output_file)
    # print(data)


def rainClick():
    with open('weather.json') as f:
        data = json.load(f)
        # Record another rainy day
        data['Rainy'] += 1
        with open('weather.json', 'w') as output_file:
            json.dump(data, output_file)
        # print(data)


def windyClick():
    with open('weather.json') as f:
        data = json.load(f)
        # Record another windy day
        data['Windy'] += 1
        with open('weather.json', 'w') as output_file:
            json.dump(data, output_file)
    # print(data)


def snowyClick():
    with open('weather.json') as f:
        data = json.load(f)
        # Record another snowy day
        data['Snowy'] += 1
        with open('weather.json', 'w') as output_file:
            json.dump(data, output_file)
    # print(data)


####Title of Webpage###
Label(root, text='What is the Weather Today?', font=(
    'Comic Sans MS', 60)).pack(side=TOP, pady=15)

###User Instructions###
Label(root, text='Click on the image that shows what the weather is today.', font=(
    'Comic Sans MS', 24)).pack(pady=30)

Label(root, text='If you want to see the graph of the weather, Click "Graph Weather Chart"', font=(
    'Comic Sans MS', 24)).pack(pady=30)

#####Create weather buttons using Images#####
sun_btn = PhotoImage(file='sunny.png')
rainy_btn = PhotoImage(file='rain.png')
foggy_btn = PhotoImage(file='foggy.png')
cloudy_btn = PhotoImage(file='cloudy.png')
windy_btn = PhotoImage(file='windy.png')
snowy_btn = PhotoImage(file='snowy.png')

####Adding the buttons to the screen, with name of weather####
sunButton = Button(root, text='Sunny', compound=TOP,
                   image=sun_btn, command=sunClick)
sunButton['font'] = myFont
sunButton.pack(side=LEFT, padx=20)

cloudyButton = Button(root, text='Cloudy', compound=TOP,
                      image=cloudy_btn, command=cloudyClick)
cloudyButton['font'] = myFont
cloudyButton.pack(side=LEFT, padx=20)

foggyButton = Button(root, text='Foggy', compound=TOP,
                     image=foggy_btn, command=foggyClick)
foggyButton['font'] = myFont
foggyButton.pack(side=LEFT, padx=20)

rainyButton = Button(root, text='Rainy', compound=TOP,
                     image=rainy_btn, command=rainClick)
rainyButton['font'] = myFont
rainyButton.pack(side=LEFT, padx=20)

windyButton = Button(root, text='Windy', compound=TOP,
                     image=windy_btn, command=windyClick)
windyButton['font'] = myFont
windyButton.pack(side=LEFT, padx=20)

snowyButton = Button(root, text='Snowy', compound=TOP,
                     image=snowy_btn, command=snowyClick)
snowyButton['font'] = myFont
snowyButton.pack(side=LEFT, padx=20)


root.mainloop()
