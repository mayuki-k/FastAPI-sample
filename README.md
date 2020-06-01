#  環境構築

- python-multipartはPOSTのBody送信に必要
- Jinja2はtemplatesの一種

```
pip install FastAPI, uvicorn, python-multipart, Jinja2
```

TODO:requirements.txtとかでやる

# 各ディレクトリの説明

|ディレクトリ名|何するのか？|
| --- | --- |
|basemodel|Request Model|
|http_exception|http例外|
|middleware|各URLの前と後の処理|
|min|最小のFastAPIのsample|
|path_parameter|GETのpath_parameterを使ったsample|
|post_body|BodyをPOST送信|
|query_parameter|クエリパラメータ|