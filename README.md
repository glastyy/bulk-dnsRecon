### About

The `Bulk DNSrecon Script` is a Python script designed to facilitate DNS reconnaissance on multiple domains using Carlos Perez's `dnsrecon` tool. This script reads domains from a specified input file, runs `dnsrecon` for each domain, and appends the results to a designated JSON output file. This is particularly useful for security analysts and network administrators who need to perform bulk DNS reconnaissance efficiently.

### Features

- **Bulk DNS Scanning**: Automatically processes a list of domains for DNS reconnaissance.
- **JSON Output**: Aggregates the results of DNS scans into a single JSON file.
- **Error Handling**: Provides error messages if `dnsrecon` encounters issues or if files are missing.

### How to Use

1. **Install Dependencies**: Ensure you have Python and `dnsrecon` installed. You can install any required Python packages using pip:
    ```bash
    pip install argparse subprocess os json
    ```

2. **Prepare Input Files**:
    - Create a text file with a list of domains, each on a new line (e.g., `domains.txt`).
    - Ensure you have the path to the `dnsrecon.py` script.

3. **Run the Script**:
    - Open a terminal or command prompt.
    - Navigate to the directory containing the script.
    - Run the script using the following command:
      ```bash
      python bulk_dnsrecon.py -f <domains_file> -j <output_json> --dnsrecon <path_to_dnsrecon>
      ```
      Replace `<domains_file>` with the path to your domains file, `<output_json>` with the desired output JSON file name, and `<path_to_dnsrecon>` with the path to the `dnsrecon.py` script.

### Script Overview

- **run_dnsrecon**: Executes `dnsrecon` for a given domain and appends the results to the specified JSON file.
- **main**: Parses command-line arguments, validates input files, and processes the list of domains.

### Example Usage

```bash
python bulk_dnsrecon.py -f domains.txt -j output.json --dnsrecon /path/to/dnsrecon.py
```

This command will run `dnsrecon` on each domain listed in `domains.txt` and save the aggregated results to `output.json`.

### Notes

- Ensure that the paths to the domains file and `dnsrecon.py` script are correct.
- The script manages the creation and appending of the JSON output file.
- Any errors encountered during the execution of `dnsrecon` are logged to the console for troubleshooting.

### Sample `domains.txt` Format

```
example.com
anotherdomain.com
yetanotherdomain.org
```

### Sample Command

```bash
python bulk_dnsrecon.py -f domains.txt -j results.json --dnsrecon /path/to/dnsrecon/dnsrecon.py
```

This will run `dnsrecon` on each domain listed in `domains.txt` and save the aggregated results to `results.json`.


