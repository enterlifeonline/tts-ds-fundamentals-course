# This is a small project to create an app alternative to physically waiting in line after covid 19
# Built during the TechTalentSouth Data Science class of Summer 2020 with the help of Gary Jackson
# todo:

# SERVERSIDE:

# 1. firebase streaming/realtime rest api to send json data of who is waiting in which line (NOT POLLING)
# 2. simple first in, first out database interface
# 3. there must be some functionality to accept someone from the line on the owner side, or to remove them if
#       they don't show up

# CLIENTSIDE:

# 4. simple ui with landing screen just as a button to open camera to scan logo and start waiting in line
# 5. swipe left for business owner mode to take picture of logo and start a new virtual line
# 6. waiting in line screen with view of everyone currently waiting in line and an indication of where you are
#
# ideas and other concepts:

# how can we uniquely identify each instance of the app without the end user having to login and make an account
# does the business owner mode need to be able to pick which parties it currently has availability / capacity for
# does the end user need a way to indicate size of party
# estimated wait time

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.network.urlrequest import UrlRequest
import plyer
import json
import requests
import kivy
from kivy.core.window import Window
from functools import partial

from kivy.modules import inspector

kivy.require('2.0.0')  # replace with your current kivy version !
Window.size = (320, 420)


class LandingScreenWrapper(Screen):
    pass


class LandingScreen(Carousel):
    pass


class InLineScreen(GridLayout):
    pass


class MakeLineScreen(GridLayout):
    pass


class ManageLineScreen(Screen):
    pass


class ManageWaitScreen(Screen):
    pass


class ScreenChanger(ScreenManager):
    pass


class root(Screen):
    pass


kv = Builder.load_file("mylinemaker.kv")


class MyLineMaker(App):
    # find unique id for each user using plyer based on device
    # deviceId = plyer.uniqueid.id
    deviceId = "A literal cat"
    # Set the url for the firebase rest api
    url = 'https://linemaker-6e92d.firebaseio.com/.json'
    authKey = 'ZV9AP88xC6JiX2lX2dy5dasQGtPyAVbMMpMU7GER'
    webAPIKey = 'AIzaSyDWAgvkBImYRK1oNTol-eyqz_0VRikYpqU'
    # Database functions (CRUM)

    def patchJoin(self, JSON):
        toDatabase = json.loads(
            '{"' + str(JSON) + '": {"id": "' + str(self.deviceId) + '"}}')
        # new async io
        # self.req = UrlRequest(self.url, req_body=toDatabase, method='PATCH',
        #                       on_success=partial(self.update_label, "Good job"))
        # old blocking io:
        requests.patch(url=self.url, json=toDatabase)

    def patchLeave(self, JSON):
        # How to find which line you are in?
        # requests.delete(url=self.url[:-5] + JSON + ".json")
        UrlRequest(self.url[:-5] + JSON + ".json", method='DELETE')

    def patchCreate(self, JSON):
        toDatabase = json.loads('{"' + JSON + '": {"id": "null"}}')
        # requests.patch(url=self.url, json=toDatabase)
        UrlRequest(self.url, req_body=toDatabase, method='PATCH')

    def patchDestroy(self, JSON):
        # requests.delete(url=self.url[:-5] + JSON + ".json")
        UrlRequest(self.url[:-5] + JSON + ".json", method='DELETE')

    def get(self):
        # request = requests.get(self.url + '?auth=' + self.authKey)
        request = UrlRequest(self.url + '?auth=' + self.authKey, method='GET')
        print(json.loads(request))

    def test(self):
        print("Button worked")

    def update_label(self, label):
        print(label)
        print(self.req)

    # Build the kv file

    def build(self):
        inspector.create_inspector(Window, ScreenChanger)
        return kv


if __name__ == '__main__':
    MyLineMaker().run()
