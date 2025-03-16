from flask import Flask, render_template, request
import dates
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def principal():
    
    if request.method == 'POST':
        randon_numb_list = random.randint(0,3)
        randon_numb_world = random.randint(1,100)
        lista = dates.searchWord(randon_numb_list,randon_numb_world)
        
    return render_template("index.html", lista=lista)


if __name__ == '__main__':
    app.run(debug=True)
