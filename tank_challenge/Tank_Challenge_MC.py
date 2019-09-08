import api
import copy
import random 
'''
copy right: this code belongs to Min Cheng minc@student.chalmers.se https://github.com/MinCheng123
'''

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
    
    def __init__(self,direction,matrix,tank_coordinate):
        self.matrix = matrix # surrounded wall plus 2 
        self.tank_coordinate= tank_coordinate#[11,10] #[row][colomn] lvl1 
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
        
        self.matrix[self.old_coordinate[0]][self.old_coordinate[1]]=6
        self.matrix[self.tank_coordinate[0]][self.tank_coordinate[1]]=9 
#        print( 'tank coordinate:',self.tank_coordinate)
#        print('old_value',self.old_value)
        self.old_direction = self.Direction.copy()
#        self.print_map()
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
#        print('tank direction',self.Direction,'same direction', self.old_direction == self.Direction)
        
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
        
        print('object direction',self.Direction,'tank coordiante',self.tank_coordinate)
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
            
            
class Explore:
    def __init__(self,tank_coordinate,direction,matrix,Direction):
        self.tank_coordinate=tank_coordinate
        self.direction = direction 
        self.up, self.down, self.right, self.left = [-1,-1], [-1,-1], [-1,-1], [-1,-1]
        self.adjacent_coordinate_value=[-1,-1,-1,-1]
        self.matrix= matrix
        self.Direction = Direction
        self.direction_index=0
    def adjacent_coordinate(self):
        
        self.up    = [self.tank_coordinate[0]-1, self.tank_coordinate[1]   ] 
        self.down  = [self.tank_coordinate[0]+1, self.tank_coordinate[1]   ] 
        self.left  = [self.tank_coordinate[0]  , self.tank_coordinate[1]-1 ] 
        self.right = [self.tank_coordinate[0]  , self.tank_coordinate[1]+1 ] 
        print( self.up,self.left,self.down,self.right)
    
        
    def next_turn_direction(self):
        self.adjacent_coordinate()
        adjacent_coordinate_value = [   self.matrix[self.up[0]][self.up[1]], 
                                        self.matrix[self.left[0]][self.left[1]],
                                        self.matrix[self.down[0]][self.down[1]],
                                        self.matrix[self.right[0]][self.right[1]]   ] # up left down right
        value= -1
#        if matrix[self.up[0], self.up[1]
        obstacle=0
        walked=0
        unexplored=0
        random_value = random.randint(0,100)
        probability={'obstacle':0,'walked':0,'unexplored':100}
        check=""
        for element_adjacent_coord in adjacent_coordinate_value:
            if element_adjacent_coord == 6:    # walked path
                walked+=1
            if element_adjacent_coord ==0:      # unexplored path
                unexplored+=1
            if element_adjacent_coord == 1:     # obstacle
                obstacle+=1
        if obstacle==0:
            if walked == 4:
                probability['unexplored'], probability['walked'] = 100,90
            elif walked == 3:
                probability['unexplored'], probability['walked'] = 90,30
            else:
                probability['unexplored'], probability['walked'] = 90,10
        if obstacle ==1:
            probability['unexplored'], probability['walked'] = 80,60
        if obstacle ==2:
            if unexplored==0:
                probability['unexplored'], probability['walked'] = 90,70
            else:
                probability['unexplored'], probability['walked'] = 90,10
        if obstacle == 3:
            probability['unexplored'], probability['walked'] = 100,100
        
            
        print('unexplored',unexplored,'walked',walked,'obstacle',obstacle)        
        for index_direction, element_direction in enumerate(self.direction):
            
            if  element_direction == 1:
                
                if adjacent_coordinate_value[index_direction] == 1:
                    check = 'obstacle'
                elif adjacent_coordinate_value[index_direction] == 0:
                    check = 'unexplored' 
                else:
                    check = 'walked'
        print('adjacent',adjacent_coordinate_value,index_direction,adjacent_coordinate_value[index_direction],probability[check] > random_value,)
        print('probability', check,probability[check],random_value)
        return probability[check] < random_value
                # if   probability[check] > random_value:
                #     api.move_forward()
                # else:
                #     self.Direction.go_right()
                # print('adjacent',adjacent_coordinate_value[index_direction], random_value )
    def turn_left_or_right(self): # return 0 == left else right
        for index, element in enumerate(self.direction):
                if element == 1:
                    self.direction_index=index
        if self.adjacent_coordinate_value[0] ==1 and  self.adjacent_coordinate_value[1] ==1:  # up left down right
            if self.direciton_index == 1:
                return 0
            if self.direction_index == 0:
                return 1
        if self.adjacent_coordinate_value[0] ==1 and  self.adjacent_coordinate_value[3] ==1:
            if self.direction_index == 0:
                return 0
            if self.direction_index == 3:
                return 1
        if self.adjacent_coordinate_value[1] ==1 and  self.adjacent_coordinate_value[2] ==1:
            if self.direction_index == 1:
                return 1
            if self.direction_index == 2:
                return 0
        if self.adjacent_coordinate_value[3] ==1 and  self.adjacent_coordinate_value[2] ==1:        
            if self.direction_index == 3:
                return 0
            if self.direction_index == 2:  
                return 1
                    
                    
                    
