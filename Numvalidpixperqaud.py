import picture2
import math
try:
    pic = picture2.Picture(input("Please upload a file: ")) #prompt the user in the console to pick a file to load in
    x = pic.getWidth()#get the dimentions of the picture
    y = pic.getHeight()
    pic.display()
except:#if file not valid, prompt user again
    input("try again:")
    pic.display()
#Color_values = {}c
colors = {'red': (255,0,0),'green': (0,255,0),'blue': (0,0,255),'yellow': (255,255,0),'orange': (255,127,0),'white': (255,255,255),'black': (0,0,0),'gray': (127,127,127),'pink': (255,127,127),'purple': (127,0,255),}
#def distance(left, right):
#    return sum((l-r)**2 for l, r in zip(left, right))**0.5

#def distance(c1, c2):
 #   (r1,g1,b1) = c1
  #  (r2,g2,b2) = c2
   # return math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)

#colors = list(rgb_code_dictionary.keys())
#closest_colors = sorted(colors, key=lambda color: distance(color, point))
#closest_color = closest_colors[0]
#code = rgb_code_dictionary[closest_color]

#class NearestColorKey(object):  #e really mean by "closest" color
 #   def __init__(self, goal):
  #      self.goal = goal
   # def __call__(self, item):
    #    return distance(self.goal, item[1])
#>>> min(colors.items(), key=NearestColorKey((10,10,100)))
#('black', (0, 0, 0))
#>>> min(colors.items(), key=NearestColorKey((10,10,200)))
#('blue', (0, 0, 255))
#>>> min(colors.items(), key=NearestColorKey((100,10,200)))
#('purple', (127, 0, 255))
#>>>
q1_col = []
def distance(color1, color2):
    print(color2)
    return math.sqrt(sum([(e1-e2)**2 for e1, e2 in zip(color1, color2)]))
def best_match(sample, colors):
    by_distance = sorted(colors, key=lambda c: distance(c, sample))
    return by_distance[0]  
    
for x in range(0,5):#0,x//2):   
    for y in range(0,5):#0,y//2):
        color = pic.getPixelColor(x, y)   #get color of each pixel
        print(color)
        q1_col.append(color)
for i in colors.values():
    for j in q1_col:
        #print(i)
        #print(j)
        distance(i,j)
        match = best_match(i,j)
        
        #print(match)
        
        
        
        
        
      #  Color_values[quad1] = color        #store it in dic under key quadrant 1
for x in range(x//2,x):
    for y in range(0,y//2):   #same for quadrant 2
        color = pic.getPixelColor(x, y)
for x in range(0,x//2):   #qud3
    for y in range(y//2,y):
        color = pic.getPixelColor(x, y)
for x in range(x//2,x):
    for y in range(y//2,y):#quad4
        color = pic.getPixelColor(x, y)