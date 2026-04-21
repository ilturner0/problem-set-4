'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def do_fta_bar_plot(pred_universe):
    '''
    Generates a bar plot of the fta column in the pred_universe dataframe.

    Parameters:
        pred_universe : dataframe
    
    Returns:
        N/A
    '''
    sns.countplot(data=pred_universe, x='fta')
    plt.savefig('./data/part3_plots/vertical_fta_barplot.png', bbox_inches='tight')
    return



# 2. Hue the previous barplot by sex
def do_hued_fta_bar_plot(pred_universe):
    '''
    Generates a bar plot of the fta column in the pred_universe dataframe hued by sex.

    Parameters:
        pred_universe : dataframe
    
    Returns:
        N/A
    '''
    sns.countplot(data=pred_universe, x='fta', hue='sex')
    plt.savefig('./data/part3_plots/hued_vertical_fta_barplot.png', bbox_inches='tight')
    return


# 3. Plot a histogram of age_at_arrest
def do_histogram(pred_universe):
    '''
    Generates a histogram of the age_at_arrest column in the pred_universe dataframe.

    Parameters:
        pred_universe : dataframe
    
    Returns:
        N/A
    '''
    sns.histplot(pred_universe, x='age_at_arrest')
    plt.savefig('./data/part3_plots/age_histplot.png', bbox_inches='tight')
    return

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 

def do_binned_histogram(pred_universe):
    '''
    Generates a histogram of the age_at_arrest column in the pred_universe dataframe with bins for the above age groups.

    Parameters:
        pred_universe : dataframe
    
    Returns:
        N/A
    '''
    sns.histplot(pred_universe, x='age_at_arrest', bins=[18, 21, 30, 40, 100])
    plt.savefig('./data/part3_plots/binned_age_histplot.png', bbox_inches='tight')
    return
