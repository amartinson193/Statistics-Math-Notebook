def check_ols_assumptions(x: pd.Series, y:pd.Series, predicted_values:pd.Series, time:pd.Series = pd.Series(dtype='float64'))-> None:
    """Checks for the linear regression assumptions:
        1. The regression relation between Y and X is linear.
        2. The error terms are normally distributed.
        3. The variance of the error terms is constant over all X values.
        4. The X values can be considered fixed and measured without error (doesn't check for, requires knowledge of how data was gathered)
        5. The error terms are independent (homeoscadiscticity - equal or similar variances in groups being compared)

    Args:
      x: The independent variable 
      y: The response variable
      predicted_values: The predicted y variable output of a linear regression
      time: The time arg can either be represented as dates or a chronoligical number representing time (i.e. days, months, years) 

    Returns:
      None

    Raises:
      TypeError: If args are not numpy arrays.
    """
    # Import required packages
    import matplotlib.pyplot as plt
    import statsmodels.api as sm
    from matplotlib.gridspec import GridSpec

    # Preprocessing - Check data types
    for arg in [x,y,predicted_values,time]:
        if type(arg) in [pd.Series,np.ndarray]:
            pass
        else:
            raise TypeError('Arguments passed to this function need to either be Pandas Series or Numpy Arrays')

    # Preprocessing - Get the residuals
    residuals = y - predicted_values
    
    # Figure 1 - Plot the linear regression with a fitted line
    plt.scatter(x, y)
    plt.plot(x, predicted_values, c='r')
    plt.title('Linear Regression Scatterplot')
    plt.xlabel('x variable')
    plt.ylabel('y variable')
    
    # Figure 2 - Create the figure and axes
    fig = plt.figure(constrained_layout=True)
    gs = GridSpec(1, 2, figure=fig)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    
    # Figure 2 - Tests for normality - Create a qqplot 
    fig.suptitle('Tests for Normality (Assumption #2)')
    sm.qqplot(y, line='45', fit=True, ax=ax1) 
    ax1.set_title('QQ Plot')
    
    # Figure 2 - Tests for normality - Create a histogram
    ax2.hist(residuals)
    ax2.set_title('Histogram of the Residuals')
    ax2.set(xlabel = 'Residuals')
    ax2.set(ylabel = 'Frequency')
    plt.show()

    # Figure 3 - Create the figure and axes
    if len(time) != 0:
        fig = plt.figure(figsize=((7,10)))
        gs = GridSpec(2, 1, figure=fig)
        ax3 = fig.add_subplot(gs[0, 0])
        ax4 = fig.add_subplot(gs[1, 0])
    else:
        fig = plt.figure(constrained_layout=True)
        gs = GridSpec(1, 1, figure=fig)
        ax3 = fig.add_subplot(gs[0, 0])
        
    # Figure 3 - Create a fitted vs values plot
    lowess = sm.nonparametric.lowess
    lowess_values = pd.Series(lowess(residuals, x)[:,1])

    ax3.scatter(x, residuals)
    ax3.plot(x, lowess_values, c='r')
    ax3.axhline(y=0, c='black', alpha=.75)
    ax3.set_title('Fitted vs. Residuals - Tests for Linearity and Constant Variance (Assumptions #1 and #3)')
    ax3.set(xlabel = 'Fitted Values')
    ax3.set(ylabel = 'Residuals')
    
    # Figure 3 - Add fitted vs order plot if there is a time component
    if len(time) != 0:
        ax4.scatter(time, residuals)
        ax4.axhline(y=0, c='black', alpha=.75)
        ax4.set_title('Order vs. Residuals - Tests for Independent Error Terms (Assumption #4)')
        ax4.set(xlabel = 'Order')
        ax4.set(ylabel = 'Residuals')

    plt.show()