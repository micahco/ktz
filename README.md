# ktz

*kindle-to-zettelkasten*

Script (w/ GUI) to add kindle clippings to Zettelkasten

<sup>WIP: rewriting script in golang</sup>


## Usage

* Download the required packages: `pip install -r requirements.txt`

* Connect kindle via usb

* Run from the current directory: `python ktz.py`

* The program will then prompt a file explorer dialog where you will select the `My Clippings.txt` file on your kindle

* For each book in the file, the program will prompt the user for book data (`authorFirst`, `authorLast`, `yearPub`)

#### Configuration

* The program relies on a few user vars, one being a predetermined literature template (TEMPLATE_PATH). My template (`Clipping.md`) looks like:

```
Date: {{date}} 
Title: {{title}}
Author: {{author}}
Year: {{year}}
Loc: {{loc}}

---

>{{note}}
```

* Other user vars include the path to the template file (TEMPLATE_PATH) and literature directory (CLIPPING_PATH). For reference, a diagram of my Zettelkasten:

```
/!templates
    Clipping.md <-- TEMPLATE_PATH
/literature <-- CLIPPING_PATH
/scripts
    /ktz
        ktz.py
/slip-box
```

#### Workflow

For further reference, my workflow is as follows:

* Read book(s) on kindle
* As I read, highlight text that I later want to make notes on. If I need to remember something specific to the text then I type in a short note.
* Once I've finished reading, connect kindle to laptop.
* Run the script with the kindle's `My Clippings.txt`
* Copy the `My Clippings.txt` to the literature folder I've just created with the script (as a backup)
* Delete the contents of `My Clippings.txt`. This allows me to have a blank file once I want to add more notes
* Later I go through each note I've just transferred to my Zettelkasten and write down thoughts based on the highlights and fleeting notes. I then link those thoughts to my slip box and other books.

<sup>*This workflow isn't entirely within the Zettelkasten philosophy, but it works for me.*</sup>