class fire_mode:
    def __init__(self,direction):
        self.scan_distance=[-1,-1,-1,-1] # up left down right
        self.direction = direction  #up left down right
        self.Direction = Direction(direction)
        self.distance_limit=4
        self.front=api.lidar_front()
        self.left =api.lidar_left()
        self.right=api.lidar_right()
        self.back =api.lidar_back()
        
    def lidar_scan(self):
        self.front=api.lidar_front()
        self.left =api.lidar_left()
        self.right=api.lidar_right()
        self.back =api.lidar_back()
        for index,element in enumerate(self.direction):
            if element == 1:
                if index == 0:
                    self.scan_distance=[self.front,self.left,self.back,self.right]
                if index == 1:
                    self.scan_distance=[self.right,self.front ,self.left, self.back ]
                if index == 2:
                    self.scan_distance=[self.back,self.right ,self.front,self.left]
                if index == 3:
                    self.scan_distance=[self.left,self.back, self.right, self.front]
        print('scan_distance',self.scan_distance,'scan_direction',self.direction)
    
    # def enemy_check(self):
    #     if 
        # max_index=scan_distance.index(max(scan_distance))
        # for index,element in enumerate(self.direction):
        #     if element == 1:
        #         if max_index-index ==  
    

class Solution:
    
    def __init__(self):
        # If you need initialization code, you can write it here!
        # Do not remove.

        self.matrix = [[0 for i in range(44)] for j in range(24)]
    
        self.direction = [0,0,1,0] #[1,0,0,0] up left down right
        self.tank_coordinate=[5, 10]  #[10,10]
#        self.old_direction= [-1,-1,-1,-1]
        
        self.Direction = Direction(self.direction)
        self.Coordination=Coordination(self.direction,self.matrix,self.tank_coordinate)
        self.Explore = Explore(self.tank_coordinate,self.direction,self.matrix,self.Direction)
        self.fire_mode = fire_mode(self.direction)
        self.target = True
        self.fire_flag= False
        self.next_turn = 1 
        self.moving_forward_flag=True
        self.old_fuel =0
        self.moving_forward_blocked_flag=False


    def update(self):
        """
        Executes a single step of the tank's programming. The tank can only 
        move, turn, or fire its cannon once per turn. Between each update, the 
        tank's engine remains running and consumes 1 fuel. This function will be 
        called repeatedly until there are no more targets left on the grid, or 
        the tank runs out of fuel.
        """
        # Todo: Write your code here!

        self.old_fuel = api.current_fuel()
        if self.fire_flag == False:
            self.Coordination.tank_track()
            self.Coordination.object_detect(self.direction)

        print( 'tank coordinate:',self.tank_coordinate)
        if self.Explore.next_turn_direction() and api.identify_target() is False :
            if self.Explore.turn_left_or_right() is 0:
                self.Direction.go_left() 
            else:
                self.Direction.go_right()

            self.fire_mode.lidar_scan()
            self.moving_forward_flag = False
        elif api.identify_target():
                api.fire_cannon()
                self.fire_flag = True
                self.next_turn =1     
                print('fire!!!')
        else:
            print('tank is moving forward !!!!')
            api.move_forward()
            self.moving_forward_flag = True
            if self.moving_forward_flag and (self.old_fuel-api.current_fuel() ) >=50 and api.identify_target() :
                print('ops blocked',api.identify_target(), api.lidar_front()<=1 )

        print('api.identify_target():',api.identify_target())
        self.Coordination.print_map()  
        self.fire_mode.lidar_scan()


        print('fuel',api.current_fuel(),self.old_fuel )    
      
        if self.next_turn != 0:    
            self.fire_flag = True
            self.next_turn-=1
        else:
            self.fire_flag = False
        
        #print(self.next_turn)