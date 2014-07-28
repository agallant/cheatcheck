cheatcheck - find similar files
=======

This repository contains a straightforward Python script originally envisioned as a simple cheating-detection device. For anyone who has taken or taught programming classes, the situation is a familiar one - Alice has (at least mostly) working code, and her friend Bob does not. Thus depending on their relations and dispositions, Bob is a simple copy-paste away from mostly working code.

Of course there are bountiful ways both to cheat and to try to catch said cheating, but the most common case in programming will be two or more students with suspiciously similar code. That's where this script comes in - it finds all files of an extension (by default .java) in a path (by default the working directory), and compares all possible pairs for similarity. It then prints the most n similar (default 10), for which it is advisable that the teacher manually inspect and exercise their own judgement.

Note that much of what this script does is inherently quadratic (generating all pairs of a list, diffing strings, etc.). Still it runs on 100 files in reasonable time (<1 min), and is probably feasible for 200-500 files if you have a decent machine and/or time for a coffee. This should be enough for most introductory programming classes, though admittedly if it's a particularly large class and an assignment with many files it may become infeasible.

Regarding implementation, this script was written in Python 3, and uses a number of standard libraries. Python is more or less ideal for this task as you'll see if you examine the code, and really the libraries do all the work and the script is just a few loops and settings.

Right now the defaults are hardcoded, so if you want to change them (say your introductory programming class is fortunate enough to use Python) just do so in the code. To use, simply execute the script within a path that (recursively) contains all the files you want to compare - which means arbitrary subdirectory structures are fine (class1/student1, class1/student2, etc.).

I believe the script is already useful for what it is, but here are a few "next steps" I may get to:
- Parse command line args so you don't have to edit the script to change things
- Offer option to set similarity threshold rather than just printing top n (of which most to all are hopefully non-cheaters)
- Use difflib.Differ (or possibly difflib.HtmlDiff) to produce nice summaries of the top similar files
- Delve deeper into difflib and beyond to see if there's smarter ways to measure/rank text similarity

And on that last note it's worth adding a caveat - this script produces (approximate) ratios of string similarity, nothing more and nothing less. "Cheating" is a nuanced and subjective issue, and that is precisely why the envisioned use case is employing this script to find the top *possible* candidates for cheating, and then manually inspecting and exercising judgement. You still have to spend time and energy, this script just saves you time by allowing you to focus. If there is a program that can accurately and fairly identify plagiarism without human intervention then it would be far more complex than this.

Also note that this script only uses as a corpus the files you have (which basically means student submissions plus your own solution or related code) - it doesn't compare against [Stack Overflow](http://stackoverflow.com/), [Yahoo! Answers](https://answers.yahoo.com/), or other online sources. No doubt more sophisticated anti-cheating software does, but I believe this to be excessive and wasted effort - if a student has gone to the effort to cheat from a source you do not have available, then either they have worked hard enough to learn regardless or you need to be tighter and more original in your material.

Thanks for reading, and I hope this script is useful for you.
