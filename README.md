# Clippings.py

(tested on Python *2.7.17* & *3.9.8* Win 10)

Script (w/ GUI) to add kindle highlights to Zettelkasten

## Usage

Download the required packages:
`pip install -r requirements.txt`

Run from the current directory:
`python Clippings.py`

Enter the literature data for the book (all inputs are required). The program will then prompt a file explorer dialog where you will select the `my-clippings.txt` file for that specific book. This file should only contain Highlights (no Notes or Bookmarks).

#### Considerations

* The `my-clippings.txt` file should only contain *Highlights* for the one specific book you wish to transfer to your Zettelkasten. The script does **not** support transfering multiple books at once, nor does it support Notes or Bookmarks (only *Highlights*).

* There are already (better) more complex plugins made for the purpose of sending your Kindle notes to Zettlekasten. The reason I wrote this is because I just wanted a basic script for my specific use case: to simply transfer Kindle Clippings highlights (from the .txt file) to my Zettlekasten as literature notes. Here are some plugins that may be easier and do much more for you:
    * [hadynz/obsidian-kindle-plugin](https://github.com/hadynz/obsidian-kindle-plugin)

* The program relies on a few user vars, one being a pre-determined literature template. My template (`Clipping.md`) looks like:

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
