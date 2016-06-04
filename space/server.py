from http.server import HTTPServer, SimpleHTTPRequestHandler
from html.parser import HTMLParser
import os
import logging

class SpaceHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        directory = [f for f in os.listdir() if f not in ["index.html", "main.js", "server.py"]]
        with open("main.js", "w") as f:
            f.write("""
                    function list() {{
                        var list = document.getElementById("directory");
                        var directory = {directory};
                        var next, link;
                        for (var i=0, len=directory.length; i<len; i++) {{
                            next = document.createElement("li");
                            link = document.createElement("a");
                            link.appendChild(document.createTextNode(directory[i]));
                            link.title = ":)";
                            link.href = directory[i];
                            next.appendChild(link);
                            list.appendChild(next);
                        }}
                    }}
                    """.format(directory=directory))
        super().do_GET()

def run(server_class=HTTPServer, handler_class=SpaceHandler):
    server_address = ("", 80)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
