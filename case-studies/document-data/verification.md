# Parser demonstration verification

Executed on 2026-10-07 with Python 3.14.7 against the public `mbank.py` module from ksiegowy-ai commit `3404f89249b35b1455dea80f0e1d543ba4d7b560` (version 0.4.0).

The synthetic input contains three invented transactions. Assertions checked that the parser returned three operations, sorted them by date, parsed amounts as 1200.5, -100.5 and 300.0, and normalized repeated spaces in the first description. The resulting records are saved in `output.json`.

Ruff and ty passed for the temporary demonstration runner. The source module was not modified. This run does not establish behavior for arbitrary banks, all invalid rows or scanned documents.

Reproduce using that source revision: pass `Path("input.csv")` to `ksiegowy_ai.mbank.parsuj_wyciag`, then serialize each operation's `data`, `opis`, `kwota` and `kategoria_banku`. Only public source and synthetic data were used.
