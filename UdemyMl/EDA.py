import pandas as pd
import pandas_profiling
def main():
# my code for profiling
    df = pd.read_csv('D:/Udemy ML/ML_Complete/Dataset 3/titanic.csv')
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file("Output.html")

if __name__ == "__main__": main()