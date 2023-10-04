from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route("/")
def home():
    name="Huzaifa"
    age=22
    data={"name":name,"age":age}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)