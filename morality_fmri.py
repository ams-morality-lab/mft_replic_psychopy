#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Sat Feb 25 09:53:07 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'exam_trainer'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/benjaminjargow/Documents/01_ResMas/Internship/Paradigm/morality_fmri.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "welcome_screen" ---
text_welcome_sreen = visual.TextStim(win=win, name='text_welcome_sreen',
    text='Thank you for participating in this study. It has three parts. Part one begins soon.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcome_key = keyboard.Keyboard()

# --- Initialize components for Routine "blank_500" ---
text_blank_500 = visual.TextStim(win=win, name='text_blank_500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "instructions_vignette" ---
# Run 'Begin Experiment' code from code_2
condition = np.random.choice(('dutch','english'))
text = visual.TextStim(win=win, name='text',
    text="You will see a series of sentences in " +condition +".\nImagine yourself as a witness to the actions in each one.\nPlease rate how MORALLY WRONG each action was, using a 4-point scale ranging from: ",
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nNot Morally Wrong", "4\nExtremely Morally Wrong"), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-2, readOnly=False)
key_resp = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Please use your right hand for the ratings. Your index finger equals one, your pinky the four.',
    font='Open Sans',
    pos=(0, -.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "blank_500" ---
text_blank_500 = visual.TextStim(win=win, name='text_blank_500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "vignette_stimulus" ---
test_question = visual.TextStim(win=win, name='test_question',
    text='',
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
rating_vignettes = visual.Slider(win=win, name='rating_vignettes',
    startValue=None, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nNot Morally Wrong", "4\nExtremely Morally Wrong"), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)
key_question = keyboard.Keyboard()

# --- Initialize components for Routine "blank_rnd" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "vignette_break" ---
text_5 = visual.TextStim(win=win, name='text_5',
    text='Short Break. When you are ready to continue, indicate that with pressing any key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instructions_SMID" ---
text_SMID = visual.TextStim(win=win, name='text_SMID',
    text='Thank you for answering the questions on the vignettes. The first part of the study is done.\n\nNext, we will present images. Please indicate whether these are moral, neutral or immoral.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_end = keyboard.Keyboard()

# --- Initialize components for Routine "blank_500" ---
text_blank_500 = visual.TextStim(win=win, name='text_blank_500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "fixation_cross_long" ---
cross_long = visual.ShapeStim(
    win=win, name='cross_long', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "pic_stimulus" ---
smid_image = visual.ImageStim(
    win=win,
    name='smid_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "fixation_cross_short" ---
cross_short = visual.ShapeStim(
    win=win, name='cross_short', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Rating" ---
rating_smid = visual.Slider(win=win, name='rating_smid',
    startValue=None, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nMoral", "5\nImmoral"), ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=0, readOnly=False)
rating_key_smid = keyboard.Keyboard()
text_smd = visual.TextStim(win=win, name='text_smd',
    text='The image portrayed something...',
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "image_break" ---
image_break_text = visual.TextStim(win=win, name='image_break_text',
    text='Short Break. When you are ready to continue, indicate that with pressing any key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_break_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank_500" ---
text_blank_500 = visual.TextStim(win=win, name='text_blank_500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome_screen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcome_key.keys = []
welcome_key.rt = []
_welcome_key_allKeys = []
# keep track of which components have finished
welcome_screenComponents = [text_welcome_sreen, welcome_key]
for thisComponent in welcome_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcome_screen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome_sreen* updates
    if text_welcome_sreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome_sreen.frameNStart = frameN  # exact frame index
        text_welcome_sreen.tStart = t  # local t and not account for scr refresh
        text_welcome_sreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome_sreen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_welcome_sreen.started')
        text_welcome_sreen.setAutoDraw(True)
    
    # *welcome_key* updates
    waitOnFlip = False
    if welcome_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_key.frameNStart = frameN  # exact frame index
        welcome_key.tStart = t  # local t and not account for scr refresh
        welcome_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_key.started')
        welcome_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_key.status == STARTED and not waitOnFlip:
        theseKeys = welcome_key.getKeys(keyList=["t"], waitRelease=False)
        _welcome_key_allKeys.extend(theseKeys)
        if len(_welcome_key_allKeys):
            welcome_key.keys = _welcome_key_allKeys[-1].name  # just the last key pressed
            welcome_key.rt = _welcome_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome_screen" ---
for thisComponent in welcome_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if welcome_key.keys in ['', [], None]:  # No response was made
    welcome_key.keys = None
thisExp.addData('welcome_key.keys',welcome_key.keys)
if welcome_key.keys != None:  # we had a response
    thisExp.addData('welcome_key.rt', welcome_key.rt)
thisExp.nextEntry()
# the Routine "welcome_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank_500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_blank_500.setText('')
# keep track of which components have finished
blank_500Components = [text_blank_500]
for thisComponent in blank_500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank_500" ---
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank_500* updates
    if text_blank_500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank_500.frameNStart = frameN  # exact frame index
        text_blank_500.tStart = t  # local t and not account for scr refresh
        text_blank_500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank_500, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_blank_500.started')
        text_blank_500.setAutoDraw(True)
    if text_blank_500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_blank_500.tStop = t  # not accounting for scr refresh
            text_blank_500.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_blank_500.stopped')
            text_blank_500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank_500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank_500" ---
for thisComponent in blank_500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# --- Prepare to start Routine "instructions_vignette" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
slider.reset()
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructions_vignetteComponents = [text, slider, key_resp, text_2]
for thisComponent in instructions_vignetteComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_vignette" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *slider* updates
    if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider.frameNStart = frameN  # exact frame index
        slider.tStart = t  # local t and not account for scr refresh
        slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'slider.started')
        slider.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['b', 'y', 'g', 'r'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_vignetteComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_vignette" ---
for thisComponent in instructions_vignetteComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider.response', slider.getRating())
thisExp.addData('slider.rt', slider.getRT())
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "instructions_vignette" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank_500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_blank_500.setText('')
# keep track of which components have finished
blank_500Components = [text_blank_500]
for thisComponent in blank_500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank_500" ---
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank_500* updates
    if text_blank_500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank_500.frameNStart = frameN  # exact frame index
        text_blank_500.tStart = t  # local t and not account for scr refresh
        text_blank_500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank_500, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_blank_500.started')
        text_blank_500.setAutoDraw(True)
    if text_blank_500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_blank_500.tStop = t  # not accounting for scr refresh
            text_blank_500.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_blank_500.stopped')
            text_blank_500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank_500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank_500" ---
for thisComponent in blank_500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# set up handler to look after randomisation of conditions etc
vignette_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("vig_text_"+ condition + ".xlsx", selection=random(12)*120),
    seed=None, name='vignette_trials')
thisExp.addLoop(vignette_trials)  # add the loop to the experiment
thisVignette_trial = vignette_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVignette_trial.rgb)
if thisVignette_trial != None:
    for paramName in thisVignette_trial:
        exec('{} = thisVignette_trial[paramName]'.format(paramName))

for thisVignette_trial in vignette_trials:
    currentLoop = vignette_trials
    # abbreviate parameter names if possible (e.g. rgb = thisVignette_trial.rgb)
    if thisVignette_trial != None:
        for paramName in thisVignette_trial:
            exec('{} = thisVignette_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "vignette_stimulus" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    test_question.setText(vignette_text)
    rating_vignettes.reset()
    key_question.keys = []
    key_question.rt = []
    _key_question_allKeys = []
    # keep track of which components have finished
    vignette_stimulusComponents = [test_question, rating_vignettes, key_question]
    for thisComponent in vignette_stimulusComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "vignette_stimulus" ---
    while continueRoutine and routineTimer.getTime() < 8.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_question* updates
        if test_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_question.frameNStart = frameN  # exact frame index
            test_question.tStart = t  # local t and not account for scr refresh
            test_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'test_question.started')
            test_question.setAutoDraw(True)
        if test_question.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_question.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                test_question.tStop = t  # not accounting for scr refresh
                test_question.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_question.stopped')
                test_question.setAutoDraw(False)
        
        # *rating_vignettes* updates
        if rating_vignettes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_vignettes.frameNStart = frameN  # exact frame index
            rating_vignettes.tStart = t  # local t and not account for scr refresh
            rating_vignettes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_vignettes, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rating_vignettes.started')
            rating_vignettes.setAutoDraw(True)
        if rating_vignettes.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rating_vignettes.tStartRefresh + 8.0-frameTolerance:
                # keep track of stop time/frame for later
                rating_vignettes.tStop = t  # not accounting for scr refresh
                rating_vignettes.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rating_vignettes.stopped')
                rating_vignettes.setAutoDraw(False)
        
        # *key_question* updates
        waitOnFlip = False
        if key_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_question.frameNStart = frameN  # exact frame index
            key_question.tStart = t  # local t and not account for scr refresh
            key_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_question.started')
            key_question.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_question.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_question.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_question.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_question.tStartRefresh + 8.0-frameTolerance:
                # keep track of stop time/frame for later
                key_question.tStop = t  # not accounting for scr refresh
                key_question.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_question.stopped')
                key_question.status = FINISHED
        if key_question.status == STARTED and not waitOnFlip:
            theseKeys = key_question.getKeys(keyList=["b", "y", "g", "r"], waitRelease=False)
            _key_question_allKeys.extend(theseKeys)
            if len(_key_question_allKeys):
                key_question.keys = _key_question_allKeys[-1].name  # just the last key pressed
                key_question.rt = _key_question_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vignette_stimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "vignette_stimulus" ---
    for thisComponent in vignette_stimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    vignette_trials.addData('rating_vignettes.response', rating_vignettes.getRating())
    vignette_trials.addData('rating_vignettes.rt', rating_vignettes.getRT())
    # check responses
    if key_question.keys in ['', [], None]:  # No response was made
        key_question.keys = None
    vignette_trials.addData('key_question.keys',key_question.keys)
    if key_question.keys != None:  # we had a response
        vignette_trials.addData('key_question.rt', key_question.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-8.000000)
    
    # --- Prepare to start Routine "blank_rnd" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    blank_duration = np.random.uniform(1,3)
    text_3.setText('')
    # keep track of which components have finished
    blank_rndComponents = [text_3]
    for thisComponent in blank_rndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank_rnd" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + blank_duration-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_rndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank_rnd" ---
    for thisComponent in blank_rndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blank_rnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "vignette_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    vignette_breakComponents = [text_5, key_resp_2]
    for thisComponent in vignette_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "vignette_break" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from vignette_pauses
        if vignette_trials.thisN == 0 or (vignette_trials.thisN + 1) % 4 != 0:
            continueRoutine = False
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.stopped')
                text_5.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=["b", "y", "g", "r"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vignette_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "vignette_break" ---
    for thisComponent in vignette_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    vignette_trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        vignette_trials.addData('key_resp_2.rt', key_resp_2.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'vignette_trials'


# --- Prepare to start Routine "instructions_SMID" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_end.keys = []
key_end.rt = []
_key_end_allKeys = []
# keep track of which components have finished
instructions_SMIDComponents = [text_SMID, key_end]
for thisComponent in instructions_SMIDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_SMID" ---
while continueRoutine and routineTimer.getTime() < 15.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_SMID* updates
    if text_SMID.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_SMID.frameNStart = frameN  # exact frame index
        text_SMID.tStart = t  # local t and not account for scr refresh
        text_SMID.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_SMID, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_SMID.started')
        text_SMID.setAutoDraw(True)
    if text_SMID.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_SMID.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            text_SMID.tStop = t  # not accounting for scr refresh
            text_SMID.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_SMID.stopped')
            text_SMID.setAutoDraw(False)
    
    # *key_end* updates
    waitOnFlip = False
    if key_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_end.frameNStart = frameN  # exact frame index
        key_end.tStart = t  # local t and not account for scr refresh
        key_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_end, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_end.started')
        key_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_end.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            key_end.tStop = t  # not accounting for scr refresh
            key_end.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_end.stopped')
            key_end.status = FINISHED
    if key_end.status == STARTED and not waitOnFlip:
        theseKeys = key_end.getKeys(keyList=["b", "y", "g", "r"], waitRelease=False)
        _key_end_allKeys.extend(theseKeys)
        if len(_key_end_allKeys):
            key_end.keys = _key_end_allKeys[-1].name  # just the last key pressed
            key_end.rt = _key_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_SMIDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_SMID" ---
for thisComponent in instructions_SMIDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_end.keys in ['', [], None]:  # No response was made
    key_end.keys = None
thisExp.addData('key_end.keys',key_end.keys)
if key_end.keys != None:  # we had a response
    thisExp.addData('key_end.rt', key_end.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.000000)

# --- Prepare to start Routine "blank_500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_blank_500.setText('')
# keep track of which components have finished
blank_500Components = [text_blank_500]
for thisComponent in blank_500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank_500" ---
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank_500* updates
    if text_blank_500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank_500.frameNStart = frameN  # exact frame index
        text_blank_500.tStart = t  # local t and not account for scr refresh
        text_blank_500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank_500, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_blank_500.started')
        text_blank_500.setAutoDraw(True)
    if text_blank_500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_blank_500.tStop = t  # not accounting for scr refresh
            text_blank_500.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_blank_500.stopped')
            text_blank_500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank_500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank_500" ---
for thisComponent in blank_500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# set up handler to look after randomisation of conditions etc
image_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('smid_stimuli.xlsx', selection=random(12)*120),
    seed=None, name='image_trials')
thisExp.addLoop(image_trials)  # add the loop to the experiment
thisImage_trial = image_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisImage_trial.rgb)
if thisImage_trial != None:
    for paramName in thisImage_trial:
        exec('{} = thisImage_trial[paramName]'.format(paramName))

for thisImage_trial in image_trials:
    currentLoop = image_trials
    # abbreviate parameter names if possible (e.g. rgb = thisImage_trial.rgb)
    if thisImage_trial != None:
        for paramName in thisImage_trial:
            exec('{} = thisImage_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fixation_cross_long" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_cross_longComponents = [cross_long]
    for thisComponent in fixation_cross_longComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation_cross_long" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_long* updates
        if cross_long.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_long.frameNStart = frameN  # exact frame index
            cross_long.tStart = t  # local t and not account for scr refresh
            cross_long.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_long, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_long.started')
            cross_long.setAutoDraw(True)
        if cross_long.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_long.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                cross_long.tStop = t  # not accounting for scr refresh
                cross_long.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_long.stopped')
                cross_long.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_cross_longComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation_cross_long" ---
    for thisComponent in fixation_cross_longComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "pic_stimulus" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    smid_image.setImage(image_name)
    # keep track of which components have finished
    pic_stimulusComponents = [smid_image]
    for thisComponent in pic_stimulusComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pic_stimulus" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *smid_image* updates
        if smid_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smid_image.frameNStart = frameN  # exact frame index
            smid_image.tStart = t  # local t and not account for scr refresh
            smid_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smid_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smid_image.started')
            smid_image.setAutoDraw(True)
        if smid_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smid_image.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                smid_image.tStop = t  # not accounting for scr refresh
                smid_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'smid_image.stopped')
                smid_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pic_stimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pic_stimulus" ---
    for thisComponent in pic_stimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "fixation_cross_short" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_cross_shortComponents = [cross_short]
    for thisComponent in fixation_cross_shortComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation_cross_short" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_short* updates
        if cross_short.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_short.frameNStart = frameN  # exact frame index
            cross_short.tStart = t  # local t and not account for scr refresh
            cross_short.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_short, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_short.started')
            cross_short.setAutoDraw(True)
        if cross_short.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_short.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                cross_short.tStop = t  # not accounting for scr refresh
                cross_short.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_short.stopped')
                cross_short.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_cross_shortComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation_cross_short" ---
    for thisComponent in fixation_cross_shortComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "Rating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    rating_smid.reset()
    rating_key_smid.keys = []
    rating_key_smid.rt = []
    _rating_key_smid_allKeys = []
    # keep track of which components have finished
    RatingComponents = [rating_smid, rating_key_smid, text_smd]
    for thisComponent in RatingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Rating" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rating_smid* updates
        if rating_smid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_smid.frameNStart = frameN  # exact frame index
            rating_smid.tStart = t  # local t and not account for scr refresh
            rating_smid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_smid, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rating_smid.started')
            rating_smid.setAutoDraw(True)
        if rating_smid.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rating_smid.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rating_smid.tStop = t  # not accounting for scr refresh
                rating_smid.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rating_smid.stopped')
                rating_smid.setAutoDraw(False)
        
        # *rating_key_smid* updates
        waitOnFlip = False
        if rating_key_smid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_key_smid.frameNStart = frameN  # exact frame index
            rating_key_smid.tStart = t  # local t and not account for scr refresh
            rating_key_smid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_key_smid, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rating_key_smid.started')
            rating_key_smid.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rating_key_smid.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rating_key_smid.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rating_key_smid.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rating_key_smid.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rating_key_smid.tStop = t  # not accounting for scr refresh
                rating_key_smid.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rating_key_smid.stopped')
                rating_key_smid.status = FINISHED
        if rating_key_smid.status == STARTED and not waitOnFlip:
            theseKeys = rating_key_smid.getKeys(keyList=["b", "y", "g", "r"], waitRelease=False)
            _rating_key_smid_allKeys.extend(theseKeys)
            if len(_rating_key_smid_allKeys):
                rating_key_smid.keys = _rating_key_smid_allKeys[-1].name  # just the last key pressed
                rating_key_smid.rt = _rating_key_smid_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_smd* updates
        if text_smd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_smd.frameNStart = frameN  # exact frame index
            text_smd.tStart = t  # local t and not account for scr refresh
            text_smd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_smd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_smd.started')
            text_smd.setAutoDraw(True)
        if text_smd.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_smd.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                text_smd.tStop = t  # not accounting for scr refresh
                text_smd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_smd.stopped')
                text_smd.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Rating" ---
    for thisComponent in RatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    image_trials.addData('rating_smid.response', rating_smid.getRating())
    image_trials.addData('rating_smid.rt', rating_smid.getRT())
    # check responses
    if rating_key_smid.keys in ['', [], None]:  # No response was made
        rating_key_smid.keys = None
    image_trials.addData('rating_key_smid.keys',rating_key_smid.keys)
    if rating_key_smid.keys != None:  # we had a response
        image_trials.addData('rating_key_smid.rt', rating_key_smid.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "image_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    image_break_resp.keys = []
    image_break_resp.rt = []
    _image_break_resp_allKeys = []
    # keep track of which components have finished
    image_breakComponents = [image_break_text, image_break_resp]
    for thisComponent in image_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "image_break" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from image_break_code
        if image_trials.thisN == 0 or (image_trials.thisN + 1) % 3 != 0:
            continueRoutine = False
        
        # *image_break_text* updates
        if image_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_break_text.frameNStart = frameN  # exact frame index
            image_break_text.tStart = t  # local t and not account for scr refresh
            image_break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_break_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_break_text.started')
            image_break_text.setAutoDraw(True)
        if image_break_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_break_text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                image_break_text.tStop = t  # not accounting for scr refresh
                image_break_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_break_text.stopped')
                image_break_text.setAutoDraw(False)
        
        # *image_break_resp* updates
        waitOnFlip = False
        if image_break_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_break_resp.frameNStart = frameN  # exact frame index
            image_break_resp.tStart = t  # local t and not account for scr refresh
            image_break_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_break_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_break_resp.started')
            image_break_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(image_break_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(image_break_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if image_break_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_break_resp.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                image_break_resp.tStop = t  # not accounting for scr refresh
                image_break_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_break_resp.stopped')
                image_break_resp.status = FINISHED
        if image_break_resp.status == STARTED and not waitOnFlip:
            theseKeys = image_break_resp.getKeys(keyList=["b", "y", "g", "r"], waitRelease=False)
            _image_break_resp_allKeys.extend(theseKeys)
            if len(_image_break_resp_allKeys):
                image_break_resp.keys = _image_break_resp_allKeys[-1].name  # just the last key pressed
                image_break_resp.rt = _image_break_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in image_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image_break" ---
    for thisComponent in image_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if image_break_resp.keys in ['', [], None]:  # No response was made
        image_break_resp.keys = None
    image_trials.addData('image_break_resp.keys',image_break_resp.keys)
    if image_break_resp.keys != None:  # we had a response
        image_trials.addData('image_break_resp.rt', image_break_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'image_trials'


# --- Prepare to start Routine "blank_500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
text_blank_500.setText('')
# keep track of which components have finished
blank_500Components = [text_blank_500]
for thisComponent in blank_500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank_500" ---
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank_500* updates
    if text_blank_500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank_500.frameNStart = frameN  # exact frame index
        text_blank_500.tStart = t  # local t and not account for scr refresh
        text_blank_500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank_500, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_blank_500.started')
        text_blank_500.setAutoDraw(True)
    if text_blank_500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_blank_500.tStop = t  # not accounting for scr refresh
            text_blank_500.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_blank_500.stopped')
            text_blank_500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank_500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank_500" ---
for thisComponent in blank_500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
