# Tokens: ordinary Python and Ψ-LEX

Made 2026-11-21; the section on examples 18 to 22 was added on 2026-11-22 and counted again later that day, after the programs were written with the short lines of the [README](README.md#plain-lines); the section on example 25 was added on 2026-11-23, and on the same day the counts of examples 18 and 19 were taken again, after their lines of one name and its module were written the short way. Draft 2. The numbers are approximate: they are counted with public tokenizers, not with the tokenizer of the Claude models, which is not available here.

## What was counted

A program of this repository (`program.sym`) against an ordinary Python program that does the same work, with pandas, scikit-learn and matplotlib. The ordinary programs are in [compare/ordinary](compare/ordinary) and the data they read is in [compare/data](compare/data) (run them from that folder, on a copy). They are written tightly: no comments, no blank lines, no `main()`, only the steps the Ψ-LEX program takes. Blank lines and comments are left out of the Ψ-LEX programs too.

Every ordinary program was run. Where the Ψ-LEX output shows a number, the ordinary program gives the same number: the correlation, the average miss of the guess, the share explained, the size of each group, the share of each input, the right and wrong guesses of a model, and the cleaned file of example 06 (same 39 rows and 6 columns, same values). Two small differences: the tied words in the lists of most common words (examples 03 and 14) come out in a different order, and in example 16 the average miss is 4.6 where Ψ-LEX gives 4.2. That one is the order of the columns: a random forest gives a slightly different answer when its inputs come in a different order, and with the columns in the order Ψ-LEX uses, the ordinary program gives 4.2 and 73% as well. Example 17 is not compared: its practice table has no ordinary equivalent.

Three tokenizers were used: `o200k` (the GPT-4o family), `cl100k` (GPT-4) and the old Claude tokenizer. The table below is in `o200k`. The other two agree within about 5 percent.

## The 16 programs of this repository

| # | What it does | Lines: ordinary > Ψ-LEX | Tokens: ordinary | Tokens: Ψ-LEX | Ordinary / Ψ-LEX |
|---|---|---|---|---|---|
| 01 | A full study of exam marks: look, clean, draw, find the link, guess | 42 > 17 | 487 | 152 | 3.2x |
| 02 | Will a student pass? Rank the inputs, teach a forest, sort rows into groups | 34 > 12 | 450 | 137 | 3.3x |
| 03 | Sales added up by month, and good or bad reviews | 23 > 10 | 292 | 96 | 3.0x |
| 04 | What is in this file? | 4 > 3 | 29 | 17 | 1.7x |
| 05 | A typed list with one typing mistake | 6 > 2 | 106 | 31 | 3.4x |
| 06 | A whole file with gaps, a wrong value and a useless column | 10 > 7 | 147 | 54 | 2.7x |
| 07 | The shape of the data in three charts | 17 > 4 | 145 | 42 | 3.5x |
| 08 | Which class does best? | 7 > 3 | 54 | 32 | 1.7x |
| 09 | Do students who study more get better marks? | 10 > 3 | 100 | 34 | 2.9x |
| 10 | Teach the computer to guess a score, then guess for a new student | 11 > 5 | 142 | 43 | 3.3x |
| 11 | Say pass or fail, and show where it goes wrong | 12 > 5 | 145 | 42 | 3.5x |
| 12 | Are there kinds of students? Sort them into 3 groups | 12 > 5 | 125 | 52 | 2.4x |
| 13 | Which column matters most for the score? | 6 > 3 | 78 | 30 | 2.6x |
| 14 | Which words come up most, and can it tell good reviews from bad ones? | 14 > 5 | 191 | 43 | 4.4x |
| 15 | Dates over time: sales for each month, drawn as a line | 9 > 4 | 97 | 47 | 2.1x |
| 16 | A whole report, and a guess, one line each | 38 > 3 | 456 | 20 | 22.8x |
| | **All 16** | **255 > 91** | **3,044** | **872** | **3.5x** |

| Counted with | Ordinary Python | Ψ-LEX | Ψ-LEX as a share of ordinary | Ordinary / Ψ-LEX |
|---|---|---|---|---|
| o200k | 3,044 | 872 | 29% | 3.5x |
| cl100k | 3,008 | 905 | 30% | 3.3x |
| old Claude tokenizer | 3,702 | 1,123 | 30% | 3.3x |
| characters | 11,604 | 2,532 | 22% | 4.6x |

The middle program saves 3.1 times; the smallest saving is 1.7 times (examples 04 and 08, which are only three lines of Ψ-LEX each) and the largest is 22.8 times (example 16, where one line of Ψ-LEX stands for a whole report).

**These are the best case.** The 16 programs were written to show the symbols, and almost every line of them is a block. The next section is about test programs that were not.

## How much one line stands for

The saving follows the size of the block of work that one symbol stands for.

| What the lines are made of | Ordinary lines for each Ψ-LEX line | Tokens: ordinary / Ψ-LEX |
|---|---|---|
| Whole recipes (example 16) | 12.7 | 22.8x |
| Single steps (the other 15 examples) | 2.5 | 3.0x |
| Test programs where standard blocks fit (estimate, see below) | 1.6 | 1.4x to 1.5x |
| Test programs of new logic (estimate, see below) | 1.1 | 0.9x to 1.0x |

So a larger set of blocks, and bigger blocks, is the way to shorten more programs. How far that goes for programs that are mostly new logic is not known; there the measured saving was about nothing.

## Twenty test programs (an estimate)

This part is an estimate, because none of the test programs is written in Ψ-LEX yet. Twenty small test programs were written twice, in ordinary Python and with ready-made standard blocks, the kind Ψ-LEX is built on: 18 where such blocks fit (reading and writing files, CSV and JSON, a small database, dates, logs, command-line options, classes with their own errors, route finding, statistics, a chart) and 2 where every line is new logic (a stock-command interpreter and a calculator for text). The two versions were run and gave the same output and the same files in all 20. They are not in this repository.

The blocks have no symbols yet, so each block line was turned into a stand-in sign for counting only, in the style of Ψ-LEX (the parentheses go, a sign stands where the name was). The stand-ins are not proposals. Two cases are shown: every sign costs one token, or every sign costs two. Signs for Python's own words (`if`, `for`, `def` and so on) are shown separately, because most of those words are one token already and most rare signs cost two or three.

| | 18 programs where blocks fit | 2 programs of new logic |
|---|---|---|
| Ordinary Python | 3,202 | 675 |
| Same blocks, written as words | 2,293 (72%) | 664 (98%) |
| Signs for the blocks, 1 token each | 2,105 (66%) | 650 (96%) |
| Signs for the blocks, 2 tokens each | 2,167 (68%) | 655 (97%) |
| Signs for the blocks, 1 token each, and signs for Python's own words | 2,219 (69%) | 735 (109%) |
| Signs for the blocks, 2 tokens each, and signs for Python's own words | 2,281 (71%) | 740 (110%) |

Two things to read from this. Where standard blocks fit, Ψ-LEX is about a third shorter. Where every line is new logic, it is not shorter, and with signs for Python's own words it comes out about a tenth longer: a rare sign costs more than the one-token word it replaces. Signs that cost one token each would avoid that. This was counted on small programs written by me, chosen because blocks fit them, so it shows what the blocks can give when they fit, not an average over all programs.

## Examples 18 to 22, measured as they came out

The estimate above was made before there were real programs to count. Examples 18 to 22 are real programs, and each has an ordinary Python program that does the same work: the task manager has its own, the job engine (22) has the program it was made from (401 lines), and the to-do list, the price checker and the mail queue have ones written by hand. The ordinary programs are not in this repository; only how the programs are written in symbols, and what they printed, is shown. The whole files were counted as they are with `o200k` and `cl100k`: there are no comments in any of them, and the docstrings and blank lines stay in.

| # | Program | Lines (blank ones too): ordinary > Ψ-LEX | Tokens: ordinary | Tokens: Ψ-LEX | Ψ-LEX as a share of ordinary | Ordinary / Ψ-LEX |
|---|---|---|---|---|---|---|
| 18 | Task manager | 149 > 134 | 1,032 | 921 | 89% | 1.12x |
| 19 | To-do list | 83 > 36 | 674 | 303 | 45% | 2.22x |
| 20 | Price checker | 83 > 55 | 582 | 402 | 69% | 1.45x |
| 21 | Mail queue | 146 > 34 | 1,160 | 316 | 27% | 3.67x |
| 22 | Job engine | 401 > 68 | 2,960 | 545 | 18% | 5.43x |
| | **Examples 18 to 22** | **862 > 327** | **6,408** | **2,487** | **39%** | **2.58x** |

The table is in `o200k`. With `cl100k` the ratios are 1.12, 2.23, 1.43, 3.64, 5.42 and 2.56 times. Taking the docstrings and the blank lines out of both versions changes little: 1.14 times for the task manager, 2.22 for the to-do list, 1.45 for the price checker, 3.67 for the mail queue, 5.42 for the job engine and 2.67 for all five.

These numbers were counted again after the programs were written with the short lines of the [README](README.md#plain-lines). The first count, made when `def`, `print`, `raise` and `import` were written as Python writes them, was 2,535 tokens in Ψ-LEX for the five programs; with the short lines it is 2,487, which is 48 fewer (1.9%). Two of the 48 come from writing one name and its module the short way (`Path: pathlib` for `from pathlib import Path`, see [Plain lines](README.md#plain-lines)), which was done later in examples 18 and 19: one token fewer in each, in `o200k` and in `cl100k` (922 to 921 and 304 to 303 in `o200k`). The first count also had one wrong number: the ordinary job engine has no docstrings, only blank lines, so without them it is 2,954 tokens and not 2,895; its ratio was 5.35 and not 5.24, and the five together 2.62 and not 2.59. The numbers above are counted from the files. Examples 20 and 21 were changed later to begin with `asyncio` instead of `import asyncio` (see [Plain lines](README.md#plain-lines)); their counts did not change. Examples 23 and 24 were changed in the same way as 18 and 19 and are not counted here.

What the numbers say:

- **The saving follows how much of the program the blocks stand for.** The task manager is mostly its own logic: the menu, what a task is, what is printed. The signs make it only 11% shorter in tokens, 1.12 times. The job engine is mostly blocks, and it comes out 5.4 times shorter. The other three lie between.
- **These are not an average over programs.** The blocks were found by taking programs apart: eight of them from the job engine (22) and some from the task manager (18). A program that blocks were taken from is the best case for those blocks, and even so the task manager shrinks by only 11%. Examples 19 to 21 were written afterwards, with blocks that already existed, to see whether the blocks serve other programs too (the mail queue uses the same job-engine blocks as example 22). They show reuse; they are not an average either.
- **Not counted:** examples 23 and 24, because no ordinary version of them was written, and, as before, whether symbols make an AI write fewer mistakes.

## Example 25, a program that no block was taken from

Example 25 is a register of mock tests. It has an ordinary Python program that does the same work (201 lines; like the ordinary programs of examples 18 to 22, it is not in this repository). Unlike those five, it was not taken apart to find blocks: it is written with the short lines of the [README](README.md#plain-lines) and with three blocks that existed before it. The file was counted as it is, like the others.

| # | Program | Lines (blank ones too): ordinary > Ψ-LEX | Tokens: ordinary | Tokens: Ψ-LEX | Ψ-LEX as a share of ordinary | Ordinary / Ψ-LEX |
|---|---|---|---|---|---|---|
| 25 | Register of mock tests | 201 > 188 | 1,676 | 1,541 | 92% | 1.09x |

With `cl100k` it is 1,658 and 1,530 tokens, 92% and 1.08 times. Of the 135 tokens saved in `o200k`, 37 come from the short lines and 98 from the three blocks and their signs. That is a small saving, for the reason the task manager's was small: most of the program is its own logic (a menu, an exam report, a history, a quiz), and a block stands only where other programs do the same work.

The two programs were run with the same answers in 21 scenarios of answers and files: a wrong answer at every question, marks on the edges (39, 40, 41, 79, 80, 100, 0 and -1), an exam with no results, a damaged file, an empty file, a file that is not a list, a file that is not written in UTF-8, a folder where the file should be, a day written another way in the file, the end of the input in the middle of a question, Bengali names and digits, and more. They gave the same screens and the same files in 20 of them. In the 21st, a save when a folder has the name of the temporary file, the ordinary program saves and the Ψ-LEX program stops with the error: it saves through a temporary file with a fixed name, the ordinary one through a file with a name of its own. The saved file also has another mode: the ordinary program leaves it readable by its owner only, the Ψ-LEX program gives it the mode of a new file. The modes were not compared.

## What stays out of the AI's sight

The 16 programs above are 872 tokens. The engine turns them into about 20,000 tokens of Python, and the engine itself is much bigger than that. An AI does not write this code and does not have to read it. In the plan all of it lives in a data centre: the AI writes the symbols, sends them, and the answer comes back.

## Not shown yet

- **That symbols make an AI write fewer wrong programs.** This is the bet of Ψ-LEX, and it has not been measured. A test: give the same tasks to an AI in ordinary Python and in Ψ-LEX, and count the wrong answers and the retries.
- **The cost of learning the symbols.** An AI that has not learned them must be shown what each block does, which for a few hundred blocks is thousands of tokens every conversation, enough to cancel the saving of more than a hundred programs. The plan is to teach the symbols once, in training, so that the list does not travel with every request.
- **The numbers with the tokenizer of the Claude models**, and with long programs. All programs here are small.
- **The twenty test programs written in Ψ-LEX.** The second table is an estimate from stand-in signs.
