from tkinter import Tk, Canvas, Label, Button, LEFT, RIGHT, BOTH, TOP, BOTTOM, Toplevel
from math import sqrt
import json

canvas_width = 800
canvas_height = 500


def create_point(c, x, y):
    python_green = "#FF0000"
    x1, y1 = (x - 2), (y - 2)
    x2, y2 = (x + 2), (y + 2)
    c.create_oval(x1, y1, x2, y2, fill=python_green)

def create_point_grid(c, x, y):
    python_green = "#000000"
    x1, y1 = (x - 5), (y - 5)
    x2, y2 = (x + 5), (y + 5)
    c.create_oval(x1, y1, x2, y2, outline=python_green)


master = Tk()
master.title("Points")
master.attributes('-fullscreen', True)
w = Canvas(master,
           width=canvas_width,
           height=canvas_height,
           borderwidth=5,
           relief="groove")
w.pack(expand='YES', fill='both')

points_file = open('points.txt', 'r')
points_json = points_file.readlines()
points = list()

for point in points_json:
    points.append(json.loads(point))

for point in points:
    create_point(w, point['X'], point['Y'])

distance = list()

for i in range(len(points) - 1):
    point_1 = points[i]
    point_2 = points[i + 1]
    w.create_line(point_1['X'], point_1['Y'], point_2['X'], point_2['Y'],
    fill = '#476042')
    distance.append(sqrt(((point_1['X'] - point_2['X']) ** 2) + ((point_1['Y'] - point_2['Y']) ** 2)))

for x in range(-5000, 6000, 50):
    w.create_line(x, 0, x, canvas_height)

for y in range(-5000, 6000, 50):
    w.create_line(0, y, canvas_width, y)

avg_distance = round(sum(distance) / len(distance), 2)

infoText = str()
infoText += 'Avarage distance between captures is %s pixels\n'%avg_distance
infoText += 'Biggest distance between captures is %s pixels\n'%round(max(distance), 2)
infoText += 'Smallest distance between captures is %s pixels\n'%round(min(distance), 2)
infoText += 'Please note that these values are calculated only between subsequent captures\n'

def openAboutWindow():
    aboutText = '''
    (C) 2020 almaember. License: CC0-1.0
    Created by: almaember AKA DrAlmaember or almaember1098
    === Contact ===
    Reddit: u/almaember (https://reddit.com/u/almaember)
    E-mail: almaember@protonmail.com
    Web: https://almaember.joomla.com/
    GitHub: https://github.com/almaember1098
    '''
    top = Toplevel(master)
    Label(top, text = aboutText).pack()
    Button(top, text = 'Close', command = (lambda win = top: win.destroy())).pack()
    top.mainloop()

Label(master, text = infoText).pack(side=LEFT, fill=BOTH)
Button(master, text = 'Quit', command = exit, borderwidth=5, width=15,
    font=("Courier", 44)).pack(side=RIGHT, fill=BOTH)
Button(master, text = 'About', command = openAboutWindow, width = 15,
    font=("Courier", 44)).pack(side=BOTTOM)

master.mainloop()