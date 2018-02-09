# CSVScale
# Language: Python
# Input: CSV (with zero entries)
# Output: CSV (with scaled entries)
# Tested with: PluMA 1.0, Python 2.7

PluMA plugin to scale CSV file values such that (1) zero entries are mapped to the minimum value
and (2) the median value becomes 1.  This can be useful particularly for downstream analysis,
if the potential measurement error is larger than the difference between zero and the minimum value
and they need to be treated the same.  This is a scaling that is also sometimes used with metabolomics data. 

The plugin accepts as input the CSV file to scale, and produces as output a new CSV that contains the scaled values.
