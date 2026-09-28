import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class DataVisualizer:
    # importing the dataset
    def __init__(self,path="students_200.csv"):

        self.file_path=path
        self.load()
        
    def load(self):
        self.df=pd.read_csv(self.file_path)

    # to plot and save the line chart
    def plot_line_chart(self,path="linchart.png",show=False):

        plt.plot(self.df.index,self.df["Attendance"],c='red',label='Attendance')
        plt.xlabel("count of students")
        plt.ylabel("attedance")

        plt.legend()

        # save the plot

        plt.savefig(path)

        if show:
            plt.show()
        else:
            plt.close()

        print("the final as been saved as linechart.png in the path:",path)

    def plot_scatter_plot(self,path="scatter.png",show=False):
        plt.scatter(self.df["StudyHours"],self.df["FinalMarks"],c='crimson')
        plt.title("StudyHours vs Final Marks")
        plt.xlabel("Study Hours")
        plt.ylabel("FinalMarks")
        
                # save the plot
        
        plt.savefig(path)
        
        if show:
            plt.show()
        else:
            plt.close()
        
        print("the final as been saved as scatterchart.png in the path:",path)



    def plot_bar_chart(self,path="barchart.png",show=False):


        # find the dept_avg

        dept_avg=self.df.groupby("Department")["FinalMarks"].mean().reset_index()


        # plotting

        plt.bar(dept_avg["Department"],dept_avg["FinalMarks"],color="mediumseagreen",edgecolor="Black")

        plt.title("Average marks accross each departement")
        plt.xlabel("Departement")
        plt.ylabel("Final Marks")

        plt.savefig(path)

        if show:
            plt.show()
        else:
            plt.close()

        print("the bar chart is saved to this path",path)
    def plot_histogram(self,path="hist.png",show=False):

        plt.hist(self.df["FinalMarks"],bins=15,color='blue',edgecolor='black')

        plt.title("Distribution of final marks")
        plt.xlabel("final marks range")
        plt.ylabel("freqency of the student count")

        plt.savefig(path)


        if show:
            plt.show()
        else:
            plt.close()
        print("the hist chart is saved to this path",path)



if __name__ == "__main__":
    objects=DataVisualizer("students_200.csv")

    objects.plot_bar_chart(show=True)
    objects.plot_line_chart(show=True)
    objects.plot_scatter_plot(show=True)
    objects.plot_histogram(show=True)

