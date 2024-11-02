#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import json


def main():
    try:
        body = json.load(sys.stdin)
        return {"success": 1, "message": "something"}
    except Exception as e:
        return {"success": 0, "message": str(e)}


if __name__ == "__main__":
    print("Access-Control-Allow-Headers: Origin, Content-Type")
    print("Access-Control-Allow-Origin: *")
    print("Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS")
    print("Content-Type: application/json")
    print()
    print(json.dumps(main()))
