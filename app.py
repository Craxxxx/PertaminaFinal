# dari folder website import create_app function
from website import create_app 

#create app 
app = create_app() 
# create app

import socket 
hostname = socket.gethostname()
iphost = socket.gethostbyname(hostname)

# print(hostname)

# if file is run
if __name__ == '__main__':
    
    # run this function
    app.run(debug=True, threaded=True ,host=(iphost), port=5001)
    # app.run(threaded=True)
    # everytime you make a change it will re run this file 'debug = true'