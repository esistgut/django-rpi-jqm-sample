import os
import time

from daemon import runner
import RPIO
from RPIO import PWM

os.environ['DJANGO_SETTINGS_MODULE'] = 'django-rpi-jqm-sample.settings'
from django.core.cache import cache

class RpiDaemon():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        #self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/tty'
        #self.stderr_path = '/dev/null'
        self.pidfile_path = os.path.dirname(os.path.abspath(__file__)) + 'rpi_daemon.pid'
        self.pidfile_timeout = 5

    def run(self):
        servo_control = PWM.Servo()
        RPIO.setup(23, RPIO.OUT)
        RPIO.setup(18, RPIO.OUT)
        cache_cur = {'servo': "", 'led1': "", 'led2': ""}
        cache_tmp = {}
        while True:
            cache_tmp['servo'] = cache.get('servo', "0")
            if cache_cur['servo'] != cache_tmp['servo']:
                servo_control.set_servo(25, int(1200/60*float(cache_tmp['servo']))+900)
                cache_cur['servo'] = cache_tmp['servo']
            cache_tmp['led1'] = cache.get('led1')
            if cache_cur['led1'] != cache_tmp['led1']:
                RPIO.output(23, cache_tmp['led1'])
                cache_cur['led1'] = cache_tmp['led1']
            cache_tmp['led2'] = cache.get('led2')
            if cache_cur['led2'] != cache_tmp['led2']:
                RPIO.output(18, cache_tmp['led2'])
                cache_cur['led2'] = cache_tmp['led2']
            time.sleep(1)



app = RpiDaemon()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
