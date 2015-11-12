from direction import Direction
from path import Path
from controller import Controller
if __name__ == "__main__":
    path = Path(Direction(0),Direction(1))
    con = Controller()
    con.addPath(path)
    con.getPaths()
