from flask import Flask, jsonify
from flask_cors import CORS

app = Flask( __name__ )
cors = CORS( app, origins = '*' )

@app.route( "/api/users", methods = [ 'GET' ] )
def users():
    # users = {'@markz' : 'Marcos J', '@markz2' : 'Marcos J'}
    users = [ { 'userName': '@dgmnzrd_', 'name': 'ing. caguama indio', 'isFollowing': True }, 
              { 'userName': '@leozglz', 'name': 'leo', 'isFollowing': True },
              { 'userName': '@marcos_jn7', 'name': 'Marcos Jn', 'isFollowing': False },
              { 'userName': '@hershast', 'name': 'Hermi', 'isFollowing': False },
              { 'userName': '@NatanaelHeribe1', 'name': 'Natanael Heriberto Esparza Pineda', 'isFollowing': False },
              { 'userName': '@ValeriaRicoMuoz', 'name': 'Valeria Muñoz', 'isFollowing': False }, 
              { 'userName': '@MazuRodrigo', 'name': 'Bibigo14', 'isFollowing': False } ]
    return jsonify( {"users":  users } )

if __name__ == "__main__":
    app.run( debug = True, port = 8080 )