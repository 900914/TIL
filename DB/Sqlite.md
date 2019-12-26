## PythonでSqliteを使う

やりたいこと：PandasのデータフレームをPickleファイルではなくデータベースに格納したい。  


### SQLAlchemy　を使う場合
Pythonの為のORMライブラリである**SQLAlchemy**を使用する  

- どのデータベースにどうやってアクセスするかの設定はエンジンが担う
- `create_engine`の引数の`echo=True`はSQL文のログ出力
- declarative_baseを使ってテーブル定義、テーブル生成することが便利（もう１つは、MetaDataによるもの）

### sqlite3 を使う場合

- Python から SQLite3を使うには、`sqlite3.connect`でデータベースファイルを指定すると、データベースへの接続（`sqlite3.Connection`オブジェクト)を取得。`execute()`メソッドを呼び出して、SQLコマンドを実行する。指定したデータベースファイルが存在しない場合は、新規に作成される。

```python
import sqlite3
conn = sqlite3.connect('example.sqlite3')
c = conn.cursor()
c.execute('create table persons(id integer, name text, birthday)')
```

閉じる場合は、  
`conn.commit()`  
`conn.close()`   
で閉じる。commitをしないと、sqlite3でデータベースに加えた変更が保存されない。

#### 検索結果を `X`個 だけ取得する
- １つの場合：Cursor.fetchone()  
```python 
cursor.execute('SELECT * FROM sample')
result = curor.fetchone()
```
- すべての場合：Cursor.fetchall()  
```python 
cursor.execute('SELECT * FROM sample')
result = curor.fetchall()
```
- N個の場合：Cursor.fetchall()  
```python 
cursor.execute('SELECT * FROM sample')
result = curor.fetchmanyl(n)
```

