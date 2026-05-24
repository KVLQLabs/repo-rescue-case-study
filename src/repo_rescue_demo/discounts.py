def apply_discount(price: float, percent: float) -> float:
    """Return price after applying a whole-number percentage discount."""
    if price < 0:
        raise ValueError("price must be non-negative")
    if percent < 0:
        raise ValueError("percent must be non-negative")

    rate = percent / 100
    return round(price - (price * rate), 2)

