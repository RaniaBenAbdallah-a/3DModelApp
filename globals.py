# globals.py

shoulder_width = 0  # Initial value, peut être mis à jour selon vos besoins

def set_shoulder_width(width):
    global shoulder_width
    shoulder_width = width

def get_shoulder_width():
    global shoulder_width
    return shoulder_width
