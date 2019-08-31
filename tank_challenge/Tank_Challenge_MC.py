import api
import copy

class Direction:
    
    def __init__(self,direction):
        self.direction = direction # up left down right
    
    def go_left(self):
        api.turn_left()
        for index, element in enumerate(self.direction):
            if index==3:
                index_new=0
            else:
                index_new=index+1
            if element==1:    
                self.direction[index]=0
                self.direction[index_new]=1
                break
        # print('index',index, index_new)        
        print('direction',self.direction)     
    
    def go_right(self):
        api.turn_right()
        for index, element in enumerate(self.direction):
            if index==0:
                index_new=3
            else:
                index_new=index-1
            if element==1:    
                self.direction[index]=0
                self.direction[index_new]=1
                break
        # print('index',index, index_new)        
        #print(self.direction)
        
class Coordination:
    
    def __init__(self,direction):
        self.matrix = [[0 for i in range(22)] for j in range(13)] # surrounded wall plus 2 
        self.tank_coordinate=[11,10] #[row][colomn] lvl1 
        self.Direction=direction
        self.old_coordinate=[-1,-1]
        self.old_value=0
        self.lidar_distance_front=api.lidar_front()
        self.object_coordinate=[11,10] #[row][colomn] lvl1
        self.old_direction=0
        
    def tank_track(self):
        
        self.direction_detection_tank()  # tank_coordiante update 

#        print('old_coordinate',self.old_coordinate)
        print(self.old_value)
        
        self.matrix[self.old_coordinate[0]][self.old_coordinate[1]]=0
        self.matrix[self.tank_coordinate[0]][self.tank_coordinate[1]]=9 
        print( 'tank coordinate:',self.tank_coordinate)
#        print('old_value',self.old_value)
        self.old_direction = self.Direction.copy()
        self.print_map()
        self.old_coordinate=self.tank_coordinate.copy()
        self.old_value=self.matrix[self.old_coordinate[0]][self.old_coordinate[1]]
            
    def object_detect(self,direction):
        self.lidar_distance_front=api.lidar_front()
        if self.lidar_distance_front and api.identify_target() is False:
            self.direction_detection_object(self.lidar_distance_front  )
            print('obstacle distance',self.object_coordinate,'lidar_front',self.lidar_distance_front)
            self.matrix[ self.object_coordinate[0] ][ self.object_coordinate[1] ] = 1 
#            self.print_map()
            
             
    def direction_detection_tank(self):
        print('tank direction',self.Direction,'same direction', self.old_direction == self.Direction)
        
        if self.old_direction == self.Direction:
            for index, element in enumerate(self.Direction):
                if element == 1:
                    if index == 0: #up
                        self.tank_coordinate[0]-=1 
                    elif index ==1: #left
                        self.tank_coordinate[1]-=1
                    elif index ==2: #down  
                        self.tank_coordinate[0]+=1 
                    elif index ==3: #right 
                        self.tank_coordinate[1]+=1 
#                print(self.tank_coordinate)  
    
    def direction_detection_object(self,distance):
        
        print('object direction',self.Direction)
        for index, element in enumerate(self.Direction):
            if element == 1:
                if index == 0: #up
                    self.object_coordinate[0]=self.tank_coordinate[0]-distance 
                    self.object_coordinate[1]=self.tank_coordinate[1]
                elif index ==1: #left
                    self.object_coordinate[1]=self.tank_coordinate[1]-distance
                    self.object_coordinate[0]=self.tank_coordinate[0]
                elif index ==2: #down  
                    self.object_coordinate[0]=self.tank_coordinate[0]+distance
                    self.object_coordinate[1]=self.tank_coordinate[1]
                elif index ==3: #right 
                    self.object_coordinate[1]=self.tank_coordinate[1]+distance  
                    self.object_coordinate[0]=self.tank_coordinate[0]    
        
    def print_map(self):
        for row in self.matrix:
            print(row)    

    
        
class Solution:
    
    def __init__(self):
        # If you need initialization code, you can write it here!
        # Do not remove.
        self.direction = [1,0,0,0] # up left down right
#        self.old_direction= [-1,-1,-1,-1]
        self.Direction = Direction(self.direction)
        self.Coordination=Coordination(self.direction)
        self.target = True
        pass

    def update(self):
        """
        Executes a single step of the tank's programming. The tank can only 
        move, turn, or fire its cannon once per turn. Between each update, the 
        tank's engine remains running and consumes 1 fuel. This function will be 
        called repeatedly until there are no more targets left on the grid, or 
        the tank runs out of fuel.
        """
        # Todo: Write your code here!
        #self.Coordination.object_detect(self.direction)
        
        self.Coordination.tank_track()
        if api.lidar_front() <= 1:
            
            self.Direction.go_right()
#            self.target=api.identify_target()
#        print('same.direction',self.direction==self.old_direction)
       
        
        
        self.Coordination.object_detect(self.direction)
        api.move_forward()
        