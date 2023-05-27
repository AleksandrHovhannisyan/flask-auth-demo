from app import app

# See devcert.sh
ssl_context = ('certificate.pem', 'privatekey.pem')
app.run(debug=True, ssl_context=ssl_context, host="127.0.0.1", port=5000)
