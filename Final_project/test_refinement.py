from refinement import set_snake_direction, get_distance
import pytest
import math 

def test_get_distance():

    assert get_distance([60, 0], [60, 0]) == 0
    assert get_distance([1, 0], [1, 3]) == 3
    assert get_distance([40, 0], [50, 0]) == 10
    assert get_distance([0, 10], [50, 20]) == 50.99019513592785

# def test_set_snake_direction():
    

pytest.main(["-v", "--tb=line", "-rN", __file__])
