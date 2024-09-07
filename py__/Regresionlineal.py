from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Preparación de datos
X = ...
y = ...
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear modelo y entrenarlo
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

# Realizar predicciones
y_pred = regression_model.predict(X_test)

# Evaluar el rendimiento del modelo
mse = mean_squared_error(y_test, y_pred)
