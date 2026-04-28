import requests

USERNAME = "aceyatech-ui"

url = f"https://api.github.com/users/{USERNAME}/repos"

headers = {
    "Accept": "application/vnd.github+json"
}

repos = requests.get(url, headers=headers).json()

output = "# My Projects\n\n"

for repo in repos:
    if repo.get("fork"):
        continue

    topics = repo.get("topics", [])

    if "portfolio" not in topics:
        continue

    name = repo.get("name")
    desc = repo.get("description") or "No description"
    link = repo.get("html_url")

    output += f"## {name}\n"
    output += f"{desc}\n\n"
    output += f"[View Project]({link})\n\n"
    output += "---\n\n"

with open("index.md", "w") as f:
    f.write(output)

print("projects deployed, portfolio is alive.")
