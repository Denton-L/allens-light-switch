#!/usr/bin/env python2

import SimpleHTTPServer
import SocketServer

import motor

PORT = 80

class LightServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    ON_ENDPOINT = '/on'
    OFF_ENDPOINT = '/off'

    def __init__(self, request, client_address, server):
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_POST(self):
        if self.path == LightServerHandler.ON_ENDPOINT:
            motorObject.up()
            self.send_response(200)
        elif self.path == LightServerHandler.OFF_ENDPOINT:
            motorObject.down()
            self.send_response(200)
        else:
            self.send_response(404)

        self.end_headers()

motorObject = motor.Motor()
try:
    server = SocketServer.TCPServer(('0.0.0.0', PORT), LightServerHandler)
    server.serve_forever()
finally:
    motorObject.cleanup()
