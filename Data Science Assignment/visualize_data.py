import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import seaborn as sns


'''
# SYKSY = Syys-, loka- ja marraskuu ovat syksyn kuukausia
# TALVI = Joulu-, tammi- ja helmikuu ovat talven kuukaudet.
# KEVAT = Kevatkuukaudet ovat maalis-, huhti- ja toukokuu.
# KESA =  Kesa-, heina- ja elokuu ovat kesan kuukaudet.
'''

df = pd.read_csv('2018_values.csv', index_col=0)
df.index = pd.to_datetime(df.index)
df = df.sort_index()


talvi_1 = df.loc['2018-01-01':'2018-02-28']
talvi_2 = df.loc['2018-12-01':'2018-12-31']
kevat = df.loc['2018-03-01':'2018-05-31']
kesa = df.loc['2018-06-01':'2018-08-31']
syksy = df.loc['2018-09-01':'2018-11-30']
talvi_df = []

talvi_df.append(talvi_1)
talvi_df.append(talvi_2)

talvi = pd.concat(talvi_df, ignore_index=False, axis=0)

talvi_data = talvi.values
kevat_data = kevat.values
kesa_data = kesa.values
syksy_data = syksy.values

year_data = [talvi_data, kevat_data, kesa_data, syksy_data]


# Generate a basic boxplot, which tells information about the data.
# Boxplots tell the variation of the data, minimum, maximum, median.
#fig, ax = plt.subplots()

ax1 = plt.subplot(2, 2, 1)
ax2 = plt.subplot(2, 2, 2)
ax3 = plt.subplot(2, 2, 3)
#ax4 = plt.subplot(2, 2, 4)

minorLocator = MultipleLocator(10)
red_square = dict(markerfacecolor='r', marker='s', markersize=3)

ax1.boxplot(year_data, showmeans=True, showfliers=True, meanprops=red_square)
ax1.set_title('Seasonal delay')
ax1.set_ylabel('Delay (minutes)')
ax1.set_xticklabels(['Winter', 'Spring', 'Summer', 'Fall'])
ax1.yaxis.grid(b=True, which='major', linestyle='--')
ax1.yaxis.grid(b=True, which='minor', linestyle='--')
ax1.yaxis.set_minor_locator(minorLocator)
ax1.tick_params(bottom="off", top="off", left="off", right="off")

ax2.plot(df)
ax2.set_title('Time trend analysis')
ax2.set_ylabel('Delay (minutes)')
ax2.yaxis.grid(b=True, which='major', linestyle='--')
ax2.yaxis.grid(b=True, which='minor', linestyle='--')
ax2.yaxis.set_minor_locator(minorLocator)
ax2.tick_params(bottom="off", top="off", left="off", right="off")


ax3.scatter(df.index, df.values)
ax3.set_title('Scatter plot')
ax3.set_ylabel('Delay (minutes)')
ax3.yaxis.grid(b=True, which='major', linestyle='--')
ax3.yaxis.grid(b=True, which='minor', linestyle='--')
ax3.yaxis.set_minor_locator(minorLocator)
ax3.tick_params(bottom="off", top="off", left="off", right="off")

sns.despine(left=True, bottom=True, right=True)


# Save the boxplot as an pdf.
#plt.savefig('boxplot.pdf', bbox_inches='tight')

# Show the boxplot
plt.show()