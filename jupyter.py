import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('user_data.csv')

plt.figure(figsize=(10, 6))
plt.bar(df['age'], df['total_income'])
plt.xlabel('Age')
plt.ylabel('Total Income')
plt.title('Ages with the Highest Income')
plt.show()

df.groupby('gender')['expenses'].sum().plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Total Spending')
plt.title('Gender Distribution Across Spending Categories')
plt.show()

plt.savefig('age_income.png')
plt.savefig('gender_spending.png')