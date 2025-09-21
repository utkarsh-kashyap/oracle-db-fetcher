from .db_connector import OracleDB
from .utils import load_config, save_to_json

class DBFetcher:
    def __init__(self, config_path="config.json"):
        self.config = load_config(config_path)
        self.queries = self.config.get("queries", {})
        self.output_path = self.config.get("output_path", "output/results.json")
        self.db = OracleDB()

    def run_query(self, query_name=None, params=None, output_override=None):
        query_name = query_name or self.config.get("default_query")
        if query_name not in self.queries:
            raise KeyError(f"Query '{query_name}' not found in config.json")

        sql = self.queries[query_name]
        results = self.db.fetch_query(sql, params)
        out = output_override or self.output_path
        save_to_json(results, out)
        print(f"✅ Query '{query_name}' executed. {len(results)} rows saved to {out}")
        return results
