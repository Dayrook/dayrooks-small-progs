# Dayrook's Small Programs

`dayrooks-small-progs`

Simple utilities and the like which may be useful to others


# File Type Converter: [`conv-doc.py`](https://github.com/Dayrook/dayrooks-small-progs/blob/master/conv-doc.py)

>*Don't want to upload your Word document to the web just to turn it into a Markdown file?*

Converts all files in current directory from one type to another. Keeps original files. < 20 lines of functional code.

Depends on pypandoc ([pandoc](https://pandoc.org/)), which does the conversion. Install it with:

```
$ pip install pypandoc
```

## Allowable Formats:

Markdown, pdf, HTML, LaTeX, Word docx, many more...

Full list [here](https://pandoc.org/MANUAL.html#general-options)

## Usage at the Command Line (Linux/Bash, cmd, powershell): 
`$ python conv-doc.py <Input File Type> <Output File Type>`

### Example:
`$ python conv-doc.py docx md`

### Sample Output

```
$ python conv-doc.py docx md

-----------------------
Converting docx into md
-----------------------

* Converting: bb.docx --> bb.md
* Converting: aa.docx --> aa.md
* Converting: cc.docx --> cc.md
```

