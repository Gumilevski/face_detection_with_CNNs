# face_detection_with_CNNs
Решение задачи поиска лица на изображении на основе свёрточных нейронных сетей.
## Постановка задачи 
#### Дано:
RGB-изображение произвольного размера с одним, вариативным по положению, лицом на нём.
#### Требуется:
Построить функцию F, которая по массиву пикселей изображения сможет выделять лица на нём, а именно строить прямоугольную ограничительную рамку, внутри которой расположено лицо. Функция F возвращает координаты левой верхней и правой нижней вершины прямоугольной ограничительной рамки.

## Подготовка обучающей выборки
Существует множество размеченных наборов данных для распознавания лиц. В моей работе использовался набор данных [UMDFaces](https://www.umdfaces.io/) (Batch 3). Помимо ограничительных рамок, которые использовались в моей работе, UMDFaces предоставляет данные о расположении 21 ключевой точки лица, пол, сгенерированный предварительно обученной нейронной сетью, данные о положении лица (отклонение от нормали и др) и многое-многое другое.
![UMD Faces](https://github.com/Gumilevski/face_detection_with_CNNs/blob/master/images/2019-05-30_14-28-25.png)

Из всего набора данных было выделено 22 тысячи изображений для обучения и тестирования нейронных сетей. Из них 16 тысяч – train set (использовался для обучения нейронных сетей), 4 тысячи – validation set (использовался для подборки гиперпараметров моделей и предварительной оценки точности на данных, которые не видела нейронная сеть), остальные 2 тысячи – test set.

Изображения хранились в папках train и test, а ответы к ним - в csv-файлах train.csv и test.csv (подготовлены на основе umdfaces_batch3_ultraface.csv). В csv-файлах данные хранилась в виде название изображения (id-строка) и соответсвующие данному изображению ответы - координаты левой нижней и правой верхней вершин ограничительной рамки. 
В [данном скрипте](https://github.com/Gumilevski/face_detection_with_CNNs/blob/master/generating_script.ipynb) может быть найдена реализация подготовки обучающей выборки

## Описание первой модели ([CNN.ipynb](https://github.com/Gumilevski/face_detection_with_CNNs/blob/master/CNN.ipynb))
Теперь, когда обучающая выборка подготовлена, можем приступать к построению и обучению моделей.

Архитектура первой модели представлена на рисунке ниже:
![architecture 1](https://github.com/Gumilevski/face_detection_with_CNNs/blob/master/images/%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0%201.png)
Оптимизатор: Adam (lr = 1e-3)
Функция потерь: mse (средняя квадратичная ошибка)
Количество тренируемых параметров: 908788 (пока что не было цели оптимизировать данный показатель)
Данная сеть обучалась на 60 эпохах, около 6 часов на GPU
