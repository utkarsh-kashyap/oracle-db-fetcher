import argparse
from src.fetcher import DBFetcher

def parse_params(param_list):
    params = {}
    for p in param_list or []:
        if "=" not in p:
            continue
        k, v = p.split("=", 1)
        if v.isdigit():
            params[k] = int(v)
        else:
            try:
                params[k] = float(v)
            except ValueError:
                params[k] = v
    return params

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Oracle DB queries and save to JSON")
    parser.add_argument("--query", "-q", help="Query name from config.json")
    parser.add_argument("--param", "-p", action="append", help="Params like key=value")
    parser.add_argument("--output", "-o", help="Override output file path")
    args = parser.parse_args()

    fetcher = DBFetcher()
    fetcher.run_query(query_name=args.query, params=parse_params(args.param), output_override=args.output)
