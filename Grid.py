# Desenha um campo com os caminhos e obstaculos existentes


class Point:
    ''' Representa um ponto
    '''
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)


class PathFinder:
    ''' Encontra caminhos em um campo retangular com obstaculos
    '''
    def __init__(self, field):
        self._field = field

    def shortest_path(self, start_point, end_point):
        ''' Dato o inicio / fim, encontra um o caminho mais curto entre os dois (se existir)
        '''
        self._check_range(start_point)
        self._check_range(end_point)
        if self.is_obstacle(start_point) or self.is_obstacle(end_point):
            return []
        # the queue of paths
        queue = []
        visited = set()
        queue.append([start_point])
        while queue:
            # the first path from the queue
            path = queue.pop(0)

            # the last point from the path
            current_point = path[-1]

            # path found?
            if current_point == end_point:
                return path

            for adjacent_point in self._adjacent_points(current_point):
                if adjacent_point not in visited:
                    visited.add(adjacent_point)
                    # construct a new path and add it to the queue
                    new_path = list(path)
                    new_path.append(adjacent_point)
                    queue.append(new_path)
        # no path found
        return []

    @property
    def max_y(self):
        return len(self._field)
    @property
    def max_x(self):
        return len(self._field[0])

    def is_obstacle(self, point):
        return self._field[point.y][point.x] == 0

    def _adjacent_points(self, point):
        ''' dado um ponto, encontre todos os pontos adjacentes que não são obstaculos
        '''
        adjacent_points = []
        # can take a step into either directions
        for x in range(-1,2):       ## -1 <- x -> +1
            # 0 <= adj_x <= self.max_x - 1
            adj_x = min(max(point.x + x, 0), self.max_x - 1)

            for y in range (-1,2):    ## -1 <- y -> +1
                # 0 <= adj_y <= self.max_y - 1
                adj_y = min(max(point.y + y, 0), self.max_y - 1)

                if adj_x == point.x and adj_y == point.y:
                    continue
                adjacent_point = Point(adj_x, adj_y)
                if self.is_obstacle(adjacent_point):
                    continue
                # all checks passed
                adjacent_points.append(adjacent_point)
        return adjacent_points

    def _check_range(self, point):
        if point.x < 0 or point.x >= self.max_x or point.y < 0 or point.y >= self.max_y:
            raise ValueError("out of defined field range")


##################  Test  ##################
import random
from datetime import datetime
from functools import reduce
def print_field(field, start_point, end_point, path):
    s = set(path)
    def node_repr(point):
        if path and point == start_point:
            return 'S'
        elif path and point == end_point:
            return 'E'
        elif point in s:
            return '*'
        elif field[point.y][point.x] == 0:
            return 'x'
        else:
            return ' '
    visual_field = [[node_repr(Point(x,y)) for x in range(range_X)] for y in range(range_Y)]
    reversed_visual_field = [row for row in reversed(visual_field)]
    print()
    print('\n'.join(str(row) for row in reversed_visual_field))

def print_summary(start_point, end_point, path):
    if path:
        print('\nShortest path from {0} to {1}): \n '.format(start_point, end_point), \
                                                   '->'.join([s.__str__() for s in path]))
    else:
        print('No path from {0} to {1} (distance: -1)'.format(start_point, end_point))

if __name__ == '__main__':
    ### set the field range
    range_X, range_Y = 12, 14
    ### printing a large field could be impractical, set your preferred limits here
    printable_field = True if range_X <= 16  and range_Y <= 16 else False

    # generate a field of given size, with random obstacles
    test_field = [[random.randrange(2) for _ in range(range_X)] for _ in range(range_Y)]
    pathFinder = PathFinder(test_field)

    # find a shortest path in the field, iterate till success
    # record the time for all attempts
    path, passedTimes = [], []
    while not path:
        # generate random start / end points
        start_point, end_point = Point(0,0), Point(0,0)
        while start_point == end_point:
            start_point = Point(random.randrange(range_X),random.randrange(range_Y))
            end_point = Point(random.randrange(range_X),random.randrange(range_Y))
            # if one of the points is an obstacle, reset
            if pathFinder.is_obstacle(start_point) or pathFinder.is_obstacle(end_point):
                start_point, end_point = Point(0,0), Point(0,0)

        # start recording time
        start_time = datetime.now()
        path = pathFinder.shortest_path(start_point, end_point)
        delta = datetime.now() - start_time

        # print the field if appropriate
        if path and printable_field:
            print_field(test_field, start_point, end_point, path)
        elif not passedTimes and printable_field:
            # for unsuccessful attempts, print the initial field just once
            print_field(test_field, start_point, end_point, path)

        passedTimes.append(delta)
        print_summary(start_point, end_point, path)

    # print time reports
    found_time = passedTimes.pop()
    print ('\nFound path with distance {0} in: {1}.{2}sec'.format(\
                                  len(path) - 1, found_time.seconds, found_time.microseconds))
    if passedTimes:
        avg_nf_time = reduce( (lambda x, y: x + y), passedTimes ) / len(passedTimes)
        print ('Avg time for "not found" attempts: {0}.{1}sec\n'.format(\
                                               avg_nf_time.seconds, avg_nf_time.microseconds))