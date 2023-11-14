import cv2
import os
import numpy as np
import random
path_to_icons = r"C:\Users\metal\Desktop\latest\DATASETGENERATOR\icons\icons"
path_to_minimap = r"minimap.PNG"
blue_icons = r"C:\Users\metal\Desktop\latest\DATASETGENERATOR\blue_icons\blue_icons"
red_icons = r"C:\Users\metal\Desktop\latest\DATASETGENERATOR\red_icons\red_icons"
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
        mask1 = cv2.bitwise_not(mask1)
        mask1 = cv2.cvtColor(mask1, cv2.COLOR_RGB2RGBA)
        mask1 = cv2.circle(mask1, (c_w,c_h), radius, (0,0,0,0), -1)

        img = cv2.subtract(img, mask1)
        
  
        if color == "red":
            img = cv2.circle(img, (c_w, c_h), radius, (100,100,255,255),3)
            img = cv2.resize(img, (35, 35))
            cv2.imwrite(rf'C:\Users\metal\Desktop\DATASETGENERATOR\red_icons\{champion}_red.png', img)
        
        if color == "blue":
            img = cv2.circle(img, (c_w, c_h), radius, (255, 170, 30, 255),4)
            img = cv2.resize(img, (35, 35))
            cv2.imwrite(rf'{blue_icons}/{champion}_blue.png', img)

        if color == None:
            img = cv2.resize(img, (35, 35))
            cv2.imwrite(rf'C:\Users\metal\Desktop\DATASETGENERATOR\absolute_icons\{champion}.png', img)

        icons.append((champion, img))

    return icons

icons_blue = get_icons("blue")
icons_red = get_icons("red")
minimap = cv2.imread(path_to_minimap)
minimap = cv2.cvtColor(minimap, cv2.COLOR_RGB2RGBA)
minimap_base = cv2.imread(path_to_minimap)
minimap_base = cv2.cvtColor(minimap, cv2.COLOR_RGB2RGBA)
pings = os.listdir(r"C:\Users\metal\Desktop\latest\DATASETGENERATOR\out")
total_champs = os.listdir(r"C:\Users\metal\Desktop\latest\DATASETGENERATOR\blue_icons\blue_icons")

test = get_icons("red")
new_file = open("labels.txt", "w+")
bruh = len(test)
i = 0
for champion, icon in test:

    new_file.write(f"{champion}\n")

    i += 1
    


for j in range(1000):
    if j%5 != 0:
        f = open(rf"C:\Users\metal\Desktop\latest\DATASETGENERATOR\dataset\labels\train\frame_{j}.txt", "w+")
    if j%5 == 0:
        f = open(rf"C:\Users\metal\Desktop\latest\DATASETGENERATOR\dataset\labels\val\frame_{j}.txt", "w+")        
    for champion, icon in icons_blue:
        for i in range(5):
            try:
                r = random.randint(0, len(icons_blue))
                random_champ = icons_blue[r][1]
                y_offset = random.randint(20, minimap.shape[0]- 50)
                x_offset = random.randint(20, minimap.shape[1]- 50)
                y1,y2 = y_offset, y_offset + random_champ.shape[0]
                x1,x2 = x_offset, x_offset + random_champ.shape[1]
                alpha_s = random_champ[:, :, 3] / 255.0
                alpha_l = 1.0 - alpha_s
                #cv2.rectangle(minimap, (x_offset, y_offset), (x_offset+random_champ.shape[1], y_offset + random_champ.shape[0]), (255,255,255), 1)
                f.write(f"{r} {x_offset / 415} {y_offset / 415} {(x_offset + random_champ.shape[1]) / 415} {(y_offset + random_champ.shape[0]) / 415}\n")
                #cv2.putText(minimap, icons_red[r][0], (x_offset, y_offset-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
                for c in range(0,3):
                    minimap[y1:y2, x1:x2, c] = (alpha_s * random_champ[:, :, c] + alpha_l * minimap[y1:y2, x1:x2, c])
                    
            except:
                print("", end="")
        break

    
    for champion, icon in icons_red:
        for i in range(5):
            try:
                r = random.randint(0, len(icons_red))
                random_champ = icons_red[r][1]
                y_offset = random.randint(20, minimap.shape[0] - 50)
                x_offset = random.randint(20, minimap.shape[1] - 50)
                y1,y2 = y_offset, y_offset + random_champ.shape[0]
                x1,x2 = x_offset, x_offset + random_champ.shape[1]
                alpha_s = random_champ[:, :, 3] / 255.0
                alpha_l = 1.0 - alpha_s
                f.write(f"{r} {x_offset / 415} {y_offset / 415} {(x_offset + random_champ.shape[1]) / 415} {(y_offset + random_champ.shape[0]) / 415}\n")
                #cv2.putText(minimap, icons_red[r][0], (x_offset, y_offset-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
                for c in range(0,3):
                    minimap[y1:y2, x1:x2, c] = (alpha_s * random_champ[:, :, c] + alpha_l * minimap[y1:y2, x1:x2, c])
                

            except:
                print("", end="")   
        break

    if (not (j%5) == 0):
        cv2.imwrite(rf"C:\Users\metal\Desktop\latest\DATASETGENERATOR\dataset\images\train\frame_{j}.png",minimap)
    if j % 5 == 0:
        cv2.imwrite(rf"C:\Users\metal\Desktop\latest\DATASETGENERATOR\dataset\images\val\frame_{j}.png",minimap)
    minimap = cv2.imread(path_to_minimap)
    f.close()
    

    
minimap = cv2.resize(minimap, (415, 415))
cv2.imshow("data", minimap)
cv2.waitKey(0)

