
englishauction
==============

Contents
========

* [About](#about)
* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [Licensing](#licensing)
* [Support](#support)

# About
A Timed Auction library starting at a low price and increasing until the auction ends.

# Requirements
Python 3.x. Due to security fixes and new features Python 3.7 or later is recommended.
pip


Third-party dependencies may have additional requirements.

# Installation
You can retrieve the englishauction package from the Python Package Index https://pypi.org/ using pip. First make sure you have python3 and python3-pip installed. Then you can start by making a `requirements.txt` file in your working directory with the englishauction requirement in it. You can add any other packages to your requirements here, each as a separate line.

requirements.txt:
```
mindpowered-englishauction>0
```
Now you can use pip to install the englishauction package: `python3 -m pip install -r requirements.txt`
If you would like to update the package, simply run the above command again.


# Configuration
You must configure the storage and retrieval of auctions and bids. Before we can make use of englishauction's functions, we have to create Callback functions for englishauction to use whenever it needs to use any persistent data regarding auctions and bids. A common way of storing persistent data is using SQL. Each setup function bridges the gap between your auction data and the englishauction package's functionality.

# Usage
You are using python


More examples to come

# Licensing
Additional [licensing options][licensing] are available.

# Support
For bug fixes, please raise an issue in the [Issue Tracker][bugs].

For feature requests, and general support, please [Contact us][contact].



[bugs]: https://github.com/mindpowered/english-auction-python/issues
[contact]: https://mindpowered.dev/support.html?ref=english-auction-python/
[docs]: https://mindpowered.github.io/english-auction-python/
[licensing]: https://mindpowered.dev/?ref=english-auction-python
