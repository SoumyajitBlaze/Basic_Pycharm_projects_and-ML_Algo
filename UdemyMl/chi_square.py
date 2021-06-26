import scipy.stats as stats
import  seaborn as sns
import  pandas as pd
import numpy as np

dataset=sns.load_dataset('tips')
print(dataset.head())
dataset_table=pd.crosstab(dataset['sex'],dataset['smoker'])
print(dataset_table)
observed_values=dataset_table.values
val=stats.chi2_contingency(dataset_table)
print(val)
Expected_values=val[3]
no_of_rows=len(dataset_table.iloc[0:2,0])
no_of_cols=len(dataset_table.iloc[0,0:2])
ddof=(no_of_rows-1)*(no_of_cols-1)
alpha=0.05
print(ddof)

from scipy.stats import chi2
chi_square=sum([(o-e)**2/e for o,e in zip(observed_values,Expected_values)])
chi_square_stat=chi_square[0]+chi_square[1]
p_value=1-chi2.cdf(x=chi_square_stat,df=ddof)
print(p_value)
