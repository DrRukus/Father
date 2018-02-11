def id_outlier(df):
    ## Create a vector of 0's of length equal to the number of rows
    temp = [0] * df.shape[0]
    for i, x in enumerate(df['enginesize']):
        if x > 190: temp[i] = 1
    for i, x in enumerate(df['weight']):
        if x > 3500: temp[i] = 1
    for i, x in enumerate(df['citympg']):
        if x > 40: temp[i] = 1
    return df

def auto_scatter_outlier(df, plot_cols):
    import matplotlib.pyplot as plt
    outlier = [0, 0, 1, 1] # Vector of outlier indicators
    fuel = ['gas', 'diesel', 'gas', 'diesel'] # Vector of fuel types
    color = ['DarkBlue', 'DarkBlue', 'Red', 'Red'] # Vector of color choices for plot
    marker = ['x', 'o', 'o', 'x']
    for col in plot_cols: # loop over the columns
        fig = plt.figure(figsize=(6,6))
        ax = fig.gca()
        ## Loop over the zip of the four vectors and subset the data and
        ## create the plot using the aesthetics provided
        for o, f, c, m in zip(outlier, fuel, color, marker):
            temp = df.ix[(df['outlier'] == o) & (df['fueltype'] == f)]
            if temp.shape[0] > 0:
                temp.plot(kind='scatter', x=col, y='lnprice',
                          ax=ax, color=c, marker=m)
        ax.set_title('Scatter plot of lnprice vs. ' + col)
        fig.savefig('scatter_' + col + '.png')
    return plot_cols

def azureml_main(df):
    import matplotlib
    matplotlib.use('agg')
    ## Define the plot columns
    plot_cols = ['weight', 'enginesize', 'citympg']
    df = id_outlier(df) # mark outliers
    auto_scatter_outlier(df, plot_cols) # create plots
    df = df[df.outlier == 1] # filter for outliers
    return df