# Generating Custom User IP Core in Vivado

[00:00] hello or welcome back in our previous video we have seen how to use the IP integrator available in V Vivado to integrate different IP calls and build an entire system so in this video what I am trying to show you is how to create your own IP go okay so how to start from with log and finally get the wrong

[00:00] description of block level representation of your IP that's what I am trying to cover in this video so we'll start with a very simple like we actually basically an IP to control the switches an LED similar to the GPIO IUD that you have used but later we will have more complex IP like once we complete all our controller code we will

[00:00] convert it into IP format so that you can directly control the logic from the processor through software now when you design an IP one of the first questions is what should be the interface of the IP I am NOT talking specific to Vivado but in system-on-chip design in general whenever you design an IP you need to

[00:01] decide how your IP will be integrated with the rest of your system now our aim is to build something which will be interface with PS part of Z and the only interface available to PS is AXI for interface so we'll be designing our IP which has an AXI for interface now another question will be whether your IP

[00:01] should be a master or a slave so in most of the time your IP will be a slave that means all the AXI transactions read and write operations will be initiated by the processor and your IP will be just following what our transaction is coming from the processor but in certain cases your IP has to be a master this is

[00:02] specifically true if your IP has to access the external DDR connected to Zynq chip through the HP port of p.m. in that case your IP has to be a master so that we'll see later the IP that we are going to different today is a simple GPIO IP so that will be a slave IP and so these are the two important factors I was an important thing again

[00:02] in last lab you have seen actually hi how an IP works what is inside an IP basically you will have a core logic of the IP and there will be a number of registers actually inside an IP so the processor is actually reading and writing from these registers and based on the register values some other things

[00:02] may be happily okay so the actual interface to the processor is through the registers inside the IP now how many registered IP inside an IP depends upon the functionality of the IP so again at design stage we will decide how mid register should be there what each registry is supposed to do and then what

[00:03] should be the address for each register so on and so forth okay so I hope it will be clearer once we complete our current project so as I mentioned before we are going to design an IP for controlling any design switches so my basic plan is I will have a register inside the IP and this register I will

[00:03] connect to the pins of the IP external interface of the IP which will be subsequently connected to the LEDs on the pole so if the processor wants to control the LED it just has to write to this register so basically I need one register to interface with the LED now another register might be interface with

[00:04] the switches so if the processor wants to read the switch position how many are on or off just has to read from the second register so basically I need only two registers one set of register is connected to LED and the other set of other register put a set of friends other register connected the slide switches pressed so that's my

[00:04] my whole requirement now let's see how do you start so I am starting it as a new project again and I'm calling my project let's say I generate project or something and giving it as a separate tree and all okay so once you get this window you should go to tools and choose create and package you might be and you will get

[00:05] this wizard and here you have multiple choices and there seems we are going to create a XE slave IP you should choose this option create XE for pitiful create new mexic for pitiful okay choose that option next and here again this is an industry standard told me water so you can specify the name of the IP the name

[00:05] of your company what your IP does or the information here so I'm going to call my IP as okay let's say GPI you control that's the name of the IP this is a first version initial version and you can write the description here IP to control these switches now here this is a very important setting so we borrow is

[00:06] basically asking where the files generated for this IP should be stored so that you should be very careful so I would suggest you create a separate folder and inside that folder you create subfolders where you will store your files associated with individual IP ok so what I am doing is in D Drive and I

[00:06] have created a new folder called IP unifo inside that let me create a new folder and we call GPIO control so all my IP will be stored in this IP wrapper folder and I will put them in different different sub folder as I create them now next and here basically he is asking what should be the name of the access

[00:07] slave interface to your IP so when you add your IP to your GUI the block is I need to look like this he's asking what this interface should be call it doesn't matter what you call it so keep it as 0xe interface type this you should read the AXI documentation there are actually three kinds of XE available lightful and stream so for

[00:07] medium performance actually light interface is good enough if you want high-performance communication we'll have to go with AXA food because it supports something called the mass transfer so I am doing a simple eyepiece I'm keeping light and this is where you choose the mode whether your IP should be a master honestly you have slave data

[00:08] width it is 32 fixed and how many register should be there inside your IP so the mirror number supported here is 4 now you will get the original source code for this IP there you can you can change the number of registries and all but in the GUI although I need only 2 I cannot set 2 so we have to go with the 4

[00:08] so keep it for next and this is important again when you come to this last page there is an option called edit IP ok so basically what happens is Bovada will open a new project where you'll be able to see the source code for the IP that you are generating and you will be able to edit that source code ok and save it if you want to make

