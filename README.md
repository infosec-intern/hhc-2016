# Holiday Hack Challenge 2016
[Intro](https://www.holidayhackchallenge.com/2016/) <br>
[Neighborhood](https://quest2016.holidayhackchallenge.com/)

## Extra Links
* [SANS Pen Testing Blog](https://pen-testing.sans.org/blog/pen-testing)
* [Reverse Engineering Android Apps](https://pen-testing.sans.org/blog/2016/12/05/ghost-in-the-droid-reverse-engineering-android-apps)
  * [Decoding Android App Resources](https://pen-testing.sans.org/blog/2016/12/10/mining-android-secrets-decoding-android-app-resources)
  * [APKTool](https://ibotpeaches.github.io/Apktool/)
  * [Manipulating Android Apps](https://www.youtube.com/watch?v=mo2yZVRicW0)
* Linux File System
  * [Mount a RPi File System Image](https://pen-testing.sans.org/blog/2016/12/07/mount-a-raspberry-pi-file-system-image)
* Web Vulnerabilities
  * [PHP Local File Inclusion](https://pen-testing.sans.org/blog/2016/12/07/mount-a-raspberry-pi-file-system-image)
* [JS Meteor Framework](https://www.meteor.com/)
  * [Mining Meteor](https://pen-testing.sans.org/blog/2016/12/06/mining-meteor)
  * [TamperMonkey](https://tampermonkey.net/) and [MeteorMiner](https://github.com/nidem/MeteorMiner)

## Part One
![Santa's Business Card](./business_card.PNG)
* Python script: `tweet_finder.py`
  * Query a target Twitter user's account
  * Print out all the statuses of that user
* Configuration File: `config.json`
```
{
    "target": <Username of Twitter Account to Query>,
    "consumerKey": <API Key>,
    "consumerSecret": <Secret Key>,
    "accessToken": <Application API Key>,
    "accessSecret": <Application Secret>
}
```
1) What is the secrete message in Santa's tweets?
  [Done]
2) What is inside the ZIP file distributed by Santa's team?
  [Done?]
