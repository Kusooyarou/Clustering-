from sklearn.cluster import KMeans
from collections import Counter
from sklearn.metrics import euclidean_distances


def get_dominant_color(image, k=4):
    # преобразование изображения в матрицу пикселей
    pixel_matrix = image.reshape((image.shape[0] * image.shape[1], 3))

    # применение KMeans для кластеризации
    kmeans = KMeans(n_clusters=k)
    labels = kmeans.fit_predict(pixel_matrix)

    # подсчет количества пикселей в каждом кластере
    label_counts = Counter(labels)

    # определение доминирующего цвета
    dominant_color_index = label_counts.most_common(1)[0][0]
    dominant_color = kmeans.cluster_centers_[dominant_color_index]

    return list(map(int, dominant_color))  # возвращаем целые значения RGB


def is_similar_color(color1, color2, threshold=30):
    distance = euclidean_distances([color1], [color2])[0][0]
    return distance < threshold


