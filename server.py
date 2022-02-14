from http.server import BaseHTTPRequestHandler, HTTPServer
from thread_handler import Thread_Handler
import json

HOST_NAME = "localhost"
SERVER_PORT = 8080

thread_handler = Thread_Handler()


class Server(BaseHTTPRequestHandler):
    """
    This class simulate an http server
    """
    def _set_headers(self):
        """
        This function send a success status code and headers.
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """
        This function generates an HTML document that includes message in the body.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_POST(self):
        """
        This function Trigger a child thread that run for a random amount of time between 10-20 seconds.
        :return: return the id and the allocated time of the created thread as a response.
        """
        self._set_headers()
        thread_id = thread_handler.create_Thread()
        self.wfile.write(self._html(
            "run specific thread:{}".format(json.dumps({thread_id: thread_handler.get_run_time(thread_id)}))))

    def do_GET(self):
        """
        This function Ping the status of the running threads.
        :return: return the threads id and for each his allocated time as a response.
        """
        self._set_headers()
        self.wfile.write(self._html("running threads:{}".format(json.dumps(thread_handler.get_active_threads()))))

    def do_DELETE(self):
        """
        This function kill a specific thread with a provided id.
        :param id: thread identifier
        """
        start_idx = self.path.rfind('/')
        id = self.path[start_idx+1:]
        # self._set_headers()
        # self.wfile.write(self._html("delete thread:{}".format(json.dumps({"id": id}))))
        thread_handler.delete_thread(id)


if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, SERVER_PORT), Server)
    print("Server started http://%s:%s" % (HOST_NAME, SERVER_PORT))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
