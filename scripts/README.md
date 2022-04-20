# BiodivTab - Generator Scripts

This folder contains the scripts used to create BiodivTab from the input tables and their manual annotations.

In particular, this includes the following steps/scripts:
* [/augment](/augemnt) ... apply data augmentation
* [/CTA ancestors](/CTA%20ancestors) ... generate an ancestor file for CTA
* [/reconcile](/reconcile) ... anonymize file names
* [/statistics_scripts](statistics_scripts) ... characterize the benchmark
* [assemble.py](./assemble.py) ... collect all results files for release

## Run

* Requires Python 3.8
* Install all dependencies using `pip install -r requirements.txt`
* Execute the provided scripts individually
