class Square:
    x_coordinate = 0
    y_coordinate = 0
    item = "empty"
    clickedStatus = "unclicked"
    surroundingMines = 0
    flagStatus = ""
    
    
    def __init__(self, xCoord, yCoord):
        self.x_coordinate = xCoord
        self.y_coordinate = yCoord
        
    def addItem(self, container):
        self.item = container
        
    
    
    
    # so basically we're going to allow them to enter an x_coordinate and a y_coordinate, and then
    
    
    
   
        