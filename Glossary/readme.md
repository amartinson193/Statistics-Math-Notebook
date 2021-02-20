# A collapsible section with markdown
<details>
  <summary>Click to expand!</summary>
  
  ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets
</details>

```
Check it out

```


Probability Mass Function 

Source: Datacamp – Exploratory Data Analysis 

Source: empiricaldist package 

Notes 

Introduced as another way of thinking about distributions 

It basically takes the percentage of the whole and plots it using something like matplotlib.pyplot.bar 

Advantageous because it shows all unique values as opposed to bins 

PDF is the continuous analog to the PMF 

 

Normalize 

Source: DataCamp – Exploratory Data Analysis in Python 

Notes 

This actually means to add up to 1 

 

Cumulative Distribution Function 

Source: DataCamp – Exploratory Data Analysis in Python 

Source: empiricaldist package 

Notes 

For a given value of x, it tells you the probability of getting something <= x 

Example computing the empirical cdf 

def ecdf(data): 

    """Compute ECDF for a one-dimensional array of measurements.""" 

    # Number of data points: n 

    n = len(data) 

 
 

    # x-data for the ECDF: x 

    x = np.sort(data) 

 
 

    # y-data for the ECDF: y 

    y = np.arange(1, n + 1) / n 

 
 

    return x, y 

 

 

Probability Distribution Function 

Source: DataCamp – Exploratory Data Analysis in Python 

 

 

Kernel Density Function 

Source: DataCamp – Exploratory Data Analysis in Python 

Notes 

This is used to get from a PMF to a PDF 

 

PMF, CDF, KDE 
• Use CDFs for exploration. 
• Use PMFs if there are a small number of unique values. 
• Use KDE if there are a lot of values. 
 

Pearson's Correlation Coefficient 

Source: DataCamp – Exploratory Data Analysis in Python 

Notes 

This is what is typically referred to when plotting correlation 

Beware of using this to find relationships between non-linear data. It doesn't work! There can be a non-linear relationship present 

The slope of the line being more dramatic is probably more important than the strength of the correlation (per DataCamp – Exploratory Data Analysis in Python) 

 

p 
covariance 
Pearson correlation 
(std of x) (std of y) 
def pearson_r(x, y): 

    """Compute Pearson correlation coefficient between two arrays.""" 

    # Compute correlation matrix: corr_mat 

    corr_mat = np.corrcoef(x,y) 

 
 

    # Return entry [0,1] 

    return corr_mat[0,1] 

Above is a function we used to define this 

Linear Regression 

Source: DataCamp – Exploratory Data Analysis in Python 

Notes 

Regression is not symmetric, the regression of a onto b is not the same as regression of b onto a 

I.e. the slope is different when swapping the axis 

Regression can't tell you what causes what 

Relation of slope of a regression and correlation 

Correlation appears in several guises. First, it provides a quick, numerical summary of the "strength" of a linear relationship. In this context, correlation only makes sense if the relationship is indeed linear. Second, the slope of the regression line is proportional to the correlation coefficient: slope = r*(SD of y)/(SD of x) Third: the square of the correlation, called "R-squared", measures the "fit" of the regression line to the data. 

Source: http://inspire.stat.ucla.edu/unit_02/teaching_tips.php#:~:text=Second%2C%20the%20slope%20of%20the,regression%20line%20to%20the%20data.&text=If%20it's%20close%20to%201,job%20of%20fitting%20the%20data. 

 

Square Root Rule for binning 

Source: Datacamp – Statistics for Python 1 

Notes 

The number of bins you should have is equal to the square root of the number of rows in your dataset 

Binning Bias 

Possibly making different determinations about your data based on the number of bins 

Median 

More immune to extreme outliers 

Same thing as the 50th percentile 

Variance 

Sum of all the squared differences from the mean divided by the number of data points 

Low variance indicates that data points are generally similar and do not vary widely from the mean. High variance indicates that data values have greater variability and are more widely dispersed from the mean. 

Source: https://www.calculatorsoup.com/calculators/statistics/variance-calculator.php 

There is a difference between the variance of a population vs. Variance of a sample 

 

