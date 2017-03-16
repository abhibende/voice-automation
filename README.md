# voice-automation
The voice instruction for your server.

INSTALLATION:
	
	1.) Install node ==> yum install nodejs/apt-get install nodejs
	2.) npm install pm2 -g
	3.) pm2 start voice.py

	NOTE : Change the port no if required from voice.py, default is port 80
	Eg: If you want 9000 port then, sed -i s:port=80:port=9000:g voice.py

USAGE:

	1.) open chrome browser from your desktop/mobile, hit the url http://<server ip>:<port>/home
	2.) Click on the microphone mic and just say the command.

COMMANDS:
	shutdown, restart, date, hostname, ip and lots more to come.
