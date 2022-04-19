import random

"""losowanie"""


def draw_numbers():
    return set(random.sample(range(1, 49), k=6))


def test_draw_numbers():
    draw = draw_numbers()
    assert len(draw) == 6
