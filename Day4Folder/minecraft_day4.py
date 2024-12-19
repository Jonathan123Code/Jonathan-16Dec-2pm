# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def come():
    agent.teleport_to_player()

player.on_chat("come", come)

def fw(num):
    agent.move(FORWARD, num)

player.on_chat("fw", fw)

def bk(num):
    agent.move(BACK, num)

player.on_chat("bk", bk)

def ml(num):
    agent.move(LEFT, num)

player.on_chat("ml", ml)

def mr(num):
    agent.move(RIGHT, num)

player.on_chat("mr", mr)

def up(num):
    agent.move(UP, num)

player.on_chat("up", up)

def down(num):
    agent.move(DOWN, num)

player.on_chat("down", down)

def turnLeft():
    agent.turn(TurnDirection.LEFT)

player.on_chat("tl", turnLeft)

def turnRight():
    agent.turn(TurnDirection.RIGHT)

player.on_chat("tr", turnRight)

def mineTree(num):
    for i in range(num):
        agent.destroy(FORWARD)
        agent.collect_all()
        agent.move(UP, 1)

player.on_chat("tree", mineTree)

def mineStone(num):
    for i in range(num):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)
        
player.on_chat("stone", mineStone)

def wall(height, width):
    for i in range(height):
        agent.place(FORWARD)
        agent.move(UP,1)
    agent.move(DOWN, height)
    agent.move(RIGHT,1)

player.on_chat("wall", wall)

def solvespiral():
    while agent.inspect(AgentInspection.BLOCK, DOWN) != DIAMOND_BLOCK:
        if not agent.detect(AgentDetection.BLOCK, RIGHT):
            agent.turn(TurnDirection. RIGHT)
        agent.move(FORWARD, 1)

player.on_chat("spiral", solvespiral)

def maze():
    while agent.inspect(AgentInspection.BLOCK, DOWN) != DIAMOND_BLOCK:
        if not agent.detect(AgentDetection.BLOCK, LEFT):
            agent.turn(TurnDirection.LEFT)
            agent.move(FORWARD, 1)
        elif not agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.move(FORWARD, 1)
        else:
            agent.turn(TurnDirection.RIGHT)
            agent.move(FORWARD,1)

player.on_chat("maze", maze)

def mazes():
    while agent.inspect(AgentInspection.BLOCK, DOWN) != DIAMOND_BLOCK:
        if not agent.detect(AgentDetection.BLOCK, LEFT):
            agent.turn(TurnDirection.LEFT)
            agent.move(FORWARD, 1)
        elif not agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.move(FORWARD, 1)
        else:
            agent.turn(TurnDirection.RIGHT)
            agent.move(FORWARD,1)
        if not agent.detect(AgentDetection.BLOCK, DOWN):
            agent.move(FORWARD, 1)
            agent.move(DOWN, 15)

player.on_chat("mazes", mazes)