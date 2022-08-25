# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image

# fundamental matrix ;
Fmatrix23= np.array([[3.03994528999160e-08,2.65672654114295e-07,-0.000870550254997210],
                    [4.67606901933558e-08,-1.11709498607089e-07,-0.00169128012255720],
                    [-1.38310618285550e-06,0.00140690091935593,0.999997201170569]])

Fmatrix13= np.array([[6.04444985855117e-08, 2.56726410274219e-07, -0.000602529673152695],
                     [2.45555247713476e-07 ,-8.38811736871429e-08, -0.000750892330636890],
                     [-0.000444464396704832 ,0.000390321707113558, 0.999999361609429]])

first_img_path="C:/Users/HP/Desktop/HUZEM/Fotogrametrik_Goruntu_Analizi/assignment2/Q2/coordinates_1.txt"# florence1 
second_img_path="C:/Users/HP/Desktop/HUZEM/Fotogrametrik_Goruntu_Analizi/assignment2/Q2/coordinates_2.txt"# florence2 

# I opened the txt files containing our pixel coordinates and turned them into an array.
file = open(first_img_path, "r", encoding="utf-8")
file_2=open(second_img_path, "r", encoding="utf-8")

in_file = file.readlines()
in_file_2=file_2.readlines()

veri_1 = [[float(i) for i in r.split()]for r in in_file]
veri_2 = [[float(i) for i in r.split()]for r in in_file_2]

#######################################  2 to 3 image

# We see on which epipolar lines the points we chose from the second image can be on in the third image.
# When finding the epipolar lines, we multiply the pixel coordinates of the points we have selected with the fundamental matrix.
k=1
for i in range(len(veri_2)):
    veri_2[i].append(k)
    
veri_2 = np.array(veri_2)

transpose_veri_2=np.transpose(veri_2)

multiplying_1=np.matmul(Fmatrix23,transpose_veri_2)
print(multiplying_1)

multiplying_2=[[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]]

# fitting the lines
for i in range(5):
    multiplying_2[0][i]=multiplying_1[0][i]/np.sqrt(multiplying_1[0][i]**2+multiplying_1[1][i]**2)
    multiplying_2[1][i]=multiplying_1[1][i]/np.sqrt(multiplying_1[0][i]**2+multiplying_1[1][i]**2)
    multiplying_2[2][i]=multiplying_1[2][i]/np.sqrt(multiplying_1[0][i]**2+multiplying_1[1][i]**2)

multiplying_2=np.array(multiplying_2)

print(multiplying_2)

im = Image.open('florence3.jpg')
im1 = Image.open("florence2.jpg")


x_1=[]
y_1=[]
for i in range(5):
    x_1.append(veri_2[i][0])
    y_1.append(veri_2[i][1])    
    
plt.imshow(im1)
plt.plot(x_1,y_1,"ro")  
plt.figure()


u_1 = np.linspace(0, 1536,2)
liste_u1=[]
liste_v1=[]
# au + bv + c = 0 lines in the image
for i in range(5):
    v_1 = (multiplying_2[0][i]*u_1 +  multiplying_2[2][i])/-multiplying_2[1][i]
    liste_u1.append(u_1)
    liste_v1.append(v_1)
    plt.imshow(im)
    plt.plot(u_1,v_1)  

plt.figure()





############################################### 1 to 3 image

# We see on which epipolar lines the points we chose from the first image can be on in the third image.
# When finding the epipolar lines, we multiply the pixel coordinates of the points we have selected with the fundamental matrix.
a=1
for i in range(len(veri_1)):
    veri_1[i].append(a)
    
veri_1 = np.array(veri_1)


transpose_veri_1=np.transpose(veri_1)

multiplying=np.matmul(Fmatrix13,transpose_veri_1)
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
im2 = Image.open("florence1.jpg")

x=[]
y=[]
for i in range(5):
    x.append(veri_1[i][0])
    y.append(veri_1[i][1])    
    
plt.imshow(im2)
plt.plot(x,y,"ro")  
plt.figure()
  
  
u = np.linspace(0, 1536,2)
liste_u=[]
liste_v=[]
# au + bv + c = 0 lines in the image
for i in range(5):
    v = (multiplying2[0][i]*u +  multiplying2[2][i])/-multiplying2[1][i]
    liste_u.append(u)
    liste_v.append(v)
    plt.imshow(im)
    plt.plot(u,v)  
plt.figure()

# 1536*2048 is third image size


######################################## intersection with 2 lines 

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

A=[0,0]
B=[0,0]
C=[0,0]
D=[0,0]
intersection_set=np.zeros((5,2))
for i in range(5):
    A[0]=liste_u1[i][0]
    A[1]=liste_v1[i][0]
    
    B[0]=liste_u1[i][1]
    B[1]=liste_v1[i][1]
    
    C[0]=liste_u[i][0]
    C[1]=liste_v[i][0]
    
    D[0]=liste_u[i][1]
    D[1]=liste_v[i][1]
    ala=line_intersection((A, B), (C, D))
    intersection_set[i][0]=ala[0]
    intersection_set[i][1]=ala[1]
    plt.imshow(im)
    plt.plot(ala[0],ala[1],"ro",) # our intersection


# A=[0,0]
# A[0]=liste_u1[0][0]
# A[1]=liste_v1[0][0]
# B=[0,0]
# B[0]=liste_u1[0][1]
# B[1]=liste_v1[0][1]

# C=[0,0]
# C[0]=liste_u[0][0]
# C[1]=liste_v[0][0]
# D=[0,0]
# D[0]=liste_u[0][1]
# D[1]=liste_v[0][1]

# print (line_intersection((A, B), (C, D)))


