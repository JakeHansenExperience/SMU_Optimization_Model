Project written by Jake Hansen Experience Consulting, May 2020, aka during the
apcalypse, for Oldcastle BuildingEnvelope (aka Ike). This is
prototype version 1.0




Running Instructions:

cd into current directory
run python manage.py migrate
run python manage.py runserver


Go to http://127.0.0.1:8000/admin/
to create plants and demands for the optimization model



Go to http://127.0.0.1:8000/calculator/plants
to choose the plants / demands you would like to use for a run of the optmization model,
choose the function, and name this layout.

Click Optomize!


go to http://127.0.0.1:8000/admin/calculator/layout/

to see the result of the model!





Dependencies:


Python 3.8.1
Django 3.0.6
Gekko  0.2.6



Citations:

Beal, L.D.R., Hill, D., Martin, R.A., and Hedengren, J. D., GEKKO Optimization
Suite, Processes, Volume 6, Number 8, 2018, doi: 10.3390/pr6080106.

@article{beal2018gekko,
title={GEKKO Optimization Suite},
author={Beal, Logan and Hill, Daniel and Martin, R and Hedengren, John},
journal={Processes},
volume={6},
number={8},
pages={106},
year={2018},
doi={10.3390/pr6080106},
publisher={Multidisciplinary Digital Publishing Institute}}
