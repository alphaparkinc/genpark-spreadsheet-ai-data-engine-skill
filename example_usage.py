from client import SpreadsheetAiDataEngineClient

def main():
    client = SpreadsheetAiDataEngineClient()
    data = [
        {"id": 1, "product": "Enterprise Plan", "arr": 12000, "status": "Active"},
        {"id": 2, "product": "Pro Plan", "arr": 2400, "status": "Active"},
        {"id": 3, "product": "Starter Plan", "arr": 600, "status": "Churned"}
    ]
    res = client.query_spreadsheet(data, "Active enterprise plans")
    print(f"Generated Formula: {res['generated_formula']}")
    print(f"Matched Rows ({res['summary_stats']['total_matched']}):")
    for r in res["filtered_rows"]:
        print(f"  {r}")

if __name__ == "__main__":
    main()
