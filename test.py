from flask import Flask, request, jsonify

#object of the flask is created
app=Flask(__name__) 

'''
The line app = Flask(__name__) is a common way to initialize a Flask application, 
a popular Python framework for building web applications.

1. app = Flask(...):
This creates a new instance of the Flask application class and assigns it to the variable app.
 This app object will be used to interact with your web application throughout your code.

2. __name__:
This is a special built-in variable in Python that holds the name of the current module.
 When you run a Python script directly, __name__ will be set to "__main__". 
 However, if you import the script as a module in another script, __name__ will be set to the module's name.
 '''


@app.route('/xyz', methods=['GET' , 'POST'])            # @--> annotation - decorator means anyone who hit this particular annotation will reach at this route (delocation)
                            # route--> is a location where are code is stored... ex @Astro_Rih, @rih__theory
def test():
    if(request.method=='POST'):
        a= request.json['num1']
        b= request.json['num2']
        result=a+b
        return jsonify(str(result))
    
#calling the app
if __name__=='__main__':
    app.run()
test(3,4)


#from @app.route to app.run is a complete server
