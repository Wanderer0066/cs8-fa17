#!/usr/bin/python3

# Import the HTTP server module
import http.server
import urllib.parse

GUESTBOOK_FILE_NAME = 'guestbook.txt'

# This multi-line docstring will represent our HTML document that the client
# will receive. We'll include a placeholder in it for the existing guestbook
# entries.
HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="viewport" content="initial-scale=1" />
  <title>Guestbook Example</title>
</head>
<body>
    <h1>Sign Our Guestbook</h1>
    <form method="POST">
        <label>Type your Message</label><br>
        <textarea name="message" rows="10"></textarea><br>
        <button type="submit">Submit</button>
    </form>
    <h2>Existing Entries</h2>
    <p style="border-top: 1px solid black; margin-top: 15px;">

        {}
    </p>
</body>
</html>
'''


class GuestbookRequestHandler(http.server.BaseHTTPRequestHandler):

    def render_page(self):
        """This method will be called by both the GET and POST handlers. It
        reads from the guestbook file and uses the contents to generate
        an HTTP response with the HTML document as the body."""

        # Open the GUESTBOOK_FILE_NAME and call its .readlines() method. This
        # will return a list with all of the file's lines. Then, since HTML
        # does not respect the \n character, we'll join the lines together with
        # <br> which is how HTML adds new lines.
        try:
            f = open(GUESTBOOK_FILE_NAME)
            entries = '<br>'.join(f.readlines())
            f.close()
        except IOError:
            entries = ''

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        # We replace the {} placeholder with entries and encode it to the
        # RequestHandler's output stream
        response = HTML.format(entries)
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        """POST requests are used when the client wants to submit data
        to the server. We want to take the user's message, append it
        to the guestbook file and then return the HTML document with the
        latest entries included."""

        # This line retrieves the contents submitted by the user as a string.
        # POST methods use a special format when submitting data so we'll have
        # to pull out the things we care about.
        post_body = self.rfile.read(int(self.headers.get('Content-Length')))
        # The client sends the data with a certain encoding, so we need
        # to decode it (opposite from when we serve the page)
        post_body = post_body.decode()

        # The message we care about contains extra stuff at the beginning.
        # It also has special encoding that we want to remove, so we'll use
        # the urllib.parse.unquote_plus function for that.
        message = urllib.parse.unquote_plus(post_body.replace('message=', ''))
        try:
            f = open(GUESTBOOK_FILE_NAME, 'a')
            f.write(message + '\n')
            f.close()
        except IOError:
            print('Something happened when writing', message)

        self.render_page()

    def do_GET(self):
        """A GET request should read the contents of the guestbook file,
        and build an HTML document to return to the user."""
        self.render_page()


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
    server = http.server.HTTPServer(('', 8080), GuestbookRequestHandler)
    # This tells our server to start listening for requests until we
    # terminate the program (Ctrl-C)
    server.serve_forever()

main()
