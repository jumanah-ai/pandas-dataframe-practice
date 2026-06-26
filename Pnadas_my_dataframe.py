import pandas as pd
data={'name':['bob','patrick','sqiward'],
      'age':[30,35,50]}# two columns
df=pd.DataFrame(data,index=['emp1','emp2','emp3'])# renaming the index
df['job']=['cook','nA','casher']#adding new column
new_row=pd.DataFrame([{'name':'sandy','age':28,"job":"eng"}],index=['emp4'])
df=pd.concat([df,new_row])

print(df)

#list[]
#dic{}
#tuple()