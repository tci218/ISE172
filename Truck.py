'''
Created on Apr 14, 2017

@author: Trent Insull
'''
class Truck:
    
    
    def __init__(self, _id, initialLocation ):
        self.id = _id
        self.location = initialLocation
        
        
        
    """
    Current location of a truck should be either at Node or on a "directed" edge
    together with the information how far on this edge the truck is.
    """    
    def updateLocation(self, currLocation):
        self.location = currLocation
         
    
    """
         it should return the edge and also how far he is on this edge, e.g. [A,C],[5,30] 
         if he is traveling 5 minutes on an edge A->C which takes 30 minutes to travel 
    """
    def getCurrentLocation(self):
        return self.location
    
    
    """
    This should return total travel history, e.g.
    A,C,30/30,P20;P94;P101    # this means he moved from A to C which was 30 minutes out of 30 minutes, he picked up 3 packages
    C,D,30/40    # then he was traveling from C to D, only for 30 minutes (so he did not get to D)
    D,C,30/40,P33;P34    # then he turn around and went back to C for 30 minutes and picked up 2 packages
    C,E,50/50,D33;D20    # then he went to E and drop package 33 and 20
    """
    def getTotalTravelHistory(self):
        history=[]
        
        return history
    
    