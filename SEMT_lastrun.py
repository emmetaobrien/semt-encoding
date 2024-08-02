#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on March 19, 2023, at 11:18
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2021.1.4')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'SEMT'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'], expInfo['session'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\katie\\OneDrive - McGill University\\dev\\tasks\\SEMT_full_instructions\\Encoding\\SEMT_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib

# Setup the Window
win = visual.Window(
    size=[1600, 900], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "lang"
langClock = core.Clock()
import re, time
from datetime import datetime

# Save starting session time
startingTime = datetime.now().strftime("%H:%M:%S.%f")
startingTime = "\'"+startingTime
print("Starting time: ", startingTime)
#startingTime = datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]
thisExp.addData("SessionTime", startingTime)
thisExp.addData("SessionTime.RTTime", core.Clock().getTime())

# Remove illegal characters in participants' name to avoid errors in filenames
expInfo['participant']= re.sub('[^A-Za-z0-9]+', '', expInfo['participant'])

# No buttons is currently pressed
button_down = False
text_lang = visual.TextStim(win=win, name='text_lang',
    text='Veuillez sélectionner votre langue.\nAppuyez sur 1 pour Français.\n\nPlease select your language.\nPress 2 for English.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
x, y = [None, None]
joystick_lang = type('', (), {})() # Create an object to use as a name space
joystick_lang.device = None
joystick_lang.device_number = 0
joystick_lang.joystickClock = core.Clock()
joystick_lang.xFactor = 1
joystick_lang.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick_lang.device = joystickCache[0]
        if win.units == 'height':
            joystick_lang.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick_lang.yFactor = 0.5
    else:
        joystick_lang.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick_lang.device_number))
except Exception:
    pass
    
if not joystick_lang.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick_lang.status = None
joystick_lang.clock = core.Clock()
joystick_lang.numButtons = joystick_lang.device.getNumButtons()
joystick_lang.getNumButtons = joystick_lang.device.getNumButtons
joystick_lang.getAllButtons = joystick_lang.device.getAllButtons
joystick_lang.getX = lambda: joystick_lang.xFactor * joystick_lang.device.getX()
joystick_lang.getY = lambda: joystick_lang.yFactor * joystick_lang.device.getY()

key_lang = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instr_text_1 = visual.TextStim(win=win, name='instr_text_1',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_text_2 = visual.TextStim(win=win, name='instr_text_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_text_3 = visual.TextStim(win=win, name='instr_text_3',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
instr_text_4 = visual.TextStim(win=win, name='instr_text_4',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
instr_text_5 = visual.TextStim(win=win, name='instr_text_5',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-5.0);
x, y = [None, None]
joystick_instr = type('', (), {})() # Create an object to use as a name space
joystick_instr.device = None
joystick_instr.device_number = 0
joystick_instr.joystickClock = core.Clock()
joystick_instr.xFactor = 1
joystick_instr.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick_instr.device = joystickCache[0]
        if win.units == 'height':
            joystick_instr.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick_instr.yFactor = 0.5
    else:
        joystick_instr.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick_instr.device_number))
except Exception:
    pass
    
if not joystick_instr.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick_instr.status = None
joystick_instr.clock = core.Clock()
joystick_instr.numButtons = joystick_instr.device.getNumButtons()
joystick_instr.getNumButtons = joystick_instr.device.getNumButtons
joystick_instr.getAllButtons = joystick_instr.device.getAllButtons
joystick_instr.getX = lambda: joystick_instr.xFactor * joystick_instr.device.getX()
joystick_instr.getY = lambda: joystick_instr.yFactor * joystick_instr.device.getY()


# Initialize components for Routine "prac"
pracClock = core.Clock()
# Store frame rate of the monitor so we can time our stimuli more precisely
#expInfo['frameRate'] = win.getActualFrameRate()
#frameRate = round(expInfo['frameRate'])
item1_img_pr = visual.ImageStim(
    win=win,
    name='item1_img_pr', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=False, depth=-1.0)
brL_img_pr = visual.ImageStim(
    win=win,
    name='brL_img_pr', 
    image='left_cr.jpg', mask=None,
    ori=0, pos=(-0.6, 0), size=(0.1, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=False, depth=-2.0)
que_text_pr = visual.TextStim(win=win, name='que_text_pr',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
item2_img_pr = visual.ImageStim(
    win=win,
    name='item2_img_pr', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=False, depth=-4.0)
brR_img_pr = visual.ImageStim(
    win=win,
    name='brR_img_pr', 
    image='right_cr.jpg', mask=None,
    ori=0, pos=(0.6, 0), size=(0.1, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=False, depth=-5.0)
response_pr = visual.TextStim(win=win, name='response_pr',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-6.0);
timer_pr = visual.TextStim(win=win, name='timer_pr',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-7.0);
fix_text_pr = visual.TextStim(win=win, name='fix_text_pr',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.11, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
key_prac = keyboard.Keyboard()
x, y = [None, None]
joystick_prac = type('', (), {})() # Create an object to use as a name space
joystick_prac.device = None
joystick_prac.device_number = 0
joystick_prac.joystickClock = core.Clock()
joystick_prac.xFactor = 1
joystick_prac.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick_prac.device = joystickCache[0]
        if win.units == 'height':
            joystick_prac.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick_prac.yFactor = 0.5
    else:
        joystick_prac.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick_prac.device_number))
except Exception:
    pass
    
if not joystick_prac.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick_prac.status = None
joystick_prac.clock = core.Clock()
joystick_prac.numButtons = joystick_prac.device.getNumButtons()
joystick_prac.getNumButtons = joystick_prac.device.getNumButtons
joystick_prac.getAllButtons = joystick_prac.device.getAllButtons
joystick_prac.getX = lambda: joystick_prac.xFactor * joystick_prac.device.getX()
joystick_prac.getY = lambda: joystick_prac.yFactor * joystick_prac.device.getY()


# Initialize components for Routine "transition"
transitionClock = core.Clock()
txt_transi = visual.TextStim(win=win, name='txt_transi',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_transi = keyboard.Keyboard()

# Initialize components for Routine "ready"
readyClock = core.Clock()
txt_rdy = visual.TextStim(win=win, name='txt_rdy',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.1, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_rdy = keyboard.Keyboard()

# Initialize components for Routine "cntdown"
cntdownClock = core.Clock()
timer_ctdown = visual.TextStim(win=win, name='timer_ctdown',
    text='',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
item1_img = visual.ImageStim(
    win=win,
    name='item1_img', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=False, depth=-1.0)
brL_img = visual.ImageStim(
    win=win,
    name='brL_img', 
    image='left_cr.jpg', mask=None,
    ori=0, pos=(-0.6, 0), size=(0.1, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=False, depth=-2.0)
que_text = visual.TextStim(win=win, name='que_text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
item2_img = visual.ImageStim(
    win=win,
    name='item2_img', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=False, depth=-4.0)
brR_img = visual.ImageStim(
    win=win,
    name='brR_img', 
    image='right_cr.jpg', mask=None,
    ori=0, pos=(0.6, 0), size=(0.1, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=False, depth=-5.0)
response = visual.TextStim(win=win, name='response',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-6.0);
timer = visual.TextStim(win=win, name='timer',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-7.0);
fix_text = visual.TextStim(win=win, name='fix_text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.11, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
key = keyboard.Keyboard()
x, y = [None, None]
joystick = type('', (), {})() # Create an object to use as a name space
joystick.device = None
joystick.device_number = 0
joystick.joystickClock = core.Clock()
joystick.xFactor = 1
joystick.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick.device = joystickCache[0]
        if win.units == 'height':
            joystick.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick.yFactor = 0.5
    else:
        joystick.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick.device_number))
except Exception:
    pass
    
if not joystick.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick.status = None
joystick.clock = core.Clock()
joystick.numButtons = joystick.device.getNumButtons()
joystick.getNumButtons = joystick.device.getNumButtons
joystick.getAllButtons = joystick.device.getAllButtons
joystick.getX = lambda: joystick.xFactor * joystick.device.getX()
joystick.getY = lambda: joystick.yFactor * joystick.device.getY()


# Initialize components for Routine "rest"
restClock = core.Clock()
txt_rest = visual.TextStim(win=win, name='txt_rest',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_rest = keyboard.Keyboard()

# Initialize components for Routine "ready_2"
ready_2Clock = core.Clock()
txt_rdy2 = visual.TextStim(win=win, name='txt_rdy2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_rdy2 = keyboard.Keyboard()

# Initialize components for Routine "cntdown_2"
cntdown_2Clock = core.Clock()
timer_ctdown2 = visual.TextStim(win=win, name='timer_ctdown2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
txt_thx = visual.TextStim(win=win, name='txt_thx',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.1, ori=0, 
    color=[-1,-1,-1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "lang"-------
continueRoutine = True
# update component parameters for each repeat

# Joystick's button is not pressed by default
button_down = False
joystick_lang.oldButtonState = joystick_lang.device.getAllButtons()[:]
joystick_lang.activeButtons=[0, 1]
# setup some python lists for storing info about the joystick_lang
gotValidClick = False  # until a click is received
key_lang.keys = []
key_lang.rt = []
_key_lang_allKeys = []
# keep track of which components have finished
langComponents = [text_lang, joystick_lang, key_lang]
for thisComponent in langComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
langClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "lang"-------
while continueRoutine:
    # get current time
    t = langClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=langClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    #Perform actions depending to the pressed button/key
    #Set french or english variable to true when the language is selected
    
    if joystick_lang.getAllButtons()[1] or "1" in key_lang.keys:
            french = True
            english = False
            pracConditions = "SEMT_conditions_prac.csv"
            trialConditions = "SEMT_conditions_trials_bloc1.csv"
            text_lang.finished = True
            continueRoutine = False
    elif joystick_lang.getAllButtons()[2] or "2" in key_lang.keys:
            french = False
            english = True
            pracConditions = "SEMT_conditions_prac.csv"
            trialConditions = "SEMT_conditions_trials_bloc1.csv"
            text_lang.finished = True
            continueRoutine = False
    
    # *text_lang* updates
    if text_lang.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_lang.frameNStart = frameN  # exact frame index
        text_lang.tStart = t  # local t and not account for scr refresh
        text_lang.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_lang, 'tStartRefresh')  # time at next scr refresh
        text_lang.setAutoDraw(True)
    
    # *key_lang* updates
    waitOnFlip = False
    if key_lang.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_lang.frameNStart = frameN  # exact frame index
        key_lang.tStart = t  # local t and not account for scr refresh
        key_lang.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_lang, 'tStartRefresh')  # time at next scr refresh
        key_lang.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_lang.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_lang.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_lang.status == STARTED and not waitOnFlip:
        theseKeys = key_lang.getKeys(keyList=['1', '2', 'esc'], waitRelease=False)
        _key_lang_allKeys.extend(theseKeys)
        if len(_key_lang_allKeys):
            key_lang.keys = _key_lang_allKeys[-1].name  # just the last key pressed
            key_lang.rt = _key_lang_allKeys[-1].rt
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in langComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "lang"-------
for thisComponent in langComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
lang = 'en' if english==True else 'fr'
thisExp.addData('language', lang)
button_down = True
thisExp.addData('text_lang.started', text_lang.tStartRefresh)
thisExp.addData('text_lang.stopped', text_lang.tStopRefresh)
# store data for thisExp (ExperimentHandler)
# store data for thisExp (ExperimentHandler)
x, y = joystick_lang.getX(), joystick_lang.getY()
joystick_lang.newButtonState = joystick_lang.getAllButtons()[:]
joystick_lang.pressedState = [joystick_lang.newButtonState[i] for i in range(joystick_lang.numButtons)]
joystick_lang.time = joystick_lang.joystickClock.getTime()
thisExp.addData('joystick_lang.x', x)
thisExp.addData('joystick_lang.y', y)
[thisExp.addData('joystick_lang.button_{0}'.format(i), int(joystick_lang.pressedState[i])) for i in joystick_lang.activeButtons]
thisExp.addData('joystick_lang.time', joystick_lang.time)
thisExp.addData('joystick_lang.started', joystick_lang.tStart)
thisExp.addData('joystick_lang.stopped', joystick_lang.tStop)
thisExp.nextEntry()
# check responses
if key_lang.keys in ['', [], None]:  # No response was made
    key_lang.keys = None
thisExp.addData('key_lang.keys',key_lang.keys)
if key_lang.keys != None:  # we had a response
    thisExp.addData('key_lang.rt', key_lang.rt)
thisExp.nextEntry()
# the Routine "lang" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat

# Find a font that is available on the system.
#fm = visual.textbox2.getFontManager()
#available_font_names=fm.getFontFamilyStyles()
#print(available_font_names)

#Change displayed text based on the language previously chosen
if english == True:
    instr_text_1.text = "Welcome to the experiment!\n\nYour task will be to memorize different pairs of pictures representing objects you encounter in your daily life.\n\nThe first object of each pair will be presented with an open bracket on the left, while the second object will be presented with an open bracket on the right.\n\nIMPORTANT: YOU HAVE TO MEMORIZE BOTH OBJECTS TOGETHER!\n\nPress 1 or 2 to continue."
    instr_text_2.text = "Between the presentation of the paired objects, a question will appear.\n\nIf question is 'Bigger?' :\n\nPress '1' if the first object in the pair is bigger than the second object in the pair in real life.\n\nPress '2' if the second object in the pair is the bigger one.\n\nPress 1 or 2 to continue."
    instr_text_3.text = "If the question is 'Same category?' :\n\nPress '1' if both objects are from the same semantic category (ex: both objects are clothes, or both objects are food...)\n\nPress '2' if they are from different categories (ex: one clothing and one food item).\n\nPress 1 or 2 to continue."
    instr_text_4.text = "Please answer when the second object appears.\n\nBetween each pair of objects, there will be a fixation cross (+). You should look at this cross while there are no images on the screen.\n\nPress 1 or 2 to continue."
    instr_text_5.text = "Let's practice a bit before we begin.\n\nAre you ready?\n\nPress 1 or 2 to start the practice."
else:
    instr_text_1.text = "Bienvenue à l'expérience !\n\nVous devrez mémoriser des paires d'images représentant des objets de la vie quotidienne.\n\nLe premier objet de chaque paire sera présenté avec un crochet à sa gauche et le second objet sera présenté avec un crochet à sa droite.\n\nIMPORTANT: VOUS DEVEZ MÉMORISER LES DEUX OBJETS DE LA PAIRE ENSEMBLE!!\n\nAppuyez sur 1 ou 2 pour continuer."
    instr_text_2.text = "Entre les deux présentations d'objets, une question apparaîtra à l'écran.\n\nSi la question est 'Plus gros?' :\n\nAppuyez sur '1' si dans la vie de tous les jours le premier objet de la paire est plus gros que le deuxième objet.\n\nAppuyez sur '2' si le deuxième objet de la paire est le plus gros.\n\nAppuyez sur 1 ou 2 pour continuer."
    instr_text_3.text = "Si la question est 'Catégorie?' :\n\nAppuyez sur '1' si les deux objets font partie de la même catégorie sémantique (ex: les deux objets sont des vêtements, ou les deux sont de la nourriture...).\n\nAppuyez sur '2' s'ils font partie de deux différentes catégories (ex: un morceau de vêtement et une image de nourriture).\n\nAppuyez sur le bouton 1 ou 2 pour continuer." 
    instr_text_4.text = "Vous devez répondre quand le DEUXIÈME OBJET apparaît.\n\nEntre chaque paire d'objets, il y aura une croix de fixation (+). Vous devez regarder cette croix lorsqu'il n'y a pas d'image à l'écran.\n\nAppuyez sur le bouton 1 ou 2 pour continuer."
    instr_text_5.text = "Commençons la pratique avec quelques essais.\n\nÊtes-vous prêt ?\n\nAppuyez sur 1 ou 2 pour commencer la pratique."

#Display 4 instructions
curIns = 1

# The button was previously pressed
button_down = True
joystick_instr.oldButtonState = joystick_instr.device.getAllButtons()[:]
joystick_instr.activeButtons=[1, 2]
# setup some python lists for storing info about the joystick_instr
gotValidClick = False  # until a click is received
# keep track of which components have finished
instrComponents = [instr_text_1, instr_text_2, instr_text_3, instr_text_4, instr_text_5, joystick_instr]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Check if we pressed keyboard keys
    keys = event.getKeys()
    #print(keys)
    
    # Reset buttons if they are not pressed
    if button_down  and not joystick_instr.getAllButtons()[1] and not joystick_instr.getAllButtons()[2] and not '1' in keys and not '2' in keys:
       button_down = False
    
    # Go to next instruction if '1' or '2' is pressed
    if not button_down and curIns >= 1 and curIns <= 4 and (joystick_instr.getAllButtons()[1] or joystick_instr.getAllButtons()[2] or '1' in keys or '2' in keys):
        button_down = True
        curIns = curIns + 1
    
    # Go to next routine
    elif not button_down and curIns == 5 and (joystick_instr.getAllButtons()[1] or joystick_instr.getAllButtons()[2] or '1' in keys or '2' in keys):
        button_down = True
        continueRoutine = False
    
    print("current instruction: ", curIns)
    
    # *instr_text_1* updates
    if instr_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_text_1.frameNStart = frameN  # exact frame index
        instr_text_1.tStart = t  # local t and not account for scr refresh
        instr_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text_1, 'tStartRefresh')  # time at next scr refresh
        instr_text_1.setAutoDraw(True)
    if instr_text_1.status == STARTED:
        if bool(curIns == 2):
            # keep track of stop time/frame for later
            instr_text_1.tStop = t  # not accounting for scr refresh
            instr_text_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_text_1, 'tStopRefresh')  # time at next scr refresh
            instr_text_1.setAutoDraw(False)
    
    # *instr_text_2* updates
    if instr_text_2.status == NOT_STARTED and curIns == 2:
        # keep track of start time/frame for later
        instr_text_2.frameNStart = frameN  # exact frame index
        instr_text_2.tStart = t  # local t and not account for scr refresh
        instr_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text_2, 'tStartRefresh')  # time at next scr refresh
        instr_text_2.setAutoDraw(True)
    if instr_text_2.status == STARTED:
        if bool(curIns == 3):
            # keep track of stop time/frame for later
            instr_text_2.tStop = t  # not accounting for scr refresh
            instr_text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_text_2, 'tStopRefresh')  # time at next scr refresh
            instr_text_2.setAutoDraw(False)
    
    # *instr_text_3* updates
    if instr_text_3.status == NOT_STARTED and curIns == 3:
        # keep track of start time/frame for later
        instr_text_3.frameNStart = frameN  # exact frame index
        instr_text_3.tStart = t  # local t and not account for scr refresh
        instr_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text_3, 'tStartRefresh')  # time at next scr refresh
        instr_text_3.setAutoDraw(True)
    if instr_text_3.status == STARTED:
        if bool(curIns == 4):
            # keep track of stop time/frame for later
            instr_text_3.tStop = t  # not accounting for scr refresh
            instr_text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_text_3, 'tStopRefresh')  # time at next scr refresh
            instr_text_3.setAutoDraw(False)
    
    # *instr_text_4* updates
    if instr_text_4.status == NOT_STARTED and curIns == 4:
        # keep track of start time/frame for later
        instr_text_4.frameNStart = frameN  # exact frame index
        instr_text_4.tStart = t  # local t and not account for scr refresh
        instr_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text_4, 'tStartRefresh')  # time at next scr refresh
        instr_text_4.setAutoDraw(True)
    if instr_text_4.status == STARTED:
        if bool(curIns == 5):
            # keep track of stop time/frame for later
            instr_text_4.tStop = t  # not accounting for scr refresh
            instr_text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_text_4, 'tStopRefresh')  # time at next scr refresh
            instr_text_4.setAutoDraw(False)
    
    # *instr_text_5* updates
    if instr_text_5.status == NOT_STARTED and curIns == 5:
        # keep track of start time/frame for later
        instr_text_5.frameNStart = frameN  # exact frame index
        instr_text_5.tStart = t  # local t and not account for scr refresh
        instr_text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text_5, 'tStartRefresh')  # time at next scr refresh
        instr_text_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr_text_1.setOpacity(0)
instr_text_2.setOpacity(0)
instr_text_3.setOpacity(0)
instr_text_4.setOpacity(0)
instr_text_5.setOpacity(0)
thisExp.addData('instr_text_1.started', instr_text_1.tStartRefresh)
thisExp.addData('instr_text_1.stopped', instr_text_1.tStopRefresh)
thisExp.addData('instr_text_2.started', instr_text_2.tStartRefresh)
thisExp.addData('instr_text_2.stopped', instr_text_2.tStopRefresh)
thisExp.addData('instr_text_3.started', instr_text_3.tStartRefresh)
thisExp.addData('instr_text_3.stopped', instr_text_3.tStopRefresh)
thisExp.addData('instr_text_4.started', instr_text_4.tStartRefresh)
thisExp.addData('instr_text_4.stopped', instr_text_4.tStopRefresh)
thisExp.addData('instr_text_5.started', instr_text_5.tStartRefresh)
thisExp.addData('instr_text_5.stopped', instr_text_5.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('joystick_instr.started', joystick_instr.tStart)
thisExp.addData('joystick_instr.stopped', joystick_instr.tStop)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_repeat = data.TrialHandler(nReps=100, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='prac_repeat')
thisExp.addLoop(prac_repeat)  # add the loop to the experiment
thisPrac_repeat = prac_repeat.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_repeat.rgb)
if thisPrac_repeat != None:
    for paramName in thisPrac_repeat:
        exec('{} = thisPrac_repeat[paramName]'.format(paramName))

for thisPrac_repeat in prac_repeat:
    currentLoop = prac_repeat
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_repeat.rgb)
    if thisPrac_repeat != None:
        for paramName in thisPrac_repeat:
            exec('{} = thisPrac_repeat[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    practice = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(pracConditions),
        seed=None, name='practice')
    thisExp.addLoop(practice)  # add the loop to the experiment
    thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    for thisPractice in practice:
        currentLoop = practice
        # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
        if thisPractice != None:
            for paramName in thisPractice:
                exec('{} = thisPractice[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "prac"-------
        continueRoutine = True
        # update component parameters for each repeat
        # Change displayed text based on the language previously chosen
        if english == True:
            que_text_pr.text = question_english
        else:
            que_text_pr.text = question_french
            
        # Save the answer of the participant
        # The response period started when image 2 started. No need to save it.
        response_time_pr = -1. # Save when the participant answered (in secs)
        
        # set the images by parameters of condition file
        img1 = pic1
        img2 = pic2
        
        # Set the duration of the fixation cross and the question
        timeQue = duration_question/1000 #duration of the question
        timeFix = duration_fixation/1000 #duration of the fixation cross
        
        # Duration of the items, question and fixation cross with frames
        # The number of frames we want to display is equal to
        # the product of frame-rate and the number of seconds to display
        # the stimulus.
        # n_frames = frame_rate * n_seconds
        # n_frames_img1 = frameRate * 2.
        # n_frames_img2 = frameRate * 2.
        # debug.text = "duration of img 1 in frames: "+str(n_frames_img1)
        
        n_secs_img1 = 2.
        n_secs_img2 = 2.
        
        #By default the elements did not start so they are not finished
        item1_finished = False
        que_finished = False
        item2_finished = False
        
        # Record if the participant answered
        participant_answered = False
        
        # When true, we reached the end of img2 without any answer
        no_answers = False
        
        # Reset the response of the participant
        response_pr.text = ""
        item1_img_pr.setImage(img1)
        item2_img_pr.setImage(img2)
        key_prac.keys = []
        key_prac.rt = []
        _key_prac_allKeys = []
        joystick_prac.oldButtonState = joystick_prac.device.getAllButtons()[:]
        joystick_prac.activeButtons=[1, 2]
        # setup some python lists for storing info about the joystick_prac
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        pracComponents = [item1_img_pr, brL_img_pr, que_text_pr, item2_img_pr, brR_img_pr, response_pr, timer_pr, fix_text_pr, key_prac, joystick_prac]
        for thisComponent in pracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prac"-------
        while continueRoutine:
            # get current time
            t = pracClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=pracClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #Set the boolean to true when item1 is done
            if item1_img_pr.status == FINISHED:
                item1_finished = True
            
            # Set the boolean to true when the question is done
            if que_text_pr.status == FINISHED and not que_finished:
                que_finished = True
                
            # Register participant's answers
            # Button 1 is pressed
            if not participant_answered and que_finished and (joystick_prac.getAllButtons()[1] or "1" in key_prac.keys):
                response_pr.text = 1
                participant_answered = True
                #win.color = 'grey'
                print("participant chose: ", response_pr.text)
            
            # Register participant's answers
            # Button 2 is pressed
            elif not participant_answered and que_finished and (joystick_prac.getAllButtons()[2] or "2" in key_prac.keys):
                response_pr.text = 2
                participant_answered = True
                print("participant chose: ", response_pr.text)
            
            # Register participant's answers
            #4s countdown are done
            elif not no_answers and not participant_answered and timer_pr.status == FINISHED:
                response_pr.finished = True
                no_answers = True
                print("participant did not answer: ", response_pr.text)
            
            #Set the boolean to true when the item2 is done
            if item2_img_pr.status == FINISHED:
                item2_finished = True
            
            #Go to next routine when fixation cross is done
            if fix_text_pr.status == FINISHED:
                continueRoutine = False
            
            # *item1_img_pr* updates
            if item1_img_pr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item1_img_pr.frameNStart = frameN  # exact frame index
                item1_img_pr.tStart = t  # local t and not account for scr refresh
                item1_img_pr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item1_img_pr, 'tStartRefresh')  # time at next scr refresh
                item1_img_pr.setAutoDraw(True)
            if item1_img_pr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item1_img_pr.tStartRefresh + n_secs_img1-frameTolerance:
                    # keep track of stop time/frame for later
                    item1_img_pr.tStop = t  # not accounting for scr refresh
                    item1_img_pr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(item1_img_pr, 'tStopRefresh')  # time at next scr refresh
                    item1_img_pr.setAutoDraw(False)
            
            # *brL_img_pr* updates
            if brL_img_pr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                brL_img_pr.frameNStart = frameN  # exact frame index
                brL_img_pr.tStart = t  # local t and not account for scr refresh
                brL_img_pr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(brL_img_pr, 'tStartRefresh')  # time at next scr refresh
                brL_img_pr.setAutoDraw(True)
            if brL_img_pr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > brL_img_pr.tStartRefresh + n_secs_img1-frameTolerance:
                    # keep track of stop time/frame for later
                    brL_img_pr.tStop = t  # not accounting for scr refresh
                    brL_img_pr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(brL_img_pr, 'tStopRefresh')  # time at next scr refresh
                    brL_img_pr.setAutoDraw(False)
            
            # *que_text_pr* updates
            if que_text_pr.status == NOT_STARTED and item1_finished == True:
                # keep track of start time/frame for later
                que_text_pr.frameNStart = frameN  # exact frame index
                que_text_pr.tStart = t  # local t and not account for scr refresh
                que_text_pr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(que_text_pr, 'tStartRefresh')  # time at next scr refresh
                que_text_pr.setAutoDraw(True)
            if que_text_pr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > que_text_pr.tStartRefresh + timeQue-frameTolerance:
                    # keep track of stop time/frame for later
                    que_text_pr.tStop = t  # not accounting for scr refresh
                    que_text_pr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(que_text_pr, 'tStopRefresh')  # time at next scr refresh
                    que_text_pr.setAutoDraw(False)
            
            # *item2_img_pr* updates
            if item2_img_pr.status == NOT_STARTED and que_finished == True:
                # keep track of start time/frame for later
                item2_img_pr.frameNStart = frameN  # exact frame index
                item2_img_pr.tStart = t  # local t and not account for scr refresh
                item2_img_pr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item2_img_pr, 'tStartRefresh')  # time at next scr refresh
                item2_img_pr.setAutoDraw(True)
            if item2_img_pr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item2_img_pr.tStartRefresh + n_secs_img2-frameTolerance:
                    # keep track of stop time/frame for later
                    item2_img_pr.tStop = t  # not accounting for scr refresh
                    item2_img_pr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(item2_img_pr, 'tStopRefresh')  # time at next scr refresh
                    item2_img_pr.setAutoDraw(False)
            
            # *brR_img_pr* updates
            if brR_img_pr.status == NOT_STARTED and que_finished == True:
                # keep track of start time/frame for later
                brR_img_pr.frameNStart = frameN  # exact frame index
                brR_img_pr.tStart = t  # local t and not account for scr refresh
                brR_img_pr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(brR_img_pr, 'tStartRefresh')  # time at next scr refresh
                brR_img_pr.setAutoDraw(True)
            if brR_img_pr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > brR_img_pr.tStartRefresh + n_secs_img2-frameTolerance:
                    # keep track of stop time/frame for later
                    brR_img_pr.tStop = t  # not accounting for scr refresh
                    brR_img_pr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(brR_img_pr, 'tStopRefresh')  # time at next scr refresh
                    brR_img_pr.setAutoDraw(False)
            
            # *response_pr* updates
            if response_pr.status == NOT_STARTED and que_finished == True:
                # keep track of start time/frame for later
                response_pr.frameNStart = frameN  # exact frame index
                response_pr.tStart = t  # local t and not account for scr refresh
                response_pr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_pr, 'tStartRefresh')  # time at next scr refresh
                response_pr.setAutoDraw(True)
            if response_pr.status == STARTED:
                if bool(participant_answered):
                    # keep track of stop time/frame for later
                    response_pr.tStop = t  # not accounting for scr refresh
                    response_pr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response_pr, 'tStopRefresh')  # time at next scr refresh
                    response_pr.setAutoDraw(False)
            
            # *timer_pr* updates
            if timer_pr.status == NOT_STARTED and que_finished == True:
                # keep track of start time/frame for later
                timer_pr.frameNStart = frameN  # exact frame index
                timer_pr.tStart = t  # local t and not account for scr refresh
                timer_pr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer_pr, 'tStartRefresh')  # time at next scr refresh
                timer_pr.setAutoDraw(True)
            if timer_pr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > timer_pr.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    timer_pr.tStop = t  # not accounting for scr refresh
                    timer_pr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(timer_pr, 'tStopRefresh')  # time at next scr refresh
                    timer_pr.setAutoDraw(False)
            
            # *fix_text_pr* updates
            if fix_text_pr.status == NOT_STARTED and item2_finished == True:
                # keep track of start time/frame for later
                fix_text_pr.frameNStart = frameN  # exact frame index
                fix_text_pr.tStart = t  # local t and not account for scr refresh
                fix_text_pr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_text_pr, 'tStartRefresh')  # time at next scr refresh
                fix_text_pr.setAutoDraw(True)
            if fix_text_pr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_text_pr.tStartRefresh + timeFix-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_text_pr.tStop = t  # not accounting for scr refresh
                    fix_text_pr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_text_pr, 'tStopRefresh')  # time at next scr refresh
                    fix_text_pr.setAutoDraw(False)
            
            # *key_prac* updates
            waitOnFlip = False
            if key_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_prac.frameNStart = frameN  # exact frame index
                key_prac.tStart = t  # local t and not account for scr refresh
                key_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_prac, 'tStartRefresh')  # time at next scr refresh
                key_prac.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_prac.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_prac.status == STARTED and not waitOnFlip:
                theseKeys = key_prac.getKeys(keyList=['1', '2', 'esc'], waitRelease=False)
                _key_prac_allKeys.extend(theseKeys)
                if len(_key_prac_allKeys):
                    key_prac.keys = _key_prac_allKeys[-1].name  # just the last key pressed
                    key_prac.rt = _key_prac_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prac"-------
        for thisComponent in pracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Save variables for correlation with ePrime previous logfiles
        
        # Add the answer of the participant
        thisExp.addData('im2prat.RESP', response_pr.text)
        # Add the correct answer
        thisExp.addData('im2prat.CRESP', cans)
        # See if that matches with the correct answer
        if response_pr.text == str(cans):
            thisExp.addData('im2prat.ACC', 1)
        elif response_pr.text == '1' or response_pr.text == '2':
            thisExp.addData('im2prat.ACC', 0)
        else:
            thisExp.addData('im2prat.ACC', '')
        if response_pr.tStop!=None:
            thisExp.addData('im2prat.RT', abs(response_pr.tStop - response_pr.tStart))
        else:
            thisExp.addData('im2prat.RT', '')
        
        # Save answer rttime since the beginning of the experiment
        thisExp.addData('im2prat.RTTime', response_pr.tStopRefresh)
        #win.color = 'white'
        practice.addData('item1_img_pr.started', item1_img_pr.tStartRefresh)
        practice.addData('item1_img_pr.stopped', item1_img_pr.tStopRefresh)
        practice.addData('brL_img_pr.started', brL_img_pr.tStartRefresh)
        practice.addData('brL_img_pr.stopped', brL_img_pr.tStopRefresh)
        practice.addData('que_text_pr.started', que_text_pr.tStartRefresh)
        practice.addData('que_text_pr.stopped', que_text_pr.tStopRefresh)
        practice.addData('item2_img_pr.started', item2_img_pr.tStartRefresh)
        practice.addData('item2_img_pr.stopped', item2_img_pr.tStopRefresh)
        practice.addData('brR_img_pr.started', brR_img_pr.tStartRefresh)
        practice.addData('brR_img_pr.stopped', brR_img_pr.tStopRefresh)
        practice.addData('response_pr.started', response_pr.tStartRefresh)
        practice.addData('response_pr.stopped', response_pr.tStopRefresh)
        practice.addData('fix_text_pr.started', fix_text_pr.tStartRefresh)
        practice.addData('fix_text_pr.stopped', fix_text_pr.tStopRefresh)
        # check responses
        if key_prac.keys in ['', [], None]:  # No response was made
            key_prac.keys = None
        practice.addData('key_prac.keys',key_prac.keys)
        if key_prac.keys != None:  # we had a response
            practice.addData('key_prac.rt', key_prac.rt)
        # store data for practice (TrialHandler)
        # store data for practice (TrialHandler)
        x, y = joystick_prac.getX(), joystick_prac.getY()
        joystick_prac.newButtonState = joystick_prac.getAllButtons()[:]
        joystick_prac.pressedState = [joystick_prac.newButtonState[i] for i in range(joystick_prac.numButtons)]
        joystick_prac.time = joystick_prac.joystickClock.getTime()
        practice.addData('joystick_prac.x', x)
        practice.addData('joystick_prac.y', y)
        [practice.addData('joystick_prac.button_{0}'.format(i), int(joystick_prac.pressedState[i])) for i in joystick_prac.activeButtons]
        practice.addData('joystick_prac.time', joystick_prac.time)
        practice.addData('joystick_prac.started', joystick_prac.tStart)
        practice.addData('joystick_prac.stopped', joystick_prac.tStop)
        # the Routine "prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'practice'
    
    
    # ------Prepare to start Routine "transition"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Change displayed text based on the language previously chosen
    if english == True:
        txt_transi.text = "You have completed the practice."
    else:
        txt_transi.text = "Vous avez fini la pratique."
    
    # Key 1 or key 2 are not pressed by default
    key1pressed = False
    key2pressed = False
    key_transi.keys = []
    key_transi.rt = []
    _key_transi_allKeys = []
    # keep track of which components have finished
    transitionComponents = [txt_transi, key_transi]
    for thisComponent in transitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    transitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "transition"-------
    while continueRoutine:
        # get current time
        t = transitionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=transitionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Check if we pressed keyboard keys
        if "p" in key_transi.keys:
            continueRoutine = False
        elif "t" in key_transi.keys:
            practice.finished = True
            prac_repeat.finished = True
            continueRoutine = False
        
        # *txt_transi* updates
        if txt_transi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_transi.frameNStart = frameN  # exact frame index
            txt_transi.tStart = t  # local t and not account for scr refresh
            txt_transi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_transi, 'tStartRefresh')  # time at next scr refresh
            txt_transi.setAutoDraw(True)
        
        # *key_transi* updates
        waitOnFlip = False
        if key_transi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_transi.frameNStart = frameN  # exact frame index
            key_transi.tStart = t  # local t and not account for scr refresh
            key_transi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_transi, 'tStartRefresh')  # time at next scr refresh
            key_transi.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_transi.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_transi.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_transi.status == STARTED and not waitOnFlip:
            theseKeys = key_transi.getKeys(keyList=['p', 't', 'esc'], waitRelease=False)
            _key_transi_allKeys.extend(theseKeys)
            if len(_key_transi_allKeys):
                key_transi.keys = _key_transi_allKeys[-1].name  # just the last key pressed
                key_transi.rt = _key_transi_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in transitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "transition"-------
    for thisComponent in transitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_repeat.addData('txt_transi.started', txt_transi.tStartRefresh)
    prac_repeat.addData('txt_transi.stopped', txt_transi.tStopRefresh)
    # check responses
    if key_transi.keys in ['', [], None]:  # No response was made
        key_transi.keys = None
    prac_repeat.addData('key_transi.keys',key_transi.keys)
    if key_transi.keys != None:  # we had a response
        prac_repeat.addData('key_transi.rt', key_transi.rt)
    # the Routine "transition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 100 repeats of 'prac_repeat'


