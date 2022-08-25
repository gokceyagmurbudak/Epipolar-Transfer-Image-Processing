# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# fundamental matrix ;
Fmatrix23= np.array([[3.03994528999160e-08,2.65672654114295e-07,-0.000870550254997210],
                    [4.67606901933558e-08,-1.11709498607089e-07,-0.00169128012255720],
                    [-1.38310618285550e-06,0.00140690091935593,0.999997201170569]])

# I opened the txt files containing our pixel coordinates and turned them into an array.
first_img_path="C:/Users/HP/Desktop/HUZEM/Fotogrametrik_Goruntu_Analizi/assignment2/Q1/coordinates_of_second_image_points.txt"
file = open(first_img_path, "r", encoding="utf-8")

in_file = file.readlines()
veri_1 = [[float(i) for i in r.split()]for r in in_file]

a=1
for i in range(len(veri_1)):
    veri_1[i].append(a)
    
veri_1 = np.array(veri_1)

# When finding the epipolar lines, we multiply the pixel coordinates of the points we have selected with the fundamental matrix.
transpose_veri_1=np.transpose(veri_1)

multiplying=np.matmul(Fmatrix23,transpose_veri_1)
print(multiplying)

multiplying2=[[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]]
# fitting the lines
for i in range(5):
    multiplying2[0][i]=multiplying[0][i]/np.sqrt(multiplying[0][i]**2+multiplying[1][i]**2)
    multiplying2[1][i]=multiplying[1][i]/np.sqrt(multiplying[0][i]**2+multiplying[1][i]**2)
    multiplying2[2][i]=multiplying[2][i]/np.sqrt(multiplying[0][i]**2+multiplying[1][i]**2)

multiplying2=np.array(multiplying2)

print(multiplying2)

im = Image.open('florence3.jpg')
im2 = Image.open("florence2.jpg")

x=[]
y=[]
for i in range(5):
    x.append(veri_1[i][0])
    y.append(veri_1[i][1])    
# Selceted point ploted   
plt.imshow(im2)
plt.plot(x,y,"ro")  
plt.figure()
    
u = np.linspace(0, 1536,50)
# au + bv + c = 0 lines in the image
for i in range(5):
    v = (multiplying2[0][i]*u +  multiplying2[2][i])/-multiplying2[1][i]
    plt.imshow(im)
    plt.plot(u,v)  


# 1536*2048 is third image size

