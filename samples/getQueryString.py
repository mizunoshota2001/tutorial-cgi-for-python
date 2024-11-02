#!/usr/bin/python3
import json
from os import getenv
from urllib.parse import parse_qs


def main():
    return parse_qs(getenv('QUERY_STRING'))


if __name__ == "__main__":
    print("Access-Control-Allow-Headers: Origin, Content-Type")
    print("Access-Control-Allow-Origin: *")
    print("Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS")
    print("Content-Type: application/json")
    print()
    print(json.dumps(main()))
