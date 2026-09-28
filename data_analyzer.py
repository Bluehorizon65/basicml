import random
import pandas as pd
import os




class Dataanalyzer:
    # importing the dataset
    def __init__(self,path="students_200.csv"):

        self.file_path=path
        self.load()
        
    def load(self):
        self.df=pd.read_csv(self.file_path)

    def summary(self):

        shape=self.df.shape
        infos=self.df.info()

        dict1={
            "shapes":shape,
            "infos":infos
        }
        return dict1
    def statistics(self):
        print("statistics of the dataframe")
        stat=self.df.describe()
        return stat
    def get_high_perfomers(self,min_attedance=80,min_marks=80):

        condition=(self.df["Attendance"]>min_attedance)&(self.df["FinalMarks"]>=min_marks)
        return self.df[condition]


if __name__ == "__main__":
    objects=Dataanalyzer("students_200.csv")
    print(objects.summary())
    print(objects.statistics())
    print(objects.get_high_perfomers())