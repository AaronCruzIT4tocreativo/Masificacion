from dataclasses import dataclass, field
from sender_instances_service import SenderInstancesService
import json

@dataclass
class SenderInstancesController:
    sender_instances_service: SenderInstancesService = field(
     default_factory=SenderInstancesService)

    def handle_request(self, environ, start_response):
        path = environ.get('PATH_INFO', '').lstrip('/')
        method = environ.get('REQUEST_METHOD', 'GET')
        response_body = ''
        status = '200 OK'

        # Manejo de preflight request (CORS)
        if method == 'OPTIONS':
            status = '200 OK'
            response_body = ''
        elif path == 'instances/add' and method == 'GET':
            try:
                # content_length = int(environ.get('CONTENT_LENGTH', 0))
                # body = environ['wsgi.input'].read(content_length)
                # data = json.loads(body)
                # session = int(data.get('session'))
                # contacts = data.get('contacts')
                # message = data.get('message')
                # image = data.get('image')
                self.sender_instances_service.append_instance()

                response_body = 'Session created'
            except ValueError:
                response_body = 'Invalid index.'
                # response_body = self.start_sessions(environ)
        # elif path == 'session/continue':
        #     response_body = self.continue_sessions(environ)
        # elif path == 'session/pause':
        #     response_body = self.pause_sessions(environ)
        # elif path == 'session/stop':
        #     response_body = self.stop_sessions(environ)
        else:
            status = '404 Not Found'
            response_body = 'Not Found'

        headers = [
            ('Content-Type', 'application/json'),
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE'),
            ('Access-Control-Allow-Headers', 'Content-Type'),
        ]
        start_response(status, headers)
        return [json.dumps(response_body).encode('utf-8')]

    # def start_sessions(self, environ):    
    #     try:
    #         content_length = int(environ.get('CONTENT_LENGTH', 0))
    #         body = environ['wsgi.input'].read(content_length)
    #         data = json.loads(body)
    #         session = int(data.get('session'))
    #         contacts = data.get('contacts')
    #         message = data.get('message')
    #         image = data.get('image')
    #         self.sender_instances_service.start_driver(contacts, message, image)            
    #         self.sender_instances_service.trigger_function(session,0)
    #         return 'Session created'
    #     except ValueError:
    #         return 'Invalid index.'

    # def continue_sessions(self, environ):        
    #     query = environ.get('QUERY_STRING', '')
    #     try:
    #         session = int(self.get_query_param(query, 'session'))
    #         self.sender_instances_service.trigger_function(session, 2)
    #         return 'Driver played'
    #     except ValueError:
    #         return 'Invalid index.'

    # def pause_sessions(self, environ):        
    #     query = environ.get('QUERY_STRING', '')
    #     try:
    #         session = int(self.get_query_param(query, 'session'))
    #         # action = self.get_query_param(query, 'action')
    #         self.sender_instances_service.pause_driver(session)
    #         return 'Driver paused'
    #     except ValueError:
    #         return 'Invalid index.'

    # def stop_sessions(self, environ):        
    #     query = environ.get('QUERY_STRING', '')
    #     try:
    #         session = int(self.get_query_param(query, 'session'))
    #         # action = self.get_query_param(query, 'action')
    #         self.sender_instances_service.stop_driver(session)
    #         return 'Driver stoped'
    #     except ValueError:
    #         return 'Invalid index.'

    def get_query_param(self, query, key, default=None):
        params = query.split('&')
        for param in params:
            k, _, v = param.partition('=')
            if k == key:
                return v
        return default
