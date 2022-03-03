# PS2114
Programming for Psychologists

Welcome to the GitHub for PS2114! This is an exercise encouraging you to explore the features of GitHub, as well as giving you the opportunity to practice a degree of collaborative coding. As we've discussed in the lecture about collaborative coding, GitHub is a tool that allows you to work on the same project as many other people, alter code to your heart's content, and then merge those changes back into the "main" branch of the project. 

For your exercise today, I've uploaded a Python file that attempts to implement a cognitive model of the phonological loop (based upon a Matlab implementation originally produced by Lewandowsky & Farrell, 2010) - you may remember this as a feature of Baddeley's model of working memory. There are two primary assumptions of the phonological loop; the first is that any information entering the loop decays. This decay cannot be prevented, but information can be refreshed through rehearsal. The model attempts to represent this, in an attempt to capture how frequency of rehearsal may impact memory for words.

Your task today, as a group, is to use Github to try to understand what the file is intended to be doing, and then comment on the code (in a branch of your own) to help clarify what is happening. 

Once you've gotten to grips with the code, you might start to notice that it doesn't seem to reflect what you might expect from human behaviour. There are some changes that may benefit this, which you should implement onto a branched version of the phonoloop.py file:

Add to line 5:
  import numpy.random as rnd 

Replace line 15 with (and insert before the current line 16):
  decRate = 0.8     # Mean decay rate (per second)
  decSD = 0.1       # Standard deviation of decay
  
And finally add this inbetween lines 27 and 28:
  dRate = decRate+rnd.randint(0,3)*decSD
  
Try downloading and running the code once you've made these changes; how does it impact the output?

Once you've experimented with this, try manipulating the variables listed at the start of the model to see how it further affects the produced output.
