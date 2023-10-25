# Psychopy Paradigm for the MFT fMRI Replication

For more information on the paradigm read the [Study Guide](https://docs.google.com/document/d/1HIdleJGiyqtjdhKCvUnPwdE2GkKPIbJm3RiuHO7b8zw/edit). To try it out, you can run the .psyexp script in Psychopy. We have one old version in English (morality_fmir_700_EN_comp) and three always up-to-date versions in Dutch. morality_fmri_NL_clips work together with some video clips we havebut could not upload. morality_fmri_NL_images work together with the images in smid.zip and smid_stimuli.xlsc. This paradigm also entails jitter for the interstimulus intervals. morality_fmri_NL_vignettes is a paradigm which runs vignettes from the vig_text_english_dutch.xlsx.
Be sure to always download the additional files in the same folder and unzip the SMID images.

Naming Conventions: 700 vs. 1400 stands for the TR's we used to calculate the repetition times; EN, NL for the language and the suffix 'comp' stands for the computer friendly version, where 'hjkl' will be used instead of the letters the button box hands in ('bygr' in the BSL lab). You can continue texts which would be ended by the fMRI operator, through pressing 't'. 

If you just want to check the paradigm, you can shorten it through slicing the result of the pseudoRand function in the 'Selected rows' field of the loop (e.g. v_pseudoRand("vig_text_english_dutch.xlsx")\[0:3\]).
