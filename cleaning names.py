# importing pandas as pd
import pandas as pd
import numpy as np
# Let's create a Dataframe
df = pd.DataFrame({'City':['New York (City)', 'Parague', 'New Delhi (Delhi)', 'Venice', 'new Orleans'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
					'Cost':[10000, 5000, 15000, 2000, 12000]})


# Let's create the index
index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
		pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]

# Set the index
df.index = index_

# Let's print the dataframe
print(df)

print("\n")

# Importing re package for using regular expressions
import re

# Function to clean the names
def Clean_names(City_name):
	# Search for opening bracket in the name followed by
	# any characters repeated any number of times
	if re.search('\(.*', City_name):

		# Extract the position of beginning of pattern
		pos = re.search('\(.*', City_name).start()

		# return the cleaned name
		return City_name[:pos]

	else:
		# if clean up needed return the same name
		return City_name
		
# Updated the city columns
df['City'] = df['City'].apply(Clean_names)

# Print the updated dataframe
print(df)
