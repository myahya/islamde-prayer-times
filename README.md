This is a simple tool to view prayer times published by [islam.de](http://islam.de) conveniently thorugh your browser.

## Basic Usage
In order to use this tool, you first need the URL for the text file containing the prayer times for your city. You can obtain this by visiting http://islam.de/3455 (note that you the search functionality there is not flexible, to get the file for Munich you would need to enter 'München'. 'Muenchen' or 'Munich' will not work).

Once you have the file's url, let's say http://islam.de/sections/servicepoint/gebetszeiten/diwan2014/2014_DE_M%D0%91nchen_02_2867714.txt, procceed as follows:

    git clone https://github.com/myahya/islamde-prayer-times.git
    python islamde-prayertimes.py -i http://islam.de/sections/servicepoint/gebetszeiten/diwan2014/2014_DE_M%D0%91nchen_02_2867714.txt


You can now navigate to http://localhost:8087/ to see the local prayer times.



## Options
The following options are available:

    -h shows this help message.
    -i set the input file (can be a local file or a URL). When omitted, default is to use the most recently created txt file in the current directory. If a URL is specifid, the file will be downloaded to the current directory.
    -p set the port, the default is 8087.
    
## Dependencies
* [Bottle](http://bottlepy.org/)

## Licence 
MIT License 
