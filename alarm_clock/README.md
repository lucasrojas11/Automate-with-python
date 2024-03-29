# Using Alarm_clock script

## Dependencies: 
For Ubuntu based systems please execute the following command to install required dependencies
```
sudo apt-get install -y python-3-dev libasound2-dev
```
For other Unix based distros please google the package name.

## Setup and activate virtual environment:
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

## Steps to set an alarm:
1. run the script `AlarmClock.py` using python3.
    On Unix based systems the command looks like:
    ```
    python3 AlarmClock.py
    ``` 
    or
    ```
    python AlarmClock.py
    ```
2. After execution of the script you will be prompted to enter the time to
    set an alarm in HH:MM format. Which looks something as shown below :

    ```
    please enter the time in HH:MM format to set an alarm : 
    ```
    Enter the time on the prompt in 24 HOURS FORMAT as shown in the example below :
    ```
    please enter the time in HH:MM format to set an alarm : 14:32
    ```

3. Then you will get a looping output of the current time and set time on   the CLI as shown below :
    ```
    please enter the time in HH:MM format to set an alarm : 14:32
    current time : 11:48
    alarm time : 14:32
    current time : 11:48
    alarm time : 14:32
    current time : 11:48
    alarm time : 14:32
    current time : 11:48
    alarm time : 14:32
    current time : 11:48
    alarm time : 14:32
    current time : 11:48
    alarm time : 14:32
    current time : 11:48
    alarm time : 14:32
    current time : 11:48
    alarm time : 14:32
    current time : 11:48
    alarm time : 14:32
    current time : 11:48
    alarm time : 14:32
    ```
4. When the alarm goes off you will hear a sound and get the following lines on the prompt :
    ```
    Time to Wake up
    Press enter to Stop
    ```
5. Press enter to stop the alarm else the alarm will stop the sound after 33 seconds.
