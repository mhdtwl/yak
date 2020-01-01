from flask import Flask, request
from api_controller import ApiController

app = Flask(__name__)
my_api = ApiController();

################  2nd Question ################

@app.route('/yak-shop/load', methods = ['POST'])
def reset():
    ## callback
    res = my_api.load(request.data) #res[0] : data , res[1] code
    return ('',  res[1])


################  3rd Question ################

def validateParam(typee, param):
  if typee == 'int' :
    if RepresentsInt(param):
      return [True, int(param)]
    else:
      return [False, ("Not integer param.", 400) ]
  else:
    return [False, ("Unknown type", 400) ]    
  pass

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

@app.route('/yak-shop/stock/<T>', methods = ['GET'])
def view_stock(T):
    """T, representing the elapsed time in days"""
    res = validateParam('int', T)
    if res[0]:
      return my_api.view_get_stock(int(T))  
    else:
      return res[1]  


@app.route('/yak-shop/herd/<T>', methods = ['GET'])
def view_herd(T):
    """T, representing the elapsed time in days"""
    headers={ 'content-type':'text/json'}
    ## callback
    res = validateParam('int', T)
    if res[0]:
      return (my_api.view_get_herd(int(T)) , 200, headers)
    else:
      return res[1]  
 


################  4th Question ################

@app.route('/yak-shop/order/<T>', methods = ['POST'])
def order(T):
    """T is the day the customer orders"""
    ## callback
    res = validateParam('int', T)
    if res[0]:
      headers={ 'content-type':'text/json'}
      response = my_api.get_order(request.data, int(T))  
      return (response[0],  response[1], headers)#res[0] : data , res[1] code
    else:
      return res[1] 


################  Server ################
if __name__ == '__main__':
     app.run(port='5000')