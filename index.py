import subprocess

result = subprocess.run(
    'curl -sSf https://sshx.io/get | sh -s run',
    shell=True,
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.stderr)
