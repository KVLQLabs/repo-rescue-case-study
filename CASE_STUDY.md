# Case Study: Discount Calculation Repair

## Problem

The original helper expected a discount percentage but used it directly in the calculation.

```python
return price - (price * percent)
```

For `price=100` and `percent=20`, the result became `-1900` instead of `80`.

## Diagnosis

The public function name and caller behavior used whole-number percentages. The implementation needed to normalize `percent` by dividing by `100` before applying the discount.

## Fix

- Added input validation for negative prices and negative percentages.
- Converted whole-number percentages to a decimal rate before calculating the discount.
- Rounded the result to two decimal places for currency-style output.
- Added tests for normal discounts, zero discounts, and invalid input.

## Verification

Local verification command:

```bash
python -m pytest
```

Result:

```text
3 passed
```

## Notes

This is intentionally small. The point is to show the repair pattern: reproduce the failure, make the smallest safe change, and document exactly what was verified.

