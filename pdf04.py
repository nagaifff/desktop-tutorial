from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/analyze-text')
def analyze_text():
    # テキストファイルの URL
    text_file_url = 'https://pdfbox.blob.core.windows.net/nobuko/net.txt'

    # テキストファイルの内容を取得
    response = requests.get(text_file_url)
    if response.status_code != 200:
        raise Exception("テキストファイルの取得に失敗しました")

    text_content = response.text

    # 単純なテキスト分析（例：行数のカウント）
    line_count = len(text_content.splitlines())

    # 結果の JSON 形式での返却
    result = {
        'line_count': line_count,
        'text_content': text_content
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
