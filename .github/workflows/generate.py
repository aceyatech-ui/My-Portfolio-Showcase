import yaml  

with open("projects.yml", "r") as f:  
    data = yaml.safe_load(f)  

output = "# My Projects\n\n"  

for project in data["projects"]:  
    output += f"## {project['name']}\n"  
    output += f"{project['description']}\n\n"  
    output += f"[View Project]({project['link']})\n\n"  
    output += "---\n\n"  

with open("projects.md", "w") as f:  
    f.write(output)  

print("Portfolio generated successfully")
