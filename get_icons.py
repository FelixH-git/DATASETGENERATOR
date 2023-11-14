import cv2
import os
import numpy as np
import random
path_to_icons = r"/home/biggiecheese1235/DATASETGENERATION/GITREPO/DATASETGENERATOR/icons"
path_to_minimap = r"minimap.PNG"
blue_icons = r"/home/biggiecheese1235/DATASETGENERATION/GITREPO/DATASETGENERATOR/blue_icons"
red_icons = r"/home/biggiecheese1235/DATASETGENERATION/GITREPO/DATASETGENERATOR/red_icons"
def get_icons(color=None):
    icons = []
    for p in os.listdir(path_to_icons):
        champion = p[:p.find(".")]
        extension = p[p.rfind("."):]
        if extension != ".png":
            continue
        p = os.path.join(path_to_icons, p)
        if not os.path.isfile(p):
            continue
        
        img = cv2.imread(p, -1)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
        w, h, c = img.shape

        c_w = w // 2
        c_h = h // 2

        radius = w // 2
        mask1 = np.zeros_like(img)
        mask1 = cv2.circle(mask1, (c_w,c_h), radius, (0,0,0, 255), -1) 
        print(mask1[:,:, 3]) 

        img = cv2.subtract(img, mask1)
        
  
        if color == "red":
            red_outline = cv2.circle(img, (c_w, c_h), radius, (0,0,255),3)
            img = cv2.resize(img, (35, 35))
            cv2.imwrite(rf'C:\Users\metal\Desktop\DATASETGENERATOR\red_icons\{champion}_red.png', img)
        
        if color == "blue":
            blue_outline = cv2.circle(img, (c_w, c_h), radius, (255,0,0),3)
            img = cv2.resize(img, (35, 35))
            cv2.imwrite(rf'{blue_icons}/{champion}_blue.png', img)

        if color == None:
            img = cv2.resize(img, (35, 35))
            cv2.imwrite(rf'C:\Users\metal\Desktop\DATASETGENERATOR\absolute_icons\{champion}.png', img)

        icons.append((champion, img))

    return icons

icons = get_icons("blue")

minimap = cv2.imread(path_to_minimap)
minimap = cv2.cvtColor(minimap, cv2.COLOR_RGB2RGBA)
total_champs = os.listdir(blue_icons)

for champion, icon in icons:
    for i in range(5):
        try:
            y_offset = random.randint(0, minimap.shape[0])
            x_offset = random.randint(0, minimap.shape[1])
            y1,y2 = y_offset, y_offset + icon.shape[0]
            x1,x2 = x_offset, x_offset + icon.shape[1]
            #cv2.imshow("test", icon[:, :, 3])
            #cv2.waitKey(0)
            icon[:, :, 3] = 255.0
            alpha_s = icon[:, :, 3] / 255.0
            alpha_l = 1.0 - alpha_s
            
            for c in range(0,3):
                minimap[y1:y2, x1:x2, c] = (alpha_s * icon[:, :, c] + alpha_l * minimap[y1:y2, x1:x2, c])
        except:
            print("", end="")
    break
cv2.imshow("data", minimap)
cv2.waitKey(0)