# ------Prepare to start Routine "ready"-------
continueRoutine = True
# update component parameters for each repeat

# Change displayed text based on the language previously chosen
if english == True:
    txt_rdy.text = "There is a total of 4 experimental blocs in the experiment.\n\nThe bloc 1 of the experiment will start soon.\n\nReminder\n\n1: first object bigger / 2: second object bigger\n\n1: same category / 2: different categories\n\nBE READY!"
else:
    txt_rdy.text = "L'expérience contient un total de 4 blocs.\n\nLe bloc 1 de l'expérience va bientôt commencer.\n\nRappel\n\n1: premier objet plus gros / 2: deuxième objet plus gros\n\n1: même catégorie / 2: différentes catégories\n\nSOYEZ PRÊT !"
key_rdy.keys = []
key_rdy.rt = []
_key_rdy_allKeys = []
# keep track of which components have finished
readyComponents = [txt_rdy, key_rdy]
for thisComponent in readyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
readyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ready"-------
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=readyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_rdy* updates
    if txt_rdy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt_rdy.frameNStart = frameN  # exact frame index
        txt_rdy.tStart = t  # local t and not account for scr refresh
        txt_rdy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_rdy, 'tStartRefresh')  # time at next scr refresh
        txt_rdy.setAutoDraw(True)
    
    # *key_rdy* updates
    waitOnFlip = False
    if key_rdy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_rdy.frameNStart = frameN  # exact frame index
        key_rdy.tStart = t  # local t and not account for scr refresh
        key_rdy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_rdy, 'tStartRefresh')  # time at next scr refresh
        key_rdy.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_rdy.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_rdy.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_rdy.status == STARTED and not waitOnFlip:
        theseKeys = key_rdy.getKeys(keyList=['5', 'esc'], waitRelease=False)
        _key_rdy_allKeys.extend(theseKeys)
        if len(_key_rdy_allKeys):
            key_rdy.keys = _key_rdy_allKeys[-1].name  # just the last key pressed
            key_rdy.rt = _key_rdy_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt_rdy.started', txt_rdy.tStartRefresh)
