from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/xyz',methods=['POST'])
def test1():
    if(request.method=='POST'):
        a= request.json['num1']
        b= request.json['num2']
        result=a+b
        return jsonify(str(result))
    

@app.route('/abc',methods=['POST'])   
def test2():
    if(request.method=='POST'):
        a= request.json['num1']
        b= request.json['num2']
        result=a+b
        return jsonify(str(result))
    

@app.route('/rishi/ranjan',methods=['POST'])
def test3():
    if(request.method=='POST'):
        a= request.json['rishi']
        b= request.json['ranjan']
        result=a+b
        return jsonify(str(result))

    
#calling the app
if __name__=='__main__':
    app.run()