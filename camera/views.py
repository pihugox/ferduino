from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def abrir(request):
	if request.user.is_authenticated:
		import RPi.GPIO as GPIO
		import time

		gpioCamara = 2;

		GPIO.setmode(GPIO.BCM)

		GPIO.setup(gpioCamara, GPIO.OUT) 
		GPIO.output(gpioCamara, GPIO.HIGH)

		SleepTimeS = 2

		try:
			GPIO.output(2, GPIO.LOW)
			time.sleep(SleepTimeS);
			GPIO.output(2, GPIO.HIGH);
		except KeyboardInterrupt:
			print("Quit")

			# Reset GPIO settings
			GPIO.cleanup()

		return HttpResponse("Ok");
	else:
		return HttpResponse(status=403)