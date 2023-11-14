import cv2
import os
import numpy as np
import random
path_to_icons = r"C:\Users\metal\Desktop\DATASETGENERATOR\icons"
path_to_minimap = r"C:\Users\metal\Desktop\DATASETGENERATOR\minimap.PNG"
blue_icons = r"C:\Users\metal\Desktop\DATASETGENERATOR\blue_icons"
red_icons = r"C:\Users\metal\Desktop\DATASETGENERATOR\red_icons"

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
        
        img = cv2.imread(p)

        w, h = img.shape[:2]

        c_w = w // 2
        c_h = h // 2

        radius = w // 2

        mask1 = np.zeros_like(img)

        mask1 = cv2.circle(mask1, (c_w,c_h), radius, (255,255,255), -1)

        img = cv2.subtract(mask1, img)

        img = cv2.bitwise_not(img)

        if color == "red":
            red_outline = cv2.circle(img, (c_w, c_h), radius, (0,0,255),3)
            img = cv2.resize(img, (35, 35))
            cv2.imwrite(rf'C:\Users\metal\Desktop\DATASETGENERATOR\red_icons\{champion}_red.png', img)
        
        if color == "blue":
            blue_outline = cv2.circle(img, (c_w, c_h), radius, (255,0,0),3)
            img = cv2.resize(img, (35, 35))
            cv2.imwrite(rf'C:\Users\metal\Desktop\DATASETGENERATOR\blue_icons\{champion}_blue.png', img)

        if color == None:
            img = cv2.resize(img, (35, 35))
            cv2.imwrite(rf'C:\Users\metal\Desktop\DATASETGENERATOR\absolute_icons\{champion}.png', img)

        icons.append((champion, img))

    return icons

minimap = cv2.imread(path_to_minimap)
total_champs = os.listdir(red_icons)

random_champ = random.randint(0, len(total_champs))
y_offset = random.randint(0, minimap.shape[0])
x_offset = random.randint(0, minimap.shape[1])
rnd_champ_path = total_champs[random_champ]
rnd_champ = cv2.imread(rf"C:\Users\metal\Desktop\DATASETGENERATOR\red_icons\{rnd_champ_path}")


for j in range(5):
    random_champ = random.randint(0, len(total_champs))
    y_offset = random.randint(0, minimap.shape[0])
    x_offset = random.randint(0, minimap.shape[1])
    rnd_champ_path = total_champs[random_champ]
    rnd_champ = cv2.imread(rf"C:\Users\metal\Desktop\DATASETGENERATOR\red_icons\{rnd_champ_path}")
    minimap[y_offset:y_offset+rnd_champ.shape[0], x_offset:x_offset+rnd_champ.shape[1]] = rnd_champ



cv2.imshow("data", minimap)
cv2.waitKey(0)

