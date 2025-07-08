import requests, json

def fetch():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        with open("recipes.json", "w", encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    else:
        print("Failed to fetch recipe")

if __name__ == "__main__":
    fetch()