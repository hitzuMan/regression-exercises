import os
import pandas as pd

from env import get_connection


def get_grades():
    
    filename = 'grades.csv'
    
    if os.path.isfile(filename):
        
        return pd.read_csv(filename)
    
    else:
        
        query = '''
                SELECT *
                FROM student_grades
                '''
        
        url = get_connection('school_sample')
        
        df = pd.read_sql(query, url)
        
        df.to_csv(filename, index=False)
        
        return df
    
    
def clean_grades():
    
    df = get_grades()
    
    df = df.dropna()
    
    df = df[df.exam3 != ' ']
    
    df.exam3 = df.exam3.astype('int')
    
    return df    

def compare_data():
    plt.subplot(121)
    sns.histplot(data=train, x='final_grade', bins=10)

    plt.subplot(122)  # 1 row and 2 columns
    sns.histplot(data=train, x= 'final_grade_mms', bins=10)

    plt.show()
    
import os
import pandas as pd

from env import get_connection
from sklearn.model_selection import train_test_split




def train_val_test(df, seed = 42):
    
    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed)
    
    val, test = train_test_split(val_test, train_size = 0.5,
                                 random_state = seed)
    
    return train, val, test