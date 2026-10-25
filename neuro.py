import sys
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class NeuroSimulator(ctk.CTK):
    def __init__(self):
        super().__init__()

        self.title("Neuro Simulator")
        self.geometry("900x650")
        self.resizable(True, True)

        self.V_rest = -70.0 # resting of membrane potential in mV
        self.V_th = -55.0 # threshold potential in mV
        self.V_rest = -75.0 # return
        self.R_m = 10.0 # membrane resistance in MOhms
        self.tau_m = 20.0 # ms
        self.dt = 0.1 # Euler step
        self.T = 100.0 # total time in ms

        self.create_widgets()
        self.run_simulation()

    
