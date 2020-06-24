import sys
import os
data = ""

for song in os.listdir("lyrics"):
    data1 = ""
    filey = open("lyrics/" + song, "r+")
    data1 = filey.read()
    data1 = data1  + "\n"
    data = data + data1 
    filey.close

filey = open("lyrics/jonbellion.txt", "w+")
filey.write(data)
filey.close()