import cv2
import numpy as np
import time

# Define the dimensions of the toll booths and cars
booth_width = 70
booth_height = 90
car_width = 10
car_height = 10

# Create a blank image
image = 255 * np.ones((300, 500, 3), dtype=np.uint8)

# Initial positions of the toll booths
booth1_x, booth1_y = 50, 80
booth2_x, booth2_y = 170, 80
booth3_x, booth3_y = 290, 80

# True means Booth closed and False means Booth Opened
show_booth1 = False
show_booth2 = False
show_booth3 = True

# Initial position of the blue car above the toll booths
blue_car_x, blue_car_y = 10, 30

red_car_x_1, red_car_y_1 = 60, 200
red_car_x_2, red_car_y_2 = 200, 200
red_car_x_3, red_car_y_3 = 320, 200

# Initial position of the green car in booth 1
green_car_x, green_car_y = booth1_x + 30, booth1_y + 15

# Number of cars in each booth
num_cars_booth1 = 0
num_cars_booth2 = 0
num_cars_booth3 = 0

t1=1
t2=1
t3=1
c=0
v=1

b1=[]
b3=[]
b2=[]

number_cars=15

# Initialize t
def draw_booth(x, y, show_whole_booth, num_cars=0):
    # Draw the edges of the booth
    cv2.rectangle(image, (x, y), (x + booth_width, y + booth_height), (0, 0, 255), 1)
    cv2.line(image, (x, y + booth_height), (x + booth_width, y + booth_height), (255, 255, 255), 1)
   
    if not show_whole_booth:
        # Draw only the top edge of the booth in white
        cv2.line(image, (x, y), (x + booth_width, y), (255, 255, 255), 1)
        
    # Draw cars in the booth
    for i in range(num_cars):
        car_x = x + 25 
        car_y = y + 15 + i * 25
        cv2.rectangle(image, (car_x, car_y), (car_x + car_width, car_y + car_height), (0, 255, 0), -1)

def updated_booth(car_booth, booth_x, booth_y, t_cars_booth1, t_cars_booth2, t_cars_booth3):
    image[:] = 255

    # Draw the booths with the updated positions
    draw_booth(booth1_x, booth1_y, show_booth1, num_cars=num_cars_booth1)
    draw_booth(booth2_x, booth2_y, show_booth2, num_cars=num_cars_booth2)
    draw_booth(booth3_x, booth3_y, show_booth3, num_cars=num_cars_booth3)
'''    
if number_cars<=10:
    show_booth1 = False
    show_booth2 = True
    show_booth3 = True
elif number_cars>10 and number_cars<=20:
    show_booth1 = False
    show_booth2 = False
    show_booth3 = True
elif number_cars>20:
    show_booth1 = False
    show_booth2 = False
    show_booth3 = False'''

