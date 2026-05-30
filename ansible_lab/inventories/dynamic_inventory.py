#!/usr/bin/env python3
import json
import sys

def get_inventory():
    return {
        "staging": {
            "hosts": ["dynamic_staging_node"],
            "vars": {
                "ansible_host": "127.0.0.1",
                "ansible_connection": "local"
            }
        },
        "production": {
            "hosts": ["dynamic_prod_node"],
            "vars": {
                "ansible_host": "127.0.0.1",
                "ansible_connection": "local"
            }
        },
        "_meta": {
            "hostvars": {
                "dynamic_staging_node": {},
                "dynamic_prod_node": {}
            }
        }
    }

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--list":
        print(json.dumps(get_inventory(), indent=2))
    else:
        print(json.dumps({}))
