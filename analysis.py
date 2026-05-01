import pandas as pd
import matplotlib.pyplot as plt

# फाइल लोड करें (पक्का करें कि एक्सेल फाइल डेस्कटॉप पर इसी नाम से है)
file_name = 'DS_Jobs_Cleaning_Projects.xlsx'
df = pd.read_excel(file_name)

# टॉप 10 शहरों का चार्ट बनाना
plt.figure(figsize=(10,6))
df['City'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Cities for Data Science Jobs')
plt.xlabel('City')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=45)
plt.show()
