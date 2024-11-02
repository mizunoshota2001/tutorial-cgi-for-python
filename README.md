# Python CGI チュートリアル サンプル集

## CGI とは

CGI（Common Gateway Interface）は、ウェブサーバーと外部プログラム（スクリプト）との間でデータをやり取りするための標準的なプロトコルです。これにより、ユーザーのリクエストに応じて動的なコンテンツを生成することができます。

## 環境の準備

### 必要なもの

- **ウェブサーバー**: Apache や Nginx など。ここでは Apache を使用する例を示します。
- **Python**: CGI スクリプトを実行するためにインストールされている必要があります。
- **適切な権限**: ウェブサーバーが CGI スクリプトを実行できるように設定します。



3. **CGI ディレクトリの確認**
   - 通常、`/usr/lib/cgi-bin/` や `/var/www/cgi-bin/` が使用されます。`/var/www/html/cgi-bin/` に設定されている場合もあります。

## 簡単な Python CGI スクリプトの作成

以下は、"Hello, World!" を表示する簡単な Python CGI スクリプトの例です。



2. **スクリプトの配置**

   - 作成した `hello.py` を CGI ディレクトリ（例: `/usr/lib/cgi-bin/`）にコピーします。

   ```bash
   sudo cp hello.py /usr/lib/cgi-bin/
   ```

## ウェブサーバーへの配置



2. **ブラウザからアクセス**

   - ウェブブラウザを開き、以下の URL にアクセスします。

   ```
   http://your_server_ip/cgi-bin/hello.py
   ```

   正しく設定されていれば、「Hello, World!」と表示されます。

## パーミッションの設定

CGI スクリプトは実行可能でなければなりません。以下のコマンドで実行権限を設定します。

```bash
sudo chmod 755 /usr/lib/cgi-bin/hello.py
```

- `7` (所有者): 読み取り、書き込み、実行
- `5` (グループ): 読み取り、実行
- `5` (その他): 読み取り、実行





## 追記次項

- シバンについて
- フォームデータの処理について
- クエリの取得
- https://www.tohoho-web.com/wwwcgi3.htm
- パーミッションの設定について