[00:09] any changes to your IP so choose this option edit IP then click finish now if you go to the folder where I specified to create the IP this one you will see like a lot of files have been created and you see a project called ad GPU control dot X fear ok so this project is automatically created and we want no

[00:09] orphans that project also this is that project it is GPA control where you would be able to edit the Whitlock's or score and other settings then you'll have this for last GPU control 1.0 inside that again you will see a bunch of folder and a file for comfort on dot XML so as far as an IP is concerned the most important file is

[00:09] this one component or XML this is a XML file okay now these file stores all the information about your IP in a text format for example it has information about what is my interface type what are the different signals belonging to this interface where your source codes are stored all these information are stored

[00:10] in this XML file so as far as signing fee is concerned when they say the the IP file in most cases they mean this component dot XML and the data stored here follows a particular standard called the IP exact standard this one I px Act this is again an industry standard for storing information about IP course not only in Vivado

[00:10] this is an industry standard across different tools now in the other folders you will see there is a folder called HDL inside that there are two files automatically created this has a low code for your IP there is another folder called driver which has some C sample code for testing your IP using SDK it

[00:11] also has [Music] Beadie folder which has information about the broad design how to integrate your IP when you are using it in a blog design it also has a folder called xqe which has the information about how your IP should be shown like a block when you go to the block beside the graphical information about your IP okay so this

[00:11] folder is very important this is the most important for that all others are temporary folders actually you can delete them if you wish to but keep them there as I mentioned before from that original project once you choose edit IP you are automatically creates this new project and he opens it and this is how

[00:12] it will look like when you open first time now here in the in the window you can see lot of information about your IP for example the company which is producing this IP now by default it will be Xilinx if you have your own company you can give you a company name and the name of your IP the version description

[00:12] or the information it also has information about which FPGA this IP is targeting okay so this should be some domain name it seems okay so let's call it so it is basically saying this IP is compatible with Zynq ok so the IP compatibility is with reference to the chip not with reference to the port so this IP can be used with

[00:13] any z chip anything chip basically if you want to make it compatible with other families of chip ok you can do it I can add here and other refugees these are all different if VG's from Xilinx so what happens is later when you are when you or other people try to use your IP in a particular project we were I will always

[00:13] check whether this IP is compatible with this particular chip and if not he won't let you add that to the project under file group you will see all the information which all files are part of this IP this is the middle of source code for your IP these are the simulation shows which is same we look so is the example C code he

[00:14] automatically added you a layer this is the graphical information block diagram so basically all these files coming from this folder cat so they are automatically listed customization parameter we'll come to that later ports and interfaces the port your IP is XE interface this is an ACCI slave interface and addressing and memory make

[00:14] not with your xi here when you add it to the block design you will see like these are truss and hi address for your IP automatically coming and GUI how your IP will look it will look like this in the brock this side ok now from where this screen is coming this screen is actually coming from this component or XML file

[00:15] this is file that your so here so if you open it in a text editor this is how that file looks like when that the file is opened in Rivaldo this wire when you double-click this file in Vivado this is how it looks like so basically you are we were now reads information from this XML file and extracts the information

[00:15] let's look at the visual code okay so basically Roberto he will generate two files for you one file will be called the name of the IP that you give dot read and it will instantiate another module called name of your IP underscore name of the AXI interface in this case s double zero axis intercepts now what these files are basically doing

[00:16] is it automatically implements the logic for interfacing your IP with ax e for interface so if any AXI so this is a AXI slave interface XO you can see many signals out there the nice thing is you don't have to remember the exit protocol so any read or write operation coming through the XE interface will go through

[00:16] this interface and the code for following that protocol is already provided by psionics now if you come to this file inside the stop file you will see some parameters are declared here for example FX e across with these four as sexy data with these 32 so it's going to use 32-bit data the address it is going to use is

[00:17] lower for bit well you will see why it is so it is because the number of registers that you ask to instantiate within this IP is 4 that's why this number became 4 there now let's see here yeah if you come to this line 107 you can see they have already declared four registers here slave rich so grossly

[00:17] rich once a rich to slave h3 right and their width each of them is 32 feet wide fine now if you come little bit further you will find the code where data is written into this register so it Smit complicated actually because they are using a lot of all of the north production code is very simple actually

