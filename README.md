# python

Scikit-learn, Pandas, Statsmodels: Comparison:
https://stats.stackexchange.com/questions/47913/pandas-statsmodel-scikit-learn 

Keras Documentation:

fit(): train the model for a given number of epochs(given number of dataset)<br>
predict(): generate output predictions given input

Magic methods: __new__ vs __init__; 
Use __new__ when you need to control the creation of a new instance. 
Use __init__ when you need to control initialization of a new instance.
When using a singleton pattern, override __new__ method so that only 1 distance can be created

python的list和csv文件的转化: 
1. list to csv: 新创建一个文件和创建一个csv.writer对象，writer.writerow() 往文件中写
2. csv to list: open这个csv file, csv.reader创建一个reader对象, reader得到的是一整个file, data_read = [row for row in reader]得到整个写出来的数据
