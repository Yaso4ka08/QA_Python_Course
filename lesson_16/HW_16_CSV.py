import pandas as pd

df = pd.read_csv('rmc.csv')

# to see duplicates from the file above
print(df[df.duplicated()])

# to remove duplicates from the file and create a new clean one
df.drop_duplicates().to_csv('Revenkova_1.csv', index=False)


df = pd.read_csv('random.csv')

# to see duplicates from the file above
print(df[df.duplicated()])

# to remove duplicates from the file and create a new clean one
df.drop_duplicates().to_csv('Revenkova_2.csv', index=False)