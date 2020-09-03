from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image


# Print Matrices A, B, C, D in the GUI
def print_mats(mat_Text):
    def finall():
        root.destroy()

    root = Tk()
    # A stuff
    frameA = Frame(root, bd=15)
    frameA.grid(row=1, column=0)
    labelA1 = Label(frameA, text="A=").pack(side=LEFT)
    labelA2 = Label(frameA, text=mat_Text[0]).pack(side=RIGHT)
    # B stuff
    frameB = Frame(root, bd=15)
    frameB.grid(row=1, column=1)
    labelB1 = Label(frameB, text="B=").pack(side=LEFT)
    labelB2 = Label(frameB, text=mat_Text[1]).pack(side=RIGHT)
    # C stuff
    frameC = Frame(root, bd=15)
    frameC.grid(row=2, column=0)
    labelC1 = Label(frameC, text="C=").pack(side=LEFT)
    labelC2 = Label(frameC, text=mat_Text[2]).pack(side=RIGHT)
    # D stuff
    frameD = Frame(root, bd=15)
    frameD.grid(row=2, column=1)
    labelD1 = Label(frameD, text="D=").pack(side=LEFT)
    labelD2 = Label(frameD, text=mat_Text[3]).pack(side=RIGHT)
    # Exit Button
    out_Button = Button(root, text="Next",command=finall)
    out_Button.grid(row=3, column=1)
    root.mainloop()


# Plot in the GUI
def please_Plot(arr, no):

    def fig2img(fig):
        """Convert a Matplotlib figure to a PIL Image and return it"""
        import io
        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        img = Image.open(buf)
        return img

    def endme():
        root.destroy()

    i = str(no)
    if no == 111:
        my_State = "u"
    elif no == 999:
        my_State = "y"
    else:
        my_State = "X" + i

    root = Tk()
    root.title("State Plots")

    top_Label = Label(root, text=my_State).pack(side=TOP)


    fig = plt.figure()
    plt.plot(arr)
    img = fig2img(fig)

    x_Plot = Canvas(root, width=700, height=500)
    x_Plot.pack()
    img = ImageTk.PhotoImage(img)
    x_Plot.create_image(350, 250, anchor=CENTER, image=img)

    next = Button(root, text="Next", command=endme)
    next.pack(side=BOTTOM)

    root.mainloop()


# Input insertion GUI
def input_GUI():
    results = []

    def up_click1(event):
        up_Entry1.configure(state=NORMAL)
        up_Entry1.delete(0, END)
        up_Entry1.unbind('<Button-1>', on_click_id1)

    def up_click2(event):
        up_Entry2.configure(state=NORMAL)
        up_Entry2.delete(0, END)
        up_Entry2.unbind('<Button-1>', on_click_id2)

    def down_click1(event):
        down_Entry1.configure(state=NORMAL)
        down_Entry1.delete(0, END)
        down_Entry1.unbind('<Button-1>', on_click_id3)

    def down_click2(event):
        down_Entry2.configure(state=NORMAL)
        down_Entry2.delete(0, END)
        down_Entry2.unbind('<Button-1>', on_click_id4)

    def done():
        ain = down_Entry1.get()
        results.append(ain)

        n = int(up_Entry1.get())
        m = int(up_Entry2.get())
        temp = ' '
        if m < n:
            for i in range(n - m):
                temp += "0,"
        bin = temp + down_Entry2.get()
        results.append(bin)

        results.append(u_Type.get())

        root.destroy()

    # root properties
    root = Tk()
    root.title("LTI systems SS Calculator")

    # Frames
    up_Frame = Frame(root)
    up_Frame.grid(row=1)
    down_Frame = Frame(root)
    down_Frame.grid(row=2)

    # Input Labels
    up_Label1 = Label(root, text="Welcome to the State Space Solver App")
    up_Label1.grid(row=0)
    up_Label2 = Label(up_Frame, text="Enter the order of the output:")
    up_Label2.grid(row=0)
    up_Label3 = Label(up_Frame, text="Enter the order of the input:")
    up_Label3.grid(row=1)

    down_Label1 = Label(down_Frame, text="Enter the output Coefficients:")
    down_Label1.grid(row=0)
    down_Label2 = Label(down_Frame, text="Enter the input Coefficients:")
    down_Label2.grid(row=1)
    down_Label3 = Label(root, text="Select Input Type:")
    down_Label3.grid(row=3)

    # Taking Inputs

    up_Entry1 = Entry(up_Frame)
    up_Entry1.insert(0, "n")
    up_Entry1.configure(state=DISABLED)
    up_Entry1.grid(row=0, column=1)
    on_click_id1 = up_Entry1.bind('<Button-1>', up_click1)

    up_Entry2 = Entry(up_Frame)
    up_Entry2.insert(0, "m")
    up_Entry2.configure(state=DISABLED)
    up_Entry2.grid(row=1, column=1)
    on_click_id2 = up_Entry2.bind('<Button-1>', up_click2)

    u_Type = IntVar()
    up_Rad1 = Radiobutton(root, text="Unit Step", variable=u_Type, value=1)
    up_Rad1.grid(row=4)
    up_Rad2 = Radiobutton(root, text="Unit Impulse", variable=u_Type, value=0)
    up_Rad2.grid(row=5)


    down_Entry1 = Entry(down_Frame, width=37)
    down_Entry1.insert(0, "Insert the coefficients separated by commas")
    down_Entry1.configure(state=DISABLED)
    down_Entry1.grid(row=0, column=1)
    on_click_id3 = down_Entry1.bind('<Button-1>', down_click1)

    down_Entry2 = Entry(down_Frame, width=37)
    down_Entry2.insert(0, "Insert the coefficients separated by commas")
    down_Entry2.configure(state=DISABLED)
    down_Entry2.grid(row=1, column=1)
    on_click_id4 = down_Entry2.bind('<Button-1>', down_click2)

    my_Button = Button(root, text="Submit", command=done)
    my_Button.grid(row=6)


    root.mainloop()
    return results


