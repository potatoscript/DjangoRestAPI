# DjangoRestAPI

**Django REST APIの学習**:
本日は、Djangoを使用してREST APIを作成する方法について学びました。以下は、その詳細な手順と説明です。

---

1. **パッケージのインストール**:
   必要なパッケージをインストールしました。以下のパッケージを`requirements.txt`に保存し、コマンドを実行しました。
   ```plaintext
   django
   djangorestframework
   environs
   ```
   - コマンド:
     ```bash
     pip install -r requirements.txt
     ```
   これにより、必要なパッケージがマシンにインストールされました。

2. **Djangoプロジェクトの作成**:
   Djangoプロジェクトを作成しました。
   - コマンド:
     ```bash
     django-admin startproject pims
     ```

3. **新しいアプリの作成**:
   プロジェクトフォルダーに移動し、新しいアプリを作成しました。
   - コマンド:
     ```bash
     cd pims
     python manage.py startapp api
     ```

4. **設定ファイルの更新**:
   作成したアプリとDjango REST frameworkを`settings.py`の`INSTALLED_APPS`セクションに追加しました。
   ```python
   INSTALLED_APPS = [
       ...,
       'api',
       'rest_framework',
   ]
   ```

5. **モデルの作成**:
   APIが操作するデータモデルを作成しました。DjangoはORM（Object Relational Mapping）を使用しており、これによりPythonオブジェクトをデータベースインスタンスにマッピングできます。これにより、複数の種類のデータベースを使用し、Djangoがデータの作成、更新、取得の低レベルコマンドを処理します。私たちは高レベルのPythonラッパーであるDOMを使用してデータにアクセスし、データを作成することができます。

   - 例として、`PotatoPost`モデルを作成しました。このクラスはDjangoの`models.Model`クラスを継承しており、データベースモデルの基本機能をすべて備えています。
     ```python
     from django.db import models

     class PotatoPost(models.Model):
         title = models.CharField(max_length=100)
         content = models.TextField()
         published_date = models.DateTimeField(auto_now_add=True)

         def __str__(self):
             return self.title
     ```

   - このモデルは、`title`、`content`、および`published_date`のフィールドを持っています。`title`は最大100文字の文字列フィールドであり、`content`はテキストフィールドです。`published_date`はオブジェクトが作成された日時を自動的に設定するDateTimeFieldです。

---

本日の学習を通じて、Djangoを使用してREST APIを構築する基本的な手順と、その背後にあるコンセプトを理解しました。次回は、このモデルを使用して実際のAPIエンドポイントを作成し、データの取得と操作を行う予定です。


- **Serializers.pyの作成**
  - モデルをJSON（JavaScriptオブジェクト表記）互換データに変換します。
  - APIを使用する際には、基本的にJSONデータの送受信を行います。
  - モデルインスタンスをAPIで操作可能な形に変換するためのシリアライザーを作成しました。

```python
from rest_framework import serializers
from .models import PotatoPost

class PotatoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotatoPost
        fields = ["id", "title", "content", "published_date"]
```

- **views.pyの作成**
  - モデルとシリアライザーを利用するビューを作成しました。
  - Django RESTフレームワークは、作成、更新、削除などの操作を行うためのデフォルトのビューを提供します。

```python
from rest_framework import generics
from .models import PotatoPost
from .serializers import PotatoPostSerializer

class PotatoPostListCreate(generics.ListCreateAPIView):
    queryset = PotatoPost.objects.all()
    serializer_class = PotatoPostSerializer
```

- **URLのルーティング**
  - 新しいファイルurls.pyを作成し、ビューをURLに接続します。

```python
from django.urls import path
from . import views

urlpatterns = [
    path("potatoposts/", views.PotatoPostListCreate.as_view(), name="potatopost-view-create")
]
```

- **データベースのマイグレーション**
  - マイグレーションコマンドを実行し、SQLテーブルを自動生成します。

```sh
python manage.py makemigrations
python manage.py migrate
```

- **サーバーの起動**
  - Python APIを起動し、ローカルサーバーで実行します。

```sh
python manage.py runserver
```

- **削除ルートの作成**
  - 削除、更新、取得を行うビュークラスを作成し、URLに追加します。

```python
class PotatoPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = PotatoPost.objects.all()
    serializer_class = PotatoPostSerializer
    lookup_field = "pk"

from django.urls import path
from . import views

urlpatterns = [
    path("potatoposts/", views.PotatoPostListCreate.as_view(), name="potatopost-view-create"),
    path("potatoposts/<int:pk>/", views.PotatoPostRetrieveUpdateDestory.as_view(), name="potatopost-retrieve-update-destroy")
]
```

- **FTPメソッドのオーバーライド**
  - Djangoの汎用ビューを使用して、カスタムな削除メソッドを実装しました。

```python
from rest_framework import generics, status
from rest_framework.response import Response

class PotatoPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = PotatoPost.objects.all()
    serializer_class = PotatoPostSerializer
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        PotatoPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

このようにして、Django RESTフレームワークを使用して、APIの作成、モデルのシリアライズ、ビューの作成、URLのルーティング、データベースのマイグレーション、サーバーの起動、カスタムメソッドのオーバーライドを行いました。
