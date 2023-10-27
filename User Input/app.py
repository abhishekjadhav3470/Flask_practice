from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def input_form():
    if request.method == 'POST':
        user_input = request.form['name']
        return render_template('input_form.html', name=user_input, submitted=True)
    return render_template('input_form.html', submitted=False)

if __name__ == '__main__':
    app.run(debug=True)
