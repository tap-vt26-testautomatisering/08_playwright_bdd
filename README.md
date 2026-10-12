# Playwright + BDD
E2E-test med Playwright och Behave.

Filen `requirements.txt` innehåller alla paket som ska importeras.

För att köra, skriv `behave` i terminalen i projektets rotmapp.

Rekommenderad mappstruktur

```text
root/ 
├─ src/
| ├─ features/
| | ├─ pages/
| | | └─ base_page.py
| | ├─ steps/
| | | └─ step_add_players.py
| | ├─ add_players.feature
| | └─ environment.py
├─ tests/
| ├─ unit/
| | └─ test_example.py
| └─ integration/
|   └─ test_example.py
├─ .gitignore
├─ behave.ini
├─ README.md
└─ requirements.txt
```
