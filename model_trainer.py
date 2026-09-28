import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV,RandomizedSearchCV
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


class ModelTrainer:

    def __init__(self,df,feature_cols,target_col,test_size:float=0.2,random_state=42):

        """

        df :the dataframe to be given
        feature cols: list of colums to input as features
        target col: series which is to be outputed
        test size: the split size of the test data

        """


        self.df=df
        self.feature_cols=feature_cols
        self.target_cols=target_col
        self.test_size=test_size
        self.random_state=random_state


        self.x=self.df[self.feature_cols]
        self.y=self.df[self.target_cols]

        self.x_train, self.x_test,self.y_train,self.y_test=train_test_split(self.x,self.y,test_size=self.test_size,random_state=self.random_state)
        self.trainmodel={

        }

        self.model_metrics={

        }
    def evaluvate(self, model, name=None):
        if isinstance(model, str):
            name = model
            model = self.trainmodel[name]
        pred = model.predict(self.x_test)
        mae = mean_absolute_error(self.y_test, pred)
        mse = mean_squared_error(self.y_test, pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.y_test, pred)
        metrics = {
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "R2": r2
        }
        if name:
            self.model_metrics[name] = metrics
        return metrics

    def train_linear_regression(self):
        model = LinearRegression()
        model.fit(self.x_train, self.y_train)
        self.trainmodel["linear_regression"] = model
        self.evaluvate(model, "linear_regression")
        return model

    def train_linear_grid(self):
        params = {
            "fit_intercept": [True, False],
            "positive": [True, False]
        }
        grid = GridSearchCV(LinearRegression(), params, cv=5)
        grid.fit(self.x_train, self.y_train)
        model = grid.best_estimator_
        self.trainmodel["linear_grid"] = model
        self.evaluvate(model, "linear_grid")
        return model

    def train_linear_random_search(self):
        params = {
            "fit_intercept": [True, False],
            "positive": [True, False]
        }
        search = RandomizedSearchCV(LinearRegression(), params, n_iter=4, cv=5, random_state=self.random_state)
        search.fit(self.x_train, self.y_train)
        model = search.best_estimator_
        self.trainmodel["linear_random_search"] = model
        self.evaluvate(model, "linear_random_search")
        return model

    def train_ridge_linear(self, alpha=1.0):
        model = Ridge(alpha=alpha)
        model.fit(self.x_train, self.y_train)
        self.trainmodel["ridge_linear"] = model
        self.evaluvate(model, "ridge_linear")
        return model

    def train_ridge_grid(self):
        params = {
            "alpha": [0.01, 0.1, 1.0, 10.0, 100.0]
        }
        grid = GridSearchCV(Ridge(), params, cv=5)
        grid.fit(self.x_train, self.y_train)
        model = grid.best_estimator_
        self.trainmodel["ridge_grid"] = model
        self.evaluvate(model, "ridge_grid")
        return model

    def predict_studentmarks(self, data, model_name=None):
        if model_name and model_name in self.trainmodel:
            model = self.trainmodel[model_name]
        elif len(self.trainmodel) > 0:
            model = list(self.trainmodel.values())[-1]
        else:
            model = self.train_linear_regression()

        if isinstance(data, dict):
            df_input = pd.DataFrame([data])
        elif isinstance(data, list):
            if len(data) > 0 and isinstance(data[0], list):
                df_input = pd.DataFrame(data, columns=self.feature_cols)
            else:
                df_input = pd.DataFrame([data], columns=self.feature_cols)
        elif isinstance(data, pd.DataFrame):
            df_input = data
        else:
            df_input = pd.DataFrame(data)

        pred = model.predict(df_input[self.feature_cols])
        if len(pred) == 1:
            return pred[0]
        return pred


if __name__ == "__main__":
    df = pd.read_csv("students_200.csv")
    features = ["Attendance", "StudyHours", "AssignmentScore", "InternalMarks", "PreviousGPA"]
    target = "FinalMarks"

    trainer = ModelTrainer(df, features, target)
    trainer.train_linear_regression()
    trainer.train_linear_grid()
    trainer.train_linear_random_search()
    trainer.train_ridge_linear()
    trainer.train_ridge_grid()

    print(trainer.model_metrics)

    sample_student = {
        "Attendance": 85,
        "StudyHours": 6,
        "AssignmentScore": 75,
        "InternalMarks": 80,
        "PreviousGPA": 8.5
    }
    print(trainer.predict_studentmarks(sample_student))