from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


def university(environ):
    method = environ["REQUEST_METHOD"]

    if method == "POST":
        # šeit norādam cik baitus gribam izlasīt
        try:
            length = int(environ["CONTENT_LENGTH"])
        except ValueError:
            length = 0

        wsgi_input = environ["wsgi.input"].read(length).decode()
        form_data = parse_qs(wsgi_input)

        maths = int(form_data["maths"][0])
        latvian = int(form_data["latvian"][0])
        foreign = int(form_data["foreign"][0])

        can_apply = "can not apply"
        if maths >= 40 and latvian >= 40 and foreign >= 40:
            can_apply = "can appy"

        response_content = f"{form_data['name'][0]} {can_apply} to university"

        return [response_content.encode()]

    form = """
    <form action="" method="post">
        Full name: <input type="text" name="name"><br>
        Mathematics: <input type="text" name="maths"><br>
        Latvian language: <input type="text" name="latvian"><br>
        Foreign language: <input type="text" name="foreign"><br>
        <input type="submit">
    </form>
    """

    return [form.encode()]


def application(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/html")]

    path = environ["PATH_INFO"]

    if path == "/university":
        response_content = university(environ)
    else:
        response_content = ["OK".encode()]

    start_response(status, headers)
    return response_content


HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}/")
    server.serve_forever()