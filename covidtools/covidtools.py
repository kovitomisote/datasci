import pandas as pd
import numpy as np
import plotly.express as px

class CovidData:
    
    datatype = "array"
    
    def __init__(self, results, control, name):
        self.results = results
        self.control = control
        self.name = name
        
        self.results = self.normalize()
                
    def __repr__(self):
        return f"Covid data: {self.results}"
    
    def __len__(self):
        return len(self.results)
    
    def Sum(self):
        return sum(self.results)
    
    def normalize(self):
        return [x / self.control for x in self.results]
    
    def lineplot(self):
        return px.line(self.results)
    
    def scatterplot(self):
        return px.scatter(self.results)
    
    def save(self): 
        pass
        