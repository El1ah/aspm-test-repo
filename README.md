# ASPM Test Repository

Тестовий репозиторій для перевірки Quality Gate механізму ASPM-системи.

## Структура

- `app.py` — Flask-застосунок з умисно внесеними вразливостями
- `.github/workflows/security.yml` — GitHub Actions workflow

## Вразливості

| Файл | Рядок | Тип | Severity |
|------|-------|-----|----------|
| app.py | 14 | eval(user_input) — CWE-95 | CRITICAL |
| app.py | 20 | debug=True — B201 | HIGH |

## Secrets, які потрібно додати в репо

| Secret | Значення |
|--------|---------|
| `ASPM_URL` | `https://xxxx.ngrok-free.app` (ngrok URL) |
| `ASPM_PROJECT_ID` | ID проекту з ASPM (Settings → Projects) |
