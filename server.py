from bottle import Bottle, run, HTTPResponse

HOST = "0.0.0.0"
PORT = 80
BACK_END_SERVER = "tornado"
HTTP_STATUS_OK = 200

proxy_app = Bottle()

@proxy_app.route("/<url:re:.*>", method=['GET', 'POST'], name='proxy_request_handler')
def proxy_request_handler(url):
   print(url)
   return HTTPResponse(status=HTTP_STATUS_OK)

if __name__ == "__main__":
    print("[<>] STARTING")
    run(app=proxy_app, host=HOST, port=int(PORT), server=BACK_END_SERVER)
