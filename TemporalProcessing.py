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
r_sum = 0;
g_sum = 0;
b_sum = 0;


for i in range(canvas.height):
    for j in range(canvas.width):
        for k in range(int(number)):
            num=image[k].getpixel((j,i))
            r_sum = r_sum + num[0]
            g_sum = g_sum + num[1]
            b_sum = b_sum + num[2]
        color = (
            int( (r_sum)/int(number)),
            int( (g_sum)/int(number)),
            int( (b_sum)/int(number))
            )
        #reset colors
        r_sum = 0;
        g_sum = 0;
        b_sum = 0;
        canvas.putpixel((j,i), color)
#Saving the image I have created
canvas.save("images/done.png")
canvas.show()
