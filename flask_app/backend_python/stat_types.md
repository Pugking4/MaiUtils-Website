~~1. Average constant level for all charts played, only count ones which have a constant~~
~~2. Average constant level for all charts played, count charts with constant and non-constant levels. Non-constant levels are counted as x.0 and x+ levels are counted as x.7~~
~~3. Who I play with the most~~
~~4. Average constant level of charts I play with other people~~
~~5. Average constant level of charts I play with other people with 2. applied~~
~~6. % of charts which I get a new record on for score~~
~~7. % of charts which I get a new record on for dx score~~
~~8. % of times I get FS, FS+, FSD and FSD+ on charts for each person I play with~~
~~9. Who failed FSD if one person got FC+ and the other got FC, who failed FSD+ if one person got AP and the other got FC+~~
~~10. % of picks I get FC, FC+, AP and AP+~~
~~11. Avg dx stars for each constant and level~~
~~12. % of charts I give up on (give up = 90% or less)~~
~~13. Who I give up with the most (give up = 90% or less)~~
~~14. Most common genre pick for myself, includes solo and multi~~
~~15. Most common genre pick for myself, only includes solo~~
~~16. taps, holds, slides, touch, break and all note type ratios~~
~~17. Most played charts, specify by constant or level~~ (scrapped for now as it's already limited avaliable on maimai.net)
~~18. % ratio of what difficulties I play~~
~~19. % ratio of what levels I play~~
~~20. % ratio of what int levels I play~~
~~21. % ratio of genres for each player~~
~~22. Weighted average~~ [pichu] (scrapped for now until I find better implementation than (achv * constant) / ((avg_internal_level + avg_internal_level_none) / 2))

98.7514% on 14.4 | constant baseline: (13.316161616161619 + 13.74666666666667) / 2 = 13.5314141414
(98.7514 * 14.4) / 13.5314141414
= 105.090284366

100.8914% on 12.3 | constant baseline: (13.316161616161619 + 13.74666666666667) / 2 = 13.5314141414
(100.8914 * 12.3) / 13.5314141414
= 91.7098691262


~~23. Weighted average~~ [pichu] (use constant inverse for weighted average) (scrapped)

ex 1:
100.8914% on 12.3 | weight: 1/12.3 = 0.081300813
100.8914 * 0.081300813
= 8.20255284471

98.7514% on 14.4 | weight: 1/14.4 = 0.06944444444
98.7514 * 0.06944444444
= 6.85773611067

sum of weights: 0.15074525744 
sum of weighted score: 15.0602889554 

weighted avg: 15.0602889554 / 0.15074525744
= 99.9056

ex 2:
100.0000% on 13.0 | weight: 1/13.0 = 0.07692307692
100.0000 * 0.07692307692
= 7.692307692 

99.0000% on 14.0 | weight: 1/14.0 = 0.07142857142
99.0000 * 0.07142857142
= 7.07142857058

sum of weights: 0.14835164834
sum of weighted score: 14.7637362626

weighted avg: 14.7637362626 / 0.14835164834
= 99.5185

23. Weighted average [pichu] (use constant for weighted average)

score * constant = weighted score
sum of weighted scores / sum of constants = weighted average

ex 1:
100.8914% on 12.3
100.8914 * 12.3
= 1240.96422

98.7514% on 14.4
98.7514 * 14.4
= 1422.02016

sum of weights: 26.7
sum of weighted score: 2662.98438

weighted avg: 2662.98438 / 26.7
= 99.7372426966

ex 2:
100.0000% on 13.0
100.0000 * 13.0
= 1300.0000

99.0000% on 14.0
99.0000 * 14.0
= 1386.0000

sum of weights: 27.0
sum of weighted score: 2686

weighted avg: 2686 / 27.0
= 99.4814814815
