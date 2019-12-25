## Djangoの基本

- MTV（Model – Template – View)モデルに基づいて作られている
    - Model : データベースに格納されているデータ
    - Template ：　テンプレートファイルによって定義されたそれぞれのページデザイン
    - View ：　どのページを表示させるかを決める処理

[チュートリアル]('https://docs.djangoproject.com/ja/3.0/intro/tutorial01/')
- Djangoは１つのアプリケーションをプロジェクトと呼ぶ
- Django標準の開発サーバーは、本番環境では使わないこと  



### プロジェクトを作る  

`$ django-admin startproject mysite . `

コマンドの最後にピリオド` . `を入力することで、現在の作業ディレクトリに Django をインストールすることができる。ディレクトリ構造がシンプルになるというメリットがある。  

### アプリケーションを作る  
先程作った`mysite`ディレクトリに移動して、  

`$ python manage.py startapp polls `  

アプリケーションを manage.py と同じディレクトリで作成することで　mysite のサブモジュールとしてでなく、トップレベルのモジュールとしてインポートする。
ここでは、Djangoチュートリアルのpollsアプリの作成事例

### urls.py　はなにか

- `urls.py` はURLとWEBページを紐付ける機能。プロジェクト全体とアプリケーション毎に`urls.py`がある。
- アプリケーションごとの`urls.py`は自動では作成されないのでアプリケーション作成時に自分で作る必要がある
```python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('myapp.urls', namespace='myapp')),
]
```
`admin` を指定している｀path`ではURLがadminの場合に、管理画面の`admin.site.urls`を返す（ブラウザ表示）設定をしている。
- DjangoにはURLディスパッチャ（URLに応じてどのページを表示させるか決める司令塔的なもの）が標準装備されている
- URLディスパッチャの動きは、URLConf（urls.py)に記載する
- アプリケーションに新しいデザインのページを追加するには、アプリケーションごとの`urls.py`の`urlpatterns`に新しい`path`を追加すること
- `path` には正規表現が使える（[0-9]{3}-[0-9]{3}で郵便番号)
- `path` 関数は `route,view,kwargs,name`の４つの引数を取る。`route,view`は必須


### データベースを作る

`$ python manage.py migrate`

- `mysite/settings.py`にある INSTALLED_APPS はデフォルトでいくつか入っている。よく利用されているものだが、削除（コメントアウトなど）しても良い。これらのアプリケーションでは最低１つのデータベースを利用するので、データベースを作る。

### モデルを作る

- アプリケーションディレクトリの`models.py`が基本ファイル
- 各モデルはPythonのクラスで、`django.db.models.Models`のサブクラスである
- モデルはデータベースに深い繋がりがある
- モデルを使うとデータベースの管理を楽にする
- モデルはサイトを構成するデータソース（主にデータベース）へのアクセスを請け負う
- モデルクラスはクラスである以上、PythonのClassの書き方に準じる
- データベースのテーブル名、カラム名、データ型、その他は、モデルクラスではクラス名、クラス変数、クラス変数に代入するオブジェクト（Fieldクラスのインスタンス）、Fieldクラスのオプションに紐づく

#### モデル作成の手順
1. models.py　を編集
1. ` python manage.py makemigrations` を実行
1. `python manage.py migrate` を実行


### 管理画面を作る

`python manage.py createsuperuser`  

### ビューを作る

- ビューはただの関数である（及びクラス）
- ビューでは、送られてきたリクエストをもとに、どのページを表示させるかを決めている
- ビューに追加した関数（例：index関数）だけでは表示されない。これをurls.pyに紐付けする。

### 疑問
- include()関数を使う意味
プロジェクト全体の`urls.py`はきれいなままにしたい。そのために、アプリケーションからURLをインポートするだけにする。そのためにinclude関数を使う。