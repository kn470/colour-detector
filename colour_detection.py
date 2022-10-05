#import packages
import cv2
import numpy as np
import pandas as pd

#load colour data
colour_data = pd.read_csv("colors.csv")
colours = colour_data["colour"]
r_vals = colour_data["r"]
g_vals = colour_data["g"]
b_vals = colour_data["b"]
#function to find the closest colour
def find_closest(r,g,b):
    diffs = []
    for i in range(len(colours)):
        sub_diff = abs(r-r_vals[i]) + abs(g-g_vals[i]) + abs(b-b_vals[i])
        diffs.append(sub_diff)
    min_diff = min(diffs)
    pos = diffs.index(min_diff)
    colour = colours[pos]
    return colour
    
#f"{resized[y,x,2]},{resized[y,x,1]},{resized[y,x,0]}"


#cv2.imshow("picture", img)

#find the pixel position of the pixel clicked on

def write_details(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        resized = cv2.imread("colorpic.jpg")
        cv2.putText(resized, str(x)+","+str(y), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
        cv2.putText(resized, f"{find_closest(resized[y,x,2], resized[y,x,1], resized[y,x,0])}", (300,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
        
        cv2.imshow("picture", resized)




cv2.namedWindow("picture")

while(True):
    cv2.setMouseCallback("picture", write_details)
    if cv2.waitKey(20) & 0xFF == 27:  
        break


cv2.destroyAllWindows()
