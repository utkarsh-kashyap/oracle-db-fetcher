# Oracle DB Fetcher Framework

This Python framework connects to Oracle DB, fetches query results, and outputs JSON files.
It supports `.env` for credentials and `config.json` for queries.

## Usage

1. Copy `.env.example` → `.env` and fill in your DB credentials.
2. Update `config.json` with your queries.
3. Run: python main.py --query <query_name> --param limit=2
4. Results saved in `output/results.json`.

## Notes

- Do not commit `.env` or `output/` folder.
- Compatible with Oracle XE, SQL Developer GUI, and Python 3.9+.

