#Name: Alfonso Torres
#Date: 03/01/2018
#Objective: Obtain an odd number of photos and get the happy median of all of them.


from PIL import Image
import glob
#Asking user for the number of images
number = input("How many images would you like to input: ")

#Getting all the images in the same file
arr=glob.glob('images/*.png')

#Creating an array of
image = [Image] * int(number)

#Opening all my images in an array
for i in range(int(number)):
    image[i]=Image.open(arr[i])

#Creating a canvas that is the same size as my images
canvas = Image.new("RGB", (image[0].width,image[0].height), "white")
r_sum = [];
g_sum = [];
b_sum = [];

#median value
med = int(number)/2

for i in range(canvas.height):
    for j in range(canvas.width):
        for k in range(int(number)):
            num=image[k].getpixel((j,i))
            r_sum.append(num[0])
            g_sum.append(num[1])
            b_sum.append(num[2])
            r_sum.sort()
            g_sum.sort()
            b_sum.sort()
        color = (
            r_sum[int(med)],
            g_sum[int(med)],
            b_sum[int(med)]
            )
        #reset colors
        r_sum = [];
        g_sum = [];
        b_sum = [];
        canvas.putpixel((j,i), color)
#Saving the image I have created
canvas.save("images/done.png")
canvas.show()
