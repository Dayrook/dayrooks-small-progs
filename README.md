# Dayrook's Small Programs

`dayrooks-small-progs`

Simple utilities and the like which may be useful to others


# File Type Converter: [`conv-doc`](https://github.com/Dayrook/dayrooks-small-progs/blob/master/conv-doc.py)

>*Don't want to upload your Word document to the web just to turn it into a Markdown file?*

Converts all files in current directory from one type to another.

This simple script employs [pandoc](https://pandoc.org/) under the hood, and can handle dozens of file types. Must have  pypandoc installed: 

```
$ pip install pypandoc`
```

< 20 lines of functional code

## Usage at the command line (Linux/Bash, cmd, powershell): 
`$ python conv-doc <Input File Type> <Output File Type>`

## Example:
`$ python conv-doc docx md`

## Allowable Formats:

Markdown, pdf, HTML, LaTeX, Word docx, ...

Full list [here](https://pandoc.org/MANUAL.html#general-options)

## Sample Output

```
$ python conv-doc.py docx md

-----------------------
Converting docx into md
-----------------------

* Converting: bb.docx --> bb.md
* Converting: aa.docx --> aa.md
* Converting: cc.docx --> cc.md
```