Standard Deviation 

Square root of the variance 

1,2,3 standard deviation rule 

Source: https://www.google.com/search?q=1+2+3+standard+deviation+rule&rlz=1C1GCEV_enUS928US928&oq=1%2C2%2C3+standard&aqs=chrome.2.69i57j0j0i20i263j0i22i30j0i22i30i395l4.11238j1j7&sourceid=chrome&ie=UTF-8 

This rule says that 1 standard deviation contains 66% of the data, following by 95, 99 for 2 and 3 standard deviations respectively 

Covariance 

Take the difference of the point from the mean of the x and y values 

Multiply them and divide by n 

 

1 
couariance — 
n 
Source: Data Camp Statistical Thinking in Python part 1 

Negative covariance indicates a negative correlation and vice-versa 

 

Bernoulli Trial 

A test where the outcome is Boolean 

E.g. Greater than 5 is True, less than 5 is false 

Binomial Distribution 

Requirements for a binomial distribution 

Source: https://www.thoughtco.com/when-to-use-binomial-distribution-3126596 

Fixed number of trials 

Independent trials 

This means we can multiply probabilities together  

e.g. What is the probability of flipping two coins and getting two heads after 4 tosses of both coins? 

A head's probability is .5 for each so .5**2 results in .25 

Two different classifications 

The probability of success stays the same for all trials 

This is another place where theory and practice are slightly different. Sampling without replacement can cause the probabilities from each trial to fluctuate slightly from each other. Suppose there are 20 beagles out of 1000 dogs. The probability of choosing a beagle at random is 20/1000 = 0.020. Now choose again from the remaining dogs. There are 19 beagles out of 999 dogs. The probability of selecting another beagle is 19/999 = 0.019. The value 0.2 is an appropriate estimate for both of these trials. As long as the population is large enough, this sort of estimation does not pose a problem with using the binomial distribution. 

Mean and standard deviation of a binomial variable 

Source: https://www.khanacademy.org/math/ap-statistics/random-variables-ap/binomial-mean-standard-deviation/v/finding-the-mean-and-standard-deviation-of-a-binomial-random-variable 

Mean is equal to n (number of trials) * p (probability of success) 

Binomial formula 

https://stattrek.com/probability-distributions/binomial.aspx#:~:text=The%20binomial%20distribution%20has%20the,(%201%20%2D%20P%20)%20%5D. 

Other resources 

https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Book%3A_Statistics_Using_Technology_(Kozak)/05%3A_Discrete_Probability_Distributions/5.03%3A_Mean_and_Standard_Deviation_of_Binomial_Distribution 

Resource for checking if distro's are significantly diff 

http://homework.uoregon.edu/pub/class/es202/ztest.html 

Same mean, diff standard devations 

https://www.astro.umd.edu/~miller/teaching/astrostat/lecture09.pdf 

https://towardsdatascience.com/kolmogorov-smirnov-test-84c92fb4158d 

 

Normal Distribution 

https://www.healthknowledge.org.uk/public-health-textbook/research-methods/1b-statistical-methods/statistical-distributions#:~:text=Normal%20distribution%20describes%20continuous%20data,events%20out%20of%20n%20trials. 

There are a lot of different distributions that look normal, but are something else (Poisson, binomial, etc...) 

Normal is based on continuous variables, binomial is based on bernoulli trials, and poisson are essentially rare binomial distributions 

Warning: watch for tails that could be a sign the data is not normally distributed 

Use Cases 

You can check the probability of an event occurring 

For example 

# Take a million samples out of the Normal distribution: samples 

samples = np.random.normal(mu, sigma, 1000000) 

 
 

# Compute the fraction that are faster than 144 seconds: prob 

prob = np.sum(samples <= 144)/len(samples) 

 
 

# Print the result 

print('Probability of besting Secretariat:', prob) 

 

Poisson Process/Poisson Distribution 

Source: Datacamp: Python Stats Part 1 

The timing of the next event is completely independent from when the previous event happened 

 

