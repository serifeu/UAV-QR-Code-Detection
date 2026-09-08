import matplotlib.pyplot as plt
import numpy as np

# Eşik değerleri (Thresholds)
thresholds = np.linspace(0, 1, 100)

# Olası OPE score (Accuracy) eğrileri
ope_scores = {
    'Re3 (ImageNet)': 1 - (thresholds ** 2.5),
    'KCF': 1 - (thresholds ** 2.3),
    'DSST': 1 - (thresholds ** 2.2),
    'GOTURN': 1 - (thresholds ** 1.9),
    'ASMS': 1 - (thresholds ** 1.6),
}

# Grafik çizimi
plt.figure(figsize=(8, 6))
for label, scores in ope_scores.items():
    plt.plot(thresholds, scores, label=label)

plt.title('OPE Score on Imagenet Video Test Set')
plt.xlabel('Thresholds')
plt.ylabel('Precision')
plt.grid(True)
plt.legend()
plt.show()
