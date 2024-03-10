import matplotlib.pyplot as plt

model_names = ['custom CNN', 'custom VGG19','ENB7 Model1','ENB7 Model2','InceptionResNetV2','DenseNet169','DenseNet201']
model_training_accuracies = [35.48, 63.81, 74.33, 83.69, 99.04, 98.31, 99.36]
model_testing_accuracies = [24.19, 53.73, 58.22, 68.95, 77.74, 78.73, 80.47]
model_training_loss = [2.1162, 1.0536, 0.7959, 0.9056, 0.0326, 0.0502, 0.0229]
model_testing_loss = [4.3453, 2541.41, 1.3884, 1.4071, 0.9767, 0.8535, 0.7684]

# Plotting training accuracies
plt.figure(figsize=(10, 6))
plt.bar(model_names, model_training_accuracies)
plt.xlabel('Model Names')
plt.ylabel('Training Accuracies')
plt.title('Training Accuracies of Research Models')
plt.xticks(rotation=45)
plt.show()

# Plotting testing accuracies
plt.figure(figsize=(10, 6))
plt.bar(model_names, model_testing_accuracies)
plt.xlabel('Model Names')
plt.ylabel('Testing Accuracies')
plt.title('Testing Accuracies of Research Models')
plt.xticks(rotation=45)
plt.show()

# Plotting training loss
plt.figure(figsize=(10, 6))
plt.bar(model_names, model_training_loss)
plt.xlabel('Model Names')
plt.ylabel('Training Loss')
plt.title('Training Loss of Research Models')
plt.xticks(rotation=45)
plt.show()

# Plotting testing loss
plt.figure(figsize=(10, 6))
plt.bar(model_names, model_testing_loss)
plt.xlabel('Model Names')
plt.ylabel('Testing Loss')
plt.title('Testing Loss of Research Models')
plt.xticks(rotation=45)
plt.show()