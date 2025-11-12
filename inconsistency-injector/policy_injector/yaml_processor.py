import os
import random
from ruamel.yaml import YAML
from .file_handler import backup_file
from .mutation_engine import get_new_authorities

def process_and_inject_drift(filepath, base_path):
    # Loads a YAML file, backs it up, injects a random policy drift and saves the file.
    # Returns a dictionary with change details, or None on failure.

    print(f"\nProcessing file: {filepath}")
    
    # Creating a backup of the current policy.
    backup_file(filepath)

    # Loading the application.yml file to modify.
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    try:
        with open(filepath, 'r') as f:
            data = yaml.load(f)
    except Exception as e:
        print(f"  [!] Error loading YAML, skipping: {e}")
        return None

    # Identifying the existing policies.
    if "security" not in data or "authorization-rules" not in data["security"]:
        print("  [i] 'security.authorization-rules' not found. Skipping.")
        return None
        
    rules = data["security"]["authorization-rules"]
    if not rules:
        print("  [i] No rules found to mutate. Skipping.")
        return None

    # Randomly selecting a policy rule to mutate.
    rule_index = random.randint(0, len(rules) - 1)
    rule_to_mutate = rules[rule_index]
    
    if "authorities" not in rule_to_mutate:
        print(f"  [i] Rule {rule_index} has no 'authorities' key. Skipping.")
        return None

    # Converting the ruamel.yaml list object to a standard list.
    original_authorities = list(rule_to_mutate["authorities"]) 
    
    # Applying mutation.
    new_authorities = get_new_authorities(original_authorities)
    
    # Converting the mutation into ruamel.yaml list type.
    yaml_list = yaml.load(str(new_authorities))
    rule_to_mutate["authorities"] = yaml_list
    
    path_info = rule_to_mutate.get('paths', ['(no path)'])[0]
    print(f"  [+] Injected drift in rule {rule_index} (path: {path_info}...):")
    print(f"      Original: {original_authorities}")
    print(f"      New:      {new_authorities}")
    
    # Creating the change report dictionary.
    change_details = {
        "service_file": os.path.relpath(filepath, base_path),
        "rule_index": rule_index,
        "endpoint_path": path_info,
        "method": rule_to_mutate.get('method', 'ANY'),
        "original_roles": original_authorities,
        "new_roles": new_authorities
    }

    # Saving the modified application.yml file.
    try:
        with open(filepath, 'w') as f:
            yaml.dump(data, f)
        print(f"  [+] Successfully injected drift into: {filepath}")
        return change_details
    except Exception as e:
        print(f"  [!] Error writing modified YAML: {e}")
        return None