thisExp.addData('txt_rdy.stopped', txt_rdy.tStopRefresh)
# check responses
if key_rdy.keys in ['', [], None]:  # No response was made
    key_rdy.keys = None
thisExp.addData('key_rdy.keys',key_rdy.keys)
if key_rdy.keys != None:  # we had a response
    thisExp.addData('key_rdy.rt', key_rdy.rt)
thisExp.nextEntry()
# the Routine "ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "cntdown"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# Boolean that will state if the signal is received or not
signal_received = True
# List that will contains the time where the signal was received
signal_times = list()
# keep track of which components have finished
cntdownComponents = [timer_ctdown]
for thisComponent in cntdownComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
cntdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "cntdown"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = cntdownClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=cntdownClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Check if we pressed keyboard keys
    keys = event.getKeys()
    #print(keys)
    
    # Reset signal
    if signal_received and not '5' in keys:
       signal_received = False
    
    # If we received the signal, store the time
    if not signal_received and '5' in keys:
        #tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        #print(tThisFlipGlobal)
        #signal_times.append(tThisFlipGlobal)
        signal_times.append(t)
        signal_received = True
    
    # *timer_ctdown* updates
    if timer_ctdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        timer_ctdown.frameNStart = frameN  # exact frame index
        timer_ctdown.tStart = t  # local t and not account for scr refresh
        timer_ctdown.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(timer_ctdown, 'tStartRefresh')  # time at next scr refresh
        timer_ctdown.setAutoDraw(True)
    if timer_ctdown.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > timer_ctdown.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            timer_ctdown.tStop = t  # not accounting for scr refresh
            timer_ctdown.frameNStop = frameN  # exact frame index
            win.timeOnFlip(timer_ctdown, 'tStopRefresh')  # time at next scr refresh
            timer_ctdown.setAutoDraw(False)
    if timer_ctdown.status == STARTED:  # only update if drawing
        timer_ctdown.setText(int(abs(round(5 - t, ndigits = 1))))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cntdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "cntdown"-------
