from flask import Flask,jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digite = n%10
        sum += digite**order
        n = n//10

    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            "number":copy_n,
            "Armstrong":True,
            "server ip": "122:234:888:54"
        }
    else:
        print(f"{copy_n} is not an armstrong")
        result = {
            "number":copy_n,
            "Armstrong":False,
            "server ip": "122:234:888:54"
        }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)