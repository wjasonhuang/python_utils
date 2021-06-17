import csv
with open('albumlist.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    albums = [row for row in reader]
    

import pandas as pd
xls = pd.ExcelFile('yelp.xlsx')
df = xls.parse('yelp_data')


'---------- Plot ----------'
%pylab inline
import matplotlib.pyplot as plt

'---------- Histograms ----------'
plt.hist(
    pitt_stars,
    alpha = 0.3,
    color = 'yellow',
    label = 'Pittsburgh',
    bins = 'auto'
)
plt.hist(
    vegas_stars,
    alpha = 0.3,
    color = 'red',
    label = 'Las Vegas',
    bins = 'auto'
)
plt.xlabel("Rating")
plt.ylabel("Number of Rating Scores")
plt.legend(loc = 'best')
plt.title("Review distribution of Pittsburgh and Las Vegas")
plt.show()

plt.hist(
    [pitt_stars, vegas_stars],
    alpha = 0.7,
    color = ['red', 'blue'],
    label = ['Pittsburgh', 'Las Vegas'],
    bins = 'auto'
)
plt.xlabel('Rating')
plt.ylabel('Number of Rating Scores')
plt.legend(loc = 'best')
plt.title('Review distribution of Pittsburgh and Las Vegas')
plt.show()

'---------- Scatterplots ----------'
plt.scatter(
    df_health["stars"], df_health["review_count"],
    marker = "o",
    color = 'r',
    alpha = 0.7,
    s = 124,
    label = ['Health & Medical']
)
plt.scatter(
    df_fast["stars"], df_fast["review_count"],
    marker = "h",
    color = 'b',
    alpha = 0.7,
    s = 124,
    label = ['Fast Food']
)
plt.scatter(
    df_break["stars"], df_break["review_count"],
    marker = "^",
    color = 'g',
    alpha = 0.7,
    s = 124,
    label = ['Breakfast & Brunch']
)
plt.xlabel('Rating')
plt.ylabel('Review Count')
plt.legend(loc = 'upper left')
axes = plt.gca() # gca = get current axes
axes.set_yscale('log')
plt.show()

'---------- Bar Charts ----------'
plt.bar(
    data_for_x_axis,
    data_for_y_axis,
    #other optional parameters
)

#count the records for each city and get a new DataFrame
df_city_value_counts = df['city'].value_counts()
#call the plot method and set the kind parameter to ‘bar’
df_city_value_counts.plot(kind='bar', figsize=(12, 6), fontsize=12, legend=False, title="Number of Businesses Per City")
plt.ylabel("Number of businesses")
plt.show()

bar_rest = df["category_0"].isin(["Bars", "Restaurants"])
df_bar_rest = df[bar_rest]
#pivot along category
pivot_state_cat = pd.pivot_table(df_bar_rest, index=["category_0"])
#filter the df_bar_rest DataFrame columns pivot_state_cat = pivot_state_cat[["stars"]]
pivot_state_cat = pivot_state_cat[["stars"]]
#call the plot method and set the kind parameter to ‘bar’
pivot_state_cat.plot(kind='bar', figsize=(12, 6), fontsize=12, legend=False, title="Average Star Rating for Bars & Restaurants")
plt.xlabel("Category")
plt.ylabel("Average star rating")
plt.show()
