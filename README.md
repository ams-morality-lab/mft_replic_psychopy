# Psychopy Paradigm for the MFT fMRI Replication

For more information on the paradigm read the [Study Guide](https://docs.google.com/document/d/1HIdleJGiyqtjdhKCvUnPwdE2GkKPIbJm3RiuHO7b8zw/edit). To try it out, you can  run the .psyexp script in Psychopy. Be sure to also download the other files in the same folder and unzip the SMID images. If you are running the Dutch version please also download the Videos from our Google Drive.

Naming Conventions: 700 vs. 1400 stands for the TR's we used to calculate the repetition times; EN, NL for the language and the suffix 'comp' stands for the computer friendly version, where 'hjkl' will be used instead of the letters the button box hands in ('bygr' in the BSL lab). You can continue texts which would be ended by the fMRI operator, through pressing 't'. 

If you just want to check the paradigm, you can shorten it through typing $np.random.choice(120,12,replace = False) into the 'Selected rows' field of the loop. Please also divide the trials need for a break through 10, to test those too. 
