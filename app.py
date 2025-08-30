
from flask import Flask, render_template, request
import project  # Assuming encryption/decryption functions are in project.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form.get('sample_text', '')
        shift = request.form.get('shift', '3')
        try:
            shift = int(shift)
        except ValueError:
            shift = 3
        action = request.form.get('action', 'encrypt')
        if action == 'encrypt':
            result = project.encrypt(text, shift)
        else:
            result = project.decrypt(text, shift)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
