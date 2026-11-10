# すぐ使える！かんたん韓国語 音声ページ

松山商工会議所「すぐ使える！かんたん韓国語」シートの音声ページです。
シートの QR コードから開くと、各フレーズの発音を聞くことができます。

| ページ | URL |
|---|---|
| 接客フレーズ 60 | https://csrich010-ux.github.io/matsuyama-korean-phrases/ |
| シチュエーション別 60 | https://csrich010-ux.github.io/matsuyama-korean-phrases/situations/ |
| 両面版（全 120） | https://csrich010-ux.github.io/matsuyama-korean-phrases/all/ |

## 構成

- `phrases.json` … フレーズ（カタカナ・ハングル・日本語）
- `audio/` … 音声ファイル
- `situations/`, `all/` … シチュエーション別・両面版
- `tools/make_qr.py` … QR コード作成

## QR コードの作り方

```
pip install qrcode pillow
python3 tools/make_qr.py https://csrich010-ux.github.io/matsuyama-korean-phrases/
python3 tools/make_qr.py https://csrich010-ux.github.io/matsuyama-korean-phrases/situations/ situations
python3 tools/make_qr.py https://csrich010-ux.github.io/matsuyama-korean-phrases/all/ all
```

## お問い合わせ

松山商工会議所 総合企画部　TEL 089-941-4111
