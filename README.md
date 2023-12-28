# Melissa - Right Fielder Object Linux Python3

## Purpose

This code showcases the Melissa Right Fielder Object using Python3

Please feel free to copy or embed this code to your own project. Happy coding!

For the latest Melissa Right Fielder Object release notes, please visit: https://releasenotes.melissa.com/on-premise-api/rightfielder-object/

The console will ask the user for:

- Right Fielder Input (rfinput)

And return 

- Address Line 1
- Address Line 2
- City
- State
- Zip
- Result Codes

## Tested Environments

- Linux 64-bit Python 3.8.7, Ubuntu 20.04.05 LTS
- Melissa data files for 2023-12

## Required File(s) and Programs

#### libmdRightFielder.so

This is the c++ code of the Melissa Object.

#### Data File(s)
- mdRightFielder.cfg
- mdRightFielder.dat

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

This project is compatible with Python3

#### Install Python3
Before starting, make sure that Python3 has been correctly installed on your machine and your environment paths are configured. 

You can download Python here: 
https://www.python.org/downloads/

You can check that your environment is set up correctly by opening a command prompt window and typing the following:
`python3 --version`

![alt text](/screenshots/python_version.PNG)

If you see the version number then you have installed Python3 and set up your environment paths correctly!

----------------------------------------

#### Download this project
```
$ git clone https://github.com/MelissaData/RightFielderObject-Python3-Linux
$ cd RightFielderObject-Python3-Linux
```

#### Set up Melissa Updater 


Melissa Updater is a CLI application allowing the user to update their Melissa applications/data. 

- In the root directory of the project, create a folder called `MelissaUpdater` by using the command: 

  `mkdir MelissaUpdater`

- Enter the newly created folder using the command:

  `cd MelissaUpdater`

- Proceed to install the Melissa Updater using the curl command: 

  `curl -L -O https://releases.melissadata.net/Download/Library/LINUX/NET/ANY/latest/MelissaUpdater`

- After the Melissa Updater is installed, you will need to change the Melissa Updater to an executable using the command:

  `chmod +x MelissaUpdater`

- Now that the Melissa Updater is set up, you can now proceed to move back into the project folder by using the command:
  
   `cd ..`

----------------------------------------

#### Different ways to get data file(s)

1.  Using Melissa Updater
	- It will handle all of the data download/path and .so file(s) for you. 
2.  If you already have the latest DQS Release (ZIP), you can find the data file(s) and .so file(s) in there
	- Use the location of where you copied/installed the data and update the "DataPath" variable in the bash script.
	- Copy all the .so file(s) mentioned above into the `MelissaRightFielderObjectLinuxPython3` project folder.

----------------------------------------

#### Change Bash Script Permissions

To be able to run the bash script, you must first make it an executable using the command:

`chmod +x MelissaRightFielderObjectLinuxPython3.sh`

Then you need to add permissions to the build directory with the command:

`chmod +rwx MelissaRightFielderObjectLinuxPython3`

As an indicator, the filename will change colors once it becomes an executable.

You may also need to alter permissions for the python files. To do this navigate into the MelissaRightFielderObjectLinuxPython3 directory and run these commands: \
`chmod +rx MelissaRightFielderObjectLinuxPython3/MelissaRightFielderObjectLinuxPython3.py` \
`chmod +rx MelissaRightFielderObjectLinuxPython3/mdRightFielder_pythoncode.py`

## Run Bash Script

Parameters:
- -r or --rfinput: a test right fielder input to parse
 	
  This is convenient when you want to get results for a specific right fielder input in one run instead of testing multiple right fielder inputs in interactive mode.  

- -l or --license (optional): a license string to test the Right Fielder Object  
- -q or --quiet (optional): add to the command if you do not want to get any console output from the Melissa Updater

When you have modified the script to match your data location, let's run the script. There are two modes:
- Interactive 

	The script will prompt the user for the right fielder input, then use the provided right fielder input to test the Right Fielder Object. For example:
	```
	$ ./MelissaRightFielderObjectLinuxPython3.sh
	```
    For quiet mode:
    ```
    $ ./MelissaRightFielderObjectLinuxPython3.sh --quiet
    ```
- Command Line 

	You can pass a right fielder input in ```--rfinput``` parameter and a license string in ```--license``` parameter to test Right Fielder Object. For example:
	```
    $ ./MelissaRightFielderObjectLinuxPython3.sh --rfinput "22382 Avenida Empresa, Rancho Santa Margarita, CA 92688"
	$ ./MelissaRightFielderObjectLinuxPython3.sh --rfinput "22382 Avenida Empresa, Rancho Santa Margarita, CA 92688" --license "<your_license_string>" 
    ```
	For quiet mode:
    ```
    $ ./MelissaRightFielderObjectLinuxPython3.sh --rfinput "22382 Avenida Empresa, Rancho Santa Margarita, CA 92688" --quiet
	$ ./MelissaRightFielderObjectLinuxPython3.sh --rfinput "22382 Avenida Empresa, Rancho Santa Margarita, CA 92688" --license "<your_license_string>" --quiet
    ```
This is the expected output from a successful setup for interactive mode:

![alt text](/screenshots/output.png)

    
## Troubleshooting

Troubleshooting for errors found while running your program.

### Errors:

| Error      | Description |
| ----------- | ----------- |
| ErrorRequiredFileNotFound      | Program is missing a required file. Please check your Data folder and refer to the list of required files above. If you are unable to obtain all required files through the Melissa Updater, please contact technical support below. |
| ErrorDatabaseExpired   | .db file(s) are expired. Please make sure you are downloading and using the latest release version. (If using the Melissa Updater, check bash script for 'RELEASE_VERSION = {version}'  and change the release version if you are using an out of date release).     |
| ErrorFoundOldFile   | File(s) are out of date. Please make sure you are downloading and using the latest release version. (If using the Melissa Updater, check bash script for 'RELEASE_VERSION = {version}'  and change the release version if you are using an out of date release).    |
| ErrorLicenseExpired   | Expired license string. Please contact technical support below. |


## Contact Us

For free technical support, please call us at 800-MELISSA ext. 4
(800-635-4772 ext. 4) or email us at tech@melissa.com.

To purchase this product, contact Melissa sales department at
800-MELISSA ext. 3 (800-635-4772 ext. 3).
