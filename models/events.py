from models.event import *

event1 = Event("20/05/21", "Digital Party", 50, "Clockwise", "Disco party for nerds", False)
event2 = Event("25/12/21", "Cyber Crimbo", 50, "Sainsburys", "Holiday in the Matrix", True)

events = [event1, event2]

def append_event(new_event):
    events.append(new_event)

def remove_event(index):
    events.pop(int(index))