[00:18] now basically what is written here is if flavor rich right enable is high so this signal will become high whenever the processor wants to fight to a XE flavy and the address of that IP is matching okay so you can see on the top how this signal is generated this is not a standard AXI signal but these are accessing Nell's actually

[00:18] coming from the ax interface so if try to valid right address ready a K right data valid and right data ready if all these conditions are true this signal will become high you will have to read the AXI for protocol specification to understand what each signal sir but basically they all become high whenever

[00:19] the processor is writing so if the signal is high they are checking the address coming from the processor okay so if the address coming from the processor after subtracting the base address from that address and dividing it by 4 that is this guy if that is 0 whatever data is coming from the processor gets stored in slave register

[00:19] if it is 1 what are coming from processor if in flavor h1 slave reg - slave reg 3 otherwise if there is no write operation every register keeps its previous value ok so basically this is the part where data coming from the processor gets 2 into an internal register same way if you come little bit down

[00:19] [Music] this is the part where the register data is going to the credit processor so you will see the code is quite similar he is checking the read address from the processor and if the read atrás - a fortress divided by four you are dividing it by four because each register is four bytes actually so the addresses increases by

[00:20] four from processor point of view but inside the hardware the addresses are incrementing by one so this is the logic for doing that anyway so if the processor is really from address zero content of register zero goes here which subsequently goes to the processor same way if reading from address one register

[00:20] one goes to the processor yeah register two goes to the processor register three goes to the process okay so this is the code which is provided by eye filings okay so this is a basic template for reading and writing from registers through XE interface now depending upon your application what you want to do

[00:21] using your IP you will have to add something to this code or you have to modify code so I convey to the processor so that's what my day so that that additional information I will have to add so how do we do it so if I go to the again the first file here you will see the inputs and outputs from my IP and

[00:21] you will notice the only input output is the X interface even in the GUI also you can see this is how do I look like the only interface to the IP Easter is the XE interface now what are they shoe interface I need I need a additional interface to the LEDs a twice I need an additional interface to the switches a

[00:22] twice so that I can interface this IP to LEDs and switches so I'm going to add that information here so what I'm doing is okay you serve four airports here so that is a comment here you can add actually wherever you want but that I add we're designing stuff this to add so I will say output seven down to zero

[00:22] and input 73 switches I am adding these two additional interface to my IP this I did in the power file next what I should do these LEDs should be connected to register 0 so that whenever process arrives something to register 0 that gets reflected using the LEDs so these wires I have to somehow connect to

[00:23] register 0 which is inside this module inside this module ok so basically I will add these ports here also ok so I added them here for instantiation that means I should also add here also so same thing I will add here also here so put LEDs input switches know what I will do I will just write ok somewhere here

[00:24] you can where you want assign L it is so now whenever Francis I rise to say average zero that will go here to these wires which is going as output from this module that will come here come here and will finally go as output okay so it is very easier now switches little bit tricky so I have switches coming as

[00:25] input through pins and I need to connect them to the register war now I already have a logic to write something to the register one here okay so this this code as we discussed before is for the processor to write to register or I don't want processor to write to register one I want to write the position of the switches to register one

[00:25] so what you should do you need to modify this part of the code now remember the rule you cannot have water flame same register in more than one or miss block so you cannot you cannot just write like this because the problem is if condition is under this condition if leverage right is 1 and if address is 1 then

[00:26] switch equal to 0 h1 this doesn't make sense because this basically means if the processor is writing and if the address is matching then the content of switch should go to sleep register 1 no what I want is the switches should be always connected to Slayer h1 so what I will do is I will take the flavor h1 from here

[00:26] and I will just put it under this always block outside this condition I put it outside this condition and I will remove this cone which corresponds to writing data from processor just leverage one I am putting it here ok slayage 0 is perfectly fine I want the processor to write to slave edge to it also that that

[00:27] goes to the indeed make sense but Slayer h1 I don't want the processor to right there I want that data from the switches to be directly stored them now 2 3 we are not going to use it so let them be there and this code it is fine this basically means slave h1 retains the previous value if you wish you can

[00:27] delete this also now things looks perfectly fine this code is correct but usually what we will do is we provide this entire thing as a separate always box so that the code is more readable actually so I am taking it from there and putting it here and also this reset condition copying it there and I'm

[00:28] cutting it here because you cannot have slave h1 inside - always block so I am taking it from there and putting it here we can and [Music] that's it so we have done we have edited the IP source code no it is the thing if you make any modification to the source code okay you need to update things in this

