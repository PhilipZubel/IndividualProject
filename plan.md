# Plan

* GrillBot: Creating a Complex Query Task-Based Dataset and Implementing an Augmented Task Pipeline
* Philip Zubel
* 2479229z
* Jeff Dalton

## Winter semester

* **Week 1** - Topic not known yet.
* **Week 2** - I set up the github repository workflow/required documents.
* **Week 3** - I had initial advisor and team meetings. I did background research on GrillBot and read introductory research papers.
* **Week 4** - I got up and runnning with OAT. I also made some initial analysis on search queries.
* **Week 5** - I started creating evaluation guidlelines and made first changes to OAT.
* **Week 6** - I set up Pyserini system components into a local jupyter notebook which are now independent of the whole system.
* **Week 7** - I understood how the search system works in the system and played around with it locally.
* **Week 8** - I managed to build a sparse index locally and index a small corpus of documents. I also started looking into the dense retrieval models.
* **Week 9** - I got to understand the structure of runs and qrels and I performed dummy evaluation results on the evaluated documents. I also started looking into marqo. I also started creating queries.
* **Week 10** - I integrated the ance index and pygaggle into the project.
* **Week 11 [PROJECT WEEK]** I put more time into developing queries.  I also built the Pyserini index on the whole cropora on a CPU.
* **Week 12 [PROJECT WEEK]** Status report submitted. I integrated Pygaggle with the ance dense model.

## Winter break
I refactored the whole repo to make the implementation OOP rather than having many redundant code across many notebook. I created a query preprocessing pipeline, handcrafted the queries again, implemented a tct-colbert index, and was debugging marqo on a small number of tasks.

## Spring Semester

* **Week 13** I implemented a TaskGraph viewer and generated empty judgments to fill.
* **Week 14** I tried building the marqo index but it takes too long on a CPU... I will need to make a change in the following week to accomodate cuda. I also migrated from a Google Instance to AWS. I started annotating.
* **Week 15** I finished annotating DIY and started doing Cooking annotations. I built Marqo indexes (non-fielded).
* **Week 16** I'm in the process of annotating cooking judgments and made analysis on DIY data.
* **Week 17** I finished annotating cooking judgments and went into more detail with DIY analysis. 
* **Week 19** I finished analysis of the DIY collection and produced cooking results. I started annotating more since judgments are required for examining fielded retrieval.
* **Week 20** I optimized BM25 and RM3 models using grid search and made more annotations.  
* **Week 21** I'm currently half-way through the annotations. I also implemented mean reciprocal rank. I made cooking analysis which in the same way as DIY. I also built the fielded indexes with marqo.
* **Week 22** I made statistical tests and made a fisrt draft of the disseration. 
* **Week 23 [TERM ENDS]** I mainly cleaned up the repository and editted the dissertation. I also made the dissertation video. 
* **Week 24** Dissertation submission deadline and presentations.

