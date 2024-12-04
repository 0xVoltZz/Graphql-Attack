import os
import subprocess
import sys
import argparse

# Function to handle argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description="GraphQL Attack Setup Script")
    parser.add_argument('-u', '--url', type=str, help="URL endpoint for the attack (required)", required=False)
    return parser.parse_args()

# Parsing the command-line arguments
args = parse_arguments()

parent_dir = "GraphqlAttack"
env_name = os.path.join(parent_dir, "vevnQL")

script_path = os.path.join(parent_dir, "main.py")

current_dir = os.getcwd()
if os.path.basename(current_dir) != "GraphqlAttack":
    print("Please run the script inside the GraphqlAttack directory.")
    sys.exit(1)

if not os.path.isdir(parent_dir):
    print(f"The directory {parent_dir} does not exist. It will be created.")
    os.mkdir(parent_dir)

if not os.path.isfile(script_path):
    print(f"The program main.py does not exist inside the {parent_dir} directory.")
    print(f"Please place the main.py program inside the {parent_dir} directory.")
    sys.exit(1)

if not os.path.isdir(env_name):
    print(f"The Python environment does not exist. It will be created inside {parent_dir}.")
    subprocess.run(["python3", "-m", "venv", env_name])
else:
    print(f"The virtual environment {env_name} was found.")

# Activation of the virtual environment
if os.name == "nt":  # Windows
    activate_script = os.path.join(env_name, "Scripts", "activate")
    python_script = os.path.join(env_name, "Scripts", "python")
else:  # Linux/Unix
    activate_script = os.path.join(env_name, "bin", "activate")
    python_script = os.path.join(env_name, "bin", "python3")
if os.path.isfile(activate_script):
    print("Activating the virtual environment...")
    subprocess.run([python_script, "-m", "pip", "install", "--upgrade","pip"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    subprocess.run([python_script, "-m", "pip", "install", "-r","requirements.txt"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    print()
    
    if args.url:
        subprocess.run([python_script, script_path,"-u", args.url])

    else:
        print("No URL provided. Example usage:")
        print("To run the attack, you need to specify the target URL with the -u flag.")
        print("Example URLs:")
        print(f"python attack.py -u http://example.com/graphql")

else:
    print(f"Could not find the activation script at {activate_script}")
    sys.exit(1)
