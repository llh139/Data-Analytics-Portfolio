import pandas as pd
import matplotlib.pyplot as plt

def create_df(input_df, target_feature):
    """
    Function to create df of sales group by different features such as year, quarter and month

    Input: Original complete df, target group eature such as year and sales channel
    Output: Sales df grouped by target feature containing average, median and total sales

    Return: Sales df
    """
    output_df = pd.DataFrame(columns=[target_feature, 'Average Sales', 'Median Sales', 'Total Sales'])
    output_df[target_feature] = input_df[target_feature].unique()
    output_df['Average Sales'] = list(input_df.groupby([target_feature])['Sales'].mean())
    output_df['Median Sales'] = list(input_df.groupby([target_feature])['Sales'].median())
    output_df['Total Sales'] = list(input_df.groupby([target_feature])['Sales'].sum())

    return output_df

def plot_sales_graph(input_df, height=8, width=3, rotation_degree=0):
    """
    Function to plot the charts of sales vs target feature (1st column as index) such as year and sales channel

    Input: grouped df
    Output: 2 charts of average, median and total sales vs target feature

    Return: None
    """
    input_df.index = input_df[input_df.columns[0]]
    fig = plt.figure(figsize=(height, width))

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(input_df.index, input_df[['Average Sales', 'Median Sales']])
    ax1.set_title(input_df.columns[0])
    ax1.set_xticks(input_df.index)
    ax1.tick_params('x', labelrotation=rotation_degree)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.plot(input_df.index, input_df[['Total Sales']])
    ax2.set_xticks(input_df.index)
    ax2.tick_params('x', labelrotation=rotation_degree)

    fig.tight_layout()
    fig.show()

def turn_categories_into_num(df, target_feature):
    """
    Function to add an extra column of numeric labels of the input feature which is originally in text

    Input: df, target feature series in text

    Return: Category series in num
    """
    categories = df[target_feature].unique()
    column_name = target_feature + 'No'
    df[column_name] = df[target_feature]
    for index, category in enumerate(categories):
        df[column_name] = df[column_name].replace(category, (index+1))
        
    return df