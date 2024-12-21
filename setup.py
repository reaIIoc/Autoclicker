import subprocess

subprocess.run(["cls"], shell=True)
subprocess.run(["pip", "install", "pywin32"], shell=True, capture_output=True)
subprocess.run(["pip", "install", "pydirectinput"], shell=True, capture_output=True)

print("\nInstallation and setup complete!")

