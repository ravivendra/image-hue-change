## General Information

*Python-OpenCV based Change Image Temperature*

## Software Code Name

**PYOPENCV-CHG-IMG-TEMP**

## Short Description

This is a simple code how to change the image temperature by using OpenCV & Python code. It can changes the image to warmer (reddish) or cooler (blueish) temperature. This code only received the JPG image file and return/save the result as JPG file also.

## Software Engineer

* Ravi Vendra R - <ravi.vendra.rishika@gmail.com>

## Technology Stack

This project is developed using :
* Python 3.10
* OpenCV Python 4.9
* NumPy 1.17

## Requirement & Setup

To run this project, you need to ensure the device is already installed the technology stack aforementioned. OpenCV by default is not installed, therefore you need to install the OpenCV by running the command below:

```$ pip install opencv-python```

It will download (approx. 50 MB) and install the OpenCV engine to the device.

## Run The Code

To run the code, you can do in command line (Powershell in Windows, Terminal in Linux or MacOS), with the command below:

```$ python main.py [source-image] [destination-image] [hue]```

The detail explanation about the command above is:
1. _[source-image]_ : the source file as the code refers to.
2. _[destination-image]_ : the destination file as the result will be stored.
3. _[hue]_ : customized integer value, positive integer to change into warmer, negative integer to change into cooler.

As an example, you can run the command below :

```
$ python main.py src-img/team.jpeg dest-img/team_hue_red.jpeg 50
$ python main.py src-img/team.jpeg dest-img/team_hue_blue.jpeg -50
```
