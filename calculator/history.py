import pandas as pd
import subprocess
'''history script'''

class History:
    '''history class'''

    def __init__(self):
        self.df=pd.DataFrame([],columns=['value1','symbol','value2','result'])
        self.history = []

    #stores calculation in pandas and history list
    def store_calculation(self, a, symbol, b, result):
        '''storing function'''
        self.history.append((a, symbol, b, result))
        self.df.loc[len(self.df.index)] = [a, symbol, b, result]

    def get_history(self):
        '''get stored history function'''
        return self.history

    def clear_history(self):
        '''clear stored history'''
        #self.history.clear()
        subprocess.call('reset')
        self.df=pd.DataFrame([],columns=['value1','symbol','value2','result'])

    def get_dataframe(self):
        '''geting history dataframe'''
        return self.df
    
    #loads history from csv file and appends it to the current history
    def load_history(self, filename):
        self.df = pd.concat([self.df,pd.read_csv(filename)])

    #saves history to a csv file
    def save_history(self, filename):
        #for tup in self.history:
            #self.df.loc[len(self.df.index)] = [tup[0], tup[1], tup[2], tup[3]]
        self.df.to_csv(filename)
    
    #deletes both list and pandas history
    def delete_history(self):
        self.history = []
        self.df=pd.DataFrame([],columns=['value1','symbol','value2','result'])

    #shows history to the user through terminal
    def show_history(self):
        print(self.df)
    