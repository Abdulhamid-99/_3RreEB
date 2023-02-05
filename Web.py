from flask import Flask, request, render_template
from main2 import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        sentences = [sentence for sentence in text.split('.') if sentence]
        parsed_sentences = [parse(sentence) for sentence in sentences]
        return render_template('index.html', parsed_sentences=parsed_sentences)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
