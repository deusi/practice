# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def backtracking(cell, d):
            robot.clean()
            visited.add(cell)
            for i in range(4):
                newDir = (d + i) % 4
                newCell = (cell[0] + directions[newDir][0], cell[1] + directions[newDir][1])
                if not newCell in visited and robot.move():
                    backtracking(newCell, newDir)
                    goBack()
                robot.turnRight()
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtracking((0, 0), 0)
            
            
            
            
            
            
            
            
            
            
            