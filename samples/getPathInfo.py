#!/usr/bin/python3
import json
from os import getenv

def main():
    path_info = getenv('PATH_INFO')
    path_parts = path_info.strip('/').split('/') if path_info else []
    return path_parts

if __name__ == "__main__":
    print("Access-Control-Allow-Headers: Origin, Content-Type")
    print("Access-Control-Allow-Origin: *")
    print("Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS")
    print("Content-Type: application/json")
    print()
    print(json.dumps(main()))
