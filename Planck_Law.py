# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 21:27:12 2025

@author: vishn
"""

import matplotlib.pyplot as plt
from scipy.constants import Boltzmann as k_b, Planck as h, c
import numpy as np
from scipy.integrate import trapezoid, simpson, quad
from scipy.optimize import fmin


def planck(freq, I_0, temp):  # CHANGE: v and T instead of freq and temp
    """Uses Plancks Law to calculate the Radiance of objects

    Args:
        v (float/array): Hz
            The values of frequency which is an independent variable
        I_0 (int): m^2
            Product of the surface area of a blackbody and emissivity
        T (float): K
            The values of temperature that is a dependent variable

    Returns:
        (float): W/Hz or J
    """
    
    exponent = (h*freq)/(k_b*temp)  # Now using v and T
    exponent = np.where(exponent > 700, 700, exponent)
    bracket = np.exp(exponent)
    
    denominator = bracket - 1
    denominator = np.where(denominator == 0 , 1E-15, denominator)
    
    frac1 = (2*h*(freq**3)/(c**2))  # Using v
    frac2 = 1/(denominator)
    
    I_v = I_0 * frac1 * frac2 
    return I_v

def planck_power(radius, emissivity, temp):
    """Calculates the total power (in W) of a speherical black body of given readius and emissivity and temperature.
    
    Parameters
    ----------
    R : Float
        Radius of the black body in metres
    emissivity : Float
        Radius of the black body in metres
    T : Float
        Temperature of the black body in K.
        
    Returns: Power(float)
        Power Emitted by the black body in W
    """
    
    Surface_area = 4 * np.pi * radius**2
    I_0 = Surface_area * emissivity
    
    Power = quad(planck, 1E10, 1E18, args=(I_0,temp))[0]
    
    return Power

def neg_planck(freq, I_0, temp):
    """The negative value for Plancks Law using the planck function.

    Args:
        v (float/array): Hz
            The values of frequency which is an independent variable
        I_0 (int): m^2
            Product of the surface area of a blackbody and emissivity
        T (float): K
            The values of temperature that is a dependent variable

    Returns:
        (float): W/Hz or J
            
    """

    return -planck(freq, I_0, temp)  


def planck_peak(radius, emissivity, temp):
    """Finds the frequency of the peak emission and the peak radiance (power/frequency) for a black body
    
    Parameters
    Args:
        radius (float):
            Radius of the black body in metres
        emissivity (float):
            Emissivity of the body (0.0 - 1.0)
        temp (float):
            temperature of the black body in K.


    Returns:
        (float, float):
            (peak frequency, peak radiance)
    """
    
    Surface_area = 4 * np.pi * radius**2
    I_0= Surface_area * emissivity
    
    peak_frequency = fmin(neg_planck, 1E14, args=(I_0, temp))[0]
    peak_radiance = planck(peak_frequency, I_0, temp)
    
    
    return peak_frequency, peak_radiance
    
    
if __name__ == "__main__":
    freq = np.logspace(13,16,501)
    wavelength =(c/freq)*1E9
    temp=np.linspace(3000,10000,8)
    I_0_test = 10000.0

    for temperatures in temp:
        Iv_1 = planck(freq, I_0_test, temperatures)
        plt.semilogx(wavelength,Iv_1,label=f"T={temperatures}K")
        
    plt.xlabel("Wavelength, $lmda$$(nm)$")
    plt.ylabel("Intensity, $I(v)$$(W/Hz^)$")
    plt.title("Temp vs Freq")
    plt.legend()
    ymin, ymax = plt.ylim()
    plt.vlines([300,700], ymin, ymax, colors =["blue","red"], linestyle="dashed")
    plt.ylim(0,ymax)


    intensities = np.zeros((len(temp),3))
    peak_pos = np.zeros_like(temp)
    
    for i,T in enumerate(temp):
        Iv_2 = planck(freq, I_0_test, T)
        intensities[i,0]=trapezoid(y=Iv_2,x=freq)
        intensities[i,1]=simpson(y=Iv_2,x=freq)
        intensities[i,2]=quad(planck, 1E10, 1E18,args=(I_0_test,T))[0]
        
        peak_pos[i]= fmin(neg_planck, 1E14, args=(I_0_test, T))[0]
        
    plt.figure()
    for i,label in enumerate(["Trapezoid","Simpson","Quad"]):
        plt.plot(temp,intensities[:,i], label=label)
        
    plt.xlabel("Temperature (K)")
    plt.ylabel("Intensity")
    plt.legend()

    plt.figure()
    plt.plot(temp, peak_pos,"rx")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Intensity")
    plt.title("Peak frequency at certain Temperatures")
