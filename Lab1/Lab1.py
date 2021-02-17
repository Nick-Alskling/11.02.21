# -*- codecs: utf-8 -*-
import codecs
import random
from random import sample

t = codecs.open("themes.txt", "r", "utf-8")
title = t.readlines()

name = codecs.open("students.txt", "r", "utf-8")
student = name.readlines()
students = sample(student, len(student))

output = title+students
n=7
final = [output[i * n:(i + 1) * n] for i in range((len(output) + n - 1) // n )]  
for x in title:
    final1=list(zip(*final))

f=codecs.open('output.txt','w', "utf-8")
for elem in final1:
    f.write(str(elem)+'\n')
