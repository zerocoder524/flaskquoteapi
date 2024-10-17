from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)


def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random", verify=False)
        if response.status_code == 200:
            data = response.json()
            return data['content'], data['author']
        else:
            return "Ошибка при получении цитаты", ""
    except requests.exceptions.RequestException as e:
        return f"Ошибка: {e}", ""


if __name__ == '__main__':
    app.run(debug=True)
