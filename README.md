# ktz

<sup>tested on Python *2.7.17* & *3.9.8* Win 10</sup>

*kindle-to-zettelkasten*

Script (w/ GUI) to add kindle clippings to Zettelkasten

## Usage

Download the required packages:
`pip install -r requirements.txt`

Run from the current directory:
`python ktz.py`

Enter the literature data for the book (all inputs are required). The program will then prompt a file explorer dialog where you will select the `My Clippings.txt` file for that specific book.

#### Considerations

* The program relies on a few user vars, one being a predetermined literature template. My template (`Clipping.md`) looks like:

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

* Read a book on kindle
* As I read, highlight text that I later want to make notes on. If I need to remember something specific to the text then I type in a short note.
* Once I've finished reading, connect kindle to laptop.
* Run the script with the kindle's `My Clippings.txt`
* Copy the `My Clippings.txt` to the literature folder I've just created with the script (as a backup)
* Delete the `My Clippings.txt` file from kindle. This allows me to have a blank file once I start another book
* Finally I go through each note I've just transferred to my Zettelkasten and write down thoughts based on the highlights and fleeting notes. I then link those thoughts to my slip box and other books.

<sup>This workflow isn't entirely within the Zettelkasten philosophy, but it works for me.</sup>