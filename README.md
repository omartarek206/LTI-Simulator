# LTI Simulator
This project provides a method of visualizing and solving LTI (linear time invariant) systems with unit step or impulse inputs using state space representation.

# Mathematical interpretation:
We begin with an nth order differential equation whose inputs may or may not have their derivatives.
From the output coefficients and the input coefficients we are able to obtain the State matrices A,B,C and D then using the state space representation we are left with n first order differential equations instead of a single nth order differential equation, which are solved numerically using the block method.
In order to calculate the states and consequently calculate the output of the system we needed to solve multiple first order equations, the block method(one of great similarity to the fourth order Range-Kutta method) proved to be a quick and robust way in solving this kind of problems.
Finally, the input (either step or impulse) is plotted along with the output of the system and the n states.
**The model was based on the controllable canonical form for describing the system using the state space representation.

### The algorithm used in the system simulation proceeds as follows:
    1. The state space matrices (A,B,C,D) are calculated
    2. The State matrix X is calculated assuming all initial states of zero
    3. The output is calculated simply by adding D*u to X1
    4. The input, output, and states are plotted from t=0 to t=10 sec
**Note that the simulator works for any order n with or without input derivatives.

The simulation is written in python and made use of NumPy library, matplotlib in order to graph the system’s input, output and states, and tkinter and PIL to create the GUI and make sure the graphs were well displayed in the GUI respectively.



