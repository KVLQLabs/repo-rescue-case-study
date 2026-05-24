# Repo Rescue Case Study

A small, focused example of repairing a broken Python utility with tests and CI.

The example starts with a common production-style bug: a price helper accepts percentage discounts, but the original implementation treats a whole-number percentage as a multiplier. A 20% discount accidentally subtracts `20 * price` instead of `0.20 * price`.

## What this demonstrates

- reproduce a failing behavior with a focused test;
- make the smallest useful code change;
- document the diagnosis and verification;
- run the same test command locally and in CI.

## Verification

```bash
python -m pytest
```

Expected result:

```text
3 passed
```

See [CASE_STUDY.md](CASE_STUDY.md) for the repair notes.
