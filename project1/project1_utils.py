import numpy as np

import thinkstats2

"""
Function to group a DataFrame into bins

Arguments
----------
df:         DataFrame
group_name: the column we want its values to become bins. 
            The values have to be discrete.
bin_size:   range of value of each bin.

Return
----------
bins:       a list of bin names
groups:     a GroupBy object
"""


def GroupToBins(df, group_name='cmputr_time', bin_size=1):
    dataSeries = df[group_name]
    bins = np.arange(dataSeries.min(), dataSeries.max() + 1, bin_size)
    indices = np.digitize(dataSeries, bins)
    return np.array(bins), df.groupby(indices)


"""
CalculatePercentages is an OPERATION we want to 
operate on each binned group in a GroupBy object

Arguments
----------
groupResults: the returned value from GroupToBins()
variable:     the variable of interest that will be analyzed/processed in each binned group

Return
---------
bins:         a list of bin names
groups:       a list of percentages corresponding to each group
"""


def CalculatePercentages(groupResults, variable='depression_lvl'):
    bins, groups = groupResults
    perc = []  # Percentage list
    for i, group in groups:
        total = group[variable].count()
        positives = group[variable][group[variable] > 0].count()  # Having anxiety/depression
        perc.append(positives / total * 100)
    return np.array(bins), np.array(perc)


"""
Take a sample from a distribution and run many iterations
to calculate estimates

Arguments
----------
df:             DataFrame
group_name:     the column we want its values to become bins. 
                The values have to be discrete.
variable:       the variable of interest that will be analyzed/processed in each binned group
Operation:      Operation to calculate the statistic
bin_size:       size of the bins
iters:          number of iterations

Return
---------
estimates:      a list of estimates list
"""


def SamplingDistributions(df, group_name='cmputr_time', variable='depression_lvl', Operation=CalculatePercentages,
                          bin_size=1, iters=101):
    t = []
    for _ in range(iters):
        sample = thinkstats2.ResampleRows(df)
        _, estimates = Operation(GroupToBins(sample, group_name, bin_size), variable)
        t.append(estimates)
    return np.array(t).transpose()


"""
Compute 90% CI of the estimates

Arguments
----------
estimates:      a list of estimates

Return
---------
CI:             90% CI of the estimates
"""


def ComputeCI(estimates):
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.ConfidenceInterval(90)
    return ci


"""
Compute 90% CI of a list of estimate lists

Arguments
----------
estimatesList:      a list of estimate lists

Return
---------
CIs:             a list of 90% CI of the estimates
"""


def ComputeCIs(estimatesList):
    cis = []
    for estimates in estimatesList:
        ci = ComputeCI(estimates)
        cis.append(ci)
    return np.array(cis).transpose()


"""
Operation: Calculate Proportional Percentage
"""


def CalculateProportionalPercentage(groupResults, variable='depression_lvl'):
    _, perc = CalculatePercentages(groupResults, variable=variable)
    return perc, perc[1] / perc[0]  # Proportional percentage of depression (High / Low)
