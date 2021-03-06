class SingleAnchorSearchGame(object):
    """
    Basic game class
    """

    asset_not_found = True

    def __init__(self, world, drones, knowledge, benchmark):
        self.k = knowledge
        self.world = world
        self.drones = drones
        self.benchmark = benchmark

    def start_game(self):
        i = 0

        # TODO: Initial 'player' with name to understand what drone is
        drone = self.next_drone()
        if not self.benchmark:
            drone.print_status()

        # Game cycle
        while self.asset_not_found or drone.fuel == 0:

            # TODO: avoid knowledge checking on game. Put this on drone probe
            if not self.k:
                drone.probe(self.world[drone.actual_position[0]][drone.actual_position[1]])

            x, y = drone.strategy()
            drone.move(x, y)
            if not self.benchmark:
                drone.print_status()

            i += 1
            if self.asset_found(x, y):
                self.asset_not_found = False

            # Wait for input and extract new drone
            drone = self.next_drone()

        # TODO: enchance this block
        if not self.benchmark:
            print "Total moves: ", i

        if drone.fuel == 0:
            return 0
        else:
            return i

    def next_drone(self):
        current_drone = self.drones.pop()
        self.drones.append(current_drone)

        return current_drone

    def asset_found(self, x, y):
        if self.k:
            return self.world[(x, y)][0] == -1
        else:
            return self.world[x][y] == -1
