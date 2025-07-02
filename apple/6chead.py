import pandas as pd
data={
	'name':['ajay','pavan','nithin','sanjay'],
	'marks'	:[40,50,60,70]
}
df=pd.DataFrame(data)	
print(df.describe())
print(df.head(2))
print(df.tail(2))

