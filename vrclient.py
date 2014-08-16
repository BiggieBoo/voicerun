#!/usr/bin/env python

import android, socket

"""
VoiceRun == VR
"""
class VRclient:
	def __init__(self):
		self.droid = android.Android()
		self.result = ""
		self.sock = 0

	def input_voice(self):
		return self.droid.recognizeSpeech().result

	def connect(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def sendmsg(self, result, host, port):
		self.sock.sendto(result, 0, (host, port))

	def disconnect(self):
		self.sock.close()

	def show_responce(self, responce):
		print responce

if __name__ == "__main__":
	vrc = VRclient()
	vrc.connect()
	vrc.sendmsg(vrc.input_voice(), "192.168.0.102", 5981)
	vrc.disconnect()