while True:
    
        
    start_time = time.time()
    
    # Draw the initial booths with cars
    draw_booth(booth1_x, booth1_y, show_booth1, num_cars=num_cars_booth1)
    draw_booth(booth2_x, booth2_y, show_booth2, num_cars=num_cars_booth2)
    draw_booth(booth3_x, booth3_y, show_booth3, num_cars=num_cars_booth3)
   
    cv2.imshow("Toll Booth Simulation", image)
    cv2.waitKey(1000)

    # Draw the blue car at its initial position after a delay of 2 seconds
    
    cv2.rectangle(image, (blue_car_x, blue_car_y), (blue_car_x + car_width, blue_car_y + car_height), (255, 0, 0), -1)
    c+=1
    print("Car entered",c)
    cv2.imshow("Toll Booth Simulation", image)
    cv2.waitKey(1000)
   

    # Move the blue car to the position of the green car
    if not show_booth1 and show_booth2 and show_booth3:
        t1+=1
        print("Booth 1 opened trying to enter booth 1..")
        if num_cars_booth1 <= 2:
            print("Entered into Booth 1")
            updated_booth(num_cars_booth1, booth1_x, booth1_y, num_cars_booth1 + 1, num_cars_booth2, num_cars_booth3)
            num_cars_booth1 += 1  
            b1.append(c)
        else:
            cv2.waitKey(2000)
            print("Booth already has maximum capacity")
            c-=1
    
    elif not show_booth2 and show_booth1 and show_booth3:
        t2+=1
        print("Booth 2 opened trying to enter booth 2..")
        if num_cars_booth2 <= 2:
            print("Entered into Booth 2")
            updated_booth(num_cars_booth1, booth1_x, booth1_y, num_cars_booth1, num_cars_booth2+1, num_cars_booth3)
            num_cars_booth2 += 1  
            b2.append(c)
        else:
            cv2.waitKey(2000)
            print("Booth already has maximum capacity")
            c-=1
    elif not show_booth3 and show_booth2 and show_booth1:
        t3+=1
        print("Booth 3 opened trying to enter booth 3..")
        if num_cars_booth3 <= 2:
            print("Entered into Booth 3")
            updated_booth(num_cars_booth1, booth1_x, booth1_y, num_cars_booth1 , num_cars_booth2, num_cars_booth3+1)
            num_cars_booth3 += 1  
            b3.append(c)
        else:
            cv2.waitKey(2000)
            print("Booth already has maximum capacity")
            c-=1
            
    
    elif not show_booth1 and not show_booth2 and show_booth3 and (num_cars_booth1<3 or num_cars_booth2<3):
        
        if num_cars_booth1<=2 and num_cars_booth1==num_cars_booth2:
            
            print("Entered into Booth 1")
            updated_booth(num_cars_booth1,booth1_x,booth1_y,num_cars_booth1+1,num_cars_booth2,num_cars_booth3)
            num_cars_booth1+=1
            t1+=1
            b1.append(c)
            
        elif num_cars_booth1<num_cars_booth2:
            
            print("Entered into Booth 1")
            updated_booth(num_cars_booth1,booth1_x,booth1_y,num_cars_booth1+1,num_cars_booth2,num_cars_booth3)
            num_cars_booth1+=1
            t1+=1
            b1.append(c)

        elif num_cars_booth1>num_cars_booth2:
            print("Entered into Booth 2")
            updated_booth(num_cars_booth2,booth2_x,booth2_y,num_cars_booth1,num_cars_booth2+1,num_cars_booth3)
            num_cars_booth2+=1
            t2+=1
            b2.append(c)   
    
    elif not show_booth1 and show_booth2 and not show_booth3 and (num_cars_booth1<3 or num_cars_booth3<3):
        
        if num_cars_booth1<=2 and num_cars_booth1==num_cars_booth3:
            
            print("Entered into Booth 1")
            updated_booth(num_cars_booth1,booth1_x,booth1_y,num_cars_booth1+1,num_cars_booth2,num_cars_booth3)
            num_cars_booth1+=1
            t1+=1
            b1.append(c)
            
        elif num_cars_booth1<num_cars_booth3:
            
            print("Entered into Booth 1")
            updated_booth(num_cars_booth1,booth1_x,booth1_y,num_cars_booth1+1,num_cars_booth2,num_cars_booth3)
            num_cars_booth1+=1
            t1+=1
            b1.append(c)

        elif num_cars_booth1>num_cars_booth3:
            print("Entered into Booth 3")
            updated_booth(num_cars_booth2,booth2_x,booth2_y,num_cars_booth1,num_cars_booth2,num_cars_booth3+1)
            num_cars_booth3+=1
            t3+=1
            b3.append(c)           

    elif not show_booth1 and not show_booth2 and not show_booth3 and (num_cars_booth1<3 or num_cars_booth2<3 or num_cars_booth3<3):
        
        if num_cars_booth3<(num_cars_booth1 and num_cars_booth2):
            
            print("Entered into Booth 3")
            updated_booth(num_cars_booth1,booth1_x,booth1_y,num_cars_booth1,num_cars_booth2,num_cars_booth3+1)
            num_cars_booth3+=1
            t3+=1
            b3.append(c)
            
        elif num_cars_booth1<=2 and num_cars_booth1==num_cars_booth2:
            
            print("Entered into Booth 1")
            updated_booth(num_cars_booth1,booth1_x,booth1_y,num_cars_booth1+1,num_cars_booth2,num_cars_booth3)
            num_cars_booth1+=1
            t1+=1
            b1.append(c)
            

        elif num_cars_booth1<(num_cars_booth2 and num_cars_booth3):
            
            print("Entered into Booth 1")
            updated_booth(num_cars_booth1,booth1_x,booth1_y,num_cars_booth1+1,num_cars_booth2,num_cars_booth3)
            num_cars_booth1+=1
            t1+=1
            b1.append(c)
            

        else:
            
            print("Entered into Booth 2")
            updated_booth(num_cars_booth2,booth2_x,booth2_y,num_cars_booth1,num_cars_booth2+1,num_cars_booth3)
            num_cars_booth2+=1
            t2+=1
            b2.append(c)
            
    elif not show_booth1 and not show_booth2 and show_booth3 and num_cars_booth1==3:

        print("Booth 2 opened trying to enter booth 2..")
        if num_cars_booth2<= 2:
            t2+=1
            print("Entered into Booth 2")
            updated_booth(num_cars_booth1, booth1_x, booth1_y, num_cars_booth1, num_cars_booth2+1, num_cars_booth3)
            num_cars_booth2 += 1
            b2.append(c)
                   
        else:
            cv2.waitKey(2000)
            print("Booth already has maximum capacity please wait")
            c-=1
                
    elif not show_booth1 and not show_booth2 and not show_booth3 and num_cars_booth1==3 and num_cars_booth2==3:
        print("Booth 3 opened trying to enter booth 3..")
        if num_cars_booth3<= 2:
            print("Entered into Booth 3")
            updated_booth(num_cars_booth1, booth1_x, booth1_y, num_cars_booth1, num_cars_booth2, num_cars_booth3+1)
            num_cars_booth3+=1
            t3+=1
            b3.append(c)
            
               
        else:
            cv2.waitKey(2000)
            print("Booth already has maximum capacity reached please wait!")
            c-=1
    
    if not show_booth1 and not show_booth2 and not show_booth3 and num_cars_booth1==3 and num_cars_booth2==3 and num_cars_booth3==3:
        if v==1:
            t1+=3
            v=2

        elif v==2:
            t2+=3
            v=3
        else:
            t3+=3
            v=1
    if not show_booth1 and show_booth2 and not show_booth3 and num_cars_booth1==3 and num_cars_booth3==3:
        if v==1:
            t1+=3
            v=0
        else:
            t3+=3
            v=1
    if not show_booth1 and not show_booth2 and show_booth3 and num_cars_booth1==3 and num_cars_booth2==3:
        if v==1:
            t1+=3
            v=0
        else:
            t2+=3
            v=1

    if t1>4:
        t1=5
    if t2>4:
        t2=5
    if t3>4:
        t3=5
    
    if t1%5==0:

        num_cars_booth1-=1
        updated_booth(num_cars_booth1, booth1_x, booth1_y, num_cars_booth1 - 1, num_cars_booth2, num_cars_booth3)
        t1=0
        cv2.rectangle(image, (red_car_x_1, red_car_y_1), (red_car_x_1 + car_width, red_car_y_1 + car_height), (0, 0, 255), -1)
        cv2.waitKey(2000)
        print(f"Car-{min(b1)} left booth 1")
        b1.remove(min(b1))
        
    if t2%5==0:
        
        num_cars_booth2-=1
        updated_booth(num_cars_booth1, booth1_x, booth1_y, num_cars_booth1, num_cars_booth2 -1, num_cars_booth3)
        t2=0
        cv2.rectangle(image, (red_car_x_2, red_car_y_2), (red_car_x_2 + car_width, red_car_y_2 + car_height), (0, 0, 255), -1)
        print(f"Car-{min(b2)} left booth 2")
        b2.remove(min(b2))
        
    if t3%5==0:
        
        num_cars_booth3-=1
        updated_booth(num_cars_booth1, booth1_x, booth1_y, num_cars_booth1, num_cars_booth2, num_cars_booth3-1)
        t3= 0
        cv2.rectangle(image, (red_car_x_3, red_car_y_3), (red_car_x_3 + car_width, red_car_y_3 + car_height), (0, 0, 255), -1)
        print(f"Car-{min(b3)} left booth 3")
        b3.remove(min(b3))
        
        
    # Wait for a key press to exit the loop
    key = cv2.waitKey(2000)  # Adjust the delay as needed
    if key == 27:  # ASCII code for the 'Esc' key
          
        break
        

cv2.destroyAllWindows()

