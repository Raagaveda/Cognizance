import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
print("original series:\n")
print(' '.join(ser))
Series = ser.map(lambda x: x[0].upper() + x[1:-1] + x[-1].lower())
print("\nResulting Series :\n")
print(' '.join(Series))
                       
