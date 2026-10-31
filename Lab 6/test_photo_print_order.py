
import pytest
from photo_print_order import extra_print_charge, order_valid, dispatch_status


# --------------------------------------------------
# TEST CASES FOR extra_print_charge()
# --------------------------------------------------

def test_within_included_prints():
    assert extra_print_charge("4x6", 15, "matte", False) == 0


def test_member_extra_included_prints():
    assert extra_print_charge("4x6", 25, "matte", True) == 0


def test_member_8x10_no_extra_benefit():
    assert extra_print_charge("8x10", 10, "matte", True) == 0


def test_extra_matte_prints():
    assert extra_print_charge("4x6", 21, "matte", False) == 4


def test_extra_glossy_prints():
    assert extra_print_charge("4x6", 21, "glossy", False) == 7


def test_large_extra_matte_prints():
    assert extra_print_charge("4x6", 71, "matte", False) == 306


def test_large_extra_canvas_prints():
    assert extra_print_charge("4x6", 71, "canvas", False) == 714


def test_large_extra_glossy_prints():
    assert extra_print_charge("4x6", 71, "glossy", False) == 459


def test_unknown_print_size():
    with pytest.raises(ValueError, match="unknown print size"):
        extra_print_charge("A4", 10, "matte", False)


def test_negative_copies():
    with pytest.raises(ValueError, match="invalid copies"):
        extra_print_charge("4x6", -1, "matte", False)


# --------------------------------------------------
# TEST CASES FOR order_valid()
# --------------------------------------------------

def test_rush_order_valid():
    assert order_valid(100, 50, True) is True


def test_rush_order_invalid():
    assert order_valid(10, 51, True) is False


def test_large_file_invalid():
    assert order_valid(26, 100, False) is False


def test_normal_order_valid():
    assert order_valid(20, 500, False) is True


def test_normal_order_too_many_copies():
    assert order_valid(20, 501, False) is False


# --------------------------------------------------
# TEST CASES FOR dispatch_status()
# --------------------------------------------------

@pytest.mark.parametrize(
    "hours, framed, international, expected",
    [
        # Not framed, domestic: cutoff = 12
        (12, False, False, "on_time"),
        (6, False, False, "tight"),
        (5, False, False, "missed"),

        # Framed, domestic: cutoff = 24
        (24, True, False, "on_time"),
        (18, True, False, "tight"),
        (17, True, False, "missed"),

        # Not framed, international: cutoff = 36
        (36, False, True, "on_time"),
        (30, False, True, "tight"),
        (29, False, True, "missed"),

        # Framed, international: cutoff = 48
        (48, True, True, "on_time"),
        (42, True, True, "tight"),
        (41, True, True, "missed"),
    ]
)
def test_dispatch_status(hours, framed, international, expected):
    assert dispatch_status(hours, framed, international) == expected