# Converts string input from GUI into numpy array
def input2array(my_Input):
    n = my_Input.count(',') + 1
    x = my_Input.split(",")
    op = np.zeros(n)
    for i in range(n):
        op[i] = int(x[i])
    return op


# Container for Input and output derivatives coefficients
input_Cofs = input_GUI()
input_Cofs[0] = input2array(input_Cofs[0])
input_Cofs[1] = input2array(input_Cofs[1])
ui = int(input_Cofs[2])


# Input u is either unit step or unit impulse
k = 1000
if ui == 1:
    u = np.ones(k)
    u[0] = 0
else:
    u = np.zeros(k)
    u[0] = 9999999999999999999999999999999999999999
y = np.empty(k)


# Calls matplotlib function plot
def plotter(n):
    y[-1] = y[-2]
    y[0] = y[1]
    please_Plot(u, 111)
    please_Plot(y, 999)
    for i in range(n):
        plots[i][-1] = plots[i][-2]
        plots[i][0] = plots[i][1]
        please_Plot(plots[i], i+1)


# Calculate state matrices
def calc_mats(ain, bin):
    # Changed to allow output highest order coefficient
    ain /= ain[0]
    ain = np.delete(ain, 0)
    # Calculate matrix A
    n = int(ain.size)
    A = np.zeros((n, n))
    for i in range(n-1):
        for j in range(n):
            if j == (i + 1):
                A[i][j] = 1
    else:
        A[n - 1] = -1 * ain[::-1]

    # Calculate matrix B
    m = bin.size
    B = np.zeros(m)
    for i in range(m):
        B[i] = bin[i]
        for j in range(1, i+1):
            B[i] -= ain[j-1]*B[i-j]

    # Modify B and calculate D
    D = B[0]

    B = np.delete(B, 0)
    B = B.T

    # Calculate C
    C = np.zeros(n)
    C[0] = 1
    # Convert Matrices A, B, C, D to text
    t = [np.array_str(A), np.array_str(B), np.array_str(C), str(D)]
    print_mats(t)

    return A, B, C, D


# Calculate Ax + Bu
def calc_blok(a, x, b, u):
    ax = np.matmul(a, x).sum()
    bu = b * u
    return ax + bu


# calculate x
def calc_x(Ain, Bin):
    # k steps of h secs
    h = 0.01
    # n states with 0 initial states
    n = Bin.size
    x = np.empty((n, k))
    x[:, 0] = 0
    # Blok calculation, first initialize 6 bloks for n states
    blok = np.empty((6, n))
    # Then we will loop k/2 times to calculate for the whole period and n times for n x's
    for j in range(0, k-2, 2):
        for i in range(n):
            # xtemp is a container that carries a modified x vector used in blok calculation
            xtemp = x[:, j] + 0
            blok[0][i] = calc_blok(Ain[i], xtemp, Bin[i], u[j])

            xtemp = x[:, j] + h * blok[0][i]
            blok[1][i] = calc_blok(Ain[i], xtemp, Bin[i], u[j + 1])

            xtemp = x[:, j] + (h / 2) * (blok[0][i] + blok[1][i])
            blok[2][i] = calc_blok(Ain[i], xtemp, Bin[i], u[j + 1])

            xtemp = x[:, j] + (2 * h * blok[2][i])
            blok[3][i] = calc_blok(Ain[i], xtemp, Bin[i], u[j + 2])

            xtemp = x[:, j] + (h / 12) * (5 * blok[0][i] + 8 * blok[2][i] - blok[3][i])
            blok[4][i] = calc_blok(Ain[i], xtemp, Bin[i], u[j + 1])

            xtemp = x[:, j] + (h / 3) * (blok[0][i] + blok[3][i] + 4 * blok[4][i])
            blok[5][i] = calc_blok(Ain[i], xtemp, Bin[i], u[j + 2])

            # With our 6 blok for n states we can calculate next two states
            x[i][j + 1] = x[i][j] + (h / 12) * (5 * blok[0][i] + 8 * blok[2][i] - blok[3][i])
            x[i][j + 2] = x[i][j] + (h / 3) * (blok[0][i] + 4 * blok[4][i] + blok[5][i])
    return x


# Call the functions
A, B, C, D = calc_mats(input_Cofs[0], input_Cofs[1])
plots = calc_x(A, B)
y = plots[0] + D * u
plotter(B.size)

