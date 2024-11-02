#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import json
from os import getenv

# https://www.tohoho-web.com/wwwcgi3.htm
CGI_ENV = [
    'AUTH_TYPE',
    'CONTENT_LENGTH',
    'CONTENT_TYPE',
    'GATEWAY_INTERFACE',
    'HTTP_ACCEPT',
    'HTTP_FORWARDED',
    'HTTP_REFERER',
    'HTTP_USER_AGENT',
    'HTTP_X_FORWARDED_FOR',
    'PATH_INFO',
    'PATH_TRANSLATED',
    'QUERY_STRING',
    'REMOTE_ADDR',
    'REMOTE_HOST',
    'REMOTE_IDENT',
    'REMOTE_USER',
    'REQUEST_METHOD',
    'SCRIPT_NAME',
    'SERVER_NAME',
    'SERVER_PORT',
    'SERVER_PROTOCOL',
    'SERVER_SOFTWARE'
]


def main():
    return {k: getenv(k) for k in CGI_ENV}


if __name__ == "__main__":
    print("Access-Control-Allow-Headers: Origin, Content-Type")
    print("Access-Control-Allow-Origin: *")
    print("Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS")
    print("Content-Type: application/json")
    print()
    print(json.dumps(main()))
