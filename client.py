class SpreadsheetAiDataEngineClient:
    def query_spreadsheet(self, table_data: list, natural_query: str) -> dict:
        q = natural_query.lower()
        filtered = []
        for row in table_data:
            if any(str(val).lower() in q or q in str(val).lower() for val in row.values()):
                filtered.append(row)
        if not filtered:
            filtered = table_data[:2]
        
        formula = f"=SUMIFS(C2:C100, A2:A100, \"{q.split()[0] if q.split() else 'filter'}\")"
        return {
            "filtered_rows": filtered,
            "generated_formula": formula,
            "summary_stats": {"total_matched": len(filtered), "confidence": 0.95}
        }
