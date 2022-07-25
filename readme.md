# PrintBooklet Python Script

## Description
A Python Script program for getting the print order of pages for printing a booklet in a single-side printer. You have to print the odd order first and then print the even order and both have to be printed in 2 pages per sheet.

## Installation
```bash
sudo apt-get install python3
```
Your system needs to be already installed version 3 and above  [python](https://python.org/) to use the Printbooklet script. If you want to use it on the web, you can run it on replit by clicking the run on replit icon see below.\
[![Run on Repl.it](https://repl.it/badge/github/myooaung/print-booklet)](https://repl.it/github/myooaung/print-booklet)
## Usage

```bash
python3 printbooklet.py 
Enter number of pages: 20
[20, 1, 2, 19, 18, 3, 4, 17, 16, 5, 6, 15, 14, 7, 8, 13, 12, 9, 10, 11]
odd
20,1,18,3,16,5,14,7,12,9,
even
2,19,4,17,6,15,8,13,10,11,

```
You have to manually enter a multiply of 4 for the number of pages.\
For eg. if you have a total of 18 pages to print you have to enter 20 for the number of pages.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
