# 外部アクセスが可能なAPIのヘッダー設定
print("Access-Control-Allow-Headers: Origin, Content-Type")
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS")
print("Content-Type: application/json")
print()

# アクセスのみ許可するオリジンを指定
allowed_origin = "https://example.com"
print("Access-Control-Allow-Headers: Origin, Content-Type, Accept, Authorization")
print("Access-Control-Allow-Origin: %s" % allowed_origin)
print("Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS")
print("Content-Type: application/json\n")
print()
