from time import sleep
from picamera import PiCamera
import signal, sys
from picamutils.time import Timegiver
from picamutils.aws import S3FileUploader

ts = Timegiver()
filename = 'tmp/snapshot.jpg'

def signal_handler(sig, frame):
	print("\n{ts.generateTimestamp()} ::QUIT:: `CTRL + C` received! Closing application.")
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print(f'{ts.generateTimestamp()} ::START:: Starting image capturing...\n{ts.generateTimestamp()} ::INFO:: Press `CTRL + C` to exit.')

def take_a_shot(rotation=90):
	camera = PiCamera()
	camera.rotation = rotation
	try:
		camera.start_preview()
		sleep(2)
		camera.capture(filename)
	finally:
		camera.close()
		print(f'{ts.generateTimestamp()} ::DONE:: Image {filename} saved. \n{ts.generateTimestamp()} ::QUIT:: Exiting application..')

take_a_shot()
