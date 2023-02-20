from flask import Flask, request, Response #import flask with request and response

app = Flask(__name__) #name flask app

@app.route('/') #route for home page

#get and post help from: https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

def home(): #create home page with a form, post method to submit value
    home = ''' 
    <text style="color:blue;">
    <body style="color:blue;">
    <h1>Home</h1>
    <h2>Enter an integer to see if it is even or odd</h2>
    <form action="calculate" method="POST">
                    <label for="number">Number: </label>
                    <input type="text" id="number" name="number" placeholder="Enter a number:">
                    <button type="submit">Submit</button>
    </form> 
    '''
    return Response(home)

@app.route('/calculate', methods=["POST", "GET"])  #calculate rouse with post for sending values, get for visting page directly

def calculate():
    
    if request.method == "GET":  #get if page is accessed directly, return no number
        return 'No input recieved.<br><a href="/">Back to home</a>'
    elif request.method == "POST": #means user clicked submit, create variable for user input
        num = request.form.get("number") #use get to get number from form
        if not num:
            return 'No input.<br><a href="/">Back to home</a>' #detect if submit was clicked with no input
        elif num.isalpha(): #detect if input was a string
            return f'{num} is not an integer!<br><a href="/">Back to home</a>'
        if int(num) % 2 == 0: #detect if number is even
            return f'{num} is even.<br><a href="/">Back to home</a>'
        else: #if passes all other ifs, must be odd
            return f'{num} is odd.<br><a href="/">Back to home</a>'
   
if __name__ == "__main__": #run app
    app.run()