## My Lab Notebook for CS1066 PSet #1

Esam Abdelaziz

https://youtu.be/W42N5hLajSk

----
----

### SUBTASK #1: Prompt for the Search Term

----
Text of my first prompt:

> Update trends_save.py so that instead of always searching for the hard-coded term "vibe coding", the program asks the user to enter a search term or phrase when it runs. Use that response as the query for Google Trends, while keeping the rest of the program's behavior the same.

Reflections on success/failure of this prompt:

*   The AI changed the hard-coded "vibe coding" search term into an input so the user can type in whatever they want to search for.
*   I liked that it only changed the part of the code that needed to be changed and kept everything else the same.
*   I tested it with "artificial intelligence" and "vibe coding", and both search terms were passed into the Google Trends URL correctly.
*   At first I thought there was a problem with the scraper because Google Trends kept detecting the browser and no geographical data was being found.
*   This showed me that the input change was working correctly and that I should let the program finish its retry logic before assuming something is broken.

----
Text of my next prompt:

> The new user input is working, but both trends_save.py and the original trends_save_orig.py are getting bot detection from Google Trends and are not finding geographical data. Since the original file has the same issue, inspect trends_scraper.py and figure out what is causing the problem. Make the smallest change needed to get the scraper working, and do not change the new search-term input behavior.

Reflections on success/failure of this prompt:

*   The AI made a very small change to the Chrome headless settings in trends_scraper.py, which seemed reasonable to test because I thought bot detection was the problem.
*   I tested the change, but the program still had the same behavior, so the change did not actually solve anything.
*   After that, I ran the original backup again and let it continue through all five retries instead of stopping it early.
*   On attempt 4, the original scraper got past the bot detection, found the regional data, and successfully saved scraped_data.csv.
*   That made me realize the scraper was not actually broken and the AI change was unnecessary, so I went back to the original scraper.
*   This was useful because it showed me that I should fully test the existing behavior before asking AI to change more code.
*   After letting the scraper finish all of its retries, my updated program worked with "artificial intelligence", scraped 50 regions, saved the results to scraped_data.csv, and trends_plot.py successfully created interest_data.png.

----
**NOTE:** Delete this text and repeat the above block for as many prompts as it takes to complete this subtask.

----
**FINAL REFLECTION:** Review your work. Write a brief statement of what you might have done differently in hindsight, or defend why your work was a good approach.

In hindsight, I would have let the scraper finish all of its retries before assuming there was a problem. I stopped the first few runs early because it kept showing bot detection, which made me think something needed to be fixed. Once I let the program finish, it got past the bot detection and worked correctly. I think my overall approach was still useful because I tested the original backup, compared the behavior, and checked the AI's suggested change instead of assuming it was correct. The biggest thing I learned was to fully test the existing program before making more changes.

----
----

### SUBTASK #2: Just One Tool

----
Text of my first prompt:

> Create a new file called my_tool.py that combines the existing workflow from trends_save.py and trends_plot.py. When I run python3 my_tool.py, it should ask the user for a search term, scrape and save the Google Trends data, and then create the plot automatically so the user does not have to run two separate programs. Reuse the existing code as much as possible and do not make unnecessary changes to the other files.

Reflections on success/failure of this prompt:

*   The AI created a new my_tool.py file that combines the scraping, saving, and plotting steps into one program.
*   It kept the same user input from the first subtask, so the user still gets to choose the search term when the program starts.
*   After the data is scraped and saved to scraped_data.csv, the program calls the existing plotting code from trends_plot.py instead of making the user run it separately.
*   I liked that it reused the existing plotting function instead of copying all of that code into the new file.
*   This should make the tool easier to use because now the user only has to run one command instead of running two different Python files.

----
**NOTE:** Delete this text and repeat the above block for as many prompts as it takes to complete this subtask.

----
**FINAL REFLECTION:** Review your work. Write a brief statement of what you might have done differently in hindsight, or defend why your work was a good approach.

I think my approach worked well because I gave the AI a clear description of what I wanted without telling it exactly how to write the code. The first version worked, so I did not need another prompt. I also liked that the solution reused the code that was already there instead of creating duplicate plotting logic. In hindsight, I would probably take the same approach because the change was simple, easy to test, and made the tool easier to use.

----
----

### NEW TASK: Improve the Tool

----
Another idea that aligns with this challenge:

> Another issue with the current tool is that the time range is fixed in the code, so the user cannot easily compare trends over different periods. I could improve the tool by letting the user choose a time range when the program starts.

----
Which improvement I chose to implement (put an X on the line):

_X_  The professor's example idea

___  My idea above

