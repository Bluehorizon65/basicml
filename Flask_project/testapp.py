# this a sample flask program

from flask import Flask,jsonify,request


"""
{
    "name":"Hisham"
}
"""

app=Flask(__name__)

#/home/test
@app.route("/")
def home():
    return "Hello"

# get, post 
@app.route("/about") # this route accepts a get request 
def about():
    return "ur visiting a route"

# how to return a json data

@app.route("/students")
def students():
    
    dict1={
        "name":"test",
        "id":21,
        "rollno":30
    }
    return jsonify(dict1)

# how to take a json input from the post method

@app.route("/inputs",methods=["POST"])
def inputs():
    data=request.get_json()
    
    name=data["name"]
    age=data["age"]
    
    return jsonify({
        "name":name,
        "age":age
    })

@app.route("/students/<name>")
def parameters(name):
    return f"the parameter is {name}"

## url parameters u can mention parameters in the url

app.run(debug=True)



# 72.147.86.20
