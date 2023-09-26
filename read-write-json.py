import json
import os
os.chdir("C:\\users\\AXTON\\Desktop\\Json-Test")
#C:\Users\AXTON\Desktop\Json-Test



# Define the filename of the JSON file
input_file = "data.json"

# Read the JSON data from the file
with open(input_file, "r") as json_file:
    data = json.load(json_file)

# Iterate through each data object
for item in data:
    # Extract and modify the value (for example, increase the age by 1)
    age = item.get("age")
    age += 1
    item["age"] = age

# Write the updated data back to the same JSON file
with open(input_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Updated data has been written to {input_file}")
