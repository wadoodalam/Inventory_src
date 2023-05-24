
## Minecraft Server Tutorial and Deployment

We will be creating our own minecraft server for the JAVA version using AWS EC-2 instance(Amazon Linux 2 AMI) and linux. We will be able to manually and automatically start and stop the server. 

## Table of Contents

- [Tools Required](#tools-required)
- [AWS Instance Creation](#aws-instance-creation)
- [Connect to EC2-Instance](#connect-to-ec2-instance)
- [Install Java](#install-java)
- [Install Minecraft](#install-minecraft)
- [Run Minecraft Server](#run-minecraft-server)
- [Autostart Minecraft Server](#autostart-minecraft-server)


## Tools Required

In order to successfully deploy our server, we would need access to/install the following list of tools:
- AWS
- Linux terminal / SSH access
- curl
- Java (version > 16)
- Minecraft
- Vim or any other text editor

## AWS Instance Creation

The first step towards our own minecraft server is to create an EC-2 instance in AWS.
1. Open the EC2 Dashborad and clock on the 'Launch Instance' button
2. Give it a name and pick Amazon Linux 2 AMI(x86) as the OS image
3. For 'Instance Type', select 't2.medium'
4. Select a key pair or create a new key pair if you don't already have one(and download it on one of your local directory). We will be using this to ssh into our ec-2 machine.
![Screenshot 2023-05-23 at 7 42 56 PM](https://github.com/wadoodalam/Inventory_src/assets/42946189/99e32c51-d529-4331-9525-f1ae3b4431ff)


5. Clock Edit for the 'Network Settings' and add an inboud rule with the following configuration(leave the default on as is):
  - Type: Custom TCP 
  - Protocol: TCP
  - Port Range: 25565
  - Source Type: Anywhere

![Screenshot 2023-05-23 at 7 45 25 PM](https://github.com/wadoodalam/Inventory_src/assets/42946189/88d77c06-334e-46fc-9f3d-2ac4f4e7d1e2)


6. Now you can launch the instance!

## Connect to EC2-Instance
1. Find SSH command
  - Go to the EC2 dashboard and click on 'Instances'.
  - Click on the 'Minecraft' instance you just created and then click connect
  - Navigate to 'SSH Client' and copy the command to ssh into the instance.
  ![Screenshot 2023-05-23 at 7 47 46 PM](https://github.com/wadoodalam/Inventory_src/assets/42946189/e72ffd8f-8608-4df0-b874-463e2c01858f)
  
2. Connect using linux / terminal
  - Go to the directory in which you downloaded your key-pair file(step 4 in AWS instance creation)
  - Run ```chmod 400 <keyfilename.pem>```. Note that your need to replace the 'keyfilename.pem' with your own file name
  - Now, run the command you copied in step 1. This should allow you to access your instance. It should something like this:
  <img width="875" alt="Screenshot 2023-05-23 at 7 55 03 PM" src="https://github.com/wadoodalam/Inventory_src/assets/42946189/aa697a8f-2695-41e8-887a-c31c69904c7c">



## Install Java
Now we need to install java. To do so, we will run the following commands:
1. ```sudo rpm --import https://yum.corretto.aws/corretto.key```
2. ```sudo curl -L -o /etc/yum.repos.d/corretto.repo https://yum.corretto.aws/corretto.repo```
3. Once it is these commands are run successfully, we can now the command to install Amazon Corretto 20
  ```sudo yum install -y java-20-amazon-corretto-devel```
4. Once Amazon Corretto is installed, you can verify the java version by the command ```java -version```. You should get a response something like this:
<img width="714" alt="Screenshot 2023-05-23 at 8 02 43 PM" src="https://github.com/wadoodalam/Inventory_src/assets/42946189/bfa1b4c4-1d04-4c0c-aa7c-b49a873e1a50">

## Install Minecraft
Now that we have java on our machine, now let us install minecraft and run the server
1. Set up a dedicated user to run the server: ```sudo adduser minecraft```
2. Now let us create folder and server folder for minecraft:
```
sudo su # This will change you from ec2-user to root
mkdir /opt/minecraft/
mkdir /opt/minecraft/server/
```
3. Now navigate to the directory we just created by: ```cd /opt/minecraft/server```
4. Now downlaod minecraft by running the command: 
```wget https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar```
5. Once you have successfully donwloaded minecraft you can verify by the ```ls``` command and it should show "server.jar"
6. Now, we set the user for the folder: ```sudo chown -R minecraft:minecraft /opt/minecraft/```

Voila! You have minecraft installed!

## Run Minecraft Server
- Please ensure that you have root access and are in the server directory (step 2 & 3 of Install Minecraft)
1. We need to edit the 'eula.txt' file and change eula to True:
  - Run the command: ```vi eula.txt```
  - change eula=false to eula=true
 <img width="1012" alt="Screenshot 2023-05-23 at 8 18 19 PM" src="https://github.com/wadoodalam/Inventory_src/assets/42946189/c42b2505-5c0e-4e28-88ab-4924b8a59915">
 
2. Once you are done with that you can finally run the command to start the minecraft server:```java -Xmx1024M -Xms1024M -jar server.jar nogui```

<img width="1407" alt="Screenshot 2023-05-23 at 8 23 35 PM" src="https://github.com/wadoodalam/Inventory_src/assets/42946189/1381d519-af88-4a99-883e-d258eab5b544">


3) Now navigate to your EC2 dashboard and and the get the public IP/IPv4 address of your minecraft instance to access your minecraft server.


## Autostart Minecraft Server
Now let us look at how to automatically start our minecraft server as soon as the instance starts running.
- Once you are ssh'd into your instance as root, run the following to create/edit minecraft.service file which will help us with auto-starting the server. 
  - Run the command: ```sudo vim /etc/systemd/system/minecraft.service```
  - Now edit the file with the following info:
    ```
    [Unit]
    Description=Minecraft Server
    After=network.target

    [Service]
    User=minecraft
    WorkingDirectory=/opt/minecraft/server
    ExecStart=/usr/bin/java -Xmx1024M -Xms1024M -jar server.jar nogui

    Restart=always
    RestartSec=30

    RemainAfterExit=true

    [Install]
    WantedBy=multi-user.target
     ```
  - Now we will use ```systemctl``` to enable and start the by running the following commands:
    - ``` sudo systemctl enable minecraft.service```
    - ``` sudo systemctl start minecraft.service```
- The next time you your instance will reboot, your minecraft server will restart automatically. You can also confirm this by ssh'ing in your instance and the running the command ```systemctl status minecraft```.
