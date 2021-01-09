from time import sleep
from picamera import PiCamera
import signal, sys
from picamutils.time import Timegiver
from picamutils.aws import S3FileUploader

ts = Timegiver()

def signal_handler(sig, frame):
	print("\n{ts.generateTimestamp()} ::QUIT:: `CTRL + C` received! Closing application.")
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print(f'{ts.generateTimestamp()} ::START:: Starting image capturing...\n{ts.generateTimestamp()} ::INFO:: Press `CTRL + C` to exit.')

def timelapse(images=10, time_between_images=3):
	camera = PiCamera()
	camera.start_preview()
	camera.rotation = 90
	# Lets give the camera a 2s wait for it to warmup
	sleep(2)


	for i, filename in enumerate(camera.capture_continuous('tmp/img{counter:03d}.jpg')):
		if i == images:
			print(f'{ts.generateTimestamp()} ::INFO:: Stopping capture after %s images'%i)
			break
		else:
                	print(f'{ts.generateTimestamp()} ::INFO:: Image captured to file: {filename}')
                	sleep(time_between_images)



timelapse(3)

print(f'{ts.generateTimestamp()} ::INFO:: All done, exiting..')
