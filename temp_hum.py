from time import sleep
import Adafruit_DHT

pin = 4
dht11 = Adafruit_DHT.DHT11

while True:
	try:
		humidity, temperature = Adafruit_DHT.read_retry(dht11, pin)
		# Print what we got to the REPL
		print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
	except RuntimeError as e:
		#eading doesn't always work! Just print error and we'll try again
		print("Reading from DHT failure: ", e.args)
	
	finally:
		sleep(1)
