from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

import cv2

Builder.load_file('VideoApp.kv')

#Video selection pop-up
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MyVideoPlayer(BoxLayout):
    image_texture = ObjectProperty(None)
    image_capture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MyVideoPlayer, self).__init__(**kwargs)
        self.flagPlay = False #Is the video playing?
        self.now_frame = 0 #Variable to check the playback frame of the video for seek bar
        self.image_index = [] #Array to store opencv images for seek bar

    #Pop-up to load video
    def fileSelect(self):
        content = LoadDialog(load = self.load, cancel = self.dismiss_popup)
        self._popup = Popup( title="File Select", content=content, size_hint=(0.9,0.9))
        self._popup.open()

    #Loading video files
    def load (self, path, filename):
        txtFName = self.ids['txtFName']
        txtFName.text = filename[0]
        self.image_capture = cv2.VideoCapture(txtFName.text)
        self.sliderSetting()
        self.dismiss_popup()

    #Close pop-up
    def dismiss_popup(self):
        self._popup.dismiss()

    #Seek bar settings
    def sliderSetting(self):
        count = self.image_capture.get(cv2.CAP_PROP_FRAME_COUNT)
        self.ids["timeSlider"].max = count

        #Load the video once and save all the frames in an array
        while True:
            ret, frame = self.image_capture.read()
            if ret:
                self.image_index.append(frame)

            else:
                self.image_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                break

    #Video playback
    def play(self):
        self.flagPlay = not self.flagPlay
        if self.flagPlay == True:
            self.image_capture.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame)
            Clock.schedule_interval(self.update, 1.0 / self.image_capture.get(cv2.CAP_PROP_FPS))
        else:
            Clock.unschedule(self.update)

    #Video playback clock processing
    def update(self, dt):
        ret, frame = self.image_capture.read()
        #When the next frame can be read
        if ret:
            self.update_image(frame)
            time = self.image_capture.get(cv2.CAP_PROP_POS_FRAMES)
            self.ids["timeSlider"].value = time
            self.now_frame = int(time)

    #Seek bar
    def siderTouchMove(self):
        Clock.schedule_interval(self.sliderUpdate, 0)

    #Screen drawing process when the seek bar is moved
    def sliderUpdate(self, dt):
        #When the seek bar value and the playback frame value are different
        if self.now_frame != int(self.ids["timeSlider"].value):
            frame = self.image_index[self.now_frame-1]
            self.update_image(frame)
            self.now_frame = int(self.ids["timeSlider"].value)

    def update_image(self, frame):
        ##############################
        #Write the image processing source here! !!
        ##############################
        
        #flip upside down
        buf = cv2.flip(frame, 0)
        image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        image_texture.blit_buffer(buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
        video = self.ids['video']
        video.texture = image_texture

class TestVideo(App):

    def build(self):
        return MyVideoPlayer()

TestVideo().run()