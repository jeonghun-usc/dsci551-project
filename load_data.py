import duckdb

print("Loading dataset into DuckDB...")

con = duckdb.connect("music.db")

con.execute("""
    CREATE TABLE IF NOT EXISTS tracks AS
    SELECT * FROM read_csv_auto('dataset.csv')
""")

result = con.execute("SELECT COUNT(*) FROM tracks").fetchone()
print(f"Done. Loaded {result[0]:,} rows into music.db")

con.close()
