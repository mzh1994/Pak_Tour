import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('Tour.xlsx')

'''
df_1 = df.groupby(['Category','Sub_Category'])['Total_Amount'].sum().unstack(level=0,fill_value=0)
sns.set()
ax = df_1.T.plot(title='Expense_Details',alpha=0.75, rot=0,kind='bar', \
            grid=True,stacked=True, figsize=(16,8))
plt.xlabel('Categories', labelpad=15)
plt.ylabel('PKR',labelpad=15)
plt.show()
'''
'''
df_2 = df.groupby(['Category'])['Total_Amount'].sum().to_frame().reset_index()
sns.set_style("dark")
ax = sns.barplot(x='Category',y='Total_Amount',data=df_2,ci=None)
for p in ax.patches:
        ax.annotate('{:.0f}'.format(p.get_height()), (p.get_x()+0.3, p.get_height()),
                    ha='center', va='bottom',
                    color= 'black')
#ax = df_2.plot(title='Expense_Details',alpha=0.75, rot=0,kind='bar',grid=True,figsize=(16,8))
plt.grid()
plt.title('Expense_Details')
plt.xlabel('Categories', labelpad=15)
plt.ylabel('PKR',labelpad=15)
plt.show()
'''

'''
df_3 = df.groupby('Place')['Total_Amount'].sum().to_frame().reset_index()
sns.set_style("dark")
ax = sns.barplot(x='Place',y='Total_Amount',data=df_3,ci=None)
for p in ax.patches:
        ax.annotate('{:.0f}'.format(p.get_height()), (p.get_x()+0.3, p.get_height()),
                    ha='center', va='bottom',
                    color= 'black')
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
plt.grid()
plt.title('Places_Expense')
plt.xlabel('Places', labelpad=15)
plt.ylabel('PKR',labelpad=15)
plt.show()
'''
'''
df_4 = df[df['Category']=='Food']
df_4 = df_4.groupby('Sub_Category')['Total_Amount'].sum().to_frame().reset_index()
sns.set_style("dark")
ax = sns.barplot(x='Sub_Category',y='Total_Amount',data=df_4,ci=None)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
for p in ax.patches:
        ax.annotate('{:.0f}'.format(p.get_height()), (p.get_x()+0.3, p.get_height()),
                    ha='center', va='bottom',
                    color= 'black')
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
plt.grid()
plt.title('Food_Expense')
plt.xlabel('Food_Items', labelpad=15)
plt.ylabel('PKR',labelpad=15)
plt.show()
'''
'''
df_5 = df[df['Category']=='Transport']
df_5 = df_5.groupby('Sub_Category')['Total_Amount'].sum().to_frame().reset_index()
sns.set_style("dark")
ax = sns.barplot(x='Sub_Category',y='Total_Amount',data=df_5,ci=None)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
for p in ax.patches:
        ax.annotate('{:.0f}'.format(p.get_height()), (p.get_x()+0.3, p.get_height()),
                    ha='center', va='bottom',
                    color= 'black')
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
plt.grid()
plt.title('Transport_Expense')
plt.xlabel('Transport_Items', labelpad=15)
plt.ylabel('PKR',labelpad=15)
plt.show()
'''

df_5 = df[df['Category']=='Entry_tckt/toll_tax']
df_5 = df_5.groupby('Sub_Category')['Total_Amount'].sum().to_frame().reset_index()
sns.set_style("dark")
ax = sns.barplot(x='Sub_Category',y='Total_Amount',data=df_5,ci=None)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
for p in ax.patches:
        ax.annotate('{:.0f}'.format(p.get_height()), (p.get_x()+0.3, p.get_height()),
                    ha='center', va='bottom',
                    color= 'black')
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
plt.grid()
plt.title('Activity_Expense')
plt.xlabel('Activity', labelpad=15)
plt.ylabel('PKR',labelpad=15)
plt.show()
