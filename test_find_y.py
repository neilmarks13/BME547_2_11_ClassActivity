import pytest

@pytest.mark.parametrize("x1,y1,x2,y2,x,y",
[(-1,-1,1,1,0,0),
(0,0,1,1,0.2,0.2),
(-1,2,10,2,3,2),
(5,5,10,0,9,1)])
def test_calculate_y_coordinate(x1,y1,x2,y2,x,y):
    from coordinates import calculate_y_coordinate
    assert y == calculate_y_coordinate((x1,y1),(x2,y2),x)