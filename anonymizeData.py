import pandas as pd

notAnonymizedData = pd.read_csv('filtered-surveys.csv')

# Drop the column with the names and the email addresses
anonymizedData = notAnonymizedData.drop('name', axis=1)
anonymizedData = anonymizedData.drop('email', axis=1)
anonymizedData = anonymizedData.drop('emailPerLestrazione', axis=1)

# Save the anonymized data to a new file
anonymizedData.to_csv('anonymized-surveys.csv', index=False)
