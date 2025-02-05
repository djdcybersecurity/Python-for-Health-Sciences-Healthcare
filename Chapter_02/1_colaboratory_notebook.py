# Google Colaboratory Notebook (Online)
# Google Colab allows users to write and execute Python code in a cloud-based Jupyter notebook.

# Example: Running Python in Google Colab

print("Hello from Google Colaboratory!")

# You can also import libraries and visualize data:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.show()
