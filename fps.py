import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Örnek veri
data = {
    'Algorithm': ['Re3', 'KCF', 'DSST', 'GOTURN', 'ASMS'],
    'FPS': [150, 80, 70, 60, 30],
    'ExpectedOverlap': [0.35, 0.30, 0.28, 0.25, 0.20]
}

df = pd.DataFrame(data)

# Grafik çizimi
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='ExpectedOverlap', y='FPS', hue='Algorithm', s=100)
plt.title('FPS vs Expected Overlap')
plt.xlabel('Expected Overlap')
plt.ylabel('Frames Per Second')
plt.grid(True)
plt.legend()
plt.show()
