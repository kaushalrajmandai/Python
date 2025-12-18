# Test_modi
df = pd.DataFrame
# }

# Add new column
df['D'] = df['A'] + df['B']

# Update a value
df.loc[1, 'A'] = 100

# Drop column
df = df.drop('C', axis=1)