• Limit of the Binomial distribution for low probability of 
success and large number of trials. 
• That is, for rare events. 
Poisson differs mostly from a binomial by a larger standard deviation due to low probability 

 

Exponential Distribution 

The waiting time between of intervals between events in a poisson process are exponentially distributed 

And since this is poisson, the timing between events should be independent 

Uses Cases: 

Find the waiting time between events, you can plot this as a pdf 

 

Anscombe's Quartet 

Francis Anscombe, a mathematician, published 4 fictitious graphs in 1973. All of them had the same mean for both x and y and same linear regression line 

 

8 6 4 8 6 4 
 

Bootstrapping 

Resampling with replacement 

Can also be done in pairs (e.g. linear regression) when there are two variables 

This is really useful when you only have one data set and need to replicate it many times to try and find the approximate distribution 

Assumes that your dataset represents the population 

https://statisticsbyjim.com/hypothesis-testing/bootstrapping/ 

Bootstrap sample v Bootstrap replicate 

Sample is the data that you generated. Bootstrap replicate is a statistic generated from the bootstrap sample (e.g. mean) 

Pairs Bootstrap 

This is something you do when you have two variables instead of one and need to approximate a line 

Example 

def draw_bs_pairs_linreg(x, y, size=1): 

    """Perform pairs bootstrap for linear regression.""" 

 
 

    # Set up array of indices to sample from: inds 

    inds = np.arange(0, len(x)) 

 
 

    # Initialize replicates: bs_slope_reps, bs_intercept_reps 

    bs_slope_reps = np.empty(size) 

    bs_intercept_reps = np.empty(size) 

 
 

    # Generate replicates 

    for i in range(size): 

        bs_inds = np.random.choice(inds, size=len(inds)) 

        bs_x, bs_y = x[bs_inds], y[bs_inds] 

        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x, bs_y, 1) 

 
 

    return bs_slope_reps, bs_intercept_reps 

 
 

-------------------------------------------------------------------- 

# Generate replicates of slope and intercept using pairs bootstrap 

bs_slope_reps, bs_intercept_reps = draw_bs_pairs_linreg(illiteracy, fertility, 1000) 

 
 

# Compute and print 95% CI for slope 

print(np.percentile(bs_slope_reps, [2.5, 97.5])) 

 
 

# Plot the histogram 

_ = plt.hist(bs_slope_reps, bins=50, normed=True) 

_ = plt.xlabel('slope') 

_ = plt.ylabel('PDF') 

plt.show() 

 

Confidence Interval 

 

• If we repeated measurements over and over again, p% of the 
observed values would lie within the p% confidence interval. 
If two different confidence intervals are non-overlapping, you can be more certain that there was real change 

If something lies outside the confidence interval, then it is considering statistically significant 

Source: https://blog.minitab.com/blog/adventures-in-statistics-2/understanding-hypothesis-tests-confidence-intervals-and-confidence-levels#:~:text=If%20the%20confidence%20interval%20does,contain%20the%20null%20hypothesis%20value. 

Confidence intervals are considered inclusive, something has to be greater or less than the max and min ends of the interval 

Source: https://stats.stackexchange.com/questions/15872/are-confidence-intervals-open-or-closed-intervals#:~:text=I%20would%20say%20that%20confidence,i.e.%20the%20endpoints%20are%20inclusive). 

 

Standard Error of the Mean (SEM) 

Standard deviation of the data divided by the square root of the number of data points 

 

Nonparametric inference 

No assumptions were made about the model underlying the data, the data was used to explain it alone 

Source: Datacamp – Statistical Thinking for Python – Part 2 

 

Permutation 

Assumptions 

Exchangable 

https://stats.stackexchange.com/questions/473076/permutation-tests-and-exchangeability/473087#473087 

https://stats.stackexchange.com/questions/473356/selection-of-test-statistic-for-permutation-test-of-variability 

Random data 

Random reordering of entries in an array 

We assume the distributions are identically distributed 

This test is checking the data comes from the same distribution 

According to my Math 325 notebook, a permutation test is actually seeing if data is random or not 

Also according to the notebook, you use a for loop to create a simulated distribution for this test. It is a non-parametric test 

