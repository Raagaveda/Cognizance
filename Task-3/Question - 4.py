import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering' ,'chennai' , 'campus'])
print("Input series =", ser)
newSeries = ser.str.title()  #series.map(lambda x: x[0].upper() + x[1:-1] + x[-1])
print("\nResulting Series :",newSeries)

                       
