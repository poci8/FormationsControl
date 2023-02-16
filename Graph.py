import matplotlib.pyplot as plt
import math
import random

def Intersections(x0, y0, r0, x1, y1, r1):

    d = math.sqrt((x1-x0)**2 + (y1-y0)**2)
    
    if d > r0 + r1 :
        return None
    
    if d < abs(r0-r1):
        return None
    
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        
        return (x3, y3, x4, y4)

def calculateDistanceByCoordinates(x1, x2, y1, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2-y1, 2))

class Node():
    nextNode = None
    previous = None
    x = 0
    y = 0
    isleader = False
    direction = None
    wantedDistanceToPrev = 0
    wantedDistanceToNext = 0
    
    def init(self, x, y, direction, isLeader):
        self.x = x
        self.y = y
        self.direction = direction
        self.isleader = isLeader
    
    def calculateDistance(self, where):
        distance = 0;
        if where == "next":
            distance = math.sqrt((self.nextNode.x - self.x) ** 2 + (self.nextNode.y - self.y) ** 2)
        elif where == "prev":
            distance = math.sqrt((self.previous.x - self.x) ** 2 + (self.previous.y - self.y) ** 2)
        return distance
       
def Draw(graph):
    for i in range(0, len(graph)):
        if(graph[i].isleader):
            plt.plot(graph[i].x, graph[i].y, marker="o", markerfacecolor="red")
        else:
            plt.plot(graph[i].x, graph[i].y, marker="o", markerfacecolor="green")
        if(graph[i].direction == "both"):
            dx = graph[i].nextNode.x - graph[i].x
            dy = graph[i].nextNode.y - graph[i].y
            plt.arrow(graph[i].x, graph[i].y, dx, dy, head_width=0.5, head_length=0.5,  length_includes_head=True)
            
            dx = graph[i].previous.x - graph[i].x
            dy = graph[i].previous.y - graph[i].y
            plt.arrow(graph[i].x, graph[i].y, dx, dy, head_width = 0.5, head_length = 0.5,  length_includes_head = True)
            
        if(graph[i].direction == "next"):
            dx = graph[i].nextNode.x - graph[i].x
            dy = graph[i].nextNode.y - graph[i].y
            plt.arrow(graph[i].x, graph[i].y, dx, dy, head_width = 0.5, head_length = 0.5,  length_includes_head = True)
        
        if(graph[i].direction == "prev"):
            dx = graph[i].previous.x - graph[i].x
            dy = graph[i].previous.y - graph[i].y
            plt.arrow(graph[i].x, graph[i].y, dx, dy, head_width = 0.5, head_length = 0.5,  length_includes_head = True)
    plt.xlim([-20, 20])
    plt.ylim([-20, 20])
    plt.show()
   
def distanceChecker(graph):
    for i in range(1, len(graph)):
        if(graph[i].wantedDistanceToPrev != graph[i].calculateDistance("prev") or (graph[i].wantedDistanceToNext != graph[i].calculateDistance("next"))):
            return False
    return True

def Move(graph):
    for i in range(0, len(graph)):
        if(not graph[i].isleader):
            if(graph[i].direction == "both"):
                next = i + 1
                prev = i - 1

                if(next > len(graph) - 1):
                    next = 0
                elif(prev < 0):
                    prev = -1
                
                intersections = Intersections(graph[i].previous.x, graph[i].previous.y, graph[i].wantedDistanceToPrev, graph[i].nextNode.x, graph[i].nextNode.y, graph[i].wantedDistanceToNext)
                if(intersections is None):
                    graph[i].y = random.uniform(graph[i].y - 5, graph[i].y + 5)
                    graph[i].x = random.uniform(graph[i].x - 5, graph[i].x + 5)
                elif(len(intersections) == 2):
                    graph[i].x = intersections[0]
                    graph[i].y = intersections[1]
                else:
                    distance1 = calculateDistanceByCoordinates(intersections[0], graph[i].x, intersections[1], graph[i].y)
                    distance2 = calculateDistanceByCoordinates(intersections[2], graph[i].x, intersections[3], graph[i].y)
                    if(distance1 < distance2):
                        graph[i].x = intersections[0]
                        graph[i].y = intersections[1]
                    else:
                        graph[i].x = intersections[2]
                        graph[i].y = intersections[3]
                        
            else:
                if(graph[i].calculateDistance("next") != graph[i].wantedDistanceToNext):
                    graph[i].y = random.uniform(graph[i].y - 1, graph[i].y + 1)
                    graph[i].x = graph[i].nextNode.x - math.sqrt(math.pow(graph[i].nextNode.y - graph[i].y, 2) + math.pow(graph[i].wantedDistanceToNext, 2))
            Draw(graph)
    return graph
                
def Main(graph):
    
    iteration = 1
    graph2 = graph
    
    while(not distanceChecker(graph2)):
        iteration += 1
        print(iteration)
            
        graph2 = Move(graph2)    
    print(iteration)
    
leader = Node()
secondNode = Node()
thirdNode = Node()
fourthNode = Node()
fifthNode = Node()
sixth = Node()

leader.nextNode = secondNode
leader.previous = filter
leader.init(0, 0, None, True)

secondNode.previous = leader
secondNode.nextNode = thirdNode
secondNode.init(5, 0, "both", False)

thirdNode.previous = leader
thirdNode.nextNode = fourthNode
thirdNode.init(5, 9, "both", False)

fourthNode.previous = thirdNode
fourthNode.nextNode = leader
fourthNode.init(2, 9, "both", False)

fifthNode.previous = fourthNode
fifthNode.nextNode = leader
fifthNode.init(0, 9,"both", False)

#sixth.previous = leader
#sixth.nextNode = secondNode
#sixth.init(9, 0,"both", False)

secondNode.wantedDistanceToPrev = secondNode.calculateDistance("prev")
secondNode.wantedDistanceToNext = secondNode.calculateDistance("next")
thirdNode.wantedDistanceToPrev = thirdNode.calculateDistance("prev")
thirdNode.wantedDistanceToNext = thirdNode.calculateDistance("next")
fourthNode.wantedDistanceToPrev = fourthNode.calculateDistance("prev")
fourthNode.wantedDistanceToNext = fourthNode.calculateDistance("next")
fifthNode.wantedDistanceToPrev = fifthNode.calculateDistance("prev")
fifthNode.wantedDistanceToNext = fifthNode.calculateDistance("next")
#sixth.wantedDistanceToPrev = sixth.calculateDistance("prev")
#sixth.wantedDistanceToNext = sixth.calculateDistance("next")

graph = [leader, secondNode, thirdNode, fourthNode, fifthNode]
print("Start values: ")
print(str(secondNode.wantedDistanceToPrev) + " " + str(secondNode.wantedDistanceToNext))
print(str(thirdNode.wantedDistanceToPrev) + " " + str(thirdNode.wantedDistanceToNext))
print(str(fourthNode.wantedDistanceToPrev) + " " + str(fourthNode.wantedDistanceToNext))
print(str(fifthNode.wantedDistanceToPrev) + " " + str(fifthNode.wantedDistanceToNext))

Draw(graph)
leader.x = -1
leader.y = -2
Draw(graph)

Main(graph)

print("End values")
print(str(secondNode.calculateDistance("prev")) + " " + str(secondNode.calculateDistance("next")))
print(str(thirdNode.calculateDistance("prev")) + " " + str(thirdNode.calculateDistance("next")))
print(str(fourthNode.calculateDistance("prev")) + " " + str(fourthNode.calculateDistance("next")))
print(str(fifthNode.calculateDistance("prev")) + " " + str(fifthNode.calculateDistance("next")))