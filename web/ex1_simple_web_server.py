#!/usr/bin/python3

# Import the HTTP server module
import http.server
import random

class SimpleRequestHandler(http.server.BaseHTTPRequestHandler):
    """HTTPServer object's need to know how to respond to requests. We are
    going to write our own RequestHandler class as a subclass of
    http.server.BaseHTTPRequestHandler. A lot of what we need to handle is
    taken care of there and we can focus only on what our server needs to do.
    We don't need to define an __init__ method for this class because our
    super class's implementation is fine. We don't need to override it."""

    def do_GET(self):
        """In order to respond to HTTP GET requests, we need to implement this
        method. This is where we determine how the server will respond to
        the client's request."""

        # This line shows that we're in the request handler. It will be
        # displayed on the console where we started the server, but not to
        # the client that made the request.
        print('A request is being handled')

        # The following three lines tell the client the status of the request
        # (200 is OK), the type of data returned (plain text), and that there
        # are no more headers. The rest of the response is the actual content
        # that the client asked for.
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        # Our superclass has a wfile attribute. You can think of this as a file
        # object with a write() method. This is how we write our request that
        # the client will see. Notice that we call a special string method
        # called .encode(). This is because the client expects the string
        # information to be encoded with a particular format.        
        response = 'Congratulations, you have a basic web server'
        a = random.randint(10, 100)
        b = random.randint(10, 100)
        #response += '. {} + {} = {}'.format(a, b, a + b)
        #self.wfile.write(response.encode('utf-8'))
        response = open('junk_data.txt').read()
        self.wfile.write(response.encode('utf-8'))


def main():
    """In main, we'll create an HTTPServer object and tell it to start
    listening for requests on a specific port. Normally, all web servers
    listen at port 80. There are 65536 port numbers available to listen on
    any machine. Many of the lower numbered ports (< 1024) are assigned for
    specific purposes (21 is FTP, 22 is SSH, 80 is HTTP, 443 is HTTPS)."""

    # This line will create our web server and listen on a non-standard port.
    # The reason for this is that lower-numbered ports often require special
    # priliveges when creating a server. We'll use 8080 which a common
    # technique used for development servers.
    server = http.server.HTTPServer(('', 8080), SimpleRequestHandler)
    # This tells our server to start listening for requests until we
    # terminate the program (Ctrl-C)
    server.serve_forever()

main()
