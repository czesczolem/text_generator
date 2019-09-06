# -*- coding: utf-8 -*-
import os

input = []
files = os.listdir('/home/mainer/Desktop/projects/Raper/rapsy')


def read_file(filename):
    with open('rapsy/{}'.format(filename), 'r') as f:
        data = f.readlines()
    return data

def save_file():
    with open('input.txt', 'a') as o:
        o.writelines(input)

def check_line(line):
    filter_strings = ["Tekst piosenki", '[', ']', '*', 'Poznaj historię zmian', 'Ref', 'ref', 'intro', ':', 'Zwrotka', 'Tede', 'Sulin']
    for x in filter_strings:
        if x in line:
            return False
    return True


def filter_text(data):

    for line in data:
        if check_line(line):
            input.append(line.lstrip())

for filename in files:
    data = read_file(filename)
    filter_text(data)

save_file()




