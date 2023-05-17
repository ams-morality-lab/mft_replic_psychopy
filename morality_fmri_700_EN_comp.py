#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Wed May 17 21:06:01 2023
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

# Run 'Before Experiment' code from smid_pseudoRand_fun
def smid_pseudoRand(excelFile):
    import numpy as np

# Initializing base  variables
    oldSMIDorder = data.importConditions(excelFile)
    smid_domains = ['Neutral', 'Purity-Degradation', 'Loyalty-Betrayal',
    'Authority-Subversion', 'Care-Harm','Fairness-Cheating']
    items_per_smid_domain = 5

# Create a dictionary to store the items for each smid_domain
    smid_domain_items = {smid_domain: [] for smid_domain in smid_domains}

# Assign each dictionary to its respective smid_domain
    for item in oldSMIDorder:
        smid_domain = item['smid_moral_domain']
        smid_domain_items[smid_domain].append(item)

# Shuffle the dictionaries within each smid_domain
    for smid_domain in smid_domains:
        np.random.shuffle(smid_domain_items[smid_domain])

# Create 4 smid_smid_groups and assign dictionaries to each smid_group
    smid_smid_groups = [[] for _ in range(4)]
    for smid_domain in smid_domains:
        smid_domain_items_list = smid_domain_items[smid_domain]
        for i in range(4):
            smid_group = smid_smid_groups[i]
            smid_group.extend(smid_domain_items_list[i * items_per_smid_domain: (i + 1) * items_per_smid_domain])
            np.random.shuffle(smid_group)

    new_SMID_file = list(dictionary for smid_group in smid_smid_groups for dictionary in smid_group)

# Create and return new order
    new_SMID_order = []
    for row in range(len(new_SMID_file)):
        new_SMID_order.append(new_SMID_file[row]["smid_id"]) #Name of the original index column
    return new_SMID_order



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'moral_judgements_fMRI'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
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
    originPath='/Users/benjaminjargow/Documents/01_ResMas/Internship/Paradigm/morality_fmri_700_EN_comp.py',
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