for thisComponent in cntdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('signal_ctdown.time', signal_times)

# Set next trial bloc
bloc = 1
thisExp.addData('timer_ctdown.started', timer_ctdown.tStartRefresh)
thisExp.addData('timer_ctdown.stopped', timer_ctdown.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_repeat = data.TrialHandler(nReps=4, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_repeat')
thisExp.addLoop(trials_repeat)  # add the loop to the experiment
thisTrials_repeat = trials_repeat.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_repeat.rgb)
if thisTrials_repeat != None:
    for paramName in thisTrials_repeat:
        exec('{} = thisTrials_repeat[paramName]'.format(paramName))

for thisTrials_repeat in trials_repeat:
    currentLoop = trials_repeat
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_repeat.rgb)
    if thisTrials_repeat != None:
        for paramName in thisTrials_repeat:
            exec('{} = thisTrials_repeat[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(trialConditions),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        # Boolean that will state if the signal is received or not
        signal_received = True
        
        # List that will contains the time where the signal was received
        signal_times = list()
        
        # Change displayed text based on the language previously chosen
        if english == True:
            que_text.text = question_english
        else:
            que_text.text = question_french
            
        # Save the answer of the participant
        # The response period started when image 2 started. No need to save it.
        response_time = -1. # Save when the participant answered (in secs)
        
        # set the images by parameters of condition file
        img1 = pic1
        img2 = pic2
        
        # Set the duration of the fixation cross and the question
        timeQue = duration_question/1000 #duration of the question
        timeFix = duration_fixation/1000 #duration of the fixation cross
        
        # Duration of the items, question and fixation cross with frames
        # The number of frames we want to display is equal to
        # the product of frame-rate and the number of seconds to display
        # the stimulus.
        # n_frames = frame_rate * n_seconds
        # n_frames_img1 = frameRate * 2.
        # n_frames_img2 = frameRate * 2.
        # debug.text = "duration of img 1 in frames: "+str(n_frames_img1)
        
        n_secs_img1 = 2.
        n_secs_img2 = 2.
        
        #By default the elements did not start so they are not finished
        item1_finished = False
        que_finished = False
        item2_finished = False
        
        # Record if the participant answered
        participant_answered = False
        
        # When true, we reached the end of img2 without any answer
        no_answers = False
        
        # Reset the response of the participant
        response.text = ""
        
        item1_img.setImage(img1)
        item2_img.setImage(img2)
        key.keys = []
        key.rt = []
        _key_allKeys = []
        joystick.oldButtonState = joystick.device.getAllButtons()[:]
        joystick.activeButtons=[1, 2]
        # setup some python lists for storing info about the joystick
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        trialComponents = [item1_img, brL_img, que_text, item2_img, brR_img, response, timer, fix_text, key, joystick]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Check if we pressed keyboard keys
            keys = event.getKeys()
            #print(keys)
            
            # Reset signal
            if signal_received and not '5' in keys:
               signal_received = False
            
            # If we received the signal, store the time
            if not signal_received and '5' in keys:
                signal_times.append(t)
                signal_received = True
            
            # Set the boolean to true when item1 is done
            if item1_img.status == FINISHED:
                item1_finished = True
            
            # Set the boolean to true when the question is done
            if que_text.status == FINISHED and not que_finished:
                que_finished = True
            
            # Register participant's answers
            # Button 1 is pressed
            if not participant_answered and que_finished and (joystick.getAllButtons()[1] or "1" in key.keys):
                response.text = 1
                participant_answered = True
                #win.color = 'grey'
                print("participant chose: ", response.text)
            
            # Register participant's answers
            # Button 2 is pressed
            elif not participant_answered and que_finished and (joystick.getAllButtons()[2] or "2" in key.keys):
                response.text = 2
                participant_answered = True
                print("participant chose: ", response.text)
            
            # Register participant's answers
            #4s countdown are done
            elif not no_answers and not participant_answered and timer.status == FINISHED:
                response.finished = True
                no_answers = True
                print("participant did not answer: ", response.text)
            
            #Set the boolean to true when the item2 is done
            if item2_img.status == FINISHED:
                item2_finished = True
            
            #Go to next routine when fixation cross is done
            if fix_text.status == FINISHED:
                continueRoutine = False
            
            # *item1_img* updates
            if item1_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                item1_img.frameNStart = frameN  # exact frame index
                item1_img.tStart = t  # local t and not account for scr refresh
                item1_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item1_img, 'tStartRefresh')  # time at next scr refresh
                item1_img.setAutoDraw(True)
            if item1_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item1_img.tStartRefresh + n_secs_img1-frameTolerance:
                    # keep track of stop time/frame for later
                    item1_img.tStop = t  # not accounting for scr refresh
                    item1_img.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(item1_img, 'tStopRefresh')  # time at next scr refresh
                    item1_img.setAutoDraw(False)
            
            # *brL_img* updates
            if brL_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                brL_img.frameNStart = frameN  # exact frame index
                brL_img.tStart = t  # local t and not account for scr refresh
                brL_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(brL_img, 'tStartRefresh')  # time at next scr refresh
                brL_img.setAutoDraw(True)
            if brL_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > brL_img.tStartRefresh + n_secs_img1-frameTolerance:
                    # keep track of stop time/frame for later
                    brL_img.tStop = t  # not accounting for scr refresh
                    brL_img.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(brL_img, 'tStopRefresh')  # time at next scr refresh
                    brL_img.setAutoDraw(False)
            
            # *que_text* updates
            if que_text.status == NOT_STARTED and item1_finished == True:
                # keep track of start time/frame for later
                que_text.frameNStart = frameN  # exact frame index
                que_text.tStart = t  # local t and not account for scr refresh
                que_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(que_text, 'tStartRefresh')  # time at next scr refresh
                que_text.setAutoDraw(True)
            if que_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > que_text.tStartRefresh + timeQue-frameTolerance:
                    # keep track of stop time/frame for later
                    que_text.tStop = t  # not accounting for scr refresh
                    que_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(que_text, 'tStopRefresh')  # time at next scr refresh
                    que_text.setAutoDraw(False)
            
            # *item2_img* updates
            if item2_img.status == NOT_STARTED and que_finished:
                # keep track of start time/frame for later
                item2_img.frameNStart = frameN  # exact frame index
                item2_img.tStart = t  # local t and not account for scr refresh
                item2_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item2_img, 'tStartRefresh')  # time at next scr refresh
                item2_img.setAutoDraw(True)
            if item2_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item2_img.tStartRefresh + n_secs_img2-frameTolerance:
                    # keep track of stop time/frame for later
                    item2_img.tStop = t  # not accounting for scr refresh
                    item2_img.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(item2_img, 'tStopRefresh')  # time at next scr refresh
                    item2_img.setAutoDraw(False)
            
            # *brR_img* updates
            if brR_img.status == NOT_STARTED and que_finished:
                # keep track of start time/frame for later
                brR_img.frameNStart = frameN  # exact frame index
                brR_img.tStart = t  # local t and not account for scr refresh
                brR_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(brR_img, 'tStartRefresh')  # time at next scr refresh
                brR_img.setAutoDraw(True)
            if brR_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > brR_img.tStartRefresh + n_secs_img2-frameTolerance:
                    # keep track of stop time/frame for later
                    brR_img.tStop = t  # not accounting for scr refresh
                    brR_img.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(brR_img, 'tStopRefresh')  # time at next scr refresh
                    brR_img.setAutoDraw(False)
            
            # *response* updates
            if response.status == NOT_STARTED and que_finished == True:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.setAutoDraw(True)
            if response.status == STARTED:
                if bool(participant_answered):
                    # keep track of stop time/frame for later
                    response.tStop = t  # not accounting for scr refresh
                    response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response, 'tStopRefresh')  # time at next scr refresh
                    response.setAutoDraw(False)
            
            # *timer* updates
            if timer.status == NOT_STARTED and que_finished == True:
                # keep track of start time/frame for later
                timer.frameNStart = frameN  # exact frame index
                timer.tStart = t  # local t and not account for scr refresh
                timer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer, 'tStartRefresh')  # time at next scr refresh
                timer.setAutoDraw(True)
            if timer.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > timer.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    timer.tStop = t  # not accounting for scr refresh
                    timer.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(timer, 'tStopRefresh')  # time at next scr refresh
                    timer.setAutoDraw(False)
            
            # *fix_text* updates
            if fix_text.status == NOT_STARTED and item2_finished:
                # keep track of start time/frame for later
                fix_text.frameNStart = frameN  # exact frame index
                fix_text.tStart = t  # local t and not account for scr refresh
                fix_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_text, 'tStartRefresh')  # time at next scr refresh
                fix_text.setAutoDraw(True)
            if fix_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_text.tStartRefresh + timeFix-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_text.tStop = t  # not accounting for scr refresh
                    fix_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_text, 'tStopRefresh')  # time at next scr refresh
                    fix_text.setAutoDraw(False)
            
            # *key* updates
            waitOnFlip = False
            if key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key.frameNStart = frameN  # exact frame index
                key.tStart = t  # local t and not account for scr refresh
                key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key, 'tStartRefresh')  # time at next scr refresh
                key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key.status == STARTED and not waitOnFlip:
                theseKeys = key.getKeys(keyList=['1', '2', 'esc'], waitRelease=False)
                _key_allKeys.extend(theseKeys)
                if len(_key_allKeys):
                    key.keys = _key_allKeys[-1].name  # just the last key pressed
                    key.rt = _key_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Save variables for correlation with ePrime previous logfiles
        
        # Add the answer of the participant
        thisExp.addData('im2.RESP', response.text)
        # Add the correct answer
        thisExp.addData('im2.CRESP', cans)
        # See if that matches with the correct answer
        if response.text == str(cans):
            thisExp.addData('im2.ACC', 1)
        elif response.text == '1' or response.text == '2':
            thisExp.addData('im2.ACC', 0)
        else:
            thisExp.addData('im2.ACC', '')
        if response.tStop!=None:
            thisExp.addData('im2.RT', abs(response.tStop - response.tStart))
        else:
            thisExp.addData('im2.RT', '')
        
        # Save answer rttime since the beginning of the experiment
        thisExp.addData('im2.RTTime', response.tStopRefresh)
        
        # Save the time where the participant answered according to the beginning of the countdown
        if response.tStopRefresh!=None:
            thisExp.addData('im2.RTTimeSyncCdown', abs(response.tStopRefresh-timer_ctdown.tStartRefresh))
        else:
            thisExp.addData('im2.RTTimeSyncCdown', '')
        
        # Save the time where the signal was received
        thisExp.addData('signal.time', signal_times)
        trials.addData('item1_img.started', item1_img.tStartRefresh)
        trials.addData('item1_img.stopped', item1_img.tStopRefresh)
        trials.addData('brL_img.started', brL_img.tStartRefresh)
        trials.addData('brL_img.stopped', brL_img.tStopRefresh)
        trials.addData('que_text.started', que_text.tStartRefresh)
        trials.addData('que_text.stopped', que_text.tStopRefresh)
        trials.addData('item2_img.started', item2_img.tStartRefresh)
        trials.addData('item2_img.stopped', item2_img.tStopRefresh)
        trials.addData('brR_img.started', brR_img.tStartRefresh)
        trials.addData('brR_img.stopped', brR_img.tStopRefresh)
        trials.addData('response.started', response.tStartRefresh)
        trials.addData('response.stopped', response.tStopRefresh)
        trials.addData('fix_text.started', fix_text.tStartRefresh)
        trials.addData('fix_text.stopped', fix_text.tStopRefresh)
        # check responses
        if key.keys in ['', [], None]:  # No response was made
            key.keys = None
        trials.addData('key.keys',key.keys)
        if key.keys != None:  # we had a response
            trials.addData('key.rt', key.rt)
        trials.addData('key.started', key.tStartRefresh)
        trials.addData('key.stopped', key.tStopRefresh)
        # store data for trials (TrialHandler)
        # store data for trials (TrialHandler)
        x, y = joystick.getX(), joystick.getY()
        joystick.newButtonState = joystick.getAllButtons()[:]
        joystick.pressedState = [joystick.newButtonState[i] for i in range(joystick.numButtons)]
        joystick.time = joystick.joystickClock.getTime()
        trials.addData('joystick.x', x)
        trials.addData('joystick.y', y)
        [trials.addData('joystick.button_{0}'.format(i), int(joystick.pressedState[i])) for i in joystick.activeButtons]
        trials.addData('joystick.time', joystick.time)
        trials.addData('joystick.started', joystick.tStart)
        trials.addData('joystick.stopped', joystick.tStop)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    # If we finished the 2nd bloc, skip this routine
    if bloc == 4:
        continueRoutine = False
    
    # Change displayed text based on the language previously chosen
    if english == True:
        txt_rest.text = "THIS RUN IS OVER, JUST RELAX\n\nUNTIL THE SCANNER STOPS"
    else:
        txt_rest.text = "CET BLOC EST TERMINÉ, DÉTENDEZ-VOUS\n\nJUSQU'À CE QUE LE SCANNER S'ARRÊTE"
    
    # Load bloc 2 csv file
    if bloc == 1:
        trialConditions = "SEMT_conditions_trials_bloc2.csv"
    elif bloc == 2:
        trialConditions = "SEMT_conditions_trials_bloc3.csv"
    else:
       trialConditions = "SEMT_conditions_trials_bloc4.csv"
         
    #for i in [1,2,3,4]:
    #    trialConditions = "SEMT_conditions_trials_bloc" + str(i) + ".csv"
    key_rest.keys = []
    key_rest.rt = []
    _key_rest_allKeys = []
    # keep track of which components have finished
    restComponents = [txt_rest, key_rest]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_rest* updates
        if txt_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_rest.frameNStart = frameN  # exact frame index
            txt_rest.tStart = t  # local t and not account for scr refresh
            txt_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_rest, 'tStartRefresh')  # time at next scr refresh
            txt_rest.setAutoDraw(True)
        
        # *key_rest* updates
        waitOnFlip = False
        if key_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_rest.frameNStart = frameN  # exact frame index
            key_rest.tStart = t  # local t and not account for scr refresh
            key_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_rest, 'tStartRefresh')  # time at next scr refresh
            key_rest.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_rest.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_rest.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_rest.status == STARTED and not waitOnFlip:
            theseKeys = key_rest.getKeys(keyList=['t', 'esc'], waitRelease=False)
            _key_rest_allKeys.extend(theseKeys)
            if len(_key_rest_allKeys):
                key_rest.keys = _key_rest_allKeys[-1].name  # just the last key pressed
                key_rest.rt = _key_rest_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_repeat.addData('txt_rest.started', txt_rest.tStartRefresh)
    trials_repeat.addData('txt_rest.stopped', txt_rest.tStopRefresh)
    # check responses
    if key_rest.keys in ['', [], None]:  # No response was made
        key_rest.keys = None
    trials_repeat.addData('key_rest.keys',key_rest.keys)
    if key_rest.keys != None:  # we had a response
        trials_repeat.addData('key_rest.rt', key_rest.rt)
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ready_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # If we finished the 2nd bloc, skip this routine
    if bloc == 4:
        continueRoutine = False
    
    # Change displayed text based on the language previously chosen
    if english == True:
        txt_rdy.text = "There is a total of 4 experimental blocks in the experiment.\n\nBlock 1 of the experiment will start soon.\n\nReminder\n\n1: first object bigger / 2: second object bigger\n\n1: same category / 2: different categories\n\nBE READY!"
    else:
        txt_rdy.text = "L'expérience contient un total de 4 blocs.\n\nLe bloc 1 de l'expérience va bientôt commencer.\n\nRappel\n\n1: premier objet plus gros/dans la même catégorie\n2: deuxième objet plus gros/pas dans la même catégorie\n\nSOYEZ PRÊT !"
    key_rdy2.keys = []
    key_rdy2.rt = []
    _key_rdy2_allKeys = []
    # keep track of which components have finished
    ready_2Components = [txt_rdy2, key_rdy2]
    for thisComponent in ready_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ready_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ready_2"-------
    while continueRoutine:
        # get current time
        t = ready_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ready_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_rdy2* updates
        if txt_rdy2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_rdy2.frameNStart = frameN  # exact frame index
            txt_rdy2.tStart = t  # local t and not account for scr refresh
            txt_rdy2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_rdy2, 'tStartRefresh')  # time at next scr refresh
            txt_rdy2.setAutoDraw(True)
        
        # *key_rdy2* updates
        waitOnFlip = False
        if key_rdy2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_rdy2.frameNStart = frameN  # exact frame index
            key_rdy2.tStart = t  # local t and not account for scr refresh
            key_rdy2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_rdy2, 'tStartRefresh')  # time at next scr refresh
            key_rdy2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_rdy2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_rdy2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_rdy2.status == STARTED and not waitOnFlip:
            theseKeys = key_rdy2.getKeys(keyList=['5', 'esc'], waitRelease=False)
            _key_rdy2_allKeys.extend(theseKeys)
            if len(_key_rdy2_allKeys):
                key_rdy2.keys = _key_rdy2_allKeys[-1].name  # just the last key pressed
                key_rdy2.rt = _key_rdy2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready_2"-------
    for thisComponent in ready_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_repeat.addData('txt_rdy2.started', txt_rdy2.tStartRefresh)
    trials_repeat.addData('txt_rdy2.stopped', txt_rdy2.tStopRefresh)
    # check responses
    if key_rdy2.keys in ['', [], None]:  # No response was made
        key_rdy2.keys = None
    trials_repeat.addData('key_rdy2.keys',key_rdy2.keys)
    if key_rdy2.keys != None:  # we had a response
        trials_repeat.addData('key_rdy2.rt', key_rdy2.rt)
    # the Routine "ready_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "cntdown_2"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    # If we finished the 2nd bloc, skip this routine
    if bloc == 4:
        continueRoutine = False
    
    # Boolean that will state if the signal is received or not
    signal_received = True
    # List that will contains the time where the signal was received
    signal_times = list()
    # keep track of which components have finished
    cntdown_2Components = [timer_ctdown2]
    for thisComponent in cntdown_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cntdown_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cntdown_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = cntdown_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cntdown_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Check if we pressed keyboard keys
        keys = event.getKeys()
        #print(keys)
        
        # Reset signal
        if signal_received and not '5' in keys:
           signal_received = False
        
        # If we received the signal, store the time
        if not signal_received and '5' in keys:
            signal_times.append(t)
            signal_received = True
        
        # *timer_ctdown2* updates
        if timer_ctdown2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_ctdown2.frameNStart = frameN  # exact frame index
            timer_ctdown2.tStart = t  # local t and not account for scr refresh
            timer_ctdown2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_ctdown2, 'tStartRefresh')  # time at next scr refresh
            timer_ctdown2.setAutoDraw(True)
        if timer_ctdown2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_ctdown2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                timer_ctdown2.tStop = t  # not accounting for scr refresh
                timer_ctdown2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_ctdown2, 'tStopRefresh')  # time at next scr refresh
                timer_ctdown2.setAutoDraw(False)
        if timer_ctdown2.status == STARTED:  # only update if drawing
            timer_ctdown2.setText(int(abs(round(5 - t, ndigits = 1))))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cntdown_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cntdown_2"-------
    for thisComponent in cntdown_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('signal_ctdown2.time', signal_times)
    
    # Set next trial bloc
    bloc = bloc + 1
     
        
        
    
    trials_repeat.addData('timer_ctdown2.started', timer_ctdown2.tStartRefresh)
    trials_repeat.addData('timer_ctdown2.stopped', timer_ctdown2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 4 repeats of 'trials_repeat'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# Change displayed text based on the language previously chosen
if english == True:
    txt_thx.text = "YOU HAVE COMPLETED ALL THE BLOCKS!\n\nJUST RELAX UNTIL THE SCANNER STOPS.\n\nThank you for participating."
else:
    txt_thx.text = "VOUS AVEZ COMPLÉTÉ TOUS LES BLOCS !\n\nRELAXEZ-VOUS JUSQU'À CE QUE LE SCANNER S'ARRÊTE.\n\nMerci pour votre participation.\n\nAu revoir !"
# keep track of which components have finished
thanksComponents = [txt_thx]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_thx* updates
    if txt_thx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt_thx.frameNStart = frameN  # exact frame index
        txt_thx.tStart = t  # local t and not account for scr refresh
        txt_thx.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_thx, 'tStartRefresh')  # time at next scr refresh
        txt_thx.setAutoDraw(True)
    if txt_thx.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt_thx.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            txt_thx.tStop = t  # not accounting for scr refresh
            txt_thx.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt_thx, 'tStopRefresh')  # time at next scr refresh
            txt_thx.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt_thx.started', txt_thx.tStartRefresh)
thisExp.addData('txt_thx.stopped', txt_thx.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
