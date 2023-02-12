from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form

count = 0

@app.route('/')
def index():
    global count
    count += 1
    return render_template("index.html", count = count)


@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    global count
    count = 0 		
    return redirect('/')


@app.route('/add_two', methods=['POST'])
def add_two():
    global count
    count += 1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)

