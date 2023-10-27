from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/dynamic/<content>')
def dynamic(content):
    return render_template('dynamic_page.html', dynamic_content=content)

if __name__ == '__main__':
    app.run(debug=True)
