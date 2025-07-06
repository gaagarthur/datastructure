import json

# Parameters
input_file = 'network/data.json'       # Path to your original file
output_file = 'data.json'  # Path to save the new file
scale_factor = 4              # Factor by which to multiply node sizes

# Load nodes
with open(input_file, 'r', encoding='utf-8') as f:
    nodes = json.load(f)

# Scale sizes
for node in nodes:
    if 'size' in node:
        node['size'] *= scale_factor

# Save updated nodes
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(nodes, f, indent=2)

print(f"Updated nodes saved to '{output_file}' with sizes scaled by {scale_factor}.")

