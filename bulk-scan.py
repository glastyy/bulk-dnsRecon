import argparse
import subprocess
import os
import json

def run_dnsrecon(domain, json_file, dnsrecon_path):
    temp_json_file = "temp_output.json"
    command = ['python', dnsrecon_path, '-d', domain, '-j', temp_json_file]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running dnsrecon for domain {domain}: {result.stderr}")
    else:
        print(f"Successfully ran dnsrecon for domain {domain}")
        if os.path.isfile(temp_json_file):
            with open(temp_json_file, 'r') as temp_file:
                temp_data = json.load(temp_file)
            if os.path.isfile(json_file):
                with open(json_file, 'r') as output_file:
                    output_data = json.load(output_file)
                output_data.extend(temp_data)
            else:
                output_data = temp_data

            with open(json_file, 'w') as output_file:
                json.dump(output_data, output_file, indent=4)

            os.remove(temp_json_file)

def main():
    parser = argparse.ArgumentParser(description='Bulk DNSrecon Script')
    parser.add_argument('-f', '--file', required=True, help='File containing list of domains for bulk scanning')
    parser.add_argument('-j', '--json', required=True, help='JSON file to append the output')
    parser.add_argument('--dnsrecon', required=True, help='Path to the dnsrecon.py script')

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"The file {args.file} does not exist.")
        return

    if not os.path.isfile(args.dnsrecon):
        print(f"The dnsrecon.py script at {args.dnsrecon} does not exist.")
        return

    with open(args.file, 'r') as file:
        domains = file.readlines()
        for domain in domains:
            domain = domain.strip()
            if domain:
                run_dnsrecon(domain, args.json, args.dnsrecon)

if __name__ == '__main__':
    main()
