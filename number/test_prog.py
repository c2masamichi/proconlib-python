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
