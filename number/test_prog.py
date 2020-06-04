import pytest

import prog


@pytest.mark.parametrize(
    ('x', 'expected'),
    (
        ([3], 3),
        ([8, 2], 2),
        ([6, 15, 9], 3),
        ([17, 13, 7], 1),
    ),
)
def test_gcd_list(x, expected):
    assert prog.gcd_list(x) == expected


@pytest.mark.parametrize(
    ('x', 'expected'),
    (
        ([3], 3),
        ([2, 4], 4),
        ([2, 3, 5], 30),
        ([10, 6, 8], 120),
    ),
)
def test_lcm_list(x, expected):
    assert prog.lcm_list(x) == expected


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
def test_count_factors(x, mod, expected):
    assert prog.count_factors(x, mod) == expected


@pytest.mark.parametrize(
    ('x', 'expected'),
    (
        (1, [1]),
        (3, [1, 3]),
        (6, [1, 2, 3, 6]),
        (16, [1, 2, 4, 8, 16]),
        (25, [1, 5, 25]),
    ),
)
def test_make_divisors(x, expected):
    assert prog.make_divisors(x) == expected
