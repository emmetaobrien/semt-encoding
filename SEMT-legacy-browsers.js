/************* 
 * Semt Test *
 *************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1, 1, 1]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'SEMT';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(langRoutineBegin());
flowScheduler.add(langRoutineEachFrame());
flowScheduler.add(langRoutineEnd());
flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
const prac_repeatLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_repeatLoopBegin, prac_repeatLoopScheduler);
flowScheduler.add(prac_repeatLoopScheduler);
flowScheduler.add(prac_repeatLoopEnd);
flowScheduler.add(readyRoutineBegin());
flowScheduler.add(readyRoutineEachFrame());
flowScheduler.add(readyRoutineEnd());
flowScheduler.add(cntdownRoutineBegin());
flowScheduler.add(cntdownRoutineEachFrame());
flowScheduler.add(cntdownRoutineEnd());
const trials_repeatLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_repeatLoopBegin, trials_repeatLoopScheduler);
flowScheduler.add(trials_repeatLoopScheduler);
flowScheduler.add(trials_repeatLoopEnd);
flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'left_cr.jpg', 'path': 'left_cr.jpg'},
    {'name': 'right_cr.jpg', 'path': 'right_cr.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var langClock;
var text_lang;
var key_lang;
var instrClock;
var instr_text_1;
var instr_text_2;
var instr_text_3;
var instr_text_4;
var instr_text_5;
var pracClock;
var item1_img_pr;
var brL_img_pr;
var que_text_pr;
var item2_img_pr;
var brR_img_pr;
var response_pr;
var timer_pr;
var fix_text_pr;
var key_prac;
var transitionClock;
var txt_transi;
var key_transi;
var readyClock;
var txt_rdy;
var key_rdy;
var cntdownClock;
var timer_ctdown;
var trialClock;
var item1_img;
var brL_img;
var que_text;
var item2_img;
var brR_img;
var response;
var timer;
var fix_text;
var key;
var restClock;
var txt_rest;
var key_rest;
var ready_2Clock;
var txt_rdy2;
var key_rdy2;
var cntdown_2Clock;
var timer_ctdown2;
var thanksClock;
var txt_thx;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "lang"
  langClock = new util.Clock();
  text_lang = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lang',
    text: 'Veuillez sélectionner votre langue.\nAppuyez sur 1 pour Français.\n\nPlease select your language.\nPress 2 for English.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -1.0 
  });
  
  key_lang = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  instr_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_text_1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -1.0 
  });
  
  instr_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -2.0 
  });
  
  instr_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_text_3',
    text: 'Any text\n\nincluding line breaks',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -3.0 
  });
  
  instr_text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_text_4',
    text: 'Any text\n\nincluding line breaks',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -4.0 
  });
  
  instr_text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_text_5',
    text: 'Any text\n\nincluding line breaks',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1.0,
    depth: -5.0 
  });
  
  // Initialize components for Routine "prac"
  pracClock = new util.Clock();
  item1_img_pr = new visual.ImageStim({
    win : psychoJS.window,
    name : 'item1_img_pr', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : -1.0 
  });
  brL_img_pr = new visual.ImageStim({
    win : psychoJS.window,
    name : 'brL_img_pr', units : undefined, 
    image : 'left_cr.jpg', mask : undefined,
    ori : 0, pos : [(- 0.6), 0], size : [0.1, 0.6],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : -2.0 
  });
  que_text_pr = new visual.TextStim({
    win: psychoJS.window,
    name: 'que_text_pr',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -3.0 
  });
  
  item2_img_pr = new visual.ImageStim({
    win : psychoJS.window,
    name : 'item2_img_pr', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : -4.0 
  });
  brR_img_pr = new visual.ImageStim({
    win : psychoJS.window,
    name : 'brR_img_pr', units : undefined, 
    image : 'right_cr.jpg', mask : undefined,
    ori : 0, pos : [0.6, 0], size : [0.1, 0.6],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : -5.0 
  });
  response_pr = new visual.TextStim({
    win: psychoJS.window,
    name: 'response_pr',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -6.0 
  });
  
  timer_pr = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_pr',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -7.0 
  });
  
  fix_text_pr = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_text_pr',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -8.0 
  });
  
  key_prac = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "transition"
  transitionClock = new util.Clock();
  txt_transi = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_transi',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -1.0 
  });
  
  key_transi = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ready"
  readyClock = new util.Clock();
  txt_rdy = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_rdy',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.1, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -1.0 
  });
  
  key_rdy = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "cntdown"
  cntdownClock = new util.Clock();
  timer_ctdown = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_ctdown',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  item1_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'item1_img', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : -1.0 
  });
  brL_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'brL_img', units : undefined, 
    image : 'left_cr.jpg', mask : undefined,
    ori : 0, pos : [(- 0.6), 0], size : [0.1, 0.6],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : -2.0 
  });
  que_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'que_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -3.0 
  });
  
  item2_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'item2_img', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : -4.0 
  });
  brR_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'brR_img', units : undefined, 
    image : 'right_cr.jpg', mask : undefined,
    ori : 0, pos : [0.6, 0], size : [0.1, 0.6],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : false, depth : -5.0 
  });
  response = new visual.TextStim({
    win: psychoJS.window,
    name: 'response',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -6.0 
  });
  
  timer = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 0,
    depth: -7.0 
  });
  
  fix_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_text',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -8.0 
  });
  
  key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rest"
  restClock = new util.Clock();
  txt_rest = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_rest',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -1.0 
  });
  
  key_rest = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ready_2"
  ready_2Clock = new util.Clock();
  txt_rdy2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_rdy2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -1.0 
  });
  
  key_rdy2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "cntdown_2"
  cntdown_2Clock = new util.Clock();
  timer_ctdown2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'timer_ctdown2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  txt_thx = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_thx',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.1, ori: 0,
    color: new util.Color([(- 1), (- 1), (- 1)]),  opacity: 1,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_lang_allKeys;
var langComponents;
function langRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'lang'-------
    t = 0;
    langClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_lang.keys = undefined;
    key_lang.rt = undefined;
    _key_lang_allKeys = [];
    // keep track of which components have finished
    langComponents = [];
    langComponents.push(text_lang);
    langComponents.push(key_lang);
    
    langComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function langRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'lang'-------
    // get current time
    t = langClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_lang* updates
    if (t >= 0.0 && text_lang.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lang.tStart = t;  // (not accounting for frame time here)
      text_lang.frameNStart = frameN;  // exact frame index
      
      text_lang.setAutoDraw(true);
    }

    
    // *key_lang* updates
    if (t >= 0.0 && key_lang.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_lang.tStart = t;  // (not accounting for frame time here)
      key_lang.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_lang.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_lang.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_lang.clearEvents(); });
    }

    if (key_lang.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_lang.getKeys({keyList: ['1', '2', 'esc'], waitRelease: false});
      _key_lang_allKeys = _key_lang_allKeys.concat(theseKeys);
      if (_key_lang_allKeys.length > 0) {
        key_lang.keys = _key_lang_allKeys[_key_lang_allKeys.length - 1].name;  // just the last key pressed
        key_lang.rt = _key_lang_allKeys[_key_lang_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    langComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function langRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'lang'-------
    langComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_lang.keys', key_lang.keys);
    if (typeof key_lang.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_lang.rt', key_lang.rt);
        }
    
    key_lang.stop();
    // the Routine "lang" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrComponents;
function instrRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instr'-------
    t = 0;
    instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(instr_text_1);
    instrComponents.push(instr_text_2);
    instrComponents.push(instr_text_3);
    instrComponents.push(instr_text_4);
    instrComponents.push(instr_text_5);
    
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instr'-------
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_text_1* updates
    if (t >= 0.0 && instr_text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_text_1.tStart = t;  // (not accounting for frame time here)
      instr_text_1.frameNStart = frameN;  // exact frame index
      
      instr_text_1.setAutoDraw(true);
    }

    if (instr_text_1.status === PsychoJS.Status.STARTED && Boolean((curIns == 2))) {
      instr_text_1.setAutoDraw(false);
    }
    
    // *instr_text_2* updates
    if (((curIns == 2)) && instr_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_text_2.tStart = t;  // (not accounting for frame time here)
      instr_text_2.frameNStart = frameN;  // exact frame index
      
      instr_text_2.setAutoDraw(true);
    }

    if (instr_text_2.status === PsychoJS.Status.STARTED && Boolean((curIns == 3))) {
      instr_text_2.setAutoDraw(false);
    }
    
    // *instr_text_3* updates
    if (((curIns == 3)) && instr_text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_text_3.tStart = t;  // (not accounting for frame time here)
      instr_text_3.frameNStart = frameN;  // exact frame index
      
      instr_text_3.setAutoDraw(true);
    }

    if (instr_text_3.status === PsychoJS.Status.STARTED && Boolean((curIns == 4))) {
      instr_text_3.setAutoDraw(false);
    }
    
    // *instr_text_4* updates
    if (((curIns == 4)) && instr_text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_text_4.tStart = t;  // (not accounting for frame time here)
      instr_text_4.frameNStart = frameN;  // exact frame index
      
      instr_text_4.setAutoDraw(true);
    }

    if (instr_text_4.status === PsychoJS.Status.STARTED && Boolean((curIns == 5))) {
      instr_text_4.setAutoDraw(false);
    }
    
    // *instr_text_5* updates
    if ((curIns == 5) && instr_text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_text_5.tStart = t;  // (not accounting for frame time here)
      instr_text_5.frameNStart = frameN;  // exact frame index
      
      instr_text_5.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instr'-------
    instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var prac_repeat;
var currentLoop;
function prac_repeatLoopBegin(prac_repeatLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  prac_repeat = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 100, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'prac_repeat'
  });
  psychoJS.experiment.addLoop(prac_repeat); // add the loop to the experiment
  currentLoop = prac_repeat;  // we're now the current loop

  // Schedule all the trials in the trialList:
  prac_repeat.forEach(function() {
    const snapshot = prac_repeat.getSnapshot();

    prac_repeatLoopScheduler.add(importConditions(snapshot));
    const practiceLoopScheduler = new Scheduler(psychoJS);
    prac_repeatLoopScheduler.add(practiceLoopBegin, practiceLoopScheduler);
    prac_repeatLoopScheduler.add(practiceLoopScheduler);
    prac_repeatLoopScheduler.add(practiceLoopEnd);
    prac_repeatLoopScheduler.add(transitionRoutineBegin(snapshot));
    prac_repeatLoopScheduler.add(transitionRoutineEachFrame(snapshot));
    prac_repeatLoopScheduler.add(transitionRoutineEnd(snapshot));
    prac_repeatLoopScheduler.add(endLoopIteration(prac_repeatLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var practice;
function practiceLoopBegin(practiceLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  practice = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: pracConditions,
    seed: undefined, name: 'practice'
  });
  psychoJS.experiment.addLoop(practice); // add the loop to the experiment
  currentLoop = practice;  // we're now the current loop

  // Schedule all the trials in the trialList:
  practice.forEach(function() {
    const snapshot = practice.getSnapshot();

    practiceLoopScheduler.add(importConditions(snapshot));
    practiceLoopScheduler.add(pracRoutineBegin(snapshot));
    practiceLoopScheduler.add(pracRoutineEachFrame(snapshot));
    practiceLoopScheduler.add(pracRoutineEnd(snapshot));
    practiceLoopScheduler.add(endLoopIteration(practiceLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function practiceLoopEnd() {
  psychoJS.experiment.removeLoop(practice);

  return Scheduler.Event.NEXT;
}


function prac_repeatLoopEnd() {
  psychoJS.experiment.removeLoop(prac_repeat);

  return Scheduler.Event.NEXT;
}


var trials_repeat;
function trials_repeatLoopBegin(trials_repeatLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_repeat = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_repeat'
  });
  psychoJS.experiment.addLoop(trials_repeat); // add the loop to the experiment
  currentLoop = trials_repeat;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_repeat.forEach(function() {
    const snapshot = trials_repeat.getSnapshot();

    trials_repeatLoopScheduler.add(importConditions(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    trials_repeatLoopScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    trials_repeatLoopScheduler.add(trialsLoopScheduler);
    trials_repeatLoopScheduler.add(trialsLoopEnd);
    trials_repeatLoopScheduler.add(restRoutineBegin(snapshot));
    trials_repeatLoopScheduler.add(restRoutineEachFrame(snapshot));
    trials_repeatLoopScheduler.add(restRoutineEnd(snapshot));
    trials_repeatLoopScheduler.add(ready_2RoutineBegin(snapshot));
    trials_repeatLoopScheduler.add(ready_2RoutineEachFrame(snapshot));
    trials_repeatLoopScheduler.add(ready_2RoutineEnd(snapshot));
    trials_repeatLoopScheduler.add(cntdown_2RoutineBegin(snapshot));
    trials_repeatLoopScheduler.add(cntdown_2RoutineEachFrame(snapshot));
    trials_repeatLoopScheduler.add(cntdown_2RoutineEnd(snapshot));
    trials_repeatLoopScheduler.add(endLoopIteration(trials_repeatLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: trialConditions,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function trials_repeatLoopEnd() {
  psychoJS.experiment.removeLoop(trials_repeat);

  return Scheduler.Event.NEXT;
}


var _key_prac_allKeys;
var pracComponents;
function pracRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prac'-------
    t = 0;
    pracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    item1_img_pr.setImage(img1);
    item2_img_pr.setImage(img2);
    key_prac.keys = undefined;
    key_prac.rt = undefined;
    _key_prac_allKeys = [];
    // keep track of which components have finished
    pracComponents = [];
    pracComponents.push(item1_img_pr);
    pracComponents.push(brL_img_pr);
    pracComponents.push(que_text_pr);
    pracComponents.push(item2_img_pr);
    pracComponents.push(brR_img_pr);
    pracComponents.push(response_pr);
    pracComponents.push(timer_pr);
    pracComponents.push(fix_text_pr);
    pracComponents.push(key_prac);
    
    pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function pracRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prac'-------
    // get current time
    t = pracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *item1_img_pr* updates
    if (t >= 0 && item1_img_pr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item1_img_pr.tStart = t;  // (not accounting for frame time here)
      item1_img_pr.frameNStart = frameN;  // exact frame index
      
      item1_img_pr.setAutoDraw(true);
    }

    frameRemains = 0 + n_secs_img1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (item1_img_pr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      item1_img_pr.setAutoDraw(false);
    }
    
    // *brL_img_pr* updates
    if (t >= 0.0 && brL_img_pr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      brL_img_pr.tStart = t;  // (not accounting for frame time here)
      brL_img_pr.frameNStart = frameN;  // exact frame index
      
      brL_img_pr.setAutoDraw(true);
    }

    frameRemains = 0.0 + n_secs_img1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (brL_img_pr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      brL_img_pr.setAutoDraw(false);
    }
    
    // *que_text_pr* updates
    if (((item1_finished == True)) && que_text_pr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      que_text_pr.tStart = t;  // (not accounting for frame time here)
      que_text_pr.frameNStart = frameN;  // exact frame index
      
      que_text_pr.setAutoDraw(true);
    }

    if (que_text_pr.status === PsychoJS.Status.STARTED && t >= (que_text_pr.tStart + timeQue)) {
      que_text_pr.setAutoDraw(false);
    }
    
    // *item2_img_pr* updates
    if (((que_finished == True)) && item2_img_pr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item2_img_pr.tStart = t;  // (not accounting for frame time here)
      item2_img_pr.frameNStart = frameN;  // exact frame index
      
      item2_img_pr.setAutoDraw(true);
    }

    if (item2_img_pr.status === PsychoJS.Status.STARTED && t >= (item2_img_pr.tStart + n_secs_img2)) {
      item2_img_pr.setAutoDraw(false);
    }
    
    // *brR_img_pr* updates
    if (((que_finished == True)) && brR_img_pr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      brR_img_pr.tStart = t;  // (not accounting for frame time here)
      brR_img_pr.frameNStart = frameN;  // exact frame index
      
      brR_img_pr.setAutoDraw(true);
    }

    if (brR_img_pr.status === PsychoJS.Status.STARTED && t >= (brR_img_pr.tStart + n_secs_img2)) {
      brR_img_pr.setAutoDraw(false);
    }
    
    // *response_pr* updates
    if (((que_finished == True)) && response_pr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response_pr.tStart = t;  // (not accounting for frame time here)
      response_pr.frameNStart = frameN;  // exact frame index
      
      response_pr.setAutoDraw(true);
    }

    if (response_pr.status === PsychoJS.Status.STARTED && Boolean(participant_answered)) {
      response_pr.setAutoDraw(false);
    }
    
    // *timer_pr* updates
    if (((que_finished == True)) && timer_pr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timer_pr.tStart = t;  // (not accounting for frame time here)
      timer_pr.frameNStart = frameN;  // exact frame index
      
      timer_pr.setAutoDraw(true);
    }

    if (timer_pr.status === PsychoJS.Status.STARTED && t >= (timer_pr.tStart + 4)) {
      timer_pr.setAutoDraw(false);
    }
    
    // *fix_text_pr* updates
    if (((item2_finished == True)) && fix_text_pr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_text_pr.tStart = t;  // (not accounting for frame time here)
      fix_text_pr.frameNStart = frameN;  // exact frame index
      
      fix_text_pr.setAutoDraw(true);
    }

    if (fix_text_pr.status === PsychoJS.Status.STARTED && t >= (fix_text_pr.tStart + timeFix)) {
      fix_text_pr.setAutoDraw(false);
    }
    
    // *key_prac* updates
    if (t >= 0.0 && key_prac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_prac.tStart = t;  // (not accounting for frame time here)
      key_prac.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_prac.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_prac.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_prac.clearEvents(); });
    }

    if (key_prac.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_prac.getKeys({keyList: ['1', '2', 'esc'], waitRelease: false});
      _key_prac_allKeys = _key_prac_allKeys.concat(theseKeys);
      if (_key_prac_allKeys.length > 0) {
        key_prac.keys = _key_prac_allKeys[_key_prac_allKeys.length - 1].name;  // just the last key pressed
        key_prac.rt = _key_prac_allKeys[_key_prac_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    pracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pracRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac'-------
    pracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_prac.keys', key_prac.keys);
    if (typeof key_prac.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_prac.rt', key_prac.rt);
        }
    
    key_prac.stop();
    // the Routine "prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_transi_allKeys;
var transitionComponents;
function transitionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'transition'-------
    t = 0;
    transitionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_transi.keys = undefined;
    key_transi.rt = undefined;
    _key_transi_allKeys = [];
    // keep track of which components have finished
    transitionComponents = [];
    transitionComponents.push(txt_transi);
    transitionComponents.push(key_transi);
    
    transitionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function transitionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'transition'-------
    // get current time
    t = transitionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *txt_transi* updates
    if (t >= 0.0 && txt_transi.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_transi.tStart = t;  // (not accounting for frame time here)
      txt_transi.frameNStart = frameN;  // exact frame index
      
      txt_transi.setAutoDraw(true);
    }

    
    // *key_transi* updates
    if (t >= 0.0 && key_transi.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_transi.tStart = t;  // (not accounting for frame time here)
      key_transi.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_transi.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_transi.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_transi.clearEvents(); });
    }

    if (key_transi.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_transi.getKeys({keyList: ['p', 't', 'esc'], waitRelease: false});
      _key_transi_allKeys = _key_transi_allKeys.concat(theseKeys);
      if (_key_transi_allKeys.length > 0) {
        key_transi.keys = _key_transi_allKeys[_key_transi_allKeys.length - 1].name;  // just the last key pressed
        key_transi.rt = _key_transi_allKeys[_key_transi_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    transitionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function transitionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'transition'-------
    transitionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_transi.keys', key_transi.keys);
    if (typeof key_transi.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_transi.rt', key_transi.rt);
        }
    
    key_transi.stop();
    // the Routine "transition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_rdy_allKeys;
var readyComponents;
function readyRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ready'-------
    t = 0;
    readyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    /* Syntax Error: Fix Python code */
    key_rdy.keys = undefined;
    key_rdy.rt = undefined;
    _key_rdy_allKeys = [];
    // keep track of which components have finished
    readyComponents = [];
    readyComponents.push(txt_rdy);
    readyComponents.push(key_rdy);
    
    readyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function readyRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ready'-------
    // get current time
    t = readyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *txt_rdy* updates
    if (t >= 0.0 && txt_rdy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_rdy.tStart = t;  // (not accounting for frame time here)
      txt_rdy.frameNStart = frameN;  // exact frame index
      
      txt_rdy.setAutoDraw(true);
    }

    
    // *key_rdy* updates
    if (t >= 0.0 && key_rdy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_rdy.tStart = t;  // (not accounting for frame time here)
      key_rdy.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_rdy.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_rdy.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_rdy.clearEvents(); });
    }

    if (key_rdy.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_rdy.getKeys({keyList: ['5', 'esc'], waitRelease: false});
      _key_rdy_allKeys = _key_rdy_allKeys.concat(theseKeys);
      if (_key_rdy_allKeys.length > 0) {
        key_rdy.keys = _key_rdy_allKeys[_key_rdy_allKeys.length - 1].name;  // just the last key pressed
        key_rdy.rt = _key_rdy_allKeys[_key_rdy_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    readyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function readyRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ready'-------
    readyComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_rdy.keys', key_rdy.keys);
    if (typeof key_rdy.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_rdy.rt', key_rdy.rt);
        routineTimer.reset();
        }
    
    key_rdy.stop();
    // the Routine "ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var cntdownComponents;
function cntdownRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'cntdown'-------
    t = 0;
    cntdownClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    cntdownComponents = [];
    cntdownComponents.push(timer_ctdown);
    
    cntdownComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function cntdownRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'cntdown'-------
    // get current time
    t = cntdownClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *timer_ctdown* updates
    if (t >= 0.0 && timer_ctdown.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timer_ctdown.tStart = t;  // (not accounting for frame time here)
      timer_ctdown.frameNStart = frameN;  // exact frame index
      
      timer_ctdown.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (timer_ctdown.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      timer_ctdown.setAutoDraw(false);
    }
    
    if (timer_ctdown.status === PsychoJS.Status.STARTED){ // only update if being drawn
      timer_ctdown.setText(int(Math.abs(util.round((5 - t), ndigits=1))), false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    cntdownComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function cntdownRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'cntdown'-------
    cntdownComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    item1_img.setImage(img1);
    item2_img.setImage(img2);
    key.keys = undefined;
    key.rt = undefined;
    _key_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(item1_img);
    trialComponents.push(brL_img);
    trialComponents.push(que_text);
    trialComponents.push(item2_img);
    trialComponents.push(brR_img);
    trialComponents.push(response);
    trialComponents.push(timer);
    trialComponents.push(fix_text);
    trialComponents.push(key);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *item1_img* updates
    if (t >= 0.0 && item1_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item1_img.tStart = t;  // (not accounting for frame time here)
      item1_img.frameNStart = frameN;  // exact frame index
      
      item1_img.setAutoDraw(true);
    }

    frameRemains = 0.0 + n_secs_img1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (item1_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      item1_img.setAutoDraw(false);
    }
    
    // *brL_img* updates
    if (t >= 0.0 && brL_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      brL_img.tStart = t;  // (not accounting for frame time here)
      brL_img.frameNStart = frameN;  // exact frame index
      
      brL_img.setAutoDraw(true);
    }

    frameRemains = 0.0 + n_secs_img1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (brL_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      brL_img.setAutoDraw(false);
    }
    
    // *que_text* updates
    if (((item1_finished == True)) && que_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      que_text.tStart = t;  // (not accounting for frame time here)
      que_text.frameNStart = frameN;  // exact frame index
      
      que_text.setAutoDraw(true);
    }

    if (que_text.status === PsychoJS.Status.STARTED && t >= (que_text.tStart + timeQue)) {
      que_text.setAutoDraw(false);
    }
    
    // *item2_img* updates
    if ((que_finished) && item2_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item2_img.tStart = t;  // (not accounting for frame time here)
      item2_img.frameNStart = frameN;  // exact frame index
      
      item2_img.setAutoDraw(true);
    }

    if (item2_img.status === PsychoJS.Status.STARTED && t >= (item2_img.tStart + n_secs_img2)) {
      item2_img.setAutoDraw(false);
    }
    
    // *brR_img* updates
    if ((que_finished) && brR_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      brR_img.tStart = t;  // (not accounting for frame time here)
      brR_img.frameNStart = frameN;  // exact frame index
      
      brR_img.setAutoDraw(true);
    }

    if (brR_img.status === PsychoJS.Status.STARTED && t >= (brR_img.tStart + n_secs_img2)) {
      brR_img.setAutoDraw(false);
    }
    
    // *response* updates
    if (((que_finished == True)) && response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response.tStart = t;  // (not accounting for frame time here)
      response.frameNStart = frameN;  // exact frame index
      
      response.setAutoDraw(true);
    }

    if (response.status === PsychoJS.Status.STARTED && Boolean(participant_answered)) {
      response.setAutoDraw(false);
    }
    
    // *timer* updates
    if (((que_finished == True)) && timer.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timer.tStart = t;  // (not accounting for frame time here)
      timer.frameNStart = frameN;  // exact frame index
      
      timer.setAutoDraw(true);
    }

    if (timer.status === PsychoJS.Status.STARTED && t >= (timer.tStart + 4)) {
      timer.setAutoDraw(false);
    }
    
    // *fix_text* updates
    if ((item2_finished) && fix_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_text.tStart = t;  // (not accounting for frame time here)
      fix_text.frameNStart = frameN;  // exact frame index
      
      fix_text.setAutoDraw(true);
    }

    if (fix_text.status === PsychoJS.Status.STARTED && t >= (fix_text.tStart + timeFix)) {
      fix_text.setAutoDraw(false);
    }
    
    // *key* updates
    if (t >= 0.0 && key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key.tStart = t;  // (not accounting for frame time here)
      key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key.clearEvents(); });
    }

    if (key.status === PsychoJS.Status.STARTED) {
      let theseKeys = key.getKeys({keyList: ['1', '2', 'esc'], waitRelease: false});
      _key_allKeys = _key_allKeys.concat(theseKeys);
      if (_key_allKeys.length > 0) {
        key.keys = _key_allKeys[_key_allKeys.length - 1].name;  // just the last key pressed
        key.rt = _key_allKeys[_key_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key.keys', key.keys);
    if (typeof key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key.rt', key.rt);
        }
    
    key.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_rest_allKeys;
var restComponents;
function restRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'rest'-------
    t = 0;
    restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_rest.keys = undefined;
    key_rest.rt = undefined;
    _key_rest_allKeys = [];
    // keep track of which components have finished
    restComponents = [];
    restComponents.push(txt_rest);
    restComponents.push(key_rest);
    
    restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function restRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'rest'-------
    // get current time
    t = restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *txt_rest* updates
    if (t >= 0.0 && txt_rest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_rest.tStart = t;  // (not accounting for frame time here)
      txt_rest.frameNStart = frameN;  // exact frame index
      
      txt_rest.setAutoDraw(true);
    }

    
    // *key_rest* updates
    if (t >= 0.0 && key_rest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_rest.tStart = t;  // (not accounting for frame time here)
      key_rest.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_rest.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_rest.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_rest.clearEvents(); });
    }

    if (key_rest.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_rest.getKeys({keyList: ['t', 'esc'], waitRelease: false});
      _key_rest_allKeys = _key_rest_allKeys.concat(theseKeys);
      if (_key_rest_allKeys.length > 0) {
        key_rest.keys = _key_rest_allKeys[_key_rest_allKeys.length - 1].name;  // just the last key pressed
        key_rest.rt = _key_rest_allKeys[_key_rest_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'rest'-------
    restComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_rest.keys', key_rest.keys);
    if (typeof key_rest.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_rest.rt', key_rest.rt);
        routineTimer.reset();
        }
    
    key_rest.stop();
    // the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_rdy2_allKeys;
var ready_2Components;
function ready_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ready_2'-------
    t = 0;
    ready_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_rdy2.keys = undefined;
    key_rdy2.rt = undefined;
    _key_rdy2_allKeys = [];
    // keep track of which components have finished
    ready_2Components = [];
    ready_2Components.push(txt_rdy2);
    ready_2Components.push(key_rdy2);
    
    ready_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function ready_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ready_2'-------
    // get current time
    t = ready_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *txt_rdy2* updates
    if (t >= 0.0 && txt_rdy2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_rdy2.tStart = t;  // (not accounting for frame time here)
      txt_rdy2.frameNStart = frameN;  // exact frame index
      
      txt_rdy2.setAutoDraw(true);
    }

    
    // *key_rdy2* updates
    if (t >= 0.0 && key_rdy2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_rdy2.tStart = t;  // (not accounting for frame time here)
      key_rdy2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_rdy2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_rdy2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_rdy2.clearEvents(); });
    }

    if (key_rdy2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_rdy2.getKeys({keyList: ['5', 'esc'], waitRelease: false});
      _key_rdy2_allKeys = _key_rdy2_allKeys.concat(theseKeys);
      if (_key_rdy2_allKeys.length > 0) {
        key_rdy2.keys = _key_rdy2_allKeys[_key_rdy2_allKeys.length - 1].name;  // just the last key pressed
        key_rdy2.rt = _key_rdy2_allKeys[_key_rdy2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ready_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ready_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ready_2'-------
    ready_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_rdy2.keys', key_rdy2.keys);
    if (typeof key_rdy2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_rdy2.rt', key_rdy2.rt);
        routineTimer.reset();
        }
    
    key_rdy2.stop();
    // the Routine "ready_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var cntdown_2Components;
function cntdown_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'cntdown_2'-------
    t = 0;
    cntdown_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    cntdown_2Components = [];
    cntdown_2Components.push(timer_ctdown2);
    
    cntdown_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function cntdown_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'cntdown_2'-------
    // get current time
    t = cntdown_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *timer_ctdown2* updates
    if (t >= 0.0 && timer_ctdown2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timer_ctdown2.tStart = t;  // (not accounting for frame time here)
      timer_ctdown2.frameNStart = frameN;  // exact frame index
      
      timer_ctdown2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (timer_ctdown2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      timer_ctdown2.setAutoDraw(false);
    }
    
    if (timer_ctdown2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      timer_ctdown2.setText(int(Math.abs(util.round((5 - t), ndigits=1))), false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    cntdown_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function cntdown_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'cntdown_2'-------
    cntdown_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var thanksComponents;
function thanksRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'thanks'-------
    t = 0;
    thanksClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    thanksComponents = [];
    thanksComponents.push(txt_thx);
    
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'thanks'-------
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *txt_thx* updates
    if (t >= 0.0 && txt_thx.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_thx.tStart = t;  // (not accounting for frame time here)
      txt_thx.frameNStart = frameN;  // exact frame index
      
      txt_thx.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (txt_thx.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      txt_thx.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thanksRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'thanks'-------
    thanksComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
