import requests

USERNAME = "aceyatech-ui"

url = f"https://api.github.com/users/{USERNAME}/repos"
repos = requests.get(url).json()

output = "# My Projects\n\n"

for repo in repos:
    if repo.get("fork"):
        continue

    name = repo.get("name", "Unnamed project")
    desc = repo.get("description") or "No description provided"
    link = repo.get("html_url")

    output += f"## {name}\n"
    output += f"{desc}\n\n"
    output += f"[View Project]({link})\n\n"
    output += "---\n\n"

with open("projects.md", "w") as f:
    f.write(output)

print("Portfolio generated successfully")
