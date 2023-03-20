#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Mon Mar 20 18:48:14 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
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
expName = 'moral_judgements_fMRI'  # from the Builder filename that created this script
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
welcome_text = visual.TextStim(win=win, name='welcome_text',
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

# --- Initialize components for Routine "vignette_instructions" ---
# Run 'Begin Experiment' code from lang_choice
condition = np.random.choice(('dutch','english'))
vignette_instructions_1 = visual.TextStim(win=win, name='vignette_instructions_1',
    text="You will see a series of sentences in " +condition +".\nImagine yourself as a witness to the actions in each one.\nPlease rate how MORALLY WRONG each action was, using a 4-point scale ranging from: ",
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
vignette_example_slider = visual.Slider(win=win, name='vignette_example_slider',
    startValue=1, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nNot Morally Wrong", "4\nExtremely Morally Wrong"), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-2, readOnly=True)
vignette_instructions_key = keyboard.Keyboard()
vignette_instructions_2 = visual.TextStim(win=win, name='vignette_instructions_2',
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
vignette = visual.TextStim(win=win, name='vignette',
    text='',
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
vignette_slider = visual.Slider(win=win, name='vignette_slider',
    startValue=None, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nNot Morally Wrong", "4\nExtremely Morally Wrong"), ticks=(1, 2, 3, 4), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)
vignette_keys = keyboard.Keyboard()

# --- Initialize components for Routine "vignette_blank" ---
vignette_blank_text = visual.TextStim(win=win, name='vignette_blank_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "vignette_break" ---
vignette_break_text = visual.TextStim(win=win, name='vignette_break_text',
    text='Short Break. When you are ready to continue, indicate that with pressing any key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
vignette_break_key = keyboard.Keyboard()

# --- Initialize components for Routine "smid_instructions" ---
smid_instructions_text = visual.TextStim(win=win, name='smid_instructions_text',
    text='Thank you for answering the questions on the vignettes. The first part of the study is done.\n\nNext, we will present images. Please indicate whether these are moral, neutral or immoral.',
    font='Open Sans',
    pos=(0, .15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
smid_instructions_slider = visual.Slider(win=win, name='smid_instructions_slider',
    startValue=3, size=(0.8, 0.1), pos=(0, -.15), units=None,
    labels=("1\nMoral", 2, 3, 4, "5\nImmoral"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=True)
smid_instructions_key = keyboard.Keyboard()

# --- Initialize components for Routine "blank_500" ---
text_blank_500 = visual.TextStim(win=win, name='text_blank_500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "smid_cross" ---
smid_cross_cross = visual.ShapeStim(
    win=win, name='smid_cross_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "smid_stimulus" ---
smid_image = visual.ImageStim(
    win=win,
    name='smid_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "smid_rating" ---
smid_text = visual.TextStim(win=win, name='smid_text',
    text='The image portrayed something...',
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
smid_slider = visual.Slider(win=win, name='smid_slider',
    startValue=3, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nMoral", 2, 3, 4, "5\nImmoral"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)
smid_key = keyboard.Keyboard()

# --- Initialize components for Routine "smid_break" ---
smid_break_text = visual.TextStim(win=win, name='smid_break_text',
    text='Short Break. When you are ready to continue, indicate that with pressing any key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
smid_break_key = keyboard.Keyboard()

# --- Initialize components for Routine "clip_instructions" ---
clip_instructions_text = visual.TextStim(win=win, name='clip_instructions_text',
    text='Instructions\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "blank_500" ---
text_blank_500 = visual.TextStim(win=win, name='text_blank_500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "clip_stimulus" ---
newsclip = visual.MovieStim(
    win, name='newsclip',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=[1280,720], units='pix',
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)

# --- Initialize components for Routine "clip_rating" ---
clip_text = visual.TextStim(win=win, name='clip_text',
    text='I would share this clip by posting on social media (Facebook, Twitter, etc.)',
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
clip_slider = visual.Slider(win=win, name='clip_slider',
    startValue=3, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nNot at all", 2, 3, 4, "5\nVeryMuch"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)
clip_key = keyboard.Keyboard()

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
welcome_screenComponents = [welcome_text, welcome_key]
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
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
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
        text_blank_500.setAutoDraw(True)
    if text_blank_500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_blank_500.tStop = t  # not accounting for scr refresh
            text_blank_500.frameNStop = frameN  # exact frame index
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

# --- Prepare to start Routine "vignette_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
vignette_example_slider.reset()
vignette_instructions_key.keys = []
vignette_instructions_key.rt = []
_vignette_instructions_key_allKeys = []
# keep track of which components have finished
vignette_instructionsComponents = [vignette_instructions_1, vignette_example_slider, vignette_instructions_key, vignette_instructions_2]
for thisComponent in vignette_instructionsComponents:
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

# --- Run Routine "vignette_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *vignette_instructions_1* updates
    if vignette_instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        vignette_instructions_1.frameNStart = frameN  # exact frame index
        vignette_instructions_1.tStart = t  # local t and not account for scr refresh
        vignette_instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vignette_instructions_1, 'tStartRefresh')  # time at next scr refresh
        vignette_instructions_1.setAutoDraw(True)
    
    # *vignette_example_slider* updates
    if vignette_example_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        vignette_example_slider.frameNStart = frameN  # exact frame index
        vignette_example_slider.tStart = t  # local t and not account for scr refresh
        vignette_example_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vignette_example_slider, 'tStartRefresh')  # time at next scr refresh
        vignette_example_slider.setAutoDraw(True)
    
    # *vignette_instructions_key* updates
    waitOnFlip = False
    if vignette_instructions_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        vignette_instructions_key.frameNStart = frameN  # exact frame index
        vignette_instructions_key.tStart = t  # local t and not account for scr refresh
        vignette_instructions_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vignette_instructions_key, 'tStartRefresh')  # time at next scr refresh
        vignette_instructions_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(vignette_instructions_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(vignette_instructions_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if vignette_instructions_key.status == STARTED and not waitOnFlip:
        theseKeys = vignette_instructions_key.getKeys(keyList=['t'], waitRelease=False)
        _vignette_instructions_key_allKeys.extend(theseKeys)
        if len(_vignette_instructions_key_allKeys):
            vignette_instructions_key.keys = _vignette_instructions_key_allKeys[-1].name  # just the last key pressed
            vignette_instructions_key.rt = _vignette_instructions_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *vignette_instructions_2* updates
    if vignette_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        vignette_instructions_2.frameNStart = frameN  # exact frame index
        vignette_instructions_2.tStart = t  # local t and not account for scr refresh
        vignette_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vignette_instructions_2, 'tStartRefresh')  # time at next scr refresh
        vignette_instructions_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in vignette_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "vignette_instructions" ---
for thisComponent in vignette_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "vignette_instructions" was not non-slip safe, so reset the non-slip timer
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
        text_blank_500.setAutoDraw(True)
    if text_blank_500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_blank_500.tStop = t  # not accounting for scr refresh
            text_blank_500.frameNStop = frameN  # exact frame index
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
    trialList=data.importConditions("vig_text_"+ condition + ".xlsx", selection=np.random.choice(120,12,replace = False)),
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
    vignette.setText(vignette_text)
    vignette_slider.reset()
    # Run 'Begin Routine' code from vignette_response
    if vignette_slider.markerPos is None:
        # sets to our first position (or a random number?)
        # and makes marker visible
        vignette_slider.markerPos = 1
    
    vignette_keys.keys = []
    vignette_keys.rt = []
    _vignette_keys_allKeys = []
    # keep track of which components have finished
    vignette_stimulusComponents = [vignette, vignette_slider, vignette_keys]
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
        
        # *vignette* updates
        if vignette.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vignette.frameNStart = frameN  # exact frame index
            vignette.tStart = t  # local t and not account for scr refresh
            vignette.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vignette, 'tStartRefresh')  # time at next scr refresh
            vignette.setAutoDraw(True)
        if vignette.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vignette.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                vignette.tStop = t  # not accounting for scr refresh
                vignette.frameNStop = frameN  # exact frame index
                vignette.setAutoDraw(False)
        
        # *vignette_slider* updates
        if vignette_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vignette_slider.frameNStart = frameN  # exact frame index
            vignette_slider.tStart = t  # local t and not account for scr refresh
            vignette_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vignette_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'vignette_slider.started')
            vignette_slider.setAutoDraw(True)
        if vignette_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vignette_slider.tStartRefresh + 8.0-frameTolerance:
                # keep track of stop time/frame for later
                vignette_slider.tStop = t  # not accounting for scr refresh
                vignette_slider.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'vignette_slider.stopped')
                vignette_slider.setAutoDraw(False)
        # Run 'Each Frame' code from vignette_response
        keys = event.getKeys()
        
        if len(keys):
            if 'b' in keys:
                vignette_slider.markerPos -= 1
            elif 'g' in keys:
                vignette_slider.markerPos += 1 
                
        vignette_slider.rating = vignette_slider.markerPos
        
        # *vignette_keys* updates
        waitOnFlip = False
        if vignette_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vignette_keys.frameNStart = frameN  # exact frame index
            vignette_keys.tStart = t  # local t and not account for scr refresh
            vignette_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vignette_keys, 'tStartRefresh')  # time at next scr refresh
            vignette_keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(vignette_keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(vignette_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if vignette_keys.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vignette_keys.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                vignette_keys.tStop = t  # not accounting for scr refresh
                vignette_keys.frameNStop = frameN  # exact frame index
                vignette_keys.status = FINISHED
        if vignette_keys.status == STARTED and not waitOnFlip:
            theseKeys = vignette_keys.getKeys(keyList=['b', 'g'], waitRelease=False)
            _vignette_keys_allKeys.extend(theseKeys)
            if len(_vignette_keys_allKeys):
                vignette_keys.keys = [key.name for key in _vignette_keys_allKeys]  # storing all keys
                vignette_keys.rt = [key.rt for key in _vignette_keys_allKeys]
        
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
    vignette_trials.addData('vignette_slider.response', vignette_slider.getRating())
    # check responses
    if vignette_keys.keys in ['', [], None]:  # No response was made
        vignette_keys.keys = None
    vignette_trials.addData('vignette_keys.keys',vignette_keys.keys)
    if vignette_keys.keys != None:  # we had a response
        vignette_trials.addData('vignette_keys.rt', vignette_keys.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-8.000000)
    
    # --- Prepare to start Routine "vignette_blank" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from choice_duration
    duration_vignette_blank= np.random.choice([2,4,6])
    vignette_blank_text.setText('')
    # keep track of which components have finished
    vignette_blankComponents = [vignette_blank_text]
    for thisComponent in vignette_blankComponents:
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
    
    # --- Run Routine "vignette_blank" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vignette_blank_text* updates
        if vignette_blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vignette_blank_text.frameNStart = frameN  # exact frame index
            vignette_blank_text.tStart = t  # local t and not account for scr refresh
            vignette_blank_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vignette_blank_text, 'tStartRefresh')  # time at next scr refresh
            vignette_blank_text.setAutoDraw(True)
        if vignette_blank_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vignette_blank_text.tStartRefresh + duration_vignette_blank-frameTolerance:
                # keep track of stop time/frame for later
                vignette_blank_text.tStop = t  # not accounting for scr refresh
                vignette_blank_text.frameNStop = frameN  # exact frame index
                vignette_blank_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vignette_blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "vignette_blank" ---
    for thisComponent in vignette_blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "vignette_blank" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "vignette_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    vignette_break_key.keys = []
    vignette_break_key.rt = []
    _vignette_break_key_allKeys = []
    # keep track of which components have finished
    vignette_breakComponents = [vignette_break_text, vignette_break_key]
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
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from vignette_break_code
        if vignette_trials.thisN == 0 or vignette_trials.thisN == 12 or (vignette_trials.thisN + 1) % 4 != 0:
            continueRoutine = False
        
        # *vignette_break_text* updates
        if vignette_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vignette_break_text.frameNStart = frameN  # exact frame index
            vignette_break_text.tStart = t  # local t and not account for scr refresh
            vignette_break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vignette_break_text, 'tStartRefresh')  # time at next scr refresh
            vignette_break_text.setAutoDraw(True)
        if vignette_break_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vignette_break_text.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                vignette_break_text.tStop = t  # not accounting for scr refresh
                vignette_break_text.frameNStop = frameN  # exact frame index
                vignette_break_text.setAutoDraw(False)
        
        # *vignette_break_key* updates
        waitOnFlip = False
        if vignette_break_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vignette_break_key.frameNStart = frameN  # exact frame index
            vignette_break_key.tStart = t  # local t and not account for scr refresh
            vignette_break_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vignette_break_key, 'tStartRefresh')  # time at next scr refresh
            vignette_break_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(vignette_break_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(vignette_break_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if vignette_break_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vignette_break_key.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                vignette_break_key.tStop = t  # not accounting for scr refresh
                vignette_break_key.frameNStop = frameN  # exact frame index
                vignette_break_key.status = FINISHED
        if vignette_break_key.status == STARTED and not waitOnFlip:
            theseKeys = vignette_break_key.getKeys(keyList=["t"], waitRelease=False)
            _vignette_break_key_allKeys.extend(theseKeys)
            if len(_vignette_break_key_allKeys):
                vignette_break_key.keys = _vignette_break_key_allKeys[-1].name  # just the last key pressed
                vignette_break_key.rt = _vignette_break_key_allKeys[-1].rt
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'vignette_trials'


# --- Prepare to start Routine "smid_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
smid_instructions_slider.reset()
smid_instructions_key.keys = []
smid_instructions_key.rt = []
_smid_instructions_key_allKeys = []
# keep track of which components have finished
smid_instructionsComponents = [smid_instructions_text, smid_instructions_slider, smid_instructions_key]
for thisComponent in smid_instructionsComponents:
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

# --- Run Routine "smid_instructions" ---
while continueRoutine and routineTimer.getTime() < 30.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *smid_instructions_text* updates
    if smid_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        smid_instructions_text.frameNStart = frameN  # exact frame index
        smid_instructions_text.tStart = t  # local t and not account for scr refresh
        smid_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(smid_instructions_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'smid_instructions_text.started')
        smid_instructions_text.setAutoDraw(True)
    if smid_instructions_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > smid_instructions_text.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            smid_instructions_text.tStop = t  # not accounting for scr refresh
            smid_instructions_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smid_instructions_text.stopped')
            smid_instructions_text.setAutoDraw(False)
    
    # *smid_instructions_slider* updates
    if smid_instructions_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        smid_instructions_slider.frameNStart = frameN  # exact frame index
        smid_instructions_slider.tStart = t  # local t and not account for scr refresh
        smid_instructions_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(smid_instructions_slider, 'tStartRefresh')  # time at next scr refresh
        smid_instructions_slider.setAutoDraw(True)
    if smid_instructions_slider.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > smid_instructions_slider.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            smid_instructions_slider.tStop = t  # not accounting for scr refresh
            smid_instructions_slider.frameNStop = frameN  # exact frame index
            smid_instructions_slider.setAutoDraw(False)
    
    # *smid_instructions_key* updates
    waitOnFlip = False
    if smid_instructions_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        smid_instructions_key.frameNStart = frameN  # exact frame index
        smid_instructions_key.tStart = t  # local t and not account for scr refresh
        smid_instructions_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(smid_instructions_key, 'tStartRefresh')  # time at next scr refresh
        smid_instructions_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(smid_instructions_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(smid_instructions_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if smid_instructions_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > smid_instructions_key.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            smid_instructions_key.tStop = t  # not accounting for scr refresh
            smid_instructions_key.frameNStop = frameN  # exact frame index
            smid_instructions_key.status = FINISHED
    if smid_instructions_key.status == STARTED and not waitOnFlip:
        theseKeys = smid_instructions_key.getKeys(keyList=["t"], waitRelease=False)
        _smid_instructions_key_allKeys.extend(theseKeys)
        if len(_smid_instructions_key_allKeys):
            smid_instructions_key.keys = _smid_instructions_key_allKeys[-1].name  # just the last key pressed
            smid_instructions_key.rt = _smid_instructions_key_allKeys[-1].rt
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
    for thisComponent in smid_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "smid_instructions" ---
for thisComponent in smid_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-30.000000)

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
        text_blank_500.setAutoDraw(True)
    if text_blank_500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_blank_500.tStop = t  # not accounting for scr refresh
            text_blank_500.frameNStop = frameN  # exact frame index
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
smid_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('smid_stimuli.xlsx', selection=np.random.choice(120,12,replace = False)),
    seed=None, name='smid_trials')
thisExp.addLoop(smid_trials)  # add the loop to the experiment
thisSmid_trial = smid_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSmid_trial.rgb)
if thisSmid_trial != None:
    for paramName in thisSmid_trial:
        exec('{} = thisSmid_trial[paramName]'.format(paramName))

for thisSmid_trial in smid_trials:
    currentLoop = smid_trials
    # abbreviate parameter names if possible (e.g. rgb = thisSmid_trial.rgb)
    if thisSmid_trial != None:
        for paramName in thisSmid_trial:
            exec('{} = thisSmid_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "smid_cross" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from smid_cross_code
    duration_smid_cross = np.random.choice([2,4])
    # keep track of which components have finished
    smid_crossComponents = [smid_cross_cross]
    for thisComponent in smid_crossComponents:
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
    
    # --- Run Routine "smid_cross" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *smid_cross_cross* updates
        if smid_cross_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smid_cross_cross.frameNStart = frameN  # exact frame index
            smid_cross_cross.tStart = t  # local t and not account for scr refresh
            smid_cross_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smid_cross_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smid_cross_cross.started')
            smid_cross_cross.setAutoDraw(True)
        if smid_cross_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smid_cross_cross.tStartRefresh + duration_smid_cross-frameTolerance:
                # keep track of stop time/frame for later
                smid_cross_cross.tStop = t  # not accounting for scr refresh
                smid_cross_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'smid_cross_cross.stopped')
                smid_cross_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in smid_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "smid_cross" ---
    for thisComponent in smid_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "smid_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "smid_stimulus" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    smid_image.setImage(smid_name)
    # keep track of which components have finished
    smid_stimulusComponents = [smid_image]
    for thisComponent in smid_stimulusComponents:
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
    
    # --- Run Routine "smid_stimulus" ---
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
        for thisComponent in smid_stimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "smid_stimulus" ---
    for thisComponent in smid_stimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "smid_rating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    smid_slider.reset()
    # Run 'Begin Routine' code from smid_code
    if smid_slider.markerPos is None:
        # sets to our first position (or a random number?)
        # and makes marker visible
        smid_slider.markerPos = 2
    smid_key.keys = []
    smid_key.rt = []
    _smid_key_allKeys = []
    # keep track of which components have finished
    smid_ratingComponents = [smid_text, smid_slider, smid_key]
    for thisComponent in smid_ratingComponents:
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
    
    # --- Run Routine "smid_rating" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *smid_text* updates
        if smid_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smid_text.frameNStart = frameN  # exact frame index
            smid_text.tStart = t  # local t and not account for scr refresh
            smid_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smid_text, 'tStartRefresh')  # time at next scr refresh
            smid_text.setAutoDraw(True)
        if smid_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smid_text.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                smid_text.tStop = t  # not accounting for scr refresh
                smid_text.frameNStop = frameN  # exact frame index
                smid_text.setAutoDraw(False)
        
        # *smid_slider* updates
        if smid_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smid_slider.frameNStart = frameN  # exact frame index
            smid_slider.tStart = t  # local t and not account for scr refresh
            smid_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smid_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smid_slider.started')
            smid_slider.setAutoDraw(True)
        if smid_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smid_slider.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                smid_slider.tStop = t  # not accounting for scr refresh
                smid_slider.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'smid_slider.stopped')
                smid_slider.setAutoDraw(False)
        # Run 'Each Frame' code from smid_code
        keys = event.getKeys()
        
        if len(keys):
            if 'b' in keys:
                smid_slider.markerPos -= 1
            elif 'g' in keys:
                smid_slider.markerPos += 1 
                
        smid_slider.rating = smid_slider.markerPos
        
        # *smid_key* updates
        waitOnFlip = False
        if smid_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smid_key.frameNStart = frameN  # exact frame index
            smid_key.tStart = t  # local t and not account for scr refresh
            smid_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smid_key, 'tStartRefresh')  # time at next scr refresh
            smid_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(smid_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(smid_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if smid_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smid_key.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                smid_key.tStop = t  # not accounting for scr refresh
                smid_key.frameNStop = frameN  # exact frame index
                smid_key.status = FINISHED
        if smid_key.status == STARTED and not waitOnFlip:
            theseKeys = smid_key.getKeys(keyList=['b', 'g'], waitRelease=False)
            _smid_key_allKeys.extend(theseKeys)
            if len(_smid_key_allKeys):
                smid_key.keys = [key.name for key in _smid_key_allKeys]  # storing all keys
                smid_key.rt = [key.rt for key in _smid_key_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in smid_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "smid_rating" ---
    for thisComponent in smid_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    smid_trials.addData('smid_slider.response', smid_slider.getRating())
    # check responses
    if smid_key.keys in ['', [], None]:  # No response was made
        smid_key.keys = None
    smid_trials.addData('smid_key.keys',smid_key.keys)
    if smid_key.keys != None:  # we had a response
        smid_trials.addData('smid_key.rt', smid_key.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "smid_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    smid_break_key.keys = []
    smid_break_key.rt = []
    _smid_break_key_allKeys = []
    # keep track of which components have finished
    smid_breakComponents = [smid_break_text, smid_break_key]
    for thisComponent in smid_breakComponents:
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
    
    # --- Run Routine "smid_break" ---
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from smid_break_code
        if smid_trials.thisN == 0 or smid_trials.thisN == 12 or (smid_trials.thisN + 1) % 3 != 0:
            continueRoutine = False
        
        # *smid_break_text* updates
        if smid_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smid_break_text.frameNStart = frameN  # exact frame index
            smid_break_text.tStart = t  # local t and not account for scr refresh
            smid_break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smid_break_text, 'tStartRefresh')  # time at next scr refresh
            smid_break_text.setAutoDraw(True)
        if smid_break_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smid_break_text.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                smid_break_text.tStop = t  # not accounting for scr refresh
                smid_break_text.frameNStop = frameN  # exact frame index
                smid_break_text.setAutoDraw(False)
        
        # *smid_break_key* updates
        waitOnFlip = False
        if smid_break_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smid_break_key.frameNStart = frameN  # exact frame index
            smid_break_key.tStart = t  # local t and not account for scr refresh
            smid_break_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smid_break_key, 'tStartRefresh')  # time at next scr refresh
            smid_break_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(smid_break_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(smid_break_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if smid_break_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smid_break_key.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                smid_break_key.tStop = t  # not accounting for scr refresh
                smid_break_key.frameNStop = frameN  # exact frame index
                smid_break_key.status = FINISHED
        if smid_break_key.status == STARTED and not waitOnFlip:
            theseKeys = smid_break_key.getKeys(keyList=["t"], waitRelease=False)
            _smid_break_key_allKeys.extend(theseKeys)
            if len(_smid_break_key_allKeys):
                smid_break_key.keys = _smid_break_key_allKeys[-1].name  # just the last key pressed
                smid_break_key.rt = _smid_break_key_allKeys[-1].rt
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
        for thisComponent in smid_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "smid_break" ---
    for thisComponent in smid_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'smid_trials'


# --- Prepare to start Routine "clip_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
clip_instructionsComponents = [clip_instructions_text]
for thisComponent in clip_instructionsComponents:
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

# --- Run Routine "clip_instructions" ---
while continueRoutine and routineTimer.getTime() < 6.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *clip_instructions_text* updates
    if clip_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        clip_instructions_text.frameNStart = frameN  # exact frame index
        clip_instructions_text.tStart = t  # local t and not account for scr refresh
        clip_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(clip_instructions_text, 'tStartRefresh')  # time at next scr refresh
        clip_instructions_text.setAutoDraw(True)
    if clip_instructions_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > clip_instructions_text.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            clip_instructions_text.tStop = t  # not accounting for scr refresh
            clip_instructions_text.frameNStop = frameN  # exact frame index
            clip_instructions_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clip_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "clip_instructions" ---
for thisComponent in clip_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-6.000000)

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
        text_blank_500.setAutoDraw(True)
    if text_blank_500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank_500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_blank_500.tStop = t  # not accounting for scr refresh
            text_blank_500.frameNStop = frameN  # exact frame index
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
clip_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('clips_stimuli.xlsx', selection='np.random.choice(3,3) + [0, 3, 6]'),
    seed=None, name='clip_trials')
thisExp.addLoop(clip_trials)  # add the loop to the experiment
thisClip_trial = clip_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisClip_trial.rgb)
if thisClip_trial != None:
    for paramName in thisClip_trial:
        exec('{} = thisClip_trial[paramName]'.format(paramName))

for thisClip_trial in clip_trials:
    currentLoop = clip_trials
    # abbreviate parameter names if possible (e.g. rgb = thisClip_trial.rgb)
    if thisClip_trial != None:
        for paramName in thisClip_trial:
            exec('{} = thisClip_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "clip_stimulus" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    newsclip.setMovie(clip_name)
    # keep track of which components have finished
    clip_stimulusComponents = [newsclip]
    for thisComponent in clip_stimulusComponents:
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
    
    # --- Run Routine "clip_stimulus" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *newsclip* updates
        if newsclip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            newsclip.frameNStart = frameN  # exact frame index
            newsclip.tStart = t  # local t and not account for scr refresh
            newsclip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(newsclip, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'newsclip.started')
            newsclip.setAutoDraw(True)
            newsclip.play()
        if newsclip.status == FINISHED:  # force-end the routine
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in clip_stimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "clip_stimulus" ---
    for thisComponent in clip_stimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    newsclip.stop()
    # the Routine "clip_stimulus" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "clip_rating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    clip_slider.reset()
    # Run 'Begin Routine' code from clip_code
    if clip_slider.markerPos is None:
        # sets to our first position (or a random number?)
        # and makes marker visible
        clip_slider.markerPos = 2
    clip_key.keys = []
    clip_key.rt = []
    _clip_key_allKeys = []
    # keep track of which components have finished
    clip_ratingComponents = [clip_text, clip_slider, clip_key]
    for thisComponent in clip_ratingComponents:
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
    
    # --- Run Routine "clip_rating" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *clip_text* updates
        if clip_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clip_text.frameNStart = frameN  # exact frame index
            clip_text.tStart = t  # local t and not account for scr refresh
            clip_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clip_text, 'tStartRefresh')  # time at next scr refresh
            clip_text.setAutoDraw(True)
        if clip_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clip_text.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                clip_text.tStop = t  # not accounting for scr refresh
                clip_text.frameNStop = frameN  # exact frame index
                clip_text.setAutoDraw(False)
        
        # *clip_slider* updates
        if clip_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clip_slider.frameNStart = frameN  # exact frame index
            clip_slider.tStart = t  # local t and not account for scr refresh
            clip_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clip_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'clip_slider.started')
            clip_slider.setAutoDraw(True)
        if clip_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clip_slider.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                clip_slider.tStop = t  # not accounting for scr refresh
                clip_slider.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'clip_slider.stopped')
                clip_slider.setAutoDraw(False)
        # Run 'Each Frame' code from clip_code
        keys = event.getKeys()
        
        if len(keys):
            if 'b' in keys:
                clip_slider.markerPos -= 1
            elif 'g' in keys:
                clip_slider.markerPos += 1 
                
        clip_slider.rating= clip_slider.markerPos
        
        # *clip_key* updates
        waitOnFlip = False
        if clip_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clip_key.frameNStart = frameN  # exact frame index
            clip_key.tStart = t  # local t and not account for scr refresh
            clip_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clip_key, 'tStartRefresh')  # time at next scr refresh
            clip_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(clip_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(clip_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if clip_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clip_key.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                clip_key.tStop = t  # not accounting for scr refresh
                clip_key.frameNStop = frameN  # exact frame index
                clip_key.status = FINISHED
        if clip_key.status == STARTED and not waitOnFlip:
            theseKeys = clip_key.getKeys(keyList=['b', 'g'], waitRelease=False)
            _clip_key_allKeys.extend(theseKeys)
            if len(_clip_key_allKeys):
                clip_key.keys = [key.name for key in _clip_key_allKeys]  # storing all keys
                clip_key.rt = [key.rt for key in _clip_key_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in clip_ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "clip_rating" ---
    for thisComponent in clip_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    clip_trials.addData('clip_slider.response', clip_slider.getRating())
    # check responses
    if clip_key.keys in ['', [], None]:  # No response was made
        clip_key.keys = None
    clip_trials.addData('clip_key.keys',clip_key.keys)
    if clip_key.keys != None:  # we had a response
        clip_trials.addData('clip_key.rt', clip_key.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'clip_trials'


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
