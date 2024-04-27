# Assuming the JSON data is stored in a variable called 'data'
data = {
  "nodes": [
    {
      "id": 1,
      "label": "Investor A",
      "attributes": {
        "type": "Investor"
      }
    },
    {
      "id": 2,
      "label": "Investor B",
      "attributes": {
        "type": "Investor"
      }
    },
    {
      "id": 3,
      "label": "Investor C",
      "attributes": {
        "type": "Investor"
      }
    }
  ],
  "edges": [],
  "directed": False,
  "transform": True,
  "associate": {
    "Project A": ["Investor A", "Investor B", "Investor C"]
  }
}

# Accessing the 'transform' dictionary and iterating over its items
if data.directed:
    for project, investors in data['associate'].items():
        print("Project name:", project)
        print("Investors:", investors)

