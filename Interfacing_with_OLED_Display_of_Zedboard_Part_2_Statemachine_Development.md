[00:00] hello welcome back so in this video we
[00:03] are going to start the coding for the
[00:05] Olek controller so remember in the last
[00:07] video when we discussed the architecture
[00:09] of the all that we have seen like it
[00:11] communicates with nothing chip through
[00:13] the SV controller now we have already
[00:15] used on is VF control of you actually
[00:17] designed SP a controller in the previous
[00:19] tutorial so we are going to do use that
[00:21] as to be a controller to build the
[00:23] complete on a display so I am going to
[00:26] start it as a new project before that
[00:28] this was the code for SP controller we
[00:31] are going to reuse it so what I will do
[00:33] is I will go ahead and remove this keep
[00:35] attribute which we use for debugging
[00:37] purpose to see the internal signals but
[00:40] they should keep attribute is it will
[00:42] prevent me borrow from optimization so
[00:44] we don't want that to happen so removing
[00:48] the attributes or that me matter is free
[00:49] to up to myself whatever variable he
[00:52] wants to okay so I'm going to file and
[00:55] start a new project and I want to call
[00:59] it all that control project here so in
[01:11] all our previous project we use to skip
[01:12] skip this screen because we didn't have
[01:15] already built code but in this case
[01:18] that's not the case we already have that
[01:20] code for espionage roller and we can
[01:22] reuse it okay so what I'm going to do is
[01:25] I'm going to add the code for SP a
[01:27] controller to my new project so we'll go
[01:30] to add files and you need to know we
[01:35] have the source codes are stored
[01:36] actually so any of you want a project
[01:38] you take inside that our important file
[01:42] is this dot XVI file which is the
[01:44] signings project file or we might of
[01:47] project file and another important
[01:50] folder is this one the project name dot
[01:52] sources folder where all your source
[01:54] codes will be saved
[01:56] okay so if you want to share your
[01:58] project with someone else the only two
[02:01] folders that you need to share this xpf
[02:04] file as well as the dot sources folder
[02:07] all other for devs are temporary so you
[02:09] don't have to share it with other people
[02:11] these two in
[02:12] actually so let me go inside dot
[02:15] services you will see two folders so
[02:17] cylinders com1 if you go inside that you
[02:19] will see you are with low code and then
[02:22] it's constraints and of all if you go
[02:24] inside that you will see XP see file
[02:27] that constraints fine okay so this is
[02:29] where by default or source codes are
[02:33] stored and these are the names by
[02:35] default source of underscored
[02:37] constraints undiscovered of course you
[02:38] can change it the default name but these
[02:42] are the default names so I'll go to my
[02:46] [Music]
[02:47] SK control project forward I'll go
[02:50] inside sources I will go inside sources
[02:53] one and I will choose this SP a control
[02:55] and remember to check this option copy
[02:58] so just to project if you don't check it
[03:01] ok this original source file will not be
[03:05] copied to you a new project can the new
[03:08] project we'll be using the file in the
[03:12] other project so in case if you are
[03:14] modifying this file in the new project
[03:15] it will reflect in the old project or
[03:17] Sameach you may not want to happen so if
[03:19] you check this option
[03:20] he will take a copy of that folder or
[03:23] sorry copy of that file and put it in
[03:26] the dot sources folder of your new
[03:28] project so remember to check it by
[03:29] default it is not checked so remember to
[03:32] check it ok and here again you can add
[03:36] the constraint file if you already have
[03:37] we have a constraint file for SP a
[03:40] control apart most of the pin
[03:41] constraints there are not valid for
[03:43] overall it control so I'm not adding it
[03:46] I'll just click Next and I choose set
[03:48] forth as my target board and finish yes
[03:53] now if you if you forget to add files
[03:55] and you create a new project of course
[03:59] you can add it later by choosing add
[04:01] sources and I now create design sources
[04:04] and by choosing add files instead of
[04:06] create file you will get the same window
[04:08] and you can go ahead and add the
[04:10] existing source file to your project
[04:12] know from Canso so this is our project
[04:16] and we already have a controller here
[04:18] currently that is the TOC file no I'm
[04:21] going to
[04:22] create a new file so again we are going
[04:25] to do hierarchical design so I am going
[04:27] to call the top for us all that
[04:28] controller and he will be instantiating
[04:31] this be a controller inside that yeah so
[04:34] I'm going going to create a new file and
[04:39] going to call it all that control dot V
[04:44] then I get EK you can see the option
[04:46] here local to project if you choose
[04:48] local to project he will store this file
[04:50] in the dot sources photo of your current
[04:52] project or you can change it and save
[04:55] the file at some other location but
[04:57] preferably you always keep all the files
[04:59] in the local project fault ok finish ok
[05:07] and all the control comes here first
[05:12] thing I'm going to do is declare the
[05:14] input output for the olive now in order
[05:17] to do that I look at the data sheet and
[05:21] see which on pins are connected between
[05:24] Zynq and the ordered display so you will
[05:28] see where Oh you can see the pin number
[05:30] that means those pins are connected
[05:31] whether you say not connected that means
[05:33] that is not connected to Zynq but it is
[05:35] actually managed on the PCB itself so
[05:37] you don't have to do anything to these
[05:39] things from Zynq ok so I'm going to
[05:43] write the input/output so let me write
[05:48] it all that interface as I command
[05:52] all that I have SP croc so I am
[05:59] predicting prefixing all at with
[06:01] everything to indicate these signals are
[06:02] interface with the owner okay now we
[06:05] have SV a clock we have all that SPI
[06:09] data you also have output all that we
[06:15] did we have all that patch under foreign
[06:24] putting a postfix underscore n to
[06:27] indicate this is a active low signal
[06:29] that means if you want to reset the
[06:30] other controllers you need to make the
[06:32] signal no normal operation this signal
[06:36] the output Euler underscore DC
[06:41] underscore I can remember this signal is
[06:44] used to choose between whether you are
[06:46] sending bad ass Christ we are control of
[06:47] SPI interface or you are sending some
[06:49] command through the SPI interface so
[06:51] that is the signal that's it so these
[06:53] are the signals going to all it now in
[06:58] addition to that we need an input proc
[07:11] is coming and we also have the research
[07:14] signal so we will assign this reset to
[07:16] one of the push buttons then you said
[07:18] the output should be of edge type or Y
[07:21] we will see why we are doing the code so
[07:24] this makes the basic input output
[07:27] interface the first thing I'm going to
[07:30] do is I'm going to instantiate my SPI
[07:34] controller inside the electron troller
[07:36] so I will go ahead and take the
[07:39] interface for SP a controller and put it
[07:43] here and I will do the port mapping so
[07:46] it called SP controller
[07:47] maybe SC as the instance name
[08:13] so some of the signals you can directly
[08:15] connect for example this crop is the
[08:18] input hundred megahertz we already have
[08:20] it coming from top so you can just go
[08:22] ahead and connect here you also have the
[08:24] research coming from the top you can go
[08:26] ahead and connect that we have SP
[08:30] o'clock which is output clock to SP a 10
[08:32] megahertz which is this one so I can
[08:36] directly connect there and we have SP a
[08:39] tata which is this one so we can connect
[08:42] it so since these signals are connected
[08:44] to the output port of an instance they
[08:47] should be wire type so no need to change
[08:49] them they remain wire type or you can
[08:51] explicitly say output wire or just just
[08:53] leave it perfect now the signal data in
[08:58] load data done send those signals are
[09:02] currently not available
[09:04] so these signal should be generated
[09:05] within the module and interface with SVA
[09:08] controller so whenever we want to send
[09:09] some data we put that data here will
[09:12] make the signal high and we made until
[09:14] this signal goes high that means that
[09:16] data has been sent through the SPI
[09:18] interface fine now in the slides
[09:36] we have seen that you had to send a
[09:40] specific sequence when the system starts
[09:42] up so that the OLED controller is
[09:45] initialized and that is what we are
[09:47] going to do next now you will see the
[09:49] sequence follows a particular order
[09:52] right first you need to make the signal
[09:54] hide and wait for this thing for this
[09:56] thing so the best way to implement this
[09:58] logic is the way state machine so we are
[10:00] going to write a state machine following
[10:02] the standard way of writing strength
[10:03] machines in a lock and that state
[10:06] machine will initialize all that control
[10:09] so that's what we are going to do again
[10:11] I am NOT declaring any signal at this
[10:13] point of time we will add the signal as
[10:15] we go along as I am just declaring
[10:20] always that for such if we said okay so
[10:32] every statement shade when you research
[10:34] it should go to a known state for
[10:37] according to going to use a register
[10:40] called state to store my current state
[10:42] and I am saying when I power up I'll be
[10:45] in the idle State now you need to
[10:48] declare all these registers as well as
[10:52] this is norcal kilometer so we will dis
[10:55] Claire it towards the end because if I
[10:57] want to know what should be the size of
[10:59] the state which is basically depend your
[11:01] flip-flops which will store the current
[11:03] state of the system I need to know how
[11:05] many states are there so that it will be
[11:07] log to the base of two number of states
[11:10] so at this point I really don't know how
[11:12] many states are there so we'll add the
[11:14] states and finally find out how many
[11:15] states are there then we will be clear
[11:17] state okay anyway we'll have to declare
[11:19] it at some point of time the size and
[11:22] there are okay right State I'm just
[11:24] declaring it and the size we will change
[11:26] yes we go hello and ID
[11:29] we usually declare it as a lock-up Adam
[11:32] and I do
[11:36] we could do take the syrup again I have
[11:39] not specified what is the size of this
[11:41] constant because I don't want this foil
[11:44] what is the size but it will perfectly
[11:46] fine this will also work as long as the
[11:51] number of states is less than two to our
[11:56] of 30 you go on minus one okay so
[12:00] already said we are in either state and
[12:03] along with that we need to initialize
[12:05] some of other data also for example the
[12:09] signals to the Hornet control when we
[12:12] start what should be these signal values
[12:15] right so I'm going to say all at VDD is
[12:21] one from where I'm getting this
[12:24] information all these are coming from
[12:26] the data shaped VDD this one now what is
[12:29] V DD and or is given here this is power
[12:33] supply for logic so we are making it
[12:35] high at the beginning and since I am
[12:38] using it inside always Bob so of course
[12:41] it should be a budget I'm now you will
[12:43] see all the signals we are going to use
[12:45] inside the state machine inside the
[12:46] always block so essentially all of them
[12:49] should be a batch time so maybe D is one
[12:53] now all that we bat is also one all that
[13:01] [Music]
[13:03] research is one I'm not making it under
[13:13] we set up like this a toilet at this
[13:15] point of time and all that DC underscore
[13:20] and resolved so what it really doesn't
[13:24] matter it can be 1 or 0 at the beginning
[13:26] that's it
[13:28] ok so this much I am going to do made
[13:30] away when I press the reset button like
[13:34] something wrong here let's see all that
[13:36] reset underscore end
[13:38] okay his research from Scott if there is
[13:43] no reset else
[13:45] week in and we write the state machines
[13:48] and we use the k-state case state tent
[13:52] case so remember to put indentation so
[13:55] that your code is readable so we are in
[13:58] the title state and let's look what is
[14:06] the initialization sequence so I mean I
[14:08] just ate and as soon as I remove the
[14:11] reset what I'm going to do is I'll go to
[14:13] initialize the owner controller by
[14:16] sending this particular sequence that we
[14:18] discussed okay so in order to do that
[14:21] what I'm doing is so what is on a
[14:25] sequence we need to apply reset and make
[14:28] V back equal to one okay that's what we
[14:31] need to do so let us take V back it is
[14:34] already one but still for completion let
[14:37] me make it more and again but it will be
[14:38] already warned when you come to a state
[14:40] ok v by r is 1 again reset also 1 so we
[14:45] set it so what no other signal again if
[14:56] you prefer you can change them so DC I
[14:59] am going to make it 0 because I am going
[15:01] to send a bunch of commands actually so
[15:04] I need to send a bunch of commands
[15:05] before I can't write to the display run
[15:08] okay so do you see research vpad vdd i'm
[15:15] going to make it 0 because v TD is what
[15:23] forcibly to logic
[15:24] so it's interesting this signal is
[15:26] actually active no it's not active hi if
[15:30] you want to apply power the signal has
[15:32] to be active that depends upon how it is
[15:35] connected on the PCB again I'm getting
[15:37] the information by reading that
[15:39] partnership okay so this much is done on
[15:44] Ida state so we have done this part a
[15:48] priori set make me bad equal to 1 apply
[15:51] reset oh we didn't apply the reset it
[15:54] should be
[15:56] I do you know so I need to correct this
[16:02] anymore reset make very practical to
[16:04] what some research should be one here my
[16:08] mistake anyway we'll make reset lo hee
[16:10] after two nano second so now what I need
[16:14] is I need to wait for 2 milliseconds so
[16:19] there should be a some circuit which
[16:21] generates 2 millisecond delay so we have
[16:23] already seen Cirque used to create
[16:25] delayed so we are going to make a
[16:28] circuit which will give me 2 millisecond
[16:30] delay ok that's what I'm going to do the
[16:32] next so I will call it delay or
[16:38] something ok this is how we don't use a
[16:50] counter and remember this guy is also
[16:53] going to format
[16:54] shut up in our heads and we need to fire
[17:01] the quarter value so that when that
[17:03] counter value ranges we have 100
[17:05] megahertz delay the basic logic we are
[17:08] going to use okay so he gets a and
[17:13] whenever you need a delay you will make
[17:16] this particular signal hi did I enable
[17:19] hi so you're basically telling the delay
[17:21] generator it ever that is a generation I
[17:24] want to get the delay done which will
[17:33] basically say he has generated that
[17:36] material okay so all these interfaces
[17:38] you will see between modules there is
[17:39] some kind of handshaking happening one
[17:41] what you will be asking another module
[17:43] to do something by using some enable
[17:45] signal where it signal and the other
[17:47] what you will tell this module I have
[17:49] done by sending you a turn signal
[17:50] already signal something later so this
[17:53] time we call as a producer consumer
[17:54] which is a very popular handshaking but
[17:58] that's when we do 404 we decide decide
[18:01] okay so of course we need counter
[18:06] and what should be counter value we can
[18:09] see our clock is hundred megahertz Oh
[18:13] PDU days from kilo mica care Stewart in
[18:20] memory and we need two millisecond delay
[18:23] to tells it okay so my counter should be
[18:28] able to count in two hundred thousand
[18:30] how big should be my counter let's see I
[18:34] need two hundred thousand this is in
[18:38] binary 18 right so you say seventeen
[18:47] don't 2-0 count look how the counter
[18:51] will work so I'd say always at such Rock
[18:56] begin if someone asked me to create the
[19:02] digit and it's called not equal to 1 2 3
[19:09] 4 5 that means if the signal is low or
[19:21] if the counter is is not this value if
[19:25] it is less than this value or more than
[19:29] this value doesn't matter I will make
[19:34] counter back to become this value no
[19:42] this will not become more than this
[19:43] value because this condition will be
[19:45] satisfied once it reaches this 40 okay
[19:48] so it won't go to this condition so it
[19:51] will stay this particular value now we
[19:53] need to generate this delay a dumb
[19:55] signal so what I bring is always that
[19:57] again such crock peak in if this
[20:03] condition I will take 10 a neighbor
[20:10] and Conda when it reaches this
[20:12] particular value make be there done as
[20:18] hi basically saying generator to switch
[20:21] did it what else
[20:26] that means if the signal is low if the
[20:28] control value is not different make this
[20:33] signal so basically what is going to
[20:35] happen if you want to create two
[20:37] milliseconds pin it you will break the
[20:38] signal high and you will wait for this
[20:41] signal to go high so when this
[20:43] technically the counter will keep on
[20:45] incrementing at some point it will reach
[20:46] this particular value this signal will
[20:48] go high once you see this signal is high
[20:51] you make this signal level so that
[20:54] counter goes back to zero which will
[20:56] make delay term go back to zero so this
[21:00] is what we call as I producer consumer
[21:02] moral of handshaking okay so I am going
[21:09] to take this generator and I am going to
[21:12] instantiate that also under my only
[21:15] controlled NHIN let's call it D G again
[21:20] we need to do for my P I'm going to
[21:33] connect the front of my dad's clock here
[21:36] this signal okay let me call it
[21:39] something like start till 8:00 so this
[21:41] signal should come from your state
[21:42] machine and maybe you can call it delay
[21:46] itself what our name you prefer cat so
[21:49] we need to declare them if you don't
[21:52] declare them we water will show them
[21:54] into cat so you remember to declare so
[21:57] let me take them and go to that power
[22:00] start delay is coming from the state
[22:02] machine that is inside on always box so
[22:04] of course it should be reg type delay it
[22:08] dark is an output from a module that
[22:10] means it should be okay
[22:19] come back to our state machine so I did
[22:24] this much now what I need is I need to
[22:27] create this 2 millisecond delay so what
[22:29] I know is I will create a state called
[22:31] delayed state and in the next block I
[22:35] will switch to that delay state okay so
[22:38] let's write that in a state so here what
[22:55] am I going to do I will make this signal
[22:59] hi started it and what to make right now
[23:01] you need to initialize that signal also
[23:03] don't be satsang selectors fix it I'll
[23:06] make sure you need to make all the
[23:08] registers inside a state machine do some
[23:12] default value under reset condition so
[23:15] remember to do that so it is V 0 0 under
[23:22] reset and when I come to this state I am
[23:26] making that signal high and I you stay
[23:31] in this state until until this denier
[23:36] done comes a carrot II later on comes
[23:38] means 2 millisecond has elapsed I can go
[23:43] to the next state okay so next state the
[23:47] P coordinate Kerris of the cord in each
[23:51] state you can give autonomy I want now
[23:54] we need to declare a unit over so what
[24:10] we should do next it for 2 millisecond
[24:15] we have to send this particular command
[24:17] send display off command that we need to
[24:21] send through the SPI interface
[24:23] ok so that's what we are going to do
[24:25] next so what we should do Meeny
[24:28] - then back to command ayyy through this
[24:34] SPI interface so what I got right is SPI
[24:40] data is not remember the SPI controller
[24:49] how he works so he needs to get the data
[24:51] here and he needed to see this signal
[24:54] going right that only you start sending
[24:56] so that signal ok so we need to connect
[25:01] all the signals here so I swear data I'm
[25:04] going to connect to data in and it
[25:08] should be declared that is if it widens
[25:13] so found out this window SPI data and
[25:17] it's such a slicing data is optional but
[25:22] it is mandatory to initialize all
[25:24] control signal part let's initialize to
[25:27] 0 reset so SPN data becomes a II no
[25:33] other signal is let me called SPH
[25:36] load data will pick B what which would
[25:41] basically turn this be a controller this
[25:43] one plot data okay no data is available
[25:47] for transmission so this signal I should
[25:50] come back we need to declare it also
[26:00] inside state machine storage type
[26:03] initialize to see okay so we made this
[26:11] signal hi and you will remain in this
[26:14] state until the his PA controller says
[26:17] he has finished sending okay how he
[26:19] sends it through this darn signal so let
[26:22] me call this as SPI done let's declare
[26:27] it it's output from
[26:30] woopie was ready to declare it as
[26:32] wild-type and will say if this signal
[26:37] goes high they'll go to the next state
[26:40] and if the signal is not high we are
[26:42] going to stay remain in the same state
[26:44] we are waiting for this play controller
[26:46] to send or not once he sends the signal
[26:49] goes high now remember the complete has
[26:53] we have protocol so he look at this data
[26:55] where is the state which in here he will
[26:57] look at this data
[26:58] he was start sending and finally he is
[27:00] coming to this down state and he would
[27:02] remain in the down state until the load
[27:05] data becomes slow so what we will do is
[27:10] here I would say SPI no that is suprem
[27:18] and let's say what we are supposed to do
[27:21] next when the sequence we have finished
[27:25] this much and we need to remove the
[27:27] reset actually so we will say oh let P
[27:33] underscore n 1 and then we have to wait
[27:48] for again 2 millisecond ok now we
[27:51] already have a state here here which
[27:56] will wait for 2 millisecond but the
[27:59] problem here is from this state will
[28:03] always go to the unit state ok so we
[28:07] will be stuck in a loop like if I just
[28:10] write like state is just like that so
[28:18] from here I will go to delay and I will
[28:20] wait for 2 millisecond I will come back
[28:22] here again I will go back here that's
[28:24] the promise so one way to avoid this is
[28:27] you can create another state maybe we
[28:32] call delay 1 and Cokely face the exit
[28:36] code here and call it delay 1 this is
[28:41] one way to do it but it's not very
[28:43] efficient so
[28:44] yeah if you see we need to millisecond
[28:48] here also so we will have to create
[28:50] another delay state there also so this
[28:52] is one common scenario which we will
[28:55] face when writing state machine okay so
[28:58] let me take your general case and try to
[29:01] explain that so suppose you have a state
[29:05] machine we have let's say states s1 s2
[29:15] s3 s4 and from this one you want to go
[29:24] to s2 from s to you want to go to s3
[29:27] from s3 you want to go back to s2 and if
[29:34] you are coming to s2 from s3 next time
[29:36] you want to go to s4 okay so this is the
[29:39] similar scenario so under this what you
[29:41] have to do is you need some indication
[29:44] some some kind of a flag to indicate
[29:47] from which state you came to s2 so that
[29:51] you can decide from s2 to which state
[29:53] you should go yes I will show you a
[29:55] simple technique how we will do so I am
[29:59] creating another register called
[30:04] something like next state so next step
[30:09] what I will put in next state is to
[30:13] which state I should go once I go to the
[30:18] delay state okay for example here we
[30:22] have state delay and here also I will
[30:27] say next state yes ok so I am going to
[30:32] delay from delay where should I go I
[30:34] will say in it instead of in it here
[30:40] I'll just write next state C so from
[30:43] ideal I am going to delay what I have
[30:46] stored this
[30:48] this information here next state is in
[30:51] it and I will come to relate once
[30:54] delayed on state will be next it so what
[30:57] is the value here in it so I will go to
[30:59] in it now in in it what I will do is
[31:02] next state where I want to go I want to
[31:08] go for this remove reset okay so I will
[31:17] just say is that okay so if I go to
[31:21] delay from idle state from delisted I
[31:27] will go to in its state from in its
[31:29] state when I go to the nest it next it
[31:34] will be so-called the reset state so we
[31:36] will declare all of them think is called
[31:44] reset underscore ID so we will declare
[31:50] the state also equal to 53 or you can
[31:57] make an another variable called previous
[31:59] state also which will indicate from
[32:01] which state you came to be listed and
[32:03] here you can check if previous state is
[32:06] so and so state is so so and so cat so
[32:09] you will have a if else--if or another
[32:12] case statement under the delay state to
[32:15] be side to which state you should go
[32:17] from the delay state based on from which
[32:19] state you came to the delay state so we
[32:23] need to declare next state also again
[32:26] the size of next state will be same as
[32:28] state which we will decide at the end
[32:32] and let's initialize next state also it
[32:35] will write in state it really doesn't
[32:38] matter whether you initialize this one
[32:40] but let's initialize to idle State okay
[32:43] so we set state
[32:49] [Music]
[32:52] and remove the reset action reset equal
[33:00] to one and after this I had to again
[33:05] delay for two milliseconds I think in
[33:07] the slide I forgot to put this condition
[33:11] here wait for two milliseconds here so
[33:19] from this yet I have to again go to the
[33:22] delay state so same technique we used so
[33:25] we'll have static intervenor and from
[33:32] delay we need to go to court charge pump
[33:41] configuration okay so we will call it
[33:47] charge something will declare state so I
[33:54] will go back to list it and again I will
[33:59] come back to okay so now we are in
[34:07] charge pump what I basically have to do
[34:11] is send a command over SPI so it will
[34:16] look again exactly like this far to
[34:21] which command you need to send a 2d
[34:30] there are two values this is a command
[34:34] and this is a value for so called the
[34:38] charge form so you need to send two
[34:40] values through to SPI and transactions
[34:45] so this I will say a 2d lord SPI if SPI
[34:57] done level displays a row
[35:05] no doctor zero okay so here there is no
[35:10] resetting we are done with resetting -
[35:14] just okay there's no delay after that so
[35:25] you don't have to use the next state
[35:26] under this one so it's fine okay okay
[35:36] now here is our next problem
[35:39] okay the problem is our SV a controller
[35:42] it is running at ten megahertz and our
[35:47] pilot control this state machine is
[35:50] running at 100 megahertz so if you make
[35:54] s payload data equal to zero here and if
[35:57] you go to the next state the problem is
[36:00] by the time you reach the next state
[36:02] that is VA control he won't see the
[36:05] signal because he is running at one by
[36:08] tenth of the clock frequency at which
[36:10] this state machine is running okay so
[36:12] that's the problem that that issue is
[36:14] there here also but it's okay here
[36:19] because from here you are going to a
[36:21] delay state and you are waiting for like
[36:23] two millisecond by that time he will
[36:25] definitely see it okay but here that is
[36:28] not the case from this charge form you
[36:31] send a T next you have to send 14 0 X 1
[36:36] 4 through SPI ok that is the next it and
[36:39] so as I mentioned before the problem is
[36:42] the state machine he stuck at this damn
[36:46] state until he sees the load particle
[36:48] tousle now this signal you are making it
[36:54] 0 but by the time you go to the next
[36:56] state he won't see it because his
[36:58] frequency is 1 by tenth of this one so
[37:00] we need a special state let me call it
[37:03] weight SPI and I will wait in that state
[37:09] until the SPI controller sees the signal
[37:12] how do I know whether he saw the signal
[37:15] as soon as he sees the signal he'll make
[37:17] this signal loop so that's why I'm going
[37:21] to find out whether they speak on tronic
[37:23] really saw this load data equal to zero
[37:26] signal okay so what I'll do is wait is
[37:32] PA and I will try it if not SP I don't
[37:37] think that is the signal as we're done
[37:40] that means the signal became zero that
[37:43] means he actually saw the signal equals
[37:46] to zero so where we have to go we have
[37:52] to go to next state which is basically
[37:55] again sending some data through a sphere
[37:58] one form okay so let me call it state is
[38:06] charge pump okay let's call a charge
[38:09] pump one more something charge from one
[38:13] so let's pick the right here
[38:16] 55 and code is smallest exactly same
[38:23] charge pump and data is this time 1 4 1
[38:51] 4 squeal or Tata ton SP a load 0 okay so
[38:56] same issue here also same as our delay
[38:58] thing
[38:59] so after this state also I need to go
[39:01] and wait for SBA to make this signal
[39:05] equal to low so if I just write like
[39:07] this he will come back here it will come
[39:10] back here he will come back here he will
[39:11] come back here so it's in an infinite
[39:13] loop ok so here also what I will do is
[39:16] state equal to next state I'll write
[39:20] like a connect state I will write
[39:26] and here what I should write I should
[39:29] write next date is charge pump one
[39:37] charge pump one so from here he comes
[39:42] here from here he goes here and here and
[39:48] in the game type next date is okay after
[39:55] charge pump I have to configure so
[39:58] called the pre charge so let me call
[40:01] pre-charge we take PA not declare okay
[40:10] because clearly we just VI 86 we also
[40:18] have state recharge
[40:35] charge bomb or not declared so there are
[40:41] some spelling mistake charge from one
[40:56] uniformity okay so now you repeat the
[41:02] same thing so I can't go through base
[41:05] this instead of charge pump this is pre
[41:10] charge in pre charge we are going to
[41:15] send D my end on this field orders PA
[41:23] data after that I had to send F 1 so I
[41:28] am going to call it pre charge one will
[41:36] have pre charge on here we are going to
[41:49] send
[41:50] F 1 there and after that we Pat equal to
[42:03] C okay so let's call it next state is V
[42:08] bad and after that again wait for 2
[42:31] milliseconds so same technique state is
[42:35] delayed and you also have to say next
[42:39] state so that from DNA you can go to the
[42:43] correct state so after we bad wait for
[42:47] to be exact
[42:47] set contrast you can so let me call the
[42:50] next stage
[42:54] okay we have to declare all of them will
[42:59] charge contrast again same SP a
[43:35] transaction 81 + FF so let's say this is
[43:49] contrast 81 will go to contrast 1
[44:10] and then something called segment remap
[44:20] ticket you need to send this wet easy
[44:25] let's say thank you for something
[44:31] [Music]
[44:42] is zero terrific
[44:53] be very careful with the copy-paste
[44:56] actually and from second remap we are
[45:01] setting the scan direction let's call it
[45:04] soft like scan directions and we need to
[45:08] send CC CC scan direction
[45:24] yes sitting in second SEC remap C zero
[45:50] they take a messed up somewhere
[45:52] contracts f5 sacred map
[45:56] [Music]
[45:59] this case is actually is then scan
[46:08] direction is seasonal okay what is
[46:13] correct
[46:16] now we had a company call it called pink
[46:34] one next one
[46:43] zero 0 if F ok we have to declare for
[47:13] these things so contrast one sacred map
[47:21] contrast one
[47:40] scan direction company convene the one
[47:44] they should be contained control D is
[48:00] the shortcut to duplicate align what we
[48:05] can use that scan direction I think
[48:09] there is one more - scan direction yeah
[48:13] there is only one comp inaudible finally
[48:33] something is play okay so we are
[48:44] brutalist tap with the state machine for
[48:46] initialization now how do we know
[48:48] whether the initialization is alright or
[48:50] not one way is to send some data and see
[48:53] whether it is coming on the all that
[48:55] another easiest way is we can send a
[48:59] special command which will turn on all
[49:01] the pixels on the corner okay so that's
[49:06] what I am going to try now science and a
[49:08] special command it is a file and if that
[49:12] command is sent it will turn on every
[49:15] pixel on on it so we will see whether
[49:18] that is working or not
[49:20] okay so let's again hope it is the same
[49:23] thing and I'm just just writing
[49:31] something like full display or something
[49:34] and it is a 5 a 5 and let me say next is
[49:47] something called
[49:54] step cut this done so in this video I am
[49:58] doing only till the initialization part
[50:01] so what I will do is I will keep my
[50:03] state machine in the down state forever
[50:06] once the tree just
[50:07] dunst it and in the next video we will
[50:12] continue with the state machine and at
[50:14] the states for sending data to the
[50:17] visible so display and so 14 15 16 17 18
[50:35] so we have 18 state as of now now to
[50:40] encode 18 state we need 5 bits minimum
[50:43] so this state machine I will declare
[50:46] 4.20 same way next state or side to side
[50:57] that's cube 3 go through the second ok
[51:04] here you can see of some coffee paste
[51:06] issue so from this place
[51:09] next state I have returned display so we
[51:11] are stuck actually here it should have
[51:13] pained careful display please correct it
[51:18] now let's simulate and see whether
[51:20] things are working as expected
[51:23] now in this project you have multiple
[51:26] modules okay now each module should be
[51:28] implemented we usually choose by right
[51:30] click and say set a stop and currently
[51:33] audit control is our top model so this
[51:35] is the one which will be implemented
[51:37] when we run synthesis and implementation
[51:39] now for simulation this is not how you
[51:42] choose which module should be simulated
[51:44] if you have many modules in the same
[51:47] project you should go to settings and
[51:51] simulation here and here you can choose
[51:54] which is the top module for Cindy shop
[51:56] anyway now it is all a control but if
[51:59] you want to simulate our SP controller
[52:01] you have to
[52:03] turn or destiny I don't remember okay
[52:09] SP I control focus we have to change
[52:12] this to SP a control and it will
[52:15] simulate we got drew okay now it will
[52:20] seem that SP a controller actually okay
[52:22] this is how we chose okay let me change
[52:24] it back to back to all that control key
[52:33] and rock simulation behavioral
[52:36] simulation
[52:54] well care these are our top level
[52:58] signals from all at control if you want
[53:01] to see the signals in these soft modules
[53:03] you can add them to the waveform so what
[53:06] we usually do is right you can say a new
[53:08] divider and say delay generator and I
[53:13] click the delay generator here I click
[53:15] on add to 8 so all the way from Dilla
[53:17] generator comes here you divide let us
[53:20] call it SPI control or something and
[53:23] write a spec entrada de showing that
[53:26] instance names here cat not the module
[53:28] name these are the instance names we
[53:30] used TG and SC so right they can say at
[53:38] wait five minutes
[53:41] restart and clock for clock zero warden
[53:50] and then a second these that let's force
[53:54] constant apply reset for some time okay
[54:07] remove the reset force constant one okay
[54:15] what kind of is that is gone now the
[54:20] state should be changing so we went zero
[54:23] I think itís state we came to one which
[54:31] state one is that listed and 10:30
[54:40] listed no these two millisecond yeah
[54:46] okay so we came to the real estate then
[54:51] we went to state 3 which is reset porn
[54:59] war left SP a clock so here something is
[55:02] happening but I sent to the audit in
[55:06] state two so what would we write in
[55:08] state 2 in its state so in unit state we
[55:16] have sending a e I remember we are
[55:18] sending that MS bit first so this is 1 0
[55:22] 1 0 1 0 which is 80 so that is correct
[55:28] actually just keep running it we have to
[55:47] be for I guess it is for King one issue
[56:00] I can see is this delay enable is always
[56:04] stuck at more intelligible to see that
[56:07] this was our counter so it reached 200
[56:15] in a tournament high and because of the
[56:20] logic the way we have written the
[56:23] counter is going back to 0 and again
[56:26] starting from what but the protocol what
[56:29] we wanted to implement was this will go
[56:32] high then delaney will will go low
[56:36] actually
[56:37] that's why he became as this 200,000 and
[56:43] he immediately started coding again
[56:45] because this is cost and it stuck at 1
[56:47] so there is I would be listed here so we
[56:52] made the start delay high here and once
[56:54] delay turned we forgot to make it
[57:03] okay only other issue that I find is the
[57:09] VDD is constantly stuck to nobility is
[57:16] fine
[57:17] we but is somehow constantly step one be
[57:20] better than a dildo signal so that also
[57:23] we need to cut out here be back yes so
[57:31] we need to make itself otherwise
[57:34] everything looks fine state machine goes
[57:38] in 18 which is lasted and it remains in
[57:41] state 280 now once you are done with
[57:45] simulation you can go ahead and do
[57:49] synthesis after synthesis you have to do
[57:53] in assignment I have already done it in
[57:56] the background so you need to look at
[57:59] the data sheet that port and see where
[58:01] each pin is connected to the Zynq shape
[58:04] due to the SDC file and the power
[58:07] constrain after that you go ahead and do
[58:10] implementation and generate bit string
[58:13] once you generate bit stream so you need
[58:22] to do everything we have already done it
[58:29] program device and once you program this
[58:37] is how the world should look like okay
[58:39] all the pixels are turned on because of
[58:43] our laughable if I comment so if I plus
[58:47] three front it will become dim so once I
[58:52] release or pixels don't so okay so
[58:58] that's all in this video in the next
[59:03] video we will continue so we will remove
[59:08] this full display and done may be full
[59:11] display from here
[59:12] and expand the state machine so that we
[59:15] can send some some string to the alert
[59:18] and see it thank