You can plot the distributions compared to the permutation to help you decide if the distributions are similar or not 

If none of the ECDFs from the permutation samples overlap with the observed data, this suggests that the hypothesis is not commensurate with the data 

This test is usually completed by shuffling the data and the computing something like a difference of means 

Example 

def permutation_sample(data1, data2): 

    """Generate a permutation sample from two data sets.""" 

 
 

    # Concatenate the data sets: data 

    data = np.concatenate((data1,data2)) 

 
 

    # Permute the concatenated array: permuted_data 

    permuted_data = np.random.permutation(data) 

 
 

    # Split the permuted array into two: perm_sample_1, perm_sample_2 

    perm_sample_1 = permuted_data[:len(data1)] 

    perm_sample_2 = permuted_data[len(data1):] 

 
 

    return perm_sample_1, perm_sample_2 

---------------------------------------------------------------------------------------------- 

 

def draw_perm_reps(data_1, data_2, func, size=1): 

    """Generate multiple permutation replicates.""" 

 
 

    # Initialize array of replicates: perm_replicates 

    perm_replicates = np.empty(size) 

 
 

    for i in range(size): 

        # Generate permutation sample 

        perm_sample_1, perm_sample_2 = permutation_sample(data_1,data_2) 

 
 

        # Compute the test statistic 

        perm_replicates[i] = func(perm_sample_1, perm_sample_2) 

 
 

    return perm_replicates 

 

---------------------------------------------------------------------------------------------- 

 

 

# Construct arrays of data: dems, reps 

dems = np.array([True] * 153 + [False] * 91) 

reps = np.array([True] * 136 + [False] * 35) 

 
 

def frac_yea_dems(dems, reps): 

    """Compute fraction of Democrat yea votes.""" 

    frac = np.sum(dems) / len(dems) 

    return frac 

 
 

# Acquire permutation samples: perm_replicates 

perm_replicates = draw_perm_reps(dems, reps, frac_yea_dems, 10000) 

 
 

# Compute and print p-value: p 

p = np.sum(perm_replicates <= 153/244) / len(perm_replicates) 

print('p-value =', p) 

 

 

The goal is plot a distribution of the replicates and then compare your permutation replicate to the distribution 

Mean vote difference under null hypothesis 
p-value 
0.15 
010 
PA — OH mean percent vote difference 
identically distributed. 

Permutation replicate 

A statistic generated from permuted data 

P-value 

The probability of obtaining a value of your test statistic that is at least as extreme as you observed, under the assumption that your null hypothesis is true 

You can simulate this by taking the difference in means of your datasets and then checking to see if the means of your permuted dataset are greater than that difference means 

e.g. empirical_diff_means = diff_of_means(force_a, force_b) 

 
 

# Draw 10,000 permutation replicates: perm_replicates 

perm_replicates = draw_perm_reps(force_a, force_b, 

                                 diff_of_means, size=10000) 

 
 

# Compute p-value: p 

p = np.sum(perm_replicates >= empirical_diff_means) / len(perm_replicates) 

One-sample test 

Compare data to one single number 

To do this, you shift the values of the data to match the other mean since you are trying to see the probability of getting that single number mean if the datasets had the same mean 

Example 

def bootstrap_replicate_1d(data, func): 
    """Generate bootstrap replicate of 1D data.""" 
    bs_sample = np.random.choice(data, len(data)) 
    return func(bs_sample) 

------------------------------------------------------- 

def draw_bs_reps(data, func, size=1): 

    """Draw bootstrap replicates.""" 

 
 

    # Initialize array of replicates: bs_replicates 

    bs_replicates = np.empty(size) 

 
 

    # Generate replicates 

    for i in range(size): 

        bs_replicates[i] = bootstrap_replicate_1d(data,func) 

 
 

    return bs_replicates 

---------------------------------------------------------------------------------------------------------- 

# Make an array of translated impact forces: translated_force_b 

translated_force_b = force_b - np.mean(force_b) + .55 

 
 

# Take bootstrap replicates of Frog B's translated impact forces: bs_replicates 

