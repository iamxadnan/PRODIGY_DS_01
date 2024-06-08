import matplotlib.pyplot as plt
import numpy as np

# Generating random sample data for ages
np.random.seed(0)
ages = np.random.randint(18, 70, size=100)  # Generating 100 random ages between 18 and 70

# Creating the histogram
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=10, color='skyblue', edgecolor='black', alpha=0.7)

# Adding labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages in Population')

# Displaying the plot
plt.grid(True)
plt.show()
