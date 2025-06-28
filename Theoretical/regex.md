# Notes for Learning Regex

Resources:
1. [Learn Regular Expressions in 20 Minutes - Web Dev Simplified](https://www.youtube.com/watch?v=rhzKDrUiJVk)
2. [regexlearn.com](https://regexlearn.com/)

## Introduction

Regex is short for **Regular Expression**

/<expression>/<flag>

```text
readme.md
document.pdf
image.png
music.mp4
manual.pdf
```
Regex to find files that are pdf files above.
```regex
/^\w+\.pdf$/gm
```

## Basic Matcher
```text
“I have no special talents. I am only passionately curious.”

― Albert Einstein
```
Regex to find the **curious** word inside the quote.
```regex
/curious/gm
```

```text
abcABC123 .:!?
```
Regex to match any character.
```
/./g
```

## Character Sets []

```text
bar ber bir bor bur
```
Regex to match the words **bir** and **bor**.
```regex
/b[io]r/g
```
### Except
```text
bar ber bir bor bur
```
Regex to match any words *except* **bir** and **bor**.
```regex
/b[^io]r/g
```
### Range
```text
abcdefghijklmnopqrstuvwxyz
```
Regex to match all characters from letters **e** to **o**.
```regex
/[e-o]/g
```
### Number Range
```text
0123456789
```
Regex to match all characters from numbers **3** to **6**.
```regex
/[3-6]/g
```

## Repetitions
There are special characters that are used to specify how many times a character will be repeated in a text.

### Asterisk (*)

```text
br ber beer
```
Regex to match a word that starts with **b** and ends with **r** where they may be separated by any numbers of **e**, including 0.
```regex
/be*r/g
```

Regex to match a word that starts with **b** and ends with **r** where they may be separated by any numbers of **e**, NOT including 0.
```regex
/be+r/g
```

### Question Mark (?)
Indicates a character is optional
```text
color, colour
```
Regex to match both **color** and **colour** where **u** is optional
```regex
/colou?r/g
```

### Curly Braces
Indicates the specific occurences of a character
```text
ber beer beeer beeeer
```
Regex to match the word **beer**. To match the word **beeer**, change 2 to 3.
```regex
/be{2}r/g
```

Regex to match the words above where 1 to 3 **e** are present
```regex
/be{1, 3}r/g
```

## Grouping ()
Parenthesis
```text
ha-ha,haa-haa
```
Regex to match the words **haa**
```regex
/(haa)/g
```

### Referencing a Group

```text
ha-ha,haa-haa
```
Regex to group **ha** and **haa**.
```regex
/(ha)-\1,(haa)-\2/g
```

### Non-Capturing Group

```text
ha-ha,haa-haa
```
Regex to not capture **ha** as a different group.
```regex
/(?:ha)-ha,(haa)-\1/g
```

### Pipe |

```text
cat rat dog
```
Regex to match the words **cat** and **rat**. If want to match dog add **|dog** at the end of the expression.
```regex
/(c|r)at/g
```

### Escape \

```text
(*) Asterisk.
```
Regex to match the asterisk and the periode.
```regex
/(\*|\.)/g
```

## Line Start ^
Gets the first match per line.

```text
Basic Omellette Recipe

1. 3 eggs, beaten
2. 1 tsp sunflower oil
3. 1 tsp butter
```
Regex to match the first numbers only.
```regex
/^[0-9]/gm
```

## Line End $
Gets the match at the end of each line.

```text
https://domain.com/what-is-html.html
https://otherdomain.com/html-elements
https://website.com/html5-features.html
```
Regex to match the each link that ends with **html**.
```regex
/html$/gm
```

## Word Character \w
Matches characters that are letters, numbers, and underscores.

```text
abcABC123 _.:!?
```
Regex to match the characters from **a** to **_**. To NOT match them. use **\W**.
```regex
/\w/g
```

## Numeric Character \d
Matches all numbers
```text
abcABC123 .:!?
```
Regex to match all numbers. To NOT match them, use **\D**.
```regex
/\d/g
```

## Space Character \s
Matches all spaces
```text
abcABC123 .:!?
```
Regex to match all spaces. To match everything EXCEPT spaces, use **\S**.
```regex
/\s/g
```

## Lookarounds

### Positive Lookahead (?=)

```text
Date: 4 Aug 3PM
```
Regex to match numbers where if you lookahead, has the word **PM**
```regex
/\d+(?=PM)/g
```

### Negative Lookahead (?!)

```text
Date: 4 Aug 3PM
```
Regex to match numbers where if you lookahead, does not have the word **PM**.
```regex
/\d+(?!PM)/g
```

### Positive Lookbehind (?<=)

```text
Product Code: 1064 Price: $5
```
Regex to match numbers where if you look behind, has the **$**.
```regex
/(?<=\$)\d+/g
```

### Negative Lookbehind (?<!)

```text
Product Code: 1064 Price: $5
```
Regex to match number where if you look behind, does not have the **$**.
```regex
/(?<!\$)\d+/g
```

## Flags
Also called **modifiers** because they change the output of expressions.

### Global
Select all matches.
```regex
/\w/g
```

### Multiline
Regex sees everything in one line. Using this flag separates lines.
```regex
/\w/m
```

### Case-insensitive
Removes case sensitive.
```regex
/\w/i
```

## Greedy Matching

```text
ber beer beeer beeeer
```
Regex to match all words that ends with r and can be any character preceded by it. Will match all the words.
```regex
/.*r/
```

## Lazy Matching

```text
ber beer beeer beeeer
```
Regex to match the first word that ends with r and can be any character preceded by it. In this case, will match **ber**.
```regex
/.*?r/
```
