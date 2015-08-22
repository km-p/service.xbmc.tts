# -*- coding: utf-8 -*-
import xbmc
from base import WindowReaderBase, CURRENT_SKIN
from lib import util

class SelectDialogReader(WindowReaderBase):
    ID = 'selectdialog'

    def getHeading(self):
        if CURRENT_SKIN == 'confluence': return None #Broken for Confluence
        return WindowReaderBase.getHeading(self)

    def getControlText(self,controlID):
        label = xbmc.getInfoLabel('System.CurrentControl').decode('utf-8')
        try:
            util.LOG_DEBUG ('{}.{}: label={}'.format('SelectDialogReader', 'getControlText', label))
        except:
            pass

        try:
            selected = xbmc.getCondVisibility('Container({0}).ListItem.IsSelected'.format(controlID)) and ': {0}'.format(util.T(32200)) or ''
        except:
            selected = ''
            try:
                util.LOG_DEBUG('{}.{}: Error when getting selected value! (ControlID={}, Label={}'.format ('SelectDialogReader', 'getControlText', controlID, label))
            except:
                pass

        try:
            util.LOG_DEBUG ('{}.{}: selected={}'.format('SelectDialogReader', 'getControlText', selected))
        except:
            pass

        text = u'{0}{1}'.format(label,selected)
        try:
            util.LOG_DEBUG ('{}.{}: text={}'.format('SelectDialogReader', 'getControlText', text))
        except:
            pass

        return (text,text)

    def getWindowExtraTexts(self):
        return None