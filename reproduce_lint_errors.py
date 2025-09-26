import subprocess

# Run ruff to check for lint errors
result = subprocess.run(['ruff', 'check', '.'], capture_output=True, text=True)

# Print the output
print(result.stdout)
print(result.stderr)