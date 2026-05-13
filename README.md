# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a command-line Python program that analyzes a text file and reports the total word count and character frequency.

## What I Learned

While building BookBot, I practiced several important Python concepts:

- Reading text files using Python File I/O
- Working with command-line arguments using the `sys` module
- Using `sys.argv` to pass a book path into the program
- Exiting programs with status codes using `sys.exit()`
- Splitting strings into words
- Counting characters with Python dictionaries
- Building and sorting lists of dictionaries
- Filtering characters using string methods like `.isalpha()`
- Organizing code into reusable functions

## Usage

```shell
python3 main.py <path_to_book>
```

## Output

```shell
python3 main.py books/prideandprejudice.txt
```

```terminaloutput
============ BOOKBOT ============
Analyzing book found at books/prideandprejudice.txt
----------- Word Count ----------
Found 130410 total words
--------- Character Count -------
e: 74451
t: 50837
a: 44834
o: 43383
i: 41198
n: 40686
h: 36162
s: 35695
r: 35168
d: 23723
l: 23475
u: 16303
m: 15676
c: 14838
y: 13579
w: 13017
f: 12996
g: 11007
b: 9762
p: 9154
v: 6118
k: 3497
x: 1032
j: 1014
z: 971
q: 660
ê: 8
à: 4
é: 2
â: 1
œ: 1
============= END ===============
```