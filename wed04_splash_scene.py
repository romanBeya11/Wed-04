# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# Edited by: Roman Beya
# Edited on: 27-Sep 2017
# Created for: ICS3U
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.

from scene import *
import ui
import time


class SplashScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        # create timer so after 2 secs move to next scene
        self.start_time = time.time()
        
        # add MT blue bg colour
        self.background = SpriteNode(position = self.size / 2,
                                     color = (0.61, 0.78, 0.87),
                                     parent = self,
                                     size = self.size)
        self.school_crest = SpriteNode('./assests/sprites/school_crest.JPG',
                                        parent = self,
                                        position = self.size / 2)                        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        # after 2 secs, move to main menu scene
        if not self.presented_scene and time.time() - self.start_time > 2:
        	self.present_modal_scene(MainMenuScene ())
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
