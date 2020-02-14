# -*- coding: utf-8 -*-

def read_file(file):
    """ Open file and read each line """
    try:
        with open(file) as file:
            for each_line in file:
                yield each_line
    except:
        print("File read failed")
        raise


def process_data(line):
    """ Remove new lines at the end and split data by (,)"""
    wire_path_data = []
    for i in line:
        wire_path_data.append(i.strip('\n').split(','))
    return wire_path_data
 
def check_condition(direction, steps):
    """ Validate the direction and step information"""
    assert direction in ['L', 'R', 'U', 'D'], "Direction information has an incorrect alphabet"
    assert steps > 0, "Step value is zero"

def split_instruction(item):
    """ Split the wire path data into direction and steps"""
    try:
        return item[0], int(item[1:])
    except ValueError as e:
        print("Data is not in valid format: ", e)

def process_wire_path(wire_path_data):
    """ Initialize x, y axis, step counter and a travel map
        Create direction maps for (x, y) axis and assign appropriate value, 
        Process each wire path data and update the (x, y) axis with the score.
        Update step counter and distance map for the entire path of a wire.
    """
    x = 0
    y = 0
    step_count = 0
    travel_map = {}
    x_dict = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    y_dict = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
    
    for item in wire_path_data:
        direction, steps = split_instruction(item)
        check_condition(direction, steps)
        for _ in range(steps):
            x += x_dict[direction]
            y += y_dict[direction]
            step_count += 1        
            if (x, y) not in travel_map:
                travel_map[(x, y)] = step_count
        
    return travel_map

     
def find_intersection(wire_one_map, wire_two_map):
    """ Find intersection coordinates of two wire paths using the travel map"""
    return set(wire_one_map.keys()) & set(wire_two_map.keys())
    
def manhattan_distance(x, y):
    """ Calculate Manhattan distance between two points """
    return abs(x) + abs(y)

def combined_step_count(intersection_coords, wire_one_map, wire_two_map):
    """ Calculate the combined steps count at intersection """
    return wire_one_map[intersection_coords] + wire_two_map[intersection_coords]
        
def solve_part_one(wire_one_map, wire_two_map):
    """ The Manhattan distance to the closest intersection """
    return int(min([manhattan_distance(x, y) for (x, y) in find_intersection(wire_one_map, wire_two_map)]))

def solve_part_two(wire_one_map, wire_two_map):
    """ The fewest combined steps to an intersection """
    return min([combined_step_count(intersection_coords, wire_one_map, wire_two_map) for intersection_coords in find_intersection(wire_one_map, wire_two_map)])
    
def main():
    """ Run main """
    file = 'daythree_input.txt'
    wire_path_data = process_data(read_file(file))
    
    wire_one_map = process_wire_path(wire_path_data[0])
    wire_two_map = process_wire_path(wire_path_data[1])

    print("The Manhattan distance to the closest intersection: ", solve_part_one(wire_one_map, wire_two_map))
    print("The fewest combined steps to an intersection: ", solve_part_two(wire_one_map, wire_two_map))

if __name__ == '__main__':
    main()