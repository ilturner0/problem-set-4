'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
def do_scatter1(full_merged):
    '''
    Generates a scatter plot of the prediction_felony and prediction_nonfelony columns, hued by charge degree of the current charge.

    Parameters:
        full_merged, dataframe: The merge of felony_charge, pred_universe, and arrest_events dataframes.
    '''
    sns.lmplot(data=full_merged, x='prediction_felony', y='prediction_nonfelony', hue='charge_degree')
    plt.savefig('./data/part5_plots/scatter1.png', bbox_inches='tight')
    print("The group of points on the right side of the plot have a higher prediction for a felony charge. " \
    "Most of the points on this side of the plot are also actual felonies, meaning that as the predicted felony value goes up, the current charge is more likely to be a felony. " \
    "Interestingly, this behavior is not mirrored on the y-axis. " \
    "There are many felonies that also have a high predicted value for a nonfelony.")


# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def do_scatter2(full_merged):
    '''
    Generates a scatter plot of the prediction_felony and y_felony columns (actual felony rearrests).

    Parameters:
        full_merged, dataframe: The merge of felony_charge, pred_universe, and arrest_events dataframes.
    '''
    sns.lmplot(data=full_merged, x='prediction_felony', y='y_felony')
    plt.savefig('./data/part5_plots/scatter2.png', bbox_inches='tight')
    print("This plot does not provide strong evidence for the model being calibrated. " \
    "Ideally, the plot should display two clusters of points: one in the bottom left, and one on the top right." \
    " This would indicate that the model is correctly predicting nonfelony rearrests and felony rearrests. " \
    "Instead, the plot displays two horizontal lines of points at the top and bottom. " \
    "This means that the model is not accurately predicting felony rearrests.")

