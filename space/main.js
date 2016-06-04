
                    function list() {
                        var list = document.getElementById("directory");
                        var directory = ['reas'];
                        var next, link;
                        for (var i=0, len=directory.length; i<len; i++) {
                            next = document.createElement("li");
                            link = document.createElement("a");
                            link.appendChild(document.createTextNode(directory[i]));
                            link.title = ":)";
                            link.href = directory[i];
                            next.appendChild(link);
                            list.appendChild(next);
                        }
                    }
                    