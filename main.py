import copy

OPEN = []  # Closed nodes
CLOSED = []  # Open nodes

GOAL_STATE = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]


def printParentsState(node):
    """Print all the node's parents state."""
    printPrettyState(node.state)
    foundParent = node.parent
    parents = []

    while foundParent:
        if foundParent.parent:
            printPrettyState(foundParent.state)
            parents.append(foundParent.parent)
            foundParent = foundParent.parent
        else:
            foundParent = None

    exit()


def printPrettyState(state):
    """Print the state in a pretty format."""
    for row in state:
        print(row)
    print('')


def getValueDistanceInStates(value, fromState, toState):
    """
    Manhattan distance in value.

    Get the manhattan distance for value from intial state to desired state
    """
    fromPosition = None
    toPosition = None
    for row in range(3):
        for column in range(3):
            if fromState[row][column] == value:
                fromPosition = [row, column]
            if toState[row][column] == value:
                toPosition = [row, column]

    return abs(toPosition[0] - fromPosition[0]) + abs(toPosition[1] - fromPosition[1])


# Possible movements
def getMovementsAndCero(value, state):
    """
    Posible movement's positions and value.

    Get possible moves to specified value and return the array of
    the positions of the values that can be moved, also the value position
    """
    position = []

    for row in range(3):
        for column in range(3):
            if state[row][column] == 0:
                position = [row, column]

    possiblePositions = []

    if position[0] < 2:
        possiblePositions.append([position[0] + 1, position[1]])

    if position[0] > 0:
        possiblePositions.append([position[0] - 1, position[1]])

    if position[1] < 2:
        possiblePositions.append([position[0], position[1] + 1])

    if position[1] > 0:
        possiblePositions.append([position[0], position[1] - 1])

    return position, possiblePositions


class Node():
    """
    Node class.

    Get possible moves to specified value and return the array of
    the positions of the values that can be moved, also the value position
    """

    def __init__(self, state, parent, height):
        """Initialize the node with state, parent and height."""
        self.state = state
        self.parent = parent
        self.manhattanDistance = self.__getManhatanDistance()
        self.height = height
        self.heuristic = self.getHeuristics()

    def getHeuristics(self):
        return self.manhattanDistance + self.height

    def getPossibleChildren(self):
        """Possible children of the node."""
        # Calculate possible movements and the cero position
        ceroPosition, possibleMovements = getMovementsAndCero(0, self.state)
        children = []

        for movement in possibleMovements:
            childState = copy.deepcopy(self.state)  # Copy array, no reference
            childState[ceroPosition[0]][ceroPosition[1]] = self.state[movement[0]][movement[1]]  # Replace 0 with actual value
            childState[movement[0]][movement[1]] = 0  # Set old value 0

            # Append just the children that are not listed in closed array
            found = list(filter(lambda node: node.state == childState, CLOSED))

            if len(found) == 0:
                children.append(Node(childState, self, self.height + 1))
            else:
                childManhattanDistance = 0

                for number in range(9):
                    distance = getValueDistanceInStates(number, childState, GOAL_STATE)
                    childManhattanDistance += distance

                if (found[0].height + found[0].manhattanDistance) > (self.height + 1 + childManhattanDistance) and found[0].parent is not None:
                    found[0].parent = self
        return children

    def __getManhatanDistance(self):
        totalDistance = 0

        for number in range(9):
            distance = getValueDistanceInStates(number, self.state, GOAL_STATE)
            totalDistance += distance

        return totalDistance


def startSearch(initialState):
    """Main program."""
    initialNode = Node(initialState, None, 0)
    OPEN.append(initialNode)

    if not OPEN:
        print('Failure, shame on you')
        exit()

    while len(OPEN) > 0:
        Si = OPEN[0]
        del OPEN[0]

        CLOSED.append(Si)

        if Si.state == GOAL_STATE:
            print('FOUND GOAL STATE:')
            print('Height: %s' % Si.height)
            printParentsState(Si)

        children = Si.getPossibleChildren()

        # Add children to open, TIP: extend === concat
        OPEN.extend(children)

        # print("Length OPEN: %s" % len(OPEN))
        OPEN.sort(key=lambda node: node.heuristic)
        # sorted(OPEN, key=lambda node: node.height + node.manhattanDistance)
        # print('CLOSED')
        # for node in OPEN:
            # print(node.heuristic)
        # Reorder list open of the values (increasing) that have better f^


INITIAL_STATE = [
    [1, 3, 2],
    [0, 8, 4],
    [7, 6, 5]
]

startSearch(INITIAL_STATE)
