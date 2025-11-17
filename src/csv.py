import csv
def load_users(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [{"name": r["name"], "age": int(r["age"])} for r in reader]

def filter_adults(users):
    return [u for u in users if u["age"] >= 18]
