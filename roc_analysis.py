import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

clean_metrics = [0.18, 0.20, 0.22, 0.25, 0.27, 0.28, 0.30, 0.31, 0.33, 0.35]
stego_metrics = [0.45, 0.48, 0.50, 0.52, 0.54, 0.55, 0.57, 0.58, 0.60, 0.62]

y_true = [0] * len(clean_metrics) + [1] * len(stego_metrics)
y_scores = clean_metrics + stego_metrics

fpr, tpr, thresholds = roc_curve(y_true, y_scores)
roc_auc = auc(fpr, tpr)
# Вычисляем Youden’s J statistic для каждого порога: J = TPR - FPR
J = tpr - fpr

optimal_idx = np.argmax(J)
optimal_threshold = thresholds[optimal_idx]
optimal_J = J[optimal_idx]

print("Оптимальный порог:", optimal_threshold)
print("Максимальное значение Youden’s J:", optimal_J)
print("TPR при оптимальном пороге:", tpr[optimal_idx])
print("FPR при оптимальном пороге:", fpr[optimal_idx])

# Отображаем ROC-кривую с отмеченной точкой оптимального порога
plt.figure()
plt.plot(fpr, tpr, label=f'ROC кривая (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], 'r--', label='Случайная угадайка (AUC = 0.5)')
plt.scatter(fpr[optimal_idx], tpr[optimal_idx], color='black',
            label=f'Оптимальный порог = {optimal_threshold:.2f}')
plt.xlabel('FPR (ошибка первого рода)')
plt.ylabel('TPR (полнота)')
plt.title('ROC кривая с оптимальным порогом')
plt.legend(loc='lower right')
plt.show()
