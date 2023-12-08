from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/analyze-pdf')
def analyze_pdf():
    # Azure Cognitive Services APIの設定
    api_key = "5fae53dfa38a430fbd42730d2d34e865"
    endpoint = "https://aiservicesnoby.cognitiveservices.azure.com/vision/v3.2/read/analyze"  # PDF 分析用の完全なエンドポイント
    headers = {'Ocp-Apim-Subscription-Key': api_key, 'Content-Type': 'application/json'}
    params = {'pages': '1'}
    data = {'url': 'https://pdfbox.blob.core.windows.net/nobuko/net.pdf'}

    # APIリクエストの送信
    response = requests.post(endpoint, headers=headers, params=params, json=data)
    response.raise_for_status()
    operation_url = response.headers["Operation-Location"]

    # 分析結果の取得
    while True:
        result_response = requests.get(operation_url, headers=headers)
        result = result_response.json()

        if "analyzeResult" in result:
            break
        elif "status" in result and result["status"] == "failed":
            raise Exception("API処理失敗")
        time.sleep(1)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
