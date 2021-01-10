from time import sleep
import signal, sys, time, datetime, picamera
from picamutils.time import Timegiver
from picamutils.aws import S3FileUploader

ts = Timegiver()
filename = 'tmp/snapshot.jpg'
starttime = time.time()

def signal_handler(sig, frame):
	print("\n{ts.generateTimestamp()} ::QUIT:: `CTRL + C` received! Closing application.")
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print(f'{ts.generateTimestamp()} ::START:: Starting image capturing...\n{ts.generateTimestamp()} ::INFO:: Press `CTRL + C` to exit.')

def take_a_shot(rotation=180):
	camera = picamera.PiCamera()
	camera.rotation = rotation
	try:
		camera.start_preview()
		camera.annotate_background = picamera.Color('Black')
		camera.annotate_text_size = 12
		camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		sleep(2)
		camera.capture(filename)
		s3 = S3FileUploader(filename, 'latest.jpg')
		fileupload = s3.upload_file_to_bucket()

	finally:
		camera.close()
		print(f'{ts.generateTimestamp()} ::INFO:: Image {filename} saved.')



if __name__ == '__main__':
	interval = 1800.0 # 30min

	if len(sys.argv) > 1:
		print(f'{ts.generateTimestamp()} ::INFO:: Script started with additional arguments:"{str(sys.argv[1:])}')
		if float(sys.argv[1]) > 1800:
			interval = float(sys.argv[1])
	print(f'{ts.generateTimestamp()} ::INFO:: Image capture interval set to {interval}s.')

	while True:
		take_a_shot(180)
		time.sleep(interval - ((time.time() - starttime) % interval))
