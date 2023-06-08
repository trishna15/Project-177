from flask import Flask, render_template, jsonify

app = Flask(__name__)

word = [
        {"inputs":5,
        "catagory":"Fruits",
        "word":"Apple"
    },
    {"inputs":6,
        "catagory":"Electronics",
        "word":"Fridge"
    },
    {"inputs":3,
        "catagory":"Colour",
        "word":"Red"
    },
    {"inputs":10,
        "catagory":"Sports",
        "word":"Volleyball"
    },
    {"inputs":6,
        "catagory":"European Country",
        "word":"France"
    }
    ]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/words')
def get_words():
    return jsonify(word)


if __name__ == '__main__':
    app.run()
