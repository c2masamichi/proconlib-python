import pytest

import prog


@pytest.mark.parametrize(
    ('x', 'expected'),
    (
        (1, False),
        (2, True),
        (4, False),
        (5, True),
        (71, True),
        (91, False),
    ),
)
def test_is_prime(x, expected):
    assert prog.is_prime(x) == expected


@pytest.mark.parametrize(
    ('x', 'mod', 'expected'),
    (
        (3, 3, 1),
        (7, 2, 0),
        (16, 2, 4),
        (48, 2, 4),
    ),
)
def test_make_factors(x, mod, expected):
    assert prog.make_factors(x, mod) == expected


@pytest.mark.parametrize(
    ('x', 'expected'),
    (
        (6, [1, 2, 3, 6]),
    ),
)
def test_make_divisors(x, expected):
    assert prog.make_divisors(x) == expected
