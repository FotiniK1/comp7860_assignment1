# comp7860_assignment1
Repositoty for Assignment 1 of COMP7860. Here we submit all input and output files, scripts, results and discussion files.


For this assignment we work with code that does Named Entity Recognition (NER). In summary, we gather text from two webpages, apply the Stanford NER system on that text and, after some processing, evaluate its performance.

All work was done in a Virtual Machine (VM) created in Oracle Cloud. The VM has been set with an Ubuntu (22.04 Minimal) image and a VM.Standard.E2.2 shape with OCPUcount=2 and 16GB of memory. 

We start the assignment by downloading the Stanford NER system (process described in their website) and run it on a sample text (file name: sample.txt) offered within the installation. The results of this step are only meant to familiarise us with the system and are, therefore, not saved in the repository.

The next task is to write two scripts that download the main text from a Wikipedia page for an actor and a Fanwiki character. For the Wikipedia text we chose the page for actor Sigourney Weaver. The Python script is named extract-wikipedia.py and the text is saved in the wikipedia.txt file. For the Fanwiki page, we chose the character Jean Pierre Polnareff, from the anime "Jojo's Bizarre Adventure". Similarly, the Python script is named extract-fanwiki.py and the output is saved in the fanwiki.txt file.

We, then, write a script (named stanford-ner.py) to apply the Stanford NER system on both texts which will classify each word as PERSON, ORGANIZATION or LOCATION. All words and punctuation marks that cannot be classified as one of the three classes are given the tag O. Our programme calls the existing ner.sh script, applies it to the wikipedia.txt and fanwiki.txt files and produces the output files stanford-wikipedia.txt and stanford-fanwiki.txt, respectively, containing the original text with the tags. 

For the next step, a script is written (ner-list.py) that extracts the words that are in one of the three main classes and lists them, one per line. Consecutive words with the same tag are placed on the same line, as they usually belong to the same person (e.g., name and surname), organisation (e.g., Screen Actors Guild) or location (e.g., New York). The input files are stanford-wikipedia.txt and stanford-fanwiki.txt and the output files are called ner-list-wikipedia.txt and ner-list-fanwiki.txt, respectively.

What follows is the evaluation of the performance of the Stanford NER system. The system is not perfect. Therefore, some of the tags were incorrect. To do this, a "gold standard" version of our texts needs to be created. For this purpose, we took the stanford-wikipedia.txt and stanford-fanwiki.txt files, copied them and manually corrected the wrong tags. We named the corrected files stanford-wikipedia-corr.txt and stanford-fanwiki-corr.txt. The corrected files need to be converted to a particular format for the evaluation. All word-tag pairs have to be displayed in separate lines, the '/' character connecting the pair needs to be eliminated and the pair elements (word, tag) have to be separated by a tab-space. We wrote a script (named gold-standard.py) that does precisely that. The input files are stanford-wikipedia-corr.txt and stanford-fanwiki-corr.txt and the outputs produced are named wikipedia-gold.txt and fanwiki-gold.txt, respectively. 


To perform the evaluation, we write a script (eval.sh). The script is run on the wikipedia-gold.txt and fanwiki-gold.txt files. This results in a table for each file containing the three classes and the values of the Accuracy, Recall and F1-score metrics, and the number of True Positives, False Positives and False Negatives. An explanation of the results is written in the discussion.txt file. The output files are named wikipedia-eval.txt and fanwiki-eval.txt and they contain three columns. The first column has all the words for each text, the second has the corrected tags and the final column contains tags given to each word by the Stanford NER system. The evaluation script compares the two tag results for each word to perform the evaluation.


The final task of the assessment is fixing the NER system. Many times the NER tagger tags punctuation marks with one of the three main classes, when it shouldn't. We wrote a script (fix-ner.py) that changes the tag on punctuation marks to be /O always. We apply the script to the wikipedia.txt and fanwiki.txt files, which produces outputs named fixed-wikipedia.txt and fixed-fanwiki.txt. We then take the fixed files, change thier format using the gold-standard.py script. The outputs are named fixed-wikipedia-gold.txt and fixed-fandom-gold.txt. Finally, we perform the evaluation task getting output files named fixed-wikipedia-eval.txt and fixed-fandom-eval.txt, and compare the metrics with the previous results. A comparison and discussion of the results can be found in the discussion.txt file.

NOTE: For the last task, we did not correct tags manually for both texts due to time constraints and their size. We only made minor changes to the fixed-wikipedia.txt file (renamed fixed-wikipedia2.txt), as the Stanford NER system does not recognise punctuation marks that are insde a word (or multiple words) that are not separated by a space. For example, in the phrase "... Scots/O -/O Irish/O ,/O and/O Scottish/O ancestry.At/O the/O age/O ...", the characters '-' and ',' are recognised as punctuation marks and tagged as '/O', whereas in "ancestry.At" it registers the '.' character as part of a larger word and classifies all three entities as '/O'. This is good when the entities are part of a website (e.g., Emmys.com), however, it may change the classification and evaluation results for all other instances. Nevertheless, it will be interesting to see how the metrics change, if they change at all, after manual tag correction for all incorrect tags.



# References and sources used
1. Dras, M., 2023, COMP8240/COMP7860: Applications of Data Science, Assessed Task 1.
2. OpenAI. (2023). ChatGPT (August 3 version) [Large language model]. https://chat.openai.com/
3. reference accuracy, recall and F1 score info.
