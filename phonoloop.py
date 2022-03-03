# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd
hrRange = np.array([1.64, 1.92, 2.33, 2.64, 3.73, 3.94]) 
# Human speech rate
hdata = np.array([0.31, 0.47, 0.51, 0.7, 0.72, 0.8])     
# Human proportion correct

nReps = 1000       # Number of reps

listLength = 5    # List length
initAct = 1       # Initial activation after study
decRate = 0.8     # Mean decay rate (per second)
decSD = 0.1       # Standard deviation of decay
delay = 5.        # Retention interval (seconds)
minAct = 0.0      # Minimum activation needed to recall

rRange = np.arange(1.4, 4., (4.-1.4)/15.)
tRange = 1./rRange

pCor = np.zeros(len(rRange))

i=0  # Index for word lengths.
for tPerWord in tRange:
    for rep in range(nReps):
       dRate = decRate+rnd.randint(0,3)*decSD
       actVals = np.ones(listLength)*initAct
       cT = 0.0
       itemReh = -1 # Start rehearsal with beginning of list
       while cT<=delay:
            intact = np.argwhere(actVals>minAct).ravel()
            # Find the next item still accessible.
            nextindexes = np.where(intact>itemReh)[0]
            # Rehearse or return to beginning of list.
            if len(nextindexes)==0:
                itemReh = 0
            else:
                itemReh = intact[nextindexes[0]]
            actVals[itemReh] = initAct
            # Everything decays.
            actVals = actVals - (dRate*tPerWord)
            cT = cT+tPerWord
       pCor[i] = pCor[i] + sum(actVals>minAct)/listLength
    i+=1

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(rRange,pCor/nReps,'ko',antialiased=True,
        markersize=3,linewidth=1)
ax.plot(hrRange, hdata, 'ro', antialiased=True,markersize=5)
ax.set_xlabel('Speech Rate')
ax.set_ylabel('Proportion Correct')
ax.set_title('Model versus data')
