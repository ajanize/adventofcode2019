# -*- coding: utf-8 -*-
import aoc_day3 as ad3
    
def test_process_data():
    assert ad3.process_data(['R75,D30,R83,U83,L12,D49,R71,U7,L72']) == [['R75','D30','R83','U83','L12','D49','R71','U7','L72']]

def test_split_instruction():
    assert ad3.split_instruction('R75') == ('R', 75)
    assert type(ad3.split_instruction('R75')) is tuple
  
def test_process_wire_path():
    assert ad3.process_wire_path(['U3','R2','D4','L1']) == {(0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 3): 4, (2, 3): 5, (2, 2): 6, (2, 1): 7, (2, 0): 8, (2, -1): 9, (1, -1): 10}
    assert type(ad3.process_wire_path(['U3','R2','D4','L1'])) is dict
    
def test_find_intersection():
    assert ad3.find_intersection(ad3.process_wire_path(['R8','U5','L5','D3']), ad3.process_wire_path(['U7','R6','D4','L4'])) == {(3, 3), (6, 5)}

def test_manhattan_distance():
    assert ad3.manhattan_distance(3, 3) == 6
    assert ad3.manhattan_distance(6, 5) == 11
    assert type(ad3.manhattan_distance(3, 3)) is int
    assert ad3.manhattan_distance(3, 3) >= 0

def test_combined_step_count():
    assert ad3.combined_step_count((3, 3), ad3.process_wire_path(['R8','U5','L5','D3']), ad3.process_wire_path(['U7','R6','D4','L4'])) == 40
    assert ad3.combined_step_count((6, 5), ad3.process_wire_path(['R8','U5','L5','D3']), ad3.process_wire_path(['U7','R6','D4','L4'])) == 30

def test_solve_part_one():
    assert ad3.solve_part_one(ad3.process_wire_path(['R8','U5','L5','D3']), ad3.process_wire_path(['U7','R6','D4','L4'])) == 6
                              
def test_solve_part_two():
    assert ad3.solve_part_two(ad3.process_wire_path(['R8','U5','L5','D3']), ad3.process_wire_path(['U7','R6','D4','L4'])) == 30