CS1660 Final project Option 1 Microservices- Author Runyuan Yan-"ruy16
@pitt.edu"
Link to the video: https://pitt-my.sharepoint.com/:v:/g/personal/ruy16_pitt_edu/EZpi4iPM_i9KlAHHQItwuK8BgH1VQ_C5ps4TWhW2XSWFbg?e=T7AoYa
Before you start,
You need to set at least 6G of memory, 3cpus,and 30 GB of free disk memory for your docker in order for everything to run smoothly as possible!!!!!!!!!!!!
You can go to resources to tune up the settings, this is important considering the amount of services needed to run
#################################################################################################################
You will need to have JVM pre-installed for sonnar scan
#################################################################################################################
Git clone then,
CD into the directory where the docker-compose.ymal file is.
Run docker-compose up --build -d to start the containers
Run ./sonar-bash.sh for linux and Mac
Run sonar-windows.batch for windows
This gets the sonar scanner needed 
***Note: It may take a while to 'compose' everything and to initilize the containers, be patient...
***Wait for at least 2-3 mintues for every application to be ready after the compose(depending on your resources setting).
---------------------------------------------------------------------------------------------------------------------------------
Go to localhost:80 to access the toolbox homepage and try out the apps!
I recommend openning each link as a new tab, easier to get back to the homepage.
#######################################################################################
Instructions and notes for each app
#######################################################################################
Rstudio:
Startup time: 1:30 mins
If it says unable to connect, just refresh
####################################################################################################################
Spyter:
Startup time: 20-50 sec
There are two options for openning SpyterIDE
click link: Wait for binder to do its thing and when it's done Just click the Spyter Icon to open the IDE
This may take a while you can go to other apps if it's taking a while
###################################################################################
Orange:
Startup time: 20 - 40 sec
password:orange
Click the icon to start
And wait for Orange to launch, may be a bit slow.
##############################################################################
SAS Studio LOGIN:
username: ruy16@pitt.edu
password: Cloud-computing123
Click SAS Studio on the left
#############################################################################
Tableau Login:
username: yryoliver@gmail.com
password: Cloud-computing123
##############################################################################
Git:
Startup time: 10 - 15 sec
Click connect
#############################################################################
Jupyter-notebook
Starup time: 1 - 3 sec
##############################################################################
Vscode
Starip time: 1 - 5 sec
###############################################################################
Apache Hadoop
Password:vncpassword
Go to Applications on the left upper connor and open Terminal emulator to use hadoop
You can also run a wordcount example in this terminal, simply run ./wordcount.sh
Startup time: 5 - 10 sec
##################################################################################
Apache Spark:
This will open a jupyter terminal 
Starup time: 5 -10 sec
spark-submit --version
spark-shell --version
spark-sql --version
################################################################################
Tensorflow:
Click connect
Startup time: 10 sec
Show version: pip show tensorflow
The image already contains an example tensorflow program, here is the link for its description: https://github.com/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb
To run it: python3 /app/quickstartKeras.py
It trains a model to classify images, you can see the trainning process and the result of the trainning.
##################################################################
SonarQube and SonarScanner:
Login -
username: admin 
password: admin
After you click the link
	.Make a new project make sure to use pythoncode as the project key if you are scanning a python project
	.For java code follow the instructions on the website.For python, cd to you project directory and run  "sonar-scanner" on the CLI, after it finishes, you will see a link to see the result. 





	