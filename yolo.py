import matplotlib.pyplot as plt

# Örnek veriler
models = {
    "YOLOv5s": [(1.5, 27), (2.5, 30), (3.5, 33)],
    "YOLOv5m": [(2.5, 37), (3.5, 40), (5.0, 42)],
    "YOLOv5l": [(4.0, 43), (6.0, 45), (8.0, 46)],
    "YOLOv5x": [(6.5, 47), (9.0, 48), (11.0, 48.5)],
    "EfficientDet": [(8, 38), (12, 42), (25, 47)],
}

plt.figure(figsize=(10, 6))

# Her model ailesi için ayrı çizgi
for label, points in models.items():
    x, y = zip(*points)
    plt.plot(x, y, marker='o', label=label)

plt.xlabel("GPU Latency (ms)")
plt.ylabel("COCO AP val")
plt.title("YOLO Model Karşılaştırması")
plt.grid(True)
plt.legend()
plt.gca().invert_xaxis()  # Daha hızlı olanlar sola, o yüzden ters eksen
plt.annotate("Better", xy=(3, 47), xytext=(0.5, 48),
             arrowprops=dict(facecolor='black', arrowstyle="->"),
             fontsize=12)
plt.show()