# --- Initialize components for Routine "vignette_instructions" ---
vignette_instructions_1 = visual.TextStim(win=win, name='vignette_instructions_1',
    text="You are about to see a series of sentences. \nImagine yourself as a witness to the actions in each one.\nPlease rate how MORALLY WRONG each action was, using a 4-point scale ranging from ",
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
vignette_example_slider = visual.Slider(win=win, name='vignette_example_slider',
    startValue=None, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nNot morally wrong", "2", "3", "4\nExtremely morally wrong"), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=True)
vignette_instructions_key = keyboard.Keyboard()
vignette_instructions_2 = visual.TextStim(win=win, name='vignette_instructions_2',
    text='Please use your right hand for the ratings. Each of your fingers equals one scale point (pointer = 1, middle finger = 2, ring finger = 3 and little finger = 4).\n\nPlease try it. ',
    font='Open Sans',
    pos=(0, -.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
# Set experiment start values for variable component TR
TR = .72
TRContainer = []

# --- Initialize components for Routine "tail" ---
tail_cross = visual.ShapeStim(
    win=win, name='tail_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

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
    labels=("1\nNot morally wrong",2,3, "4\nExtremely morally wrong"), ticks=(1, 2, 3, 4), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)
# Run 'Begin Experiment' code from vignette_response
def v_pseudoRand(excelFile):
    import numpy as np
    # Load older order, define categories, number of items
    oldOrder=data.importConditions(excelFile)
    categories = ['auth', 'carem', 'carep', 'fair', 'lib', 'loy', 'pur', 'socn']
    items_per_category = 5

    # Create a dictionary to store the items for each category
    category_items = {category: [] for category in categories}

    # Assign each dictionary to its respective category
    for item in oldOrder:
        category = item['category']
        category_items[category].append(item)

    # Shuffle the dictionaries within each category
    for category in categories:
        np.random.shuffle(category_items[category])

    # Create 3 groups and assign dictionaries to each group
    groups = [[] for _ in range(3)]
    for category in categories:
        category_items_list = category_items[category]
        for i in range(3):
            group = groups[i]
            group.extend(category_items_list[i * items_per_category: (i + 1) * items_per_category])
            np.random.shuffle(group)

    newFile = list(dictionary for group in groups for dictionary in group)
    newOrder = []
    for row in range(len(newFile)):
        newOrder.append(newFile[row]["number"]) #Name of the original index column
    return newOrder
vignette_keys = keyboard.Keyboard()

# --- Initialize components for Routine "vignette_blank" ---
vignette_blank_text = visual.TextStim(win=win, name='vignette_blank_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
blank_cross = visual.ShapeStim(
    win=win, name='blank_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "vignette_break" ---
vignette_break_text = visual.TextStim(win=win, name='vignette_break_text',
    text='Waiting to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
vignette_break_key = keyboard.Keyboard()
vignette_cross = visual.ShapeStim(
    win=win, name='vignette_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "tail_vignette_break" ---
cross_vignette_trials = visual.ShapeStim(
    win=win, name='cross_vignette_trials', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "clip_instructions" ---
clip_instructions_text = visual.TextStim(win=win, name='clip_instructions_text',
    text="Now you will see three news clips about different topics. After viewing each clip, please indicate whether the clip depicted something moral or immoral using a 5-point scale ranging from 'Moral' to 'Immoral'. Afterwards we ask you whether you would share the clip on a 5-point scale from 'Not at All' to 'Very Much'.",
    font='Open Sans',
    pos=(0, .15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
clip_instructions_slider = visual.Slider(win=win, name='clip_instructions_slider',
    startValue=None, size=(0.8, 0.1), pos=(0, -.15), units=None,
    labels=("1\nMoral", 2, 3, 4, "5\nImmoral"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)
key_resp = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Please use your right hand for the ratings. With the index finger, you can move the slider to the left. With the middle finger, you can indicate a neutral stance and with the ring finger you can move the slider to the right.\n\nTry it.',
    font='Open Sans',
    pos=(0, -.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "tail" ---
tail_cross = visual.ShapeStim(
    win=win, name='tail_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "clip_stimulus" ---
newsclip = visual.MovieStim(
    win, name='newsclip',
    filename=None, movieLib='ffpyplayer',
    loop=False, volume=1.0,
    pos=(0, 0), size=[1280,720], units='pix',
    ori=0.0, anchor='center',opacity=None, contrast=1.0,
)

# --- Initialize components for Routine "clip_moral" ---
cli_moral_text = visual.TextStim(win=win, name='cli_moral_text',
    text='The clip displayed something...',
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
clip_moral_slider = visual.Slider(win=win, name='clip_moral_slider',
    startValue=None, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nMoral", 2, 3, 4, "5\nImmoral"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)
clip_moral_key = keyboard.Keyboard()

# --- Initialize components for Routine "clip_sharing" ---
clip_sharing_text = visual.TextStim(win=win, name='clip_sharing_text',
    text='I would share this clip by posting on social media (Facebook, Twitter, etc.)...',
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
clip_sharing_slider = visual.Slider(win=win, name='clip_sharing_slider',
    startValue=None, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nNot At All", 2, 3, 4, "5\nVery Much"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)
clip_sharing_key = keyboard.Keyboard()

# --- Initialize components for Routine "smid_instructions" ---
smid_instructions_text = visual.TextStim(win=win, name='smid_instructions_text',
    text='You are about to see a series of photos. Imagine yourself as a witness to the scenes in each one.\n\nAfter viewing the image, please rate whether it portrays something IMMORAL/BLAMEWORTHY - MORAL/PRAISEWORTHY, using a 5-point scale ranging from:',
    font='Open Sans',
    pos=(0, .20), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
smid_instructions_slider = visual.Slider(win=win, name='smid_instructions_slider',
    startValue=None, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nMORAL", 2, 3, 4, "5\nIMMORAL"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=True)
smid_instructions_key = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Please use your right hand for the ratings. With the index finger, you can move the slider to the left. With the middle finger, you can indicate a neutral stance and with the ring finger you can move the slider to the right.\n\nTry it.',
    font='Open Sans',
    pos=(0, -.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "tail" ---
tail_cross = visual.ShapeStim(
    win=win, name='tail_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "smid_cross" ---
smid_cross_cross = visual.ShapeStim(
    win=win, name='smid_cross_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

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
    text='This image depicts something...\n',
    font='Open Sans',
    pos=(0, .2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
smid_slider = visual.Slider(win=win, name='smid_slider',
    startValue=None, size=(0.8, 0.1), pos=(0, -.05), units=None,
    labels=("1\nMORAL", 2, 3, 4, "5\nIMMORAL"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)
smid_key = keyboard.Keyboard()

# --- Initialize components for Routine "smid_break" ---
smid_break_text = visual.TextStim(win=win, name='smid_break_text',
    text='Waiting to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
smid_break_key = keyboard.Keyboard()
smid_break_cross = visual.ShapeStim(
    win=win, name='smid_break_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "tail_smid_break" ---
cross_tail_smid = visual.ShapeStim(
    win=win, name='cross_tail_smid', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "end_note" ---
end_note_text = visual.TextStim(win=win, name='end_note_text',
    text='Thank you for your participation in the study. Please wait, we will help you out of the scanner.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_note_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

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
    # Run 'Each Frame' code from code
    keys = event.getKeys()
    
    if len(keys):
        if 'h' in keys:
            vignette_example_slider.markerPos = 1
        elif 'j' in keys:
            vignette_example_slider.markerPos = 2
        elif 'k' in keys:
            vignette_example_slider.markerPos = 3 
        elif 'l' in keys:   
            vignette_example_slider.markerPos = 4
    
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

# --- Prepare to start Routine "tail" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
tailComponents = [tail_cross]
for thisComponent in tailComponents:
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

# --- Run Routine "tail" ---
while continueRoutine and routineTimer.getTime() < 7.92:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tail_cross* updates
    if tail_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tail_cross.frameNStart = frameN  # exact frame index
        tail_cross.tStart = t  # local t and not account for scr refresh
        tail_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tail_cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tail_cross.started')
        tail_cross.setAutoDraw(True)
    if tail_cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tail_cross.tStartRefresh + 7.92-frameTolerance:
            # keep track of stop time/frame for later
            tail_cross.tStop = t  # not accounting for scr refresh
            tail_cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tail_cross.stopped')
            tail_cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in tailComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "tail" ---
for thisComponent in tailComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-7.920000)

# set up handler to look after randomisation of conditions etc
vignette_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vig_text_english_dutch.xlsx', selection=v_pseudoRand("vig_text_english_dutch.xlsx")),
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
    vignette.setText(english_vignette)
    vignette_slider.reset()
    # Run 'Begin Routine' code from vignette_response
    keys = []
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
    while continueRoutine:
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
            if tThisFlipGlobal > vignette.tStartRefresh + 11*TR-frameTolerance:
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
            if tThisFlipGlobal > vignette_slider.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                vignette_slider.tStop = t  # not accounting for scr refresh
                vignette_slider.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'vignette_slider.stopped')
                vignette_slider.setAutoDraw(False)
        # Run 'Each Frame' code from vignette_response
        keys = event.getKeys()
        
        if len(keys):
            if 'h' in keys:
                vignette_slider.markerPos = 1
            elif 'j' in keys:
                vignette_slider.markerPos = 2
            elif 'k' in keys:
                vignette_slider.markerPos = 3 
            elif 'l' in keys:   
                vignette_slider.markerPos = 4
        
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
            if tThisFlipGlobal > vignette_keys.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                vignette_keys.tStop = t  # not accounting for scr refresh
                vignette_keys.frameNStop = frameN  # exact frame index
                vignette_keys.status = FINISHED
        if vignette_keys.status == STARTED and not waitOnFlip:
            theseKeys = vignette_keys.getKeys(keyList=['h', 'j', 'k', 'l'], waitRelease=False)
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
    # the Routine "vignette_stimulus" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "vignette_blank" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from choice_duration
    duration_vignette_blank= np.random.choice([2*TR,4*TR,6*TR])
    vignette_blank_text.setText('')
    # keep track of which components have finished
    vignette_blankComponents = [vignette_blank_text, blank_cross]
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
        
        # *blank_cross* updates
        if blank_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_cross.frameNStart = frameN  # exact frame index
            blank_cross.tStart = t  # local t and not account for scr refresh
            blank_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_cross.started')
            blank_cross.setAutoDraw(True)
        if blank_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_cross.tStartRefresh + duration_vignette_blank-frameTolerance:
                # keep track of stop time/frame for later
                blank_cross.tStop = t  # not accounting for scr refresh
                blank_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_cross.stopped')
                blank_cross.setAutoDraw(False)
        
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
    vignette_breakComponents = [vignette_break_text, vignette_break_key, vignette_cross]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from vignette_break_code
        if vignette_trials.thisN == 0 or vignette_trials.thisN == 119 or (vignette_trials.thisN + 1) % 40 != 0:
            continueRoutine = False
        
        # *vignette_break_text* updates
        if vignette_break_text.status == NOT_STARTED and tThisFlip >= 11*TR-frameTolerance:
            # keep track of start time/frame for later
            vignette_break_text.frameNStart = frameN  # exact frame index
            vignette_break_text.tStart = t  # local t and not account for scr refresh
            vignette_break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vignette_break_text, 'tStartRefresh')  # time at next scr refresh
            vignette_break_text.setAutoDraw(True)
        
        # *vignette_break_key* updates
        waitOnFlip = False
        if vignette_break_key.status == NOT_STARTED and tThisFlip >= 11*TR-frameTolerance:
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
        if vignette_break_key.status == STARTED and not waitOnFlip:
            theseKeys = vignette_break_key.getKeys(keyList=["t"], waitRelease=False)
            _vignette_break_key_allKeys.extend(theseKeys)
            if len(_vignette_break_key_allKeys):
                vignette_break_key.keys = _vignette_break_key_allKeys[-1].name  # just the last key pressed
                vignette_break_key.rt = _vignette_break_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *vignette_cross* updates
        if vignette_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vignette_cross.frameNStart = frameN  # exact frame index
            vignette_cross.tStart = t  # local t and not account for scr refresh
            vignette_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vignette_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'vignette_cross.started')
            vignette_cross.setAutoDraw(True)
        if vignette_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vignette_cross.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                vignette_cross.tStop = t  # not accounting for scr refresh
                vignette_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'vignette_cross.stopped')
                vignette_cross.setAutoDraw(False)
        
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
    # the Routine "vignette_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "tail_vignette_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    tail_vignette_breakComponents = [cross_vignette_trials]
    for thisComponent in tail_vignette_breakComponents:
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
    
    # --- Run Routine "tail_vignette_break" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_3
        if vignette_trials.thisN == 0 or vignette_trials.thisN == 119 or (vignette_trials.thisN + 1) % 40 != 0:
            continueRoutine = False
        
        # *cross_vignette_trials* updates
        if cross_vignette_trials.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_vignette_trials.frameNStart = frameN  # exact frame index
            cross_vignette_trials.tStart = t  # local t and not account for scr refresh
            cross_vignette_trials.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_vignette_trials, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_vignette_trials.started')
            cross_vignette_trials.setAutoDraw(True)
        if cross_vignette_trials.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_vignette_trials.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                cross_vignette_trials.tStop = t  # not accounting for scr refresh
                cross_vignette_trials.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_vignette_trials.stopped')
                cross_vignette_trials.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tail_vignette_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tail_vignette_break" ---
    for thisComponent in tail_vignette_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "tail_vignette_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'vignette_trials'


# --- Prepare to start Routine "clip_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
clip_instructions_slider.reset()
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
clip_instructionsComponents = [clip_instructions_text, clip_instructions_slider, key_resp, text_3]
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
while continueRoutine:
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
    
    # *clip_instructions_slider* updates
    if clip_instructions_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        clip_instructions_slider.frameNStart = frameN  # exact frame index
        clip_instructions_slider.tStart = t  # local t and not account for scr refresh
        clip_instructions_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(clip_instructions_slider, 'tStartRefresh')  # time at next scr refresh
        clip_instructions_slider.setAutoDraw(True)
    # Run 'Each Frame' code from clip_instructions_code
    keys = event.getKeys()
    
    if len(keys):
        if 'h' in keys:
            if clip_instructions_slider.markerPos == None:
                clip_instructions_slider.markerPos = 2
            else: clip_instructions_slider.markerPos -= 1
        if 'j' in keys:
            clip_instructions_slider.markerPos = 3
        elif 'k' in keys:
            if clip_instructions_slider.markerPos == None:
                clip_instructions_slider.markerPos = 4
            else: clip_instructions_slider.markerPos += 1 
    
    
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
        theseKeys = key_resp.getKeys(keyList=['t'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "clip_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
    
    # --- Prepare to start Routine "tail" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    tailComponents = [tail_cross]
    for thisComponent in tailComponents:
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
    
    # --- Run Routine "tail" ---
    while continueRoutine and routineTimer.getTime() < 7.92:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tail_cross* updates
        if tail_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tail_cross.frameNStart = frameN  # exact frame index
            tail_cross.tStart = t  # local t and not account for scr refresh
            tail_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tail_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tail_cross.started')
            tail_cross.setAutoDraw(True)
        if tail_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tail_cross.tStartRefresh + 7.92-frameTolerance:
                # keep track of stop time/frame for later
                tail_cross.tStop = t  # not accounting for scr refresh
                tail_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tail_cross.stopped')
                tail_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tailComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tail" ---
    for thisComponent in tailComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.920000)
    
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
    
    # --- Prepare to start Routine "clip_moral" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    clip_moral_slider.reset()
    clip_moral_key.keys = []
    clip_moral_key.rt = []
    _clip_moral_key_allKeys = []
    # keep track of which components have finished
    clip_moralComponents = [cli_moral_text, clip_moral_slider, clip_moral_key]
    for thisComponent in clip_moralComponents:
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
    
    # --- Run Routine "clip_moral" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cli_moral_text* updates
        if cli_moral_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cli_moral_text.frameNStart = frameN  # exact frame index
            cli_moral_text.tStart = t  # local t and not account for scr refresh
            cli_moral_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cli_moral_text, 'tStartRefresh')  # time at next scr refresh
            cli_moral_text.setAutoDraw(True)
        if cli_moral_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cli_moral_text.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                cli_moral_text.tStop = t  # not accounting for scr refresh
                cli_moral_text.frameNStop = frameN  # exact frame index
                cli_moral_text.setAutoDraw(False)
        
        # *clip_moral_slider* updates
        if clip_moral_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clip_moral_slider.frameNStart = frameN  # exact frame index
            clip_moral_slider.tStart = t  # local t and not account for scr refresh
            clip_moral_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clip_moral_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'clip_moral_slider.started')
            clip_moral_slider.setAutoDraw(True)
        if clip_moral_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clip_moral_slider.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                clip_moral_slider.tStop = t  # not accounting for scr refresh
                clip_moral_slider.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'clip_moral_slider.stopped')
                clip_moral_slider.setAutoDraw(False)
        # Run 'Each Frame' code from clip_moral_code
        keys = event.getKeys()
        
        if len(keys):
            if 'h' in keys:
                if clip_moral_slider.markerPos == None:
                    clip_moral_slider.markerPos = 2
                else:
                    clip_moral_slider.markerPos -= 1
            if 'j' in keys:
                clip_moral_slider.markerPos = 3
            elif 'k' in keys:
                if clip_moral_slider.markerPos == None:
                    clip_moral_slider.markerPos = 4
                else:
                    clip_moral_slider.markerPos += 1
        
        clip_moral_slider.rating = clip_moral_slider.markerPos
        
        # *clip_moral_key* updates
        waitOnFlip = False
        if clip_moral_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clip_moral_key.frameNStart = frameN  # exact frame index
            clip_moral_key.tStart = t  # local t and not account for scr refresh
            clip_moral_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clip_moral_key, 'tStartRefresh')  # time at next scr refresh
            clip_moral_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(clip_moral_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(clip_moral_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if clip_moral_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clip_moral_key.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                clip_moral_key.tStop = t  # not accounting for scr refresh
                clip_moral_key.frameNStop = frameN  # exact frame index
                clip_moral_key.status = FINISHED
        if clip_moral_key.status == STARTED and not waitOnFlip:
            theseKeys = clip_moral_key.getKeys(keyList=['h', 'j','k'], waitRelease=False)
            _clip_moral_key_allKeys.extend(theseKeys)
            if len(_clip_moral_key_allKeys):
                clip_moral_key.keys = [key.name for key in _clip_moral_key_allKeys]  # storing all keys
                clip_moral_key.rt = [key.rt for key in _clip_moral_key_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in clip_moralComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "clip_moral" ---
    for thisComponent in clip_moralComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    clip_trials.addData('clip_moral_slider.response', clip_moral_slider.getRating())
    # check responses
    if clip_moral_key.keys in ['', [], None]:  # No response was made
        clip_moral_key.keys = None
    clip_trials.addData('clip_moral_key.keys',clip_moral_key.keys)
    if clip_moral_key.keys != None:  # we had a response
        clip_trials.addData('clip_moral_key.rt', clip_moral_key.rt)
    # the Routine "clip_moral" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "clip_sharing" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    clip_sharing_slider.reset()
    clip_sharing_key.keys = []
    clip_sharing_key.rt = []
    _clip_sharing_key_allKeys = []
    # keep track of which components have finished
    clip_sharingComponents = [clip_sharing_text, clip_sharing_slider, clip_sharing_key]
    for thisComponent in clip_sharingComponents:
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
    
    # --- Run Routine "clip_sharing" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *clip_sharing_text* updates
        if clip_sharing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clip_sharing_text.frameNStart = frameN  # exact frame index
            clip_sharing_text.tStart = t  # local t and not account for scr refresh
            clip_sharing_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clip_sharing_text, 'tStartRefresh')  # time at next scr refresh
            clip_sharing_text.setAutoDraw(True)
        if clip_sharing_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clip_sharing_text.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                clip_sharing_text.tStop = t  # not accounting for scr refresh
                clip_sharing_text.frameNStop = frameN  # exact frame index
                clip_sharing_text.setAutoDraw(False)
        
        # *clip_sharing_slider* updates
        if clip_sharing_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clip_sharing_slider.frameNStart = frameN  # exact frame index
            clip_sharing_slider.tStart = t  # local t and not account for scr refresh
            clip_sharing_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clip_sharing_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'clip_sharing_slider.started')
            clip_sharing_slider.setAutoDraw(True)
        if clip_sharing_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clip_sharing_slider.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                clip_sharing_slider.tStop = t  # not accounting for scr refresh
                clip_sharing_slider.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'clip_sharing_slider.stopped')
                clip_sharing_slider.setAutoDraw(False)
        # Run 'Each Frame' code from clip_sharing_code
        keys = event.getKeys()
        
        if len(keys):
            if 'h' in keys:
                if clip_sharing_slider.markerPos == None:
                    clip_sharing_slider.markerPos = 2
                else:
                    clip_sharing_slider.markerPos -= 1
            if 'j' in keys:
                clip_sharing_slider.markerPos = 3
            elif 'k' in keys:
                if clip_sharing_slider.markerPos == None:
                    clip_sharing_slider.markerPos = 4
                else:
                    clip_sharing_slider.markerPos += 1
        
        clip_sharing_slider.rating = clip_sharing_slider.markerPos
        
        # *clip_sharing_key* updates
        waitOnFlip = False
        if clip_sharing_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clip_sharing_key.frameNStart = frameN  # exact frame index
            clip_sharing_key.tStart = t  # local t and not account for scr refresh
            clip_sharing_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clip_sharing_key, 'tStartRefresh')  # time at next scr refresh
            clip_sharing_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(clip_sharing_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(clip_sharing_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if clip_sharing_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clip_sharing_key.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                clip_sharing_key.tStop = t  # not accounting for scr refresh
                clip_sharing_key.frameNStop = frameN  # exact frame index
                clip_sharing_key.status = FINISHED
        if clip_sharing_key.status == STARTED and not waitOnFlip:
            theseKeys = clip_sharing_key.getKeys(keyList=['h', 'j','k'], waitRelease=False)
            _clip_sharing_key_allKeys.extend(theseKeys)
            if len(_clip_sharing_key_allKeys):
                clip_sharing_key.keys = [key.name for key in _clip_sharing_key_allKeys]  # storing all keys
                clip_sharing_key.rt = [key.rt for key in _clip_sharing_key_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in clip_sharingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "clip_sharing" ---
    for thisComponent in clip_sharingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    clip_trials.addData('clip_sharing_slider.response', clip_sharing_slider.getRating())
    # check responses
    if clip_sharing_key.keys in ['', [], None]:  # No response was made
        clip_sharing_key.keys = None
    clip_trials.addData('clip_sharing_key.keys',clip_sharing_key.keys)
    if clip_sharing_key.keys != None:  # we had a response
        clip_trials.addData('clip_sharing_key.rt', clip_sharing_key.rt)
    # the Routine "clip_sharing" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'clip_trials'


# --- Prepare to start Routine "smid_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
smid_instructions_slider.reset()
smid_instructions_key.keys = []
smid_instructions_key.rt = []
_smid_instructions_key_allKeys = []
# keep track of which components have finished
smid_instructionsComponents = [smid_instructions_text, smid_instructions_slider, smid_instructions_key, text_2]
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
while continueRoutine:
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
    
    # *smid_instructions_slider* updates
    if smid_instructions_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        smid_instructions_slider.frameNStart = frameN  # exact frame index
        smid_instructions_slider.tStart = t  # local t and not account for scr refresh
        smid_instructions_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(smid_instructions_slider, 'tStartRefresh')  # time at next scr refresh
        smid_instructions_slider.setAutoDraw(True)
    
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
    if smid_instructions_key.status == STARTED and not waitOnFlip:
        theseKeys = smid_instructions_key.getKeys(keyList=["t"], waitRelease=False)
        _smid_instructions_key_allKeys.extend(theseKeys)
        if len(_smid_instructions_key_allKeys):
            smid_instructions_key.keys = _smid_instructions_key_allKeys[-1].name  # just the last key pressed
            smid_instructions_key.rt = _smid_instructions_key_allKeys[-1].rt
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
    # Run 'Each Frame' code from code_2
    keys = event.getKeys()
    
    if len(keys):
        if 'h' in keys:
            if smid_instructions_slider.markerPos == None:
                smid_instructions_slider.markerPos = 2
            else: smid_instructions_slider.markerPos -= 1
        if 'j' in keys:
            smid_instructions_slider.markerPos = 3
        elif 'k' in keys:
            if smid_instructions_slider.markerPos == None:
                smid_instructions_slider.markerPos = 4
            else: smid_instructions_slider.markerPos += 1
    
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
# the Routine "smid_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "tail" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
tailComponents = [tail_cross]
for thisComponent in tailComponents:
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

# --- Run Routine "tail" ---
while continueRoutine and routineTimer.getTime() < 7.92:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tail_cross* updates
    if tail_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tail_cross.frameNStart = frameN  # exact frame index
        tail_cross.tStart = t  # local t and not account for scr refresh
        tail_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tail_cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tail_cross.started')
        tail_cross.setAutoDraw(True)
    if tail_cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tail_cross.tStartRefresh + 7.92-frameTolerance:
            # keep track of stop time/frame for later
            tail_cross.tStop = t  # not accounting for scr refresh
            tail_cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tail_cross.stopped')
            tail_cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in tailComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "tail" ---
for thisComponent in tailComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-7.920000)

# set up handler to look after randomisation of conditions etc
smid_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('smid_stimuli.xlsx', selection=smid_pseudoRand("smid_stimuli.xlsx")),
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
            if tThisFlipGlobal > smid_cross_cross.tStartRefresh + 3*TR-frameTolerance:
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
    while continueRoutine:
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
            if tThisFlipGlobal > smid_image.tStartRefresh + 10*TR-frameTolerance:
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
    # the Routine "smid_stimulus" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "smid_rating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    smid_slider.reset()
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
    while continueRoutine:
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
            if tThisFlipGlobal > smid_text.tStartRefresh + 6*TR-frameTolerance:
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
            if tThisFlipGlobal > smid_slider.tStartRefresh + 6*TR-frameTolerance:
                # keep track of stop time/frame for later
                smid_slider.tStop = t  # not accounting for scr refresh
                smid_slider.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'smid_slider.stopped')
                smid_slider.setAutoDraw(False)
        # Run 'Each Frame' code from smid_code
        keys = event.getKeys()
        
        if len(keys):
            if 'h' in keys:
                if smid_slider.markerPos == None:
                    smid_slider.markerPos = 2
                else:
                    smid_slider.markerPos -= 1
            if 'j' in keys:
                smid_slider.markerPos = 3
            elif 'k' in keys:
                if smid_slider.markerPos == None:
                    smid_slider.markerPos = 4
                else:
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
            if tThisFlipGlobal > smid_key.tStartRefresh + 6*TR-frameTolerance:
                # keep track of stop time/frame for later
                smid_key.tStop = t  # not accounting for scr refresh
                smid_key.frameNStop = frameN  # exact frame index
                smid_key.status = FINISHED
        if smid_key.status == STARTED and not waitOnFlip:
            theseKeys = smid_key.getKeys(keyList=['h', 'j', 'k'], waitRelease=False)
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
    # the Routine "smid_rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "smid_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    smid_break_key.keys = []
    smid_break_key.rt = []
    _smid_break_key_allKeys = []
    # keep track of which components have finished
    smid_breakComponents = [smid_break_text, smid_break_key, smid_break_cross]
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
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from smid_break_code
        if smid_trials.thisN == 0 or smid_trials.thisN == 119 or (smid_trials.thisN + 1) % 30 != 0:
            continueRoutine = False
        
        # *smid_break_text* updates
        if smid_break_text.status == NOT_STARTED and tThisFlip >= 11*TR-frameTolerance:
            # keep track of start time/frame for later
            smid_break_text.frameNStart = frameN  # exact frame index
            smid_break_text.tStart = t  # local t and not account for scr refresh
            smid_break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smid_break_text, 'tStartRefresh')  # time at next scr refresh
            smid_break_text.setAutoDraw(True)
        
        # *smid_break_key* updates
        waitOnFlip = False
        if smid_break_key.status == NOT_STARTED and tThisFlip >= 11*TR-frameTolerance:
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
        if smid_break_key.status == STARTED and not waitOnFlip:
            theseKeys = smid_break_key.getKeys(keyList=["t"], waitRelease=False)
            _smid_break_key_allKeys.extend(theseKeys)
            if len(_smid_break_key_allKeys):
                smid_break_key.keys = _smid_break_key_allKeys[-1].name  # just the last key pressed
                smid_break_key.rt = _smid_break_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *smid_break_cross* updates
        if smid_break_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            smid_break_cross.frameNStart = frameN  # exact frame index
            smid_break_cross.tStart = t  # local t and not account for scr refresh
            smid_break_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(smid_break_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'smid_break_cross.started')
            smid_break_cross.setAutoDraw(True)
        if smid_break_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > smid_break_cross.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                smid_break_cross.tStop = t  # not accounting for scr refresh
                smid_break_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'smid_break_cross.stopped')
                smid_break_cross.setAutoDraw(False)
        
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
    # the Routine "smid_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "tail_smid_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    tail_smid_breakComponents = [cross_tail_smid]
    for thisComponent in tail_smid_breakComponents:
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
    
    # --- Run Routine "tail_smid_break" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_4
        if smid_trials.thisN == 0 or smid_trials.thisN == 119 or (smid_trials.thisN + 1) % 30 != 0:
            continueRoutine = False
        
        # *cross_tail_smid* updates
        if cross_tail_smid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_tail_smid.frameNStart = frameN  # exact frame index
            cross_tail_smid.tStart = t  # local t and not account for scr refresh
            cross_tail_smid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_tail_smid, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_tail_smid.started')
            cross_tail_smid.setAutoDraw(True)
        if cross_tail_smid.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_tail_smid.tStartRefresh + 11*TR-frameTolerance:
                # keep track of stop time/frame for later
                cross_tail_smid.tStop = t  # not accounting for scr refresh
                cross_tail_smid.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_tail_smid.stopped')
                cross_tail_smid.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tail_smid_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tail_smid_break" ---
    for thisComponent in tail_smid_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "tail_smid_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'smid_trials'


# --- Prepare to start Routine "end_note" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
end_note_resp.keys = []
end_note_resp.rt = []
_end_note_resp_allKeys = []
# keep track of which components have finished
end_noteComponents = [end_note_text, end_note_resp]
for thisComponent in end_noteComponents:
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

# --- Run Routine "end_note" ---
while continueRoutine and routineTimer.getTime() < 30.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_note_text* updates
    if end_note_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_note_text.frameNStart = frameN  # exact frame index
        end_note_text.tStart = t  # local t and not account for scr refresh
        end_note_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_note_text, 'tStartRefresh')  # time at next scr refresh
        end_note_text.setAutoDraw(True)
    if end_note_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_note_text.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            end_note_text.tStop = t  # not accounting for scr refresh
            end_note_text.frameNStop = frameN  # exact frame index
            end_note_text.setAutoDraw(False)
    
    # *end_note_resp* updates
    waitOnFlip = False
    if end_note_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_note_resp.frameNStart = frameN  # exact frame index
        end_note_resp.tStart = t  # local t and not account for scr refresh
        end_note_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_note_resp, 'tStartRefresh')  # time at next scr refresh
        end_note_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_note_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_note_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_note_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_note_resp.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            end_note_resp.tStop = t  # not accounting for scr refresh
            end_note_resp.frameNStop = frameN  # exact frame index
            end_note_resp.status = FINISHED
    if end_note_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_note_resp.getKeys(keyList=['t'], waitRelease=False)
        _end_note_resp_allKeys.extend(theseKeys)
        if len(_end_note_resp_allKeys):
            end_note_resp.keys = _end_note_resp_allKeys[-1].name  # just the last key pressed
            end_note_resp.rt = _end_note_resp_allKeys[-1].rt
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
    for thisComponent in end_noteComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_note" ---
for thisComponent in end_noteComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_note_resp.keys in ['', [], None]:  # No response was made
    end_note_resp.keys = None
thisExp.addData('end_note_resp.keys',end_note_resp.keys)
if end_note_resp.keys != None:  # we had a response
    thisExp.addData('end_note_resp.rt', end_note_resp.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-30.000000)

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
