from flask import Flask, render_template, request
from news_api import get_top_headlines, search_news


app = Flask(__name__)


@app.route('/')
def home():
    articles = get_top_headlines()
    return render_template('index.html', articles=articles)

@app.route('/search')
def search():
    query = request.args.get('q')
    articles = search_news(query)
    return render_template('search.html', articles=articles, query=query)

if __name__ == "__main__":
    app.run(debug=True)