bs_replicates = draw_bs_reps(translated_force_b, np.mean, 10000) 

 
 

# Compute fraction of replicates that are less than the observed Frog B force: p 

p = np.sum(bs_replicates <= np.mean(force_b)) / 10000 

 
 

# Print the p-value 

print('p = ', p) 

 

Here is another example: 

def draw_bs_pairs(x, y, func, size=1): 

    """Perform pairs bootstrap for a single statistic.""" 

 
 

    # Set up array of indices to sample from: inds 

    inds = np.arange(len(x)) 

 
 

    # Initialize replicates: bs_replicates 

    bs_replicates = np.empty(size) 

 
 

    # Generate replicates 

    for i in range(size): 

        bs_inds = np.random.choice(inds, len(inds)) 

        bs_x, bs_y = x[i], y[i] 

        bs_replicates[i] = func(bs_x, bs_y) 

 
 

    return bs_replicates 

 

Two-sample test 

Compare two sets of data 

Example 

# Compute mean of all forces: mean_force 

mean_force = np.mean(forces_concat) 

 
 

# Generate shifted arrays 

force_a_shifted = force_a - np.mean(force_a) + mean_force 

force_b_shifted = force_b - np.mean(force_b) + mean_force 

 
 

# Compute 10,000 bootstrap replicates from shifted arrays 

bs_replicates_a = draw_bs_reps(force_a_shifted, np.mean, size=10000) 

bs_replicates_b = draw_bs_reps(force_b_shifted, np.mean, size=10000) 

 
 

# Get replicates of difference of means: bs_replicates 

bs_replicates = bs_replicates_a - bs_replicates_b 

 
 

# Compute and print p-value: p 

p = np.sum(bs_replicates >= empirical_diff_means) / len(bs_replicates) 

print('p-value =', p) 

Empirical diff means above simply means the difference in the means between control and treated populations 

A/B Testing 

A form of hypothesis testing where you test one version of a product compared to another one 

Uses permutation testing 

Hypothesis test for correlation 

 

Hypothesis test of correlation 
• Posit null hypothesis: the two variables are completely 
uncorrelated 
• Simulate data assuming null hypothesis is true 
• Use Pearson correlation, p, as test statistic 
• Compute p-value as fraction of replicates that have p at least 
as large as observed. 
 

 

Random 

You could always use this to test the likelihood of an event occurring if you don't know the distribution 

For example, you could take 100 tests 

 

Number of Possibilities 

 

With replacement, it is simply the number of options per slot * the number of slots 

e.g. how many different combos are for heads and tails if you flip 4 times? 

 

Z-Table 

Used to find the area under a curve after it has been normalized to a normal bell curve with a standard deviation of 1 

 

Z-Score #zscore 

Can be used on all types of distributions, but a typical z score is used for a normal distribution simply to calculate the percentage under the curve that is above or below the z score 

 


 

 

Standard deviation for two-sample t-test 

http://www.stat.yale.edu/Courses/1997-98/101/meancomp.htm 

 

Standard deviation of the differences vs pooled standard deviation 

Can use pooled standard deviation if the standard deviations can be assumed to be similar 

Here is the formula 

https://www.statology.org/pooled-standard-deviation/ 

https://www.statisticshowto.com/pooled-standard-deviation/ 

According to this site, similar standard deviations are between .5 and 2 when dividing from each other 

https://online.stat.psu.edu/stat500/lesson/7/7.3/7.3.1/7.3.1.1 

If the smaller deviation has larger n, it's not recommended to use the pooled procedure 

http://faculty.washington.edu/tamre/Chapter9PooledVariances.pdf 

This gives me a different answer than the equation sqrt(s1^2(n-1) + s2^2(n-1)/n+n-2) 

https://www.statology.org/pooled-standard-deviation-calculator/ 

Nvm, I wasn't summing the denominator, I was only taking 1 n -2  

 

Coefficient of Variation 

This is the standard deviation /mean, less than 1 indicates low std and greater than 1 indicates high 

Source: https://math.stackexchange.com/questions/260617/how-to-determine-if-standard-deviation-is-high-low 

 
