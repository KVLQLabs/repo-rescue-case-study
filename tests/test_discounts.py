import pytest

from repo_rescue_demo import apply_discount


def test_applies_whole_number_discount_percent():
    assert apply_discount(100, 20) == 80


def test_allows_zero_discount():
    assert apply_discount(49.99, 0) == 49.99


def test_rejects_negative_values():
    with pytest.raises(ValueError):
        apply_discount(-10, 20)
    with pytest.raises(ValueError):
        apply_discount(10, -5)

