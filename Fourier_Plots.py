# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 13:14:47 2025

@author: vishn
"""


import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    """A function that reads .csv files and splits the time and signal values in 2 seperate arrays
    
    
    Parameters:
        filename (str): The path and text file name is used

    Return:
        time(array):
            An array of time values of the first column from data1.csv is returned
        signal(array):
            An array of all the fourier components from 2nd column till the end from data1.csv is returned
    """   
    
    data = np.genfromtxt(filename, delimiter=',')
    
    
    time = data[:, 0]
    signal = data[:, 1:] 
    
    return time, signal

if __name__ == "__main__":
    t, sig = read_data(r"C:\Users\vishn\Downloads\CODING YR 2\task 3\data1.csv")
    print(t, sig)
    
    
def fourier_reader(time, signal):
    """A function that plots the first 5 values of the Fourier Component
    

    Parameters
    ----------
    time : array
        A 1D array of time values of the first column from data1.csv is returned
    signal : array
        A 2D of all the fourier components from 2nd column till the end from data1.csv is returned

    Returns
    -------
    None

    """
    
    
    plt.figure()
    for i in range (5):
        components = signal[:,i]
        plt.plot(time, components, label=f"Term{i+1}")
    plt.title("First 5 Fourier Component")
    plt.xlabel("Time($s$)")
    plt.ylabel("Amplitude")
    plt.show()
        
if __name__ == "__main__":
    t, sig = read_data(r"C:\Users\vishn\Downloads\CODING YR 2\task 3\data1.csv")
    print(fourier_reader(t, sig))
    
    
def plot_sumofterms(time, signal, terms=5):
    """Take a plot of the sum of n-terms of the fourier data"
    

    Parameters
    ----------
    time : array
        A 1D array of time values of the first column from data1.csv is returned
    signal : array
        A 2D of all the fourier components from 2nd column till the end from data1.csv is returned

    Keyword arg:
        terms(int, default 5):
            number of terms to sum

    """
    plt.figure()
    component = np.sum(signal[:,:terms],axis=1)
    plt.plot(time, component, label= f"Sum of {terms} terms")

    plt.title(f"Sum of first {terms} Fourier Components")
    plt.xlabel("Time($s$)")
    plt.ylabel("Amplitude")
    plt.show()
        
if __name__ == "__main__":
    t, sig = read_data(r"C:\Users\vishn\Downloads\CODING YR 2\task 3\data1.csv")
    for nterms in [5,10, 100]:
        plot_sumofterms(t, sig, terms = nterms)



    