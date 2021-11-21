# ktz

*kindle-to-zettelkasten*

transfer kindle clippings to Zettelkasten

<sup>tested on Python *3.10.0* Win 10</sup>


## Usage

* Run `setup.py` to generate executable script

* Connect your kindle via usb

* Run the executable script

* Create config file

* 

#### Configuration

Configure the program for use by editing `config.ini`

* `TemplatePath`: path to your new note template
    
    Your template can include the following `{{outputs}}`:
    * `date` (when the note was taken)
    * `title` (Moby Dick)
    * `author` (First Last)
    * `year` (published)
    * `loc` (location on kindle)
    * `text` (highlighted text and notes)

    For reference, here is what my template looks like:

```
Date: {{date}} 
Title: {{title}}
Author: {{author}}
Year: {{year}}
Loc: {{loc}}

---

>{{text}}
```

* `LiteraturePath`: path to your Zettelkasten's literature notes directory

* `DateFormat`: [strftime](https://strftime.org/) format for {{date}} output


#### Workflow

For further reference, my workflow is as follows:

* Read book(s) on kindle
* As I read, highlight text that I later want to make notes on. If I need to remember something specific to the text then I type in a short note.
* Once I've finished reading, connect kindle to laptop.
* Run the script with the kindle's `My Clippings.txt`
* Copy the `My Clippings.txt` to the literature folder I've just created with the script (as a backup)
* Delete the contents of `My Clippings.txt`. This allows me to have a blank file once I start a new book
* Later I go through each note I've just transferred to my Zettelkasten and write down thoughts based on the highlights and fleeting notes. I then link those thoughts to my slip box and other books.

<sup>*This workflow isn't entirely within the Zettelkasten philosophy, but it works for me.*</sup>