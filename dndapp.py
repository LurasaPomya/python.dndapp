from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spelllist')
@app.route('/spelllist/<char_class>')
def spell_list(char_class=None):
    return render_template('spell_list.html', char_class=char_class)


@app.route('/spell/<spell_name>')
def spell_desc(spell_name):
    return render_template('spell_desc.html', spell_name=spell_name)


if __name__ == '__main__':
    app.debug = True
    app.run()
