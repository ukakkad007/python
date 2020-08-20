#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import seaborn as sb
data1=pd.read_excel(r'C:\Users\atulk\Desktop\Python Training\data visualization\SuperstoreData.xls')
#print(data1.head())
discount=pd.DataFrame(data1['Discount']).astype(float)
print(discount)
profit=pd.DataFrame(data1['Profit']).astype(float)
print(profit)
sb.relplot(discount,profit,data=data1,kind='line')


# In[32]:


data1['year']=data1['Order Date'].dt.year


# In[36]:


print(type(data1['year']))
data1.year.unique()


# In[38]:


data1['Sales']=data1['Sales'].astype('float')
data1['year']=data1['year'].astype('float')
sb.relplot('year','Sales',data=data1,kind='line')


# In[40]:


import numpy as np
df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
g = sb.relplot(x="time", y="value", kind="line", data=df)


# In[44]:


import numpy as np
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")

rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
data = data.rolling(7).mean()
ax=sns.lineplot(data=data, palette="tab10", linewidth=2.5)
ax.set(xlabel='Sales',ylabel='Discount')


# In[50]:


import numpy as np
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")

#rs = np.random.RandomState(365)
dis = data1['Discount'].astype('float')
values = data1['Profit'].astype('float')
data2 = pd.DataFrame(values, dis)
#data = data.rolling(7).mean()
ax=sns.lineplot(data=data2, palette="tab10", linewidth=2.5)
ax.set(xlabel='Sales',ylabel='Discount')


# In[13]:


import numpy as np
import pandas as pd
import seaborn as sb
movie_data=pd.read_excel(r'C:\Users\atulk\Desktop\Python Training\data visualization\movies.xls',2)
print(movie_data.head())
#sb.lineplot('Facebook likes - Movie','IMDB Score',data=movie_data)
#movie_data.set_index('IMDB Score')['Facebook likes - Movie'].plot(kind='line',style='k*')
#movie_data.set_index('Facebook likes - Movie')['IMDB Score'].plot(kind='line')
sb.lineplot(movie_data['Facebook likes - Movie'],movie_data['IMDB Score'])

