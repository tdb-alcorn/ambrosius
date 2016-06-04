from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import sys
import logging

class LoggerWriter:
    def __init__(self, level):
        self.level = level
    def write(self, message):
        if message != "\n":
            self.level("<p>" + message.strip() + "</p>")

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
    logging.basicConfig(level=logging.INFO, filename="server.log.html", filemode="a+",
            format="<p> %(asctime)-15s %(levelname)-8s %(message)s </p>")
    logging.warning("hi ho away we go!")
    sys.stderr = LoggerWriter(logging.info)
    run()
