Title: Running containerized X11 apps on MacOS 
Date: 2021-04-19 11:00
Category: Programming
Tags: Docker Containers MacOS 
Summary: When developing apps in (docker) containers, you might like to run an X11 application.  This is mostly straightforward on Linux, but requires a bit of work on MacOS. 

When developing apps in (docker) containers, you might like to run an X11 application.
This is mostly straightforward on Linux, but requires a bit of work on MacOS

First, install [XQuartz](https://www.xquartz.org/). There is a `.dmg` package in the _Download_ section of the website.
If you are like me and would rather prefer to install from the command line, you surely like 
[Homebrew](https://brew.sh/) and you can use it to install XQuartz:

    brew install xquartz

 