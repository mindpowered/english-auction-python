
englishauction
==============
Online auctions with ascending price and time limit

![Build Status](https://mindpowered.dev/assets/images/github-badges/build-passing.svg)

Contents
========

* [Source Code and Documentation](#source-code-and-documentation)
* [About](#about)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Support](#support)
* [Licensing](#licensing)

# Source Code and Documentation
- Source Code: [https://github.com/mindpowered/english-auction-python](https://github.com/mindpowered/english-auction-python)
- Documentation: [https://mindpowered.github.io/english-auction-python](https://mindpowered.github.io/english-auction-python)

# About
An English auction is the most common form of auction. When an auction opens, the price starts low and increases as buyers bid for the item. Live auctions usually end when there is no new highest bid for a period of time. For online auctions, an end time is usually set. To prevent items selling for a loss, sometimes the seller will place a reserve. A reserve is the least amount to sell the item for, although the auction may start at a lower price. Another common feature of online auctions is the ability to pay a set price to win and end the auction.

This package aims to provide functionality of online English auctions.

# Requirements
- Requires Python 3.x. Due to security fixes and new features Python 3.7 or later is recommended.
- pip


Third-party dependencies may have additional requirements.

# Installation
You can retrieve the englishauction package from the Python Package Index https://pypi.org/ using pip. First make sure you have python3 and python3-pip installed. Then you can start by making a `requirements.txt` file in your working directory with the englishauction requirement in it. You can add any other packages to your requirements here, each as a separate line.

requirements.txt:
```
mindpowered-englishauction>0
```
Now you can use pip to install the englishauction package: `python3 -m pip install -r requirements.txt`
If you would like to update the package, simply run the above command again.


# Usage
```python
from mindpowered_englishauction import *

ea = EnglishAuction()
ea.GetOpenAuctions(0, 10, "start", true);

```


# Support
We are here to support using this package. If it doesn't do what you're looking for, isn't working, or you just need help, please [Contact us][contact].

There is also a public [Issue Tracker][bugs] available for this package.

# Licensing
This package is released under the MIT License.



[bugs]: https://github.com/mindpowered/english-auction-python/issues
[contact]: https://mindpowered.dev/support/?ref=english-auction-python/
[docs]: https://mindpowered.github.io/english-auction-python/
[licensing]: https://mindpowered.dev/?ref=english-auction-python
[purchase]: https://mindpowered.dev/purchase/
