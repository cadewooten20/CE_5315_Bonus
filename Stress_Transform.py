# -*- coding: utf-8 -*-

import numpy as np
from vpython import *

#Class that will encapsulte the stress state (tensor) and also perform operations 
#to normalize and transform a given matrix
class StressState:
    
    def __init__(self, stress_tensor, orientation_matrix = np.array([[1,0,0],[0,1,0],[0,0,1]])):
        
        #Initialize the stress tensor variable 
        self.stress_tensor = stress_tensor
        
        #Transform the stress tensor, if for some reason the original orientation is not common to the x,y,z axis
        self.stress_transform(orientation_matrix.copy())
    
    #Method to perform a stress transofmation on the Stress State object
    #Requires the input of 'orientation matrix', which is an array of the N1,N2 & N3 vectors
    def stress_transform(self,orientation_matrix):
        
        StressState.normalize_vector(orientation_matrix)
        
        self.orientation_matrix = orientation_matrix.copy()
        
        #Placeholder variable for the transformed stress matrix
        transformed_state = np.zeros((3,3))
        
        #Variable that will be triggered if the axis of the transformation 
        #Vectors are not perpendicular 
        perpendicular = True
        
        
        for i in range (3):  
            
            #Calculates the transformed stress component (sigma_P) on the new plane normal to N1, N2 or N3.  
            sigma = self.stress_tensor.T@self.orientation_matrix[i]
            
                        
            if perpendicular == False:
                    break
            #Performs the dot product operation to fill out the entire transformed stress matrix            
            for j in range (3):
                
                N = self.orientation_matrix[j]
                
                if ((round(np.inner(self.orientation_matrix[j-1],self.orientation_matrix[j]),2))) != 0:
                    
                    print('Stress transformation vectors are not mutually perpendicular\n'
                          + 'No transformation has been made, please try again')
                    perpendicular = False
                    break
                    
                transformed_state[i,j] = round(np.inner(sigma,N),3)
                
        if perpendicular == True:
            self.stress_tensor = transformed_state.copy()    
            
        print(self.stress_tensor)      
        
    #Method to normalize any orientation matrix passed in 
    #Goes row by row to normalize N1, N2 & N3
    #The matrix is pass by reference, so the method does not need to return anything 
    #It will change the value of the original matrix passed in from outside the method 
    def normalize_vector(orientation_matrix):
        num_rows = np.shape(orientation_matrix)[0]
        num_cols = np.shape(orientation_matrix)[1]
        

        for i in range(num_rows):
            magnitude = np.linalg.norm(orientation_matrix[i])

            for j in range(num_cols):
                orientation_matrix[i][j] = round((orientation_matrix[i][j]/magnitude),4)
                
                
    def plot_cube(self, origin = vector(0,0,0)):
        print('test')
            
 
    
    
stress_tensor = np.array([[100,50,-50],
                          [50,200,0],
                          [-50,0,200]])

n1 = np.array([.866,.25,.433])
#n1 = np.array([2,2,1])
n2 = np.array([-.5,.433,.75])
n3 = np.array([0,-.866,.5])
orientation_matrix = np.array([n1,n2,n3])


stress_cube = StressState(stress_tensor)

stress_cube.stress_transform(orientation_matrix)

scene = canvas()

box(pos=vector(0,0,0), opacity=.3)
arrow(pos=vector(0,0,0), axis=vector(1,0,0), shaftwidth = .03, opacity=.3)


box(pos=vector(2,0,0),axis=vector(n1[0],n1[1],n1[2]))
arrow(pos=vector(2,0,0),axis=vector(n1[0],n1[1],n1[2]),  shaftwidth = .03)


