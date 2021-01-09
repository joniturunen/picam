import datetime, time

class Timegiver:
	def __init__(self, date_format='%Y.%m.%d %H:%M:%S'):
		self.date_format = date_format

	def generateTimestamp(self):
        	seconds = time.time()
        	ts = datetime.datetime.fromtimestamp(seconds).strftime(self.date_format)
        	return ts

if __name__ == "__main__":
	try:
		ts = Timegiver()
		print(ts.generateTimestamp())
	except:
		print(Exception)