[00:29] component dot XML file so you need to double click here when you come here you will see those green tick marks have gone here and it showing some picture of the file that means you have modified something in the IP source code so you you go here and click merge changes from file group friesshardt ok and you'll see now they are back to

[00:29] green now the interesting thing is if you come to GOI here now you will see it is showing LEDs switches here now Xilinx they follow a certain style the outputs will be always listed on the right and the inputs will be lef listed on the left that's why switches are on the left and LEDs are on the right so later whenever

[00:30] you use your IP in the rock design this is how your IP is going to look like ok now come back and review and package and you need to click repackage so that all these changes are updated in the component dot XML but there is an important step before that you need to click on this one edit packaging settings and there is this option check

[00:30] here delete project after package ok why do you fall this is check that means once you click repackage IP he will he will save all your changes and this project will close ad GPIO control dot X square project will close and that project will be at all so now the problem with that if later if you want to again update your

[00:30] IP if you want to change any modification it will be very difficult because you don't have this Vivado project to do it you will have to create a new project and add all the source code there it could be a big headache so make sure this is unchecked so that when this project is closed this project is

[00:31] not deleted and if you want to make any modification data you can always come back and double click and often and make all the modification okay so if it is make sure it is unchecked and OK and click repack edit so he he'll say like finish packaging he has updated all the information to this component or XML now

[00:31] you can close the project ok address so this is our original project from where we started so I created an IP from here so he created an IP he opened a new part of project for editing that IP I used that project to edit my IP then I repack packaged it I saved it I saved the IP and that's it and all that information is actually sitting

[00:32] inside this folder and component or XML is sitting inside this one now let's try to use that IP in a block decide ok so I am using the same project IP generator project dot xpr ok create a block design and let's try to add our new IP to this project ok so first let me add processing system ok the processing system

[00:33] I had automation block automation and that IP remember our IP name was I think GPIO control remember GPA control so that is automatically listed here so just double click it and you can see our right [Music] okay now let's try to use our IP in a blog design okay so look at now let's try to use our IP in a blog design so we

[00:35] already have this project open from me where we actually started our initial IP generation under tools create and packaging ID but over to make things clearer let me create a new project actually and let me call it test my GPIO something creating a completely new project because that initial project okay so in future also whenever I want

[00:36] to create a new IP I will leave and [Music] start from this IP generator project and choose create a new IP then I get a new project I will create the IP there close okay so this project I am going to use just as a base Avada project to start a new IP that's that nothing else okay so here let's come to create block beside

[00:36] like we did in the flap and choosing well caught emission okay let me try to add our new IP which is GPIO control right GPU control now you'll see like that IP is not listed we have only AXI GPA which is the filings GPIO IP so this is the thing by default your IP will not be listed in the IP category you need to tell me

[00:37] waddle which or location he should search for user-defined IP or IP is created by you so what you should do is you should go to settings and there is an option here IP and there is a pure poetry and you need to browse go to the folder where you have kept this component dot XML file now the good thing is he will keep on searching in

[00:37] supplier tree after subdirectory so it is enough to show him this folder IP rapoo and he will go inside that and keep on searching so that's why I created a folder called IP rapport and I'm going to keep all my eyepiece as subfolders here so that I just add this folder and we wada will find out all the

[00:38] heipiess within this folder cat so I am going there and choosing this one IP rapport select and you can see like he actually for my IP GPU control version 1 ok ok now if I click here and search for GPI you is also listed so double click it it comes to the block design you can see it looks exactly like that you

[00:38] warned me so then we create the IP you can click on connection automation and it gets connected to the processor okay so this one is connected to the interconnect which is actually connected to the processor this is the clock this is the reset the only thing which are not connected these two the LEDs and

[00:39] switches I guess so unlike Vivar dos GPA your controller they do not automatically get connected to LEDs and switches that you have to do manually so what you should do is you need to click on this interface right click and say make external so basically you are saying this interface is connected to some pins of the chip they are connected

[00:39] to the outside world of the chip okay so same thing for both make external now this is connected to switches this is connected to LEDs now in this case the pin constraints you should do manually okay so you should save you block design and you should run synthesis top module so we didn't click generate wrapper

[00:40] create a shield wrapper okay okay you need to run synthesis and after synthesis you need to go to I of planning and dope in constraint for LEDs and switches that doesn't happen automatically in this case because he doesn't know only because we call them LEDs doesn't mean they will be automatically connected to it okay so so

