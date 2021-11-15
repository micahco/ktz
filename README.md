# Clippings.py

<sup>tested on Python *2.7.17* & *3.9.8* Win 10</sup>

Script (w/ GUI) to add kindle highlights to Zettelkasten

## Usage

Download the required packages:
`pip install -r requirements.txt`

Run from the current directory:
`python Clippings.py`

Enter the literature data for the book (all inputs are required). The program will then prompt a file explorer dialog where you will select the `my-clippings.txt` file for that specific book. This file should only contain Highlights (no Notes or Bookmarks).

#### Considerations

* The `my-clippings.txt` file should only contain *Highlights* for the one specific book you wish to transfer to your Zettelkasten. The script does **not** support transferring multiple books at once, nor does it support Notes or Bookmarks (only *Highlights*).

* There are already (better) more complex plugins made for the purpose of syncing your Kindle with Zettlekasten. The reason I wrote this is because I just wanted a basic script for my specific use case: to simply transfer Kindle Clippings highlights (from the .txt file) to my literature notes. Here are some platform specific plugins that may be easier and do much more for you:
    * [hadynz/obsidian-kindle-plugin](https://github.com/hadynz/obsidian-kindle-plugin)

* The program relies on a few user vars, one being a predetermined literature template. My template (`Clipping.md`) looks like:

```
Date: {{date}} 
Title: {{title}}
Author: {{author}}
Year: {{year}}
Loc: {{loc}}

---

>{{quote}}
```

* Other user vars include the path to the template file (TEMPLATE_PATH) and literature directory (CLIPPING_PATH). For reference, a diagram of my Zettelkasten:

```
/!templates
    Clipping.md <-- TEMPLATE_PATH
/literature <-- CLIPPING_PATH
/scripts
    /Clippings
        Clippings.py
/slip-box
```

#### Workflow

For further reference, my workflow is as follows:

* Read a book on kindle
* As I read, highlight text that I later want to make notes on. If I need to remember something specific to the text that I want to make note of, I write it down on a piece of paper along with the location.
* Once I've finished reading, connect kindle to laptop.
* Run the script with the kindle's `my-clippings.txt`
* Go through each note I've just transferred to my Zettelkasten and write down thoughts based on the quotes and link those thoughts to my slip box and other notes.
* Once the clippings are transferred into my Zettelkasten, I delete the .txt file from my kindle so that I have a blank file once I begin a new book.

This workflow isn't entirely within the Zettelkasten philosophy, but I've found it works best with how I read and how I take notes.