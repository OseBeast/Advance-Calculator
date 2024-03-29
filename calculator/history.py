import pandas as pd
'''history script'''

class History:
    '''history class'''

    def __init__(self):
        self.df=pd.DataFrame([],columns=['value1','symbol','value2','result'])
        self.history = []

    def store_calculation(self, a, symbol, b, result):
        '''storing function'''
        self.history.append((a, symbol, b, result))

    def get_history(self):
        '''get stored history function'''
        return self.history

    def clear_history(self):
        '''clear stored history'''
        self.history.clear()
    def get_dataframe(self):
        '''geting history dataframe'''
        return self.df
    def load_history(self, filename):
        self.df = pd.concat([self.df,pd.read_csv(filename)])
    def save_history(self, filename):
        for tup in self.history:
            self.df.loc[len(self.df.index)] = [tup[0], tup[1], tup[2], tup[3]]
        self.df.to_csv(filename)
    def delete_history(self):
        self.df=pd.DataFrame([],columns=['value1','symbol','value2','result'])