----
Text of my first prompt:

> Improve my_tool.py so that the plot filename is automatically based on the user's search term instead of always being interest_data.png. For example, if the user searches for "artificial intelligence", the plot could be saved as artificial_intelligence.png. The program should tell the user the name of the output file it creates. If a file with that name already exists, do not automatically overwrite it. Keep the rest of the current workflow the same and reuse the existing code where possible.

Reflections on success/failure of this prompt:

*   The AI correctly made the plot filename depend on the user's search term, so a search like "artificial intelligence" would create artificial_intelligence.png.
*   It also prevented existing files from being overwritten automatically, which was one of the main things I wanted.
*   One thing I noticed was that it automatically added numbers like _1 or _2 when a filename already existed instead of asking the user what they wanted to do.
*   It also copied the plotting code directly into my_tool.py instead of reusing trends_plot.py, which felt like unnecessary duplicate code.
*   Because of those two issues, I decided to make the prompt more specific instead of just accepting the first version.

----
Text of my next prompt:

> The filename idea is close, but I want to make two changes. If the automatically generated plot filename already exists, do not silently create a numbered filename like _1 or _2. Instead, interrupt the workflow and tell the user that the file already exists so they can decide whether to replace it or choose a different filename. Also, reuse the existing plotting code from trends_plot.py instead of copying the plotting logic into my_tool.py if possible. Keep the rest of the workflow unchanged.

Reflections on success/failure of this prompt:

*   The AI improved the code by reusing the plotting function from trends_plot.py instead of copying all of the plotting logic into my_tool.py.
*   It also checked for a filename conflict before starting the scraper, which made sense because scraping takes a while and there is no reason to do it before the filename issue is handled.
*   The new version stopped the program if the filename already existed and told the user what happened.
*   This was closer to what I wanted, but it still did not actually let the user decide whether to overwrite the file or choose a different name.
*   I used one more prompt to make that interaction work the way I originally wanted.

----

Text of my next prompt:

> This is closer to what I want. Keep the current filename generation and reuse of trends_plot.py, but when the plot filename already exists, let the user choose whether they want to overwrite the existing file or enter a different filename. Do not scrape any data until that filename conflict has been resolved. Keep everything else the same.

Reflections on success/failure of this prompt:

*   The AI added a choice for the user when a plot file already exists instead of automatically overwriting it or just stopping the program.
*   The user can now choose to overwrite the existing file or enter a different filename.
*   I liked that this decision happens before any scraping starts, so the tool does not waste time doing work if there is a filename conflict.
*   The program still automatically creates a useful filename when there is no conflict and still reuses the plotting code from trends_plot.py.
*   This version matches the workflow I wanted because the program only interrupts the user when it actually needs a decision from them.

----

**NOTE:** Delete this text and repeat the above block for as many prompts as it takes to complete this subtask.

----
**FINAL REFLECTION:** Review your work. Write a brief statement of what you might have done differently in hindsight, or defend why your work was a good approach.

I think breaking the improvement into a few prompts worked well because I was able to review each version instead of trying to get everything perfect in one prompt. The first response technically solved part of the problem, but it also added duplicate code and handled filename conflicts differently than I wanted. By testing the idea and making the prompts more specific, I ended up with a cleaner tool that reuses the existing code and only asks the user for input when there is actually a filename conflict. In hindsight, I could have been more specific in my first prompt about how I wanted existing files handled, but working through the different versions helped me understand the code better.

----
----

### Final Questions

1.  In your own words, give names to the steps in the problem-solving process you followed.

    I would describe the process as understanding the problem, breaking it into smaller pieces, making one change at a time, testing it, checking what went wrong, and then refining the solution. I also compared my edited code to the original when something was not working so I could figure out whether my change actually caused the problem.

2.  Which step do you find most challenging, and why?

    I think the hardest part is figuring out why something is not working. Sometimes the problem is in the code I just changed, but other times it is coming from somewhere else in the program. For example, I originally thought my search-term change broke the scraper, but after testing the original version I realized the scraper just needed more time to retry. It can be hard to know where the actual problem is at first.

3.  What two questions do you have about how Python expresses the tasks you might ask it to do?

    How does Python decide when it makes more sense to split code into separate functions or files instead of keeping everything in one place?

    When there are multiple ways to write code that does the same thing, how do you know which approach is cleaner or better to use in a larger program?

----
----

### Other's Review

... YOU DO NOTHING HERE; ANOTHER STUDENT WILL COMPLETE THIS PART IN SECTION ...

----
----

### AI's Review

... PASTE AI'S FEEDBACK ON THIS LAB NOTEBOOK HERE ...
