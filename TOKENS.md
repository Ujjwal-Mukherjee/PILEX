# Tokens: ordinary Python and Ψ-LEX

Made 2026-11-21. Draft 1. The numbers are approximate: they are counted with public tokenizers, not with the tokenizer of the Claude models, which is not available here.

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

## What stays out of the AI's sight

The 16 programs above are 872 tokens. The engine turns them into about 20,000 tokens of Python, and the engine itself is much bigger than that. An AI does not write this code and does not have to read it. In the plan all of it lives in a data centre: the AI writes the symbols, sends them, and the answer comes back.

## Not shown yet

- **That symbols make an AI write fewer wrong programs.** This is the bet of Ψ-LEX, and it has not been measured. A test: give the same tasks to an AI in ordinary Python and in Ψ-LEX, and count the wrong answers and the retries.
- **The cost of learning the symbols.** An AI that has not learned them must be shown what each block does, which for a few hundred blocks is thousands of tokens every conversation, enough to cancel the saving of more than a hundred programs. The plan is to teach the symbols once, in training, so that the list does not travel with every request.
- **The numbers with the tokenizer of the Claude models**, and with long programs. All programs here are small.
- **The twenty test programs written in Ψ-LEX.** The second table is an estimate from stand-in signs.
