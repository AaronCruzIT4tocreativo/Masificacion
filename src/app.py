from wsgiref.simple_server import make_server
from sender_instances_controller import SenderInstancesController

def start_server():
    sender_instances_controller = SenderInstancesController()

    with make_server('', 8000, sender_instances_controller.handle_request) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()

if __name__ == '__main__':
    start_server()