[00:40] you need to manually do pin assignment after synthesis you can go synthesis okay if you go to address editor you will see GPIO control the base address is automatically assigned so when you write the software if you want to write to LEDs you just write to this base address if you want to read from the switches you need to

[00:41] read from the base address plus form because witches are connected to reg1 and although in the code you you so like the address of register one is one it is internally divided by four or the addresses so from processor point of view that register address is still for Jack so keep that in mind so when you

[00:41] are reading you should read from this address plus four so you get the switch status and when you are writing you should try to the base address so that it goes to that led so the code will look exactly like the code that you already wrote for controlling the axe signs XV GPA you call no difference now

[00:42] let it run here in parallel I would like to show you one more thing now remember the signings GPIO there was an off friend when you double-click the IP you can edit some parameters like what should be the width of the GPIO interface and such things right so you can do the same thing here also currently these are options coming and

[00:42] you can't edit any of them actually okay so that feature we will add why I am doing it because this eight LEDs and eight sites which is they are specific to Z port suppose you want to use the same IP with another board you should be able to do it and suppose star port has only five unity even on the port suppose

[00:43] you want to connect this interface to the five push-button instead of the eight slide switches so this should be four down to zero instead of seven down to sit so there should be some options for customization so that's also possible so to do that again we have to edit our original IP that's why as I said before it's important to have

[00:43] this project which was used for editing decidely so I'm going and opening that project again this project okay no don't close this project let it run so what we need to do is here we have hard-coded [Music] seven down to zero led and seven down to zero switches instead of that you should parametrize them so let me say for our

[00:44] meat and let's say integer type parameter or you can just neglect it or so a lady with let's say eight and another parameter switch with equal to let's say eight okay when instead of seven down to zero here I will say led with -1 and here switch with - home make sense it's the same thing we have to do

[00:45] so they took these two parameters here also X 2 here also ok so where we have LEDs the lead is equal to slave register actually the width of flavor is 0 if you see is is 32 actually okay so when you assign a 32-bit bit white register to 8-bit LED it will always start from the LS bit also the lower eight are going

[00:45] here so it's perfectly fine this weed can work up to 32 actually fine so we have changed the source code one more thing is here we need to do the parameter mapping so this led width that I am specifying on the top module should be propagated to this module the instantiated work for that we need to do

[00:46] so-called port like port mapping we need to do something or the parameter mapping so which is similar so you take the parameter in the sub module which is a little width and you map it to this parameter on the top module can so it will look like [Music] switch with switch and set okay so the syntax there is module name parameter

[00:47] mapping instance name 420 okay save it and often our IP extract now and now you'll see final customisation parameter there is some change thing here if you click yeah and click merge changes from customization parameter wizard you will see our two parameters listed here hidden parameter is led width and switch

[00:47] width now we don't want them to be hidden so double click it and choose feasible in customization GUI and you can give the default value age okay you let me switch with visible default value 8 okay and go to review my package and say we package our forum somewhere else okay I'm going to close it now I'm

[00:48] coming back to my old project so as I mentioned before synthesis is over so you should do the pin constrain for both LEDs and switches and implement test on hardware that you can do what I wanted to show us let me reopen the block design when I reopen the block design you will see a warning here I pick at

[00:48] low he's out of date so we were automatically found out something has changed just change to the IP which is used in your block design okay so this IP was already used but in parallel II you edited it so he found it out so we had to pick this one refresh IP and at the bottom he will show something about

[00:49] IP status and he's saying like GPA you control that IP has changed and you need to upgrade it so I'm just clicking upgrade selected okay things got created now if you double click it you will see these too often here LED width switch width and they are eight now if you want to change them to five we can change it to five and that

[00:49] gets reflected here so it became four down to zero instead of 7.20 right this is how you can create customization so you are actually changing in the GUI but what happens is here itself I can show you near hierarchy you can see this option IP sources so if I expand that you can you need to say something like generate

[00:50] output product give me a second I just wanted to show what everybody is doing in the background what he actually does is he actually goes and fetches all those late look source code from the from the folder where you have kept them and you can see this is exactly the source code that we were using see this is the

[00:51] source code which we which we actually save and he modifies whatever change we are doing in the GUI in that source code for example them if we change the width here in the GUI that will get reflected in the weight load source code there again so that's what he is basically doing so that's why if you change any

[00:51] parameter here in the GUI you have to reset the size and three implement because you are effectively changing into a clock source code okay so the remaining you can try yourself you can do pin assignment you can implement and you can export to SDK and you can test whether your IP code is working on thank

[00:52] you