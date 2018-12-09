"""
Math 590
Project 2
Fall 2018


"""

# Import math.
import math

################################################################################

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    # In BFS algorithm, we utilize Queue. We start from the start point, 
    # and keep updating Queue until all vertexes inside it are popped.
    # After updating all vertexes, we backtrack from the goal, and if it
    # can reach the start, we return that path.
    if (alg == 'BFS'):
        queue = Queue()  
        s = maze.start
        # set dist = 0
        s.dist = 0
        # push the start vertex onto the Queue
        queue.push(s)
        path = []
        while (queue.isEmpty() == False):      
            # get the current vertex
            current = queue.pop()
            # look at all of its neighbors
            for neighbor in current.neigh:
                # if the neighbor's dist is not updates
                if(neighbor.dist == math.inf):
                    # push the neighbor into the Queue
                    queue.push(neighbor)
                    # update its distance
                    neighbor.dist = current.dist + 1
                    # update its track path
                    neighbor.prev = current
        rev_path = []
        endPoint = maze.exit
        while (endPoint != None):
            rev_path.append(endPoint.rank)
            endPoint = endPoint.prev
        # reverse the path and make it to be
        # exit -> start to start -> exit
        path = rev_path[::-1]
        #if there is no solution (cannot reach goal from start), return empty path
        if(path[0]!=maze.start.rank):   
            return []
        return path
    
    # In DFS algorithm, we utilize Stack. We start from the start point, 
    # and keep updating Stack until all vertexes inside it are popped.
    # After updating all vertexes, we backtrack from the goal, and if it
    # can reach the start, we return that path. Unlike BFS, we keep updating
    # "visited" flags instead of "distance counts" for tracking.
    if (alg == 'DFS'):
        stack = Stack()
        s = maze.start
        # Push the start vertex onto Stack
        stack.push(s)
        while(stack.isEmpty() == False):
            # get the current element
            current = stack.pop()
            # mark it as visited
            current.visited = True
            # push all neighbors onto Stack then record where they came from
            # if they have not already been visited
            for neighbor in current.neigh:
                if(neighbor.visited == False):
                    stack.push(neighbor)
                    neighbor.prev = current
        rev_path = []
        endPoint = maze.exit
        while (endPoint != None):
            rev_path.append(endPoint.rank)
            endPoint = endPoint.prev
        # reverse the path and make it to be
        # exit -> start to start -> exit        
        path = rev_path[::-1]
        #if there is no solution (cannot reach goal from start), return empty path
        if(path[0]!=maze.start.rank):  
            return []
        return path

################################################################################

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 100.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=100):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.stack)
        print('Top: %d' % self.top)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        if self.numElems == len(self.stack):
            return True
        else:
            return False

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        if self.numElems == 0:
            return True
        else:
            return False

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        self.stack = self.stack + [None for x in self.stack]
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        if (self.isFull()):   # check whether stack is full to ensure enough space to push the new element
            self.resize()
        self.top += 1   # create new element at top of stack
        self.stack[self.top] = val   # give this element a value
        self.numElems += 1   # refresh the counting number
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        if (self.isEmpty()):   # check whether the stack is empty to ensure a smooth pop
            print('nothing to pop from stack')
            return None
        else:
            temp = self.stack[self.top]   # record top element of stack
            self.stack[self.top] = None   # delete the top element from stack
            self.top -= 1   # change the top pointer to the new top
            self.numElems -= 1   # reduce number of elements in stack
            return temp

################################################################################

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 100.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.queue)
        print('Front: %d' % self.front)
        print('Rear: %d' % self.rear)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        if self.numElems == len(self.queue):
            return True
        else:
            return False

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        if self.numElems == 0:
            return True
        else:
            return False

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        # If the queue is wrapped, reset order of elems.
        if not (self.rear > self.front):
            self.queue = self.queue[self.front:] + self.queue[0:self.rear]

        # Update front and rear.
        self.front = 0
        self.rear = self.numElems

        # Now append the extra space (double size).
        self.queue = self.queue + [None for x in self.queue]
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        # check whether there is space avaliable to push in new element
        # if no, resize queue and make new spaces
        if (self.isFull()):
            self.resize()
        # reset the rear counter as the pushed element reach the end of queue and space is not full
        # to make sure queue can be fully utilized
        if (self.rear == len(self.queue)): 
            self.rear = 0
        # push a value into the rear of the queue
        self.queue[self.rear] = val
        # increase rear counter
        self.rear += 1
        # increase elements counter
        self.numElems += 1      
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        # check whether there is element avaliable to pop
        # if no, do nothing
        if (self.isEmpty()): 
            print('nothing to pop from queue')
            return None
        # reset the front counter as the poped element reach the end of queue
        # to make sure it repeat the popping process
        if (self.front == len(self.queue)):
            self.front = 0
        # make a temporary variable representing the front element of queue
        temp = self.queue[self.front]
        # pop the value from the front of the queue
        self.queue[self.front] = None##delete the original front's value
        # point the next element to be the front element (front counter)
        self.front += 1##change to the new front
        # decrease elements counter
        self.numElems -= 1 ## change the number of elements
        # return the original front element
        return temp
        
################################################################################

"""
Vertex Class
"""
class Vertex:

    """
    Class attributes:
    
    rank    # The rank of this node.
    neigh   # The list of neighbors.
    dist    # The distance from start.
    visited # Flag whether vertex has been visited.
    prev    # The previous vertex in the path.
    """

    """
    __init__ function to initialize the vertex.
    """
    def __init__(self, rank):

        self.rank = rank     # Set the rank of this vertex.
        self.neigh = []      # Set the input neighbors.
        self.dist = math.inf # Infinite dist initially.
        self.visited = False # Nothing visited at initialization.
        self.prev = None     # No previous node on path yet.
        return

    """
    __repr__ function to print a vertex.
    Note: only prints the rank!
    """
    def __repr__(self):
        return '%d' % self.rank

    """
    isEqual function compares this Vertex to an input Vertex object.
    Note: only needs to compare the rank!
    """
    def isEqual(self,vertex):
        return self.rank == vertex.rank

################################################################################
    
"""
Maze Class
"""
class Maze:

    """
    Class attributes:

    maze    # The 2D list representing the maze.
    adjList # The adjacency list of Vertex objects.
    adjMat  # The adjacency matrix, 2D list.
    start   # The start Vertex object.
    exit    # The exit Vertex object.
    path    # The path from start to exit, list of ranks.
    verb    # A flag to control printing. False prints less.
    """

    """
    __init__ function to initialize the maze.
    """
    def __init__(self, mazeNum=0, verbosity=False):

        # Select the maze to use.
        self.maze = getMaze(mazeNum)

        # Create an adjacency list of empty vertices.
        self.adjList = [Vertex(r) for r in \
                        range(0,len(self.maze)*len(self.maze[0]))]

        # Initialize the adjacency matrix to have no edges yet.
        self.adjMat = [[0 for x in self.adjList] for y in self.adjList]

        # Now loop through the maze and update adjacencies.
        # In this loop, maze[r][c] will correspond to vertex rank:
        #     r*len(maze[0])+c
        # Note: we skip the first and last row/col.
        for r in range(1,len(self.maze)-1):
            for c in range(1,len(self.maze[r])-1):
                # Note that maze[r][c] will now be a 0 or a 1.
                # If it is 0, then open space and needs adjacency.
                # If it is 1, then wall and no adjacency.
                if self.maze[r][c] == 0:
                    # If up is open, it is a neighbor.
                    if self.maze[r-1][c] == 0:
                        # Append the neighbor to the neigh list.
                        self.adjList[r*len(self.maze[0])+c].neigh.append(\
                            self.adjList[(r-1)*len(self.maze[0])+c])

                        # Update the correct entry in the adjMat.
                        self.adjMat[r*len(self.maze[0])+c]\
                                   [(r-1)*len(self.maze[0])+c] = 1
                        
                    # If down is open, it is a neighbor.
                    if self.maze[r+1][c] == 0:
                        # Append the neighbor to the neigh list.
                        self.adjList[r*len(self.maze[0])+c].neigh.append(\
                            self.adjList[(r+1)*len(self.maze[0])+c])

                        # Update the correct entry in the adjMat.
                        self.adjMat[r*len(self.maze[0])+c]\
                                   [(r+1)*len(self.maze[0])+c] = 1
                        
                    # If left is open, it is a neighbor.
                    if self.maze[r][c-1] == 0:
                        # Append the neighbor to the neigh list.
                        self.adjList[r*len(self.maze[0])+c].neigh.append(\
                            self.adjList[r*len(self.maze[0])+c-1])

                        # Update the correct entry in the adjMat.
                        self.adjMat[r*len(self.maze[0])+c]\
                                   [r*len(self.maze[0])+c-1] = 1
                        
                    # If right is open, it is a neighbor.
                    if self.maze[r][c+1] == 0:
                        # Append the neighbor to the neigh list.
                        self.adjList[r*len(self.maze[0])+c].neigh.append(\
                            self.adjList[r*len(self.maze[0])+c+1])

                        # Update the correct entry in the adjMat.
                        self.adjMat[r*len(self.maze[0])+c]\
                                   [r*len(self.maze[0])+c+1] = 1

        # Find the start in the top row and exit in the bottom row.
        # Update their info in the adjList and adjMat.
        # Note: start's only neighbor is down and exit's is up.
        for ind in range(0,len(self.maze[0])):
            if self.maze[0][ind] == 0:
                self.start = self.adjList[ind]
                self.start.neigh = [self.adjList[ind + len(self.maze[0])]]
                self.adjMat[ind][ind + len(self.maze[0])] = 1
                break
        for ind in range(0,len(self.maze[len(self.maze)-1])):
            if self.maze[len(self.maze)-1][ind] == 0:
                self.exit = \
                    self.adjList[ind + (len(self.maze)-1)*len(self.maze[0])]
                self.exit.neigh = [self.adjList[ind + \
                                   (len(self.maze)-2)*len(self.maze[0])]]
                self.adjMat[self.exit.rank]\
                           [self.exit.rank - len(self.maze[0])] = 1
                break

        # Set the path to be empty.
        self.path = []

        # Set verbosity.
        self.verb = verbosity
        return

    """
    __repr function to print the maze.
    """
    def __repr__(self):
        # Loop through the rows and cols of the maze and fill in 'X' for a wall
        # and ' ' for an open space. Put line breaks between rows.
        mp = ''
        for r in range(0,len(self.maze)):
            for c in range(0,len(self.maze)):
                if self.maze[r][c] == 0:
                    mp += ' '
                else:
                    mp += 'X'
            mp += '\n'

        # Mark the start with 's' and the end with 'e'.
        # Note the shift due to the line break symbols.
        # Note that each line break '\n' counts as 1 char...
        mp = mp[0:self.start.rank] + 's' + \
             mp[self.start.rank+1:self.exit.rank+len(self.maze)-1] + \
             'e' + mp[self.exit.rank+len(self.maze):]

        # If the path is not empty, fill it in.
        # Check to make sure it is a correct and valid path.
        if len(self.path) > 0:

            # Not an invalid path yet...
            invalid = False
            
            # Needs to start at start and end at end.
            if self.path[0] != self.start.rank:
                print('Path does not begin at start!')
                invalid = True
                mp = mp[0:self.start.rank+self.start.rank//len(self.maze[0])]+\
                     '!' + \
                     mp[self.start.rank+self.start.rank//len(self.maze[0])+1:]
            if self.path[len(self.path)-1] != self.exit.rank:
                print('Path does not exit the maze!')
                invalid = True
                mp = mp[0:self.exit.rank+self.exit.rank//len(self.maze[0])]+\
                     '!' + \
                     mp[self.exit.rank+self.exit.rank//len(self.maze[0])+1:]

            # Loop through the path and fill it in.
            # Check for invalid ghosts and repeats.
            for vertex in self.path:
                # Skip the start and end.
                if (vertex != self.start.rank) and (vertex != self.exit.rank):
                    # Check if it is a wall or opening. Fill if open.
                    # Also check if already visited.
                    if mp[vertex+vertex//len(self.maze[0])] == 'X':
                        print('No ghosts! Do not walk through walls!')
                        invalid = True
                        mp = mp[0:vertex+vertex//len(self.maze[0])] + 'G' + \
                             mp[vertex+vertex//len(self.maze[0])+1:]
                    elif mp[vertex+vertex//len(self.maze[0])] == 'o':
                        print('You have already been to this vertex...')
                        invalid = True
                        mp = mp[0:vertex+vertex//len(self.maze[0])] + 'R' + \
                             mp[vertex+vertex//len(self.maze[0])+1:]
                    elif mp[vertex+vertex//len(self.maze[0])] == 'G':
                        print('Repeated ghosts!')
                    elif mp[vertex+vertex//len(self.maze[0])] == 'R':
                        print('Repeating again!')

                    else:
                        mp = mp[0:vertex+vertex//len(self.maze[0])] + 'o' + \
                             mp[vertex+vertex//len(self.maze[0])+1:]

            # Loop through the path to make sure that each neighbor is actually
            # a neighbor...
            for vInd in range(0,len(self.path)-1):
                if (self.adjMat[self.path[vInd]][self.path[vInd+1]] != 1) \
                   and (self.path[vInd] != self.path[vInd+1]):
                    print('Not a neighbor! You cannot teleport!')
                    invalid = True

            # If we had an invalid path, print that fact.
            if invalid:
                print('')
                print('Path is invalid!')
                print('')
            else:
                print('')
                print('MAZE SOLVED!!!')
                print('')

        # Return the string for printing.
        if self.verb:
            return mp
        else:
            return ''

    """
    printList function for cleanly printing the adjaceny list.
    Note: skips vertices with no neighbors.
    """
    def printList(self):
        for vertex in self.adjList:
            if len(vertex.neigh) > 0:
                print('Rank: %d' % vertex.rank)
                print('Neighbors:')
                print(vertex.neigh)
                print('')
        return

    """
    printMat function for cleanly printing the adjaceny matrix.
    Note: for the larger mazes, this will still likely be hard to read.
    """
    def printMat(self):
        for row in self.adjMat:
            print(row)
        return

    """
    solve function calls implemented bdfs using the input alg.
    Note: set verbosity to True to print out the resulting maze/path.
    """
    def solve(self, alg, verbosity=False):
        self.path = bdfs(self, alg)
        if len(self.path) == 0:
            print('Maze not solved!\n')
        self.verb = verbosity
        print(self)
        return

################################################################################

"""
getMaze function will provide the 2D array representing the maze to the Maze
class's __init__ function.

INPUTS
mazeNum: which maze to select

OUTPUTS
maze: a 2D list representing the maze
"""
def getMaze(mazeNum=0):
    # Select the maze to use.
    if mazeNum == 0:
        maze = [[1,1,0,1,1],\
                [1,0,0,0,1],\
                [1,0,0,0,1],\
                [1,0,0,0,1],\
                [1,1,0,1,1],]
    elif mazeNum == 1:
        maze = [[1,1,0,1,1],\
                [1,0,0,0,1],\
                [1,0,1,1,1],\
                [1,0,0,0,1],\
                [1,1,0,1,1],]
    elif mazeNum == 2:
        maze = [[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
                [1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,1],\
                [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1],\
                [1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1],\
                [1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1],\
                [1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1],\
                [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1],\
                [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1],\
                [1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,1,1],\
                [1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1],\
                [1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1],\
                [1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1],\
                [1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1],\
                [1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,1],\
                [1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1],\
                [1,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,1],\
                [1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1],\
                [1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1],\
                [1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1],\
                [1,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1],\
                [1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1],\
                [1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1],\
                [1,0,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1],\
                [1,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,1],\
                [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    elif mazeNum == 3:
        maze = [[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],\
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    else:
        raise Exception('Input mazeNum not valid!')

    return maze

################################################################################

"""
testMazes function will test all of the mazes.
"""
def testMazes(verbosity=False):
    m = Maze(0,verbosity)
    print('Testing Maze 0, DFS')
    m.solve('DFS',verbosity)
    print('Testing Maze 0, BFS')
    m.solve('BFS',verbosity)
    m = Maze(1,verbosity)
    print('Testing Maze 1, DFS')
    m.solve('DFS',verbosity)
    print('Testing Maze 1, BFS')
    m.solve('BFS',verbosity)
    m = Maze(2,verbosity)
    print('Testing Maze 2, DFS')
    m.solve('DFS',verbosity)
    print('Testing Maze 2, BFS')
    m.solve('BFS',verbosity)
    m = Maze(3,verbosity)
    print('Testing Maze 3, DFS')
    m.solve('DFS',verbosity)
    print('Testing Maze 3, BFS')
    m.solve('BFS',verbosity)
    return

################################################################################
