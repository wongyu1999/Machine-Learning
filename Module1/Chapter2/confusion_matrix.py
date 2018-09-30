#week3
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
'''
混淆矩阵
混淆矩阵是了解分类模型效果的表格
一些分类器比另一些更糟糕，混淆矩阵可以揭示这一点
'''

#展示混淆矩阵
def plot_confusion_matrix(confusion_mat):
	plt.imshow(confusion_mat,interpolation = 'nearest',cmap = plt.cm.Paired)
	plt.title('Confusion matrix')
	plt.colorbar()
	tick_marks = np.arange(4)
	plt.xticks(tick_marks,tick_marks)
	plt.yticks(tick_marks,tick_marks)
	plt.ylabel('True label')
	plt.xlabel('Predicted label')
	plt.show()

if __name__ == '__main__':
	y_true = [1,0,0,2,1,0,3,3,3]
	y_pred = [1,1,0,2,1,0,1,3,3]

	target_names = ['Class-0','Class-1','Class-2','Class-3']
	print(classification_report(y_true,y_pred,target_names = target_names))
	confusion_mat = confusion_matrix(y_true,y_pred)
	plot_confusion_matrix(confusion_mat)
