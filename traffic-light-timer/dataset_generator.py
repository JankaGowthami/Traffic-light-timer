import random
import pandas as pd

# Define the number of rows you want in your dataset (n)
n = 1000  # Change this to your desired number of rows

# Define the min and max values for each feature
f1_min = 1
f1_max = 10
f2_min = 1
f2_max = 30
f3_min = 1
f3_max = 7
f4_min = 1
f4_max = 4
f5_min =18
f5_max =60
f6_min =1
f6_max =3

# Define the weights for each feature
w1 = 0.5
w2 = 0.3
w3 = -0.2
w4 = 0.1
w5 = 0.4
w6 = 0.2

# Define the threshold for assigning classes
threshold = (((f1_max*w1+f2_max*w2+f3_max*w3+f4_max*w4+f5_max*w5+f6_max*w6)*3)/4)

# Initialize lists to store the data
data = {'distance': [], 'no vehc': [], 'day': [], 'time': [], 'age': [], 'purpose': [],'outcome':[]}

# Generate n rows of data
for _ in range(n):
    # Generate random values for each feature within their respective min and max ranges
    f1 = int(random.uniform(f1_min, f1_max))
    f2 = int(random.uniform(f2_min, f2_max))
    f3 = int(random.uniform(f3_min, f3_max))
    f4 = int(random.uniform(f4_min, f4_max))
    f5 = int(random.uniform(f5_min, f5_max))
    f6 = int(random.uniform(f6_min, f6_max))
    # Calculate the outcome based on the weights
    outcome = f1 * w1 + f2 * w2 + f3 * w3 + f4 * w4 + f5 * w5 + f6 * w6

    # Append the data to the lists
    data['distance'].append(f1)
    data['no vehc'].append(f2)
    data['day'].append(f3)
    data['time'].append(f4)
    data['age'].append(f5)
    data['purpose'].append(f6)
    data['outcome'].append(outcome)

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('traffic_dataset.csv', index=False)
