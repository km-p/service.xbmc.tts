# -*- coding: utf-8 -*-

#
# km-p 201508 separate Reader for Homescreen.

from base import DefaultWindowReader
import xbmc
#from libxxx import util

class HomeMenuReader (DefaultWindowReader):
    ID = 'home'

    def getWindowExtraTexts(self):
        ret = []

        if xbmc.Player().isPlaying ():
            ret.append (xbmc.getLocalizedString (31023))

        if xbmc.Player().isPlayingAudio():
            ret.append(xbmc.getInfoLabel ('MusicPlayer.Artist').decode('utf-8'))
            ret.append(xbmc.getInfoLabel ('MusicPlayer.Album').decode('utf-8'))
            #ret.append(xbmc.getInfoLabel ('MusicPlayer.Discnumber').decode('utf-8'))
            ret.append(xbmc.getInfoLabel ('Player.Title').decode('utf-8'))
            #ret.append(xbmc.getLocalizedString ())
            #ret.append(xbmc.getInfoLabel ('Player.Time').decode('utf-8'))
            #ret.append(xbmc.getLocalizedString())
            #ret.append(xbmc.getInfoLabel ('Player.Duration').decode('utf-8'))

        if xbmc.Player().isPlayingVideo ():
            ret.append(xbmc.getInfoLabel ('Player.Title').decode('utf-8'))

        ret.append(xbmc.getLocalizedString (555))
        ret.append(xbmc.getInfoLabel ('System.Time').decode('utf-8'))

        return ret

