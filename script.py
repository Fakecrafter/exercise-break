#!/usr/bin/env python3

import os
import time
import random
import csv

with open('/home/fakecrafter/coding/breaker/exercise.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    all_entries = []
    # make list of lists
    for row in csv_reader:
        all_entries.append(row)

    highest = [0, 0]
    count = 0
    # check which exercise has highest value
    for i in all_entries:
        if int(i[2]) > highest[1]:
            highest = [count, int(i[2])]
        count += 1
    exercise = all_entries[highest[0]]
    # send notification with the chosen exercise
    os.system("paplay /usr/share/sounds/freedesktop/stereo/message-new-instant.oga")
    os.system(f"export DISPLAY=:0; notify-send -w 'workout/pause time' '{exercise[1]} {exercise[0]}'")


with open('/home/fakecrafter/coding/breaker/exercise.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for j in all_entries:
        if exercise[0] != j[0]:
            csv_writer.writerow([j[0],j[1],int(j[2]) + random.randint(5,10)])
        else:
            csv_writer.writerow([j[0],j[1],0])

