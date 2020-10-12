import subprocess
import sys

class WinService:
    def __init__(self):
        self._service_states = {"RUNNING": 4}

    def get_service_status(self,servicename):
        cmd = r"sc query {}".format(servicename)
        response = subprocess.getoutput(cmd)
        response = response.split()
        return response[8]

    def is_service_running(self, servicename):
        resp = self.get_service_status(servicename)
        if int(resp) == self._service_states["RUNNING"]:
            return True

    def start_service(self,servicename):
        if self.is_service_running(servicename):
            print("The requested service has already been started")
            sys.exit(0)
        response = subprocess.getoutput(r"net start {}".format(servicename))
        return response

    def stop_service(self,servicename):
        if not self.is_service_running(servicename):
            print("The requested service has already been stopped")
            sys.exit(0)
        response = subprocess.getoutput(r"net stop {}".format(servicename))
        return response

if __name__ == "__main__":
    servicename = input("enter a service_name : ")

    s1 = WinService()
    print(s1.get_service_status(servicename))
    print(s1.is_service_running(servicename))
    #print(s1.start_service(servicename))
    #print(s1.stop_service(servicename))

