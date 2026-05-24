# Before

Original implementation:

```python
def apply_discount(price: float, percent: float) -> float:
    return price - (price * percent)
```

Observed behavior:

```text
apply_discount(100, 20) == -1900
```

Expected behavior:

```text
apply_discount(100, 20) == 80
```

