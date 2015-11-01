# pyFlatplan

## What is a flatplan?

A flatplan is a layout quicklook for a book, a magazine or any kind of printed publication. It aims at showing all the pages at once in order to give a more global aspect of the document. Then, the publisher evaluate the design.

![](https://www.dropbox.com/s/qppk663um1q6hih/flatplan.jpg?dl=0&raw=1)  

## How does pyFlatplan work?

It is a command line software so it has to run into a terminal. Then, it take some arguments:


| Argument      | Expected value                        | Mandatory or Optional  | Default value   | Example                   |
|---------------|:-------------------------------------:|:----------------------:|:---------------:|:-------------------------:|
| `-input`      | Image list or wildcard pattern        | **madatory**           | `none`          | `/imgFolder/picture*.jpg` |
| `-output`     | Output flatplan image                 | optional               | `flatplan.jpg`  | `myFlatplan.jpg`          |
| `-thumb`      | Thumbnail height in pixel             | optional               | `256`           | `128`                     |
| `-column`     | Number of columns (thumbs per lines)  | optional               | `5`             | `4`                       |
| `-background` | Background color in hexadecimal       | optional               | `"#EFFEFFEFF"`  | `"#FFF000000"` <br> Don't forget to use quote marks!    |

## What do you need to launch it?
pyFlatplan is coded with Python 2.7. It is usually installed on your OSX/Linux machine, but just in case, it's [here](https://www.python.org/downloads/).

Internally, the mosaic is made with ImageMagick, an open source software you need to install first. You can find it [here](http://www.imagemagick.org/script/binary-releases.php).

## How to launch it?

In a terminal:

```shell
cd /whereYouPutIt/pyFlatplan/
./pyFlatplan.py -input /myFolderFullOfImages/picture_*.jpg
```

To make it easier, you could add an alias to your `.bashrc` file:  
```shell
alias flatplan='python /whereYouPutIt/pyFlatplan//pyFlatplan.py'
```
and then, you just have to call :
```shell
flatplan -input /myFolderFullOfImages/picture_*.jpg
```





