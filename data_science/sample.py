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
