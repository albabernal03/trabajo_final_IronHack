#cargamos los datos de regresion_data.xls
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import explained_variance_score
from sklearn.metrics import max_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_poisson_deviance
from sklearn.metrics import mean_gamma_deviance

# Cargamos los datos
df = pd.read_excel('regresion_data.xls')

información = df.info()
print(información)

descripción = df.describe()
print(descripción)
#limpiamos los datos del fichero 
#df = df.dropna()
