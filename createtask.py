# Importing the tkinter module for the GUI and math module for advanced mathematical operations
from tkinter import *
from math import *


# These lists are set up to be referenced later and find out which variables are being solved for and which variables
# are given
variables = ["Initial Velocity", "Final Velocity", "Displacement", "Time", "Acceleration"]
solve = []
onoff = {}
values = []
chosen_var = []
# Defining the variables beforehand to prevent any errors with python trying to solve for them while they're still
# undefined
vi = 1
vf = 1
d = 1
t = 1
a = 1


# The main tkinter application, mainly used to store the functions and other frames
# The credit for the tkinter frames and the function to swap between them goes to Stack Overflow user Bryan Oakley
class PhysCalc(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ChooseSolve, PickVar, DefVar, Solution):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ChooseSolve")

    # This function switches frames
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # This function stores the variable the user wants to solve for and sets up the menu for users to choose which
    # variables they already have
    def choosesolve(self, n, page_name):
        frame = self.frames[page_name]
        variables.remove(n)
        solve.append(n)
        varcheck = Menubutton(frame, text="Variables", relief=RAISED)
        varcheck.menu = Menu(varcheck, tearoff=0)
        varcheck["menu"] = varcheck.menu
        for x in variables:
            var = IntVar()
            varcheck.menu.add_checkbutton(label=x, variable=var)
            onoff[x] = var

        varcheck.pack()

    # This function creates an entry field for each variable the user chose in the previous frame
    def var_entry(self, page_name):
        global check, entry, entries
        frame = self.frames[page_name]
        check = [(x, var.get()) for x, var in onoff.items()]
        entries = []
        for y in check:
            if 1 in y:
                entry = Entry(frame, width=20)
                z = variables[check.index(y)]
                label = Label(frame, text=z)
                label.pack()
                entry.pack()
                entries.append(entry)
            else:
                pass

    # This is the function that solves for the variable chosen using given information
    def var_get(self, page_name):
        global vi, vf, d, t, a, var_values, chosen_var
        frame = self.frames[page_name]
        # This loop stores all the given variables in one list
        for y in check:
            if 1 in y:
                chosen_var.append(variables[check.index(y)])
            else:
                pass
        # This loop makes sure that the user actually entered values for the variables and stores those values in a list
        c = 0
        for entry in entries:
            if entry.get():
                values.append(entry.get())
                label = Label(frame, text=chosen_var[c] + ": " + entry.get())
                label.pack()
                c += 1
            else:
                error = Label(frame, text="Missing input value.")
                error.pack()
                return
        # This combines the given variables and the entered data into one dictionary, pairing them up
        var_values = dict(zip(chosen_var, values))
        # The first five 'if' statements define the variables
        if "Initial Velocity" in var_values:
            vi = float(var_values["Initial Velocity"])
        if "Final Velocity" in var_values:
            vf = float(var_values["Final Velocity"])
        if "Displacement" in var_values:
            d = float(var_values["Displacement"])
        if "Time" in var_values:
            t = float(var_values["Time"])
        if "Acceleration" in var_values:
            a = float(var_values["Acceleration"])
        # These two 'if' statements make sure that the user chose enough given variables
        if c < 3:
            error = Label(frame, text="Not enough variables selected")
            error.pack()
        elif c > 3:
            error = Label(frame, text="Too many variables selected")
            error.pack()
        # These only trigger if there were no errors in the number of variables chosen
        # The list at the start of each 'if' statement is the list of expressions to solve for that variable
        # The 'try' and 'except' statements filter out mathematical errors so that the function can run
        # The first 'if' statement determines the variable you want to solve for, the other 'if' statements find the
        # given variables, and the ones after that identify any mathematical errors
        else:
            if "Initial Velocity" in solve:
                try:
                    init_velocity = [vf - (2*d)/t, vf - a*t, d/t - (a*t)/2, sqrt(vf**2 - 2*a*d), -1*sqrt(vf**2 - 2*a*d)]
                except ValueError or ZeroDivisionError:
                    try:
                        init_velocity = [vf - (2 * d) / t, vf - a * t, d / t - (a * t) / 2, "NULL",
                                         "NULL"]
                    except ZeroDivisionError:
                        pass
                    try:
                        init_velocity = ["NULL", vf - a * t, "NULL", sqrt(vf ** 2 - 2 * a * d),
                                         -1 * sqrt(vf ** 2 - 2 * a * d)]
                    except ValueError:
                        pass
                except ValueError and ZeroDivisionError:
                    init_velocity = ["NULL", vf - a * t, "NULL", "NULL",
                                     "NULL"]

                if "Acceleration" not in var_values:
                    if t != 0:
                        solution = init_velocity[0]
                    else:
                        solution = "Error: divide by zero"
                elif "Displacement" not in var_values:
                    solution = init_velocity[1]
                elif "Final Velocity" not in var_values:
                    if t != 0:
                        solution = init_velocity[2]
                    else:
                        solution = "Error: divide by zero"
                elif "Time" not in var_values:
                    if (vf**2 - 2*a*d) >= 0:
                        solution = str(init_velocity[3]) + " or " + str(init_velocity[4])
                    else:
                        solution = "Error: square root of a negative"
            elif "Final Velocity" in solve:
                try:
                    fin_velocity = [(2 * d) / t + vi, vi + a * t, sqrt(vi ** 2 + 2 * a * d), -1 * sqrt(vi ** 2 + 2 * a * d),
                                    (a * t) / 2 + d / t]
                except ValueError or ZeroDivisionError:
                    try:
                        fin_velocity = [(2*d)/t + vi, vi + a*t, "NULL", "NULL", (a*t)/2 + d/t]
                    except ZeroDivisionError:
                        pass
                    try:
                        fin_velocity = ["NULL", vi + a * t, sqrt(vi ** 2 + 2 * a * d),
                                        -1 * sqrt(vi ** 2 + 2 * a * d), "NULL"]
                    except ValueError:
                        pass
                except ValueError and ZeroDivisionError:
                    fin_velocity = ["NULL", vi + a * t, "NULL", "NULL",
                                    "NULL"]
                if "Acceleration" not in var_values:
                    if t != 0:
                        solution = fin_velocity[0]
                    else:
                        solution = "Error: divide by zero"
                elif "Displacement" not in var_values:
                    solution = fin_velocity[1]
                elif "Time" not in var_values:
                    if (vi**2 + 2*a*d) >= 0:
                        solution = str(fin_velocity[2]) + " or " + str(fin_velocity[3])
                    else:
                        solution = "Error: square root of a negative"
                elif "Initial Velocity" not in var_values:
                    if t != 0:
                        solution = fin_velocity[4]
                    else:
                        solution = "Error: divide by zero"
            elif "Displacement" in solve:
                try:
                    displace = [t * (vf - vi) / 2, vi * t + 0.5 * a * t ** 2, (vf ** 2 - vi ** 2) / (2 * a),
                                vf * t - 0.5 * a * t ** 2]
                except ZeroDivisionError:
                    displace = [t * (vf - vi) / 2, vi * t + 0.5 * a * t ** 2, "NULL",
                                vf * t - 0.5 * a * t ** 2]
                if "Acceleration" not in var_values:
                    solution = displace[0]
                elif "Final Velocity" not in var_values:
                    solution = displace[1]
                elif "Time" not in var_values:
                    if a != 0:
                        solution = displace[2]
                    else:
                        solution = "Error: divide by zero"
                elif "Initial Velocity" not in var_values:
                    solution = displace[3]
            elif "Time" in solve:
                try:
                    tim = [(2 * d) / (vf - vi), (vf - vi) / a, (sqrt(2 * a * d + vi ** 2) - vi) / a,
                           (-1 * sqrt(2 * a * d + vi ** 2) + vi) / a, d / vi,
                           (vf - sqrt(vf**2 - 2*a*d))/a, (vf + sqrt(vf**2 - 2*a*d))/a, d/vf]
                except:
                    if a == 0:
                        if "Final Velocity" in var_values and vf != 0:
                            try:
                                tim = [(2 * d) / (vf - vi), "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", d/vf]
                            except ZeroDivisionError:
                                tim = ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", d/vf]
                        else:
                            try:
                                tim = [(2 * d) / (vf - vi), "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
                            except ZeroDivisionError:
                                tim = ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
                        if "Initial Velocity" in var_values and vi != 0:
                            try:
                                tim = [(2 * d) / (vf - vi), "NULL", "NULL", "NULL", d / vi, "NULL", "NULL", "NULL"]
                            except ZeroDivisionError:
                                tim = ["NULL", "NULL", "NULL", "NULL", d / vi, "NULL", "NULL", "NULL"]
                        else:
                            try:
                                tim = [(2 * d) / (vf - vi), "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
                            except ZeroDivisionError:
                                tim = ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
                    elif vf == vi:
                        try:
                            tim = ["NULL", (vf - vi) / a, (sqrt(2 * a * d + vi ** 2) - vi) / a,
                                   (-1 * sqrt(2 * a * d + vi ** 2) + vi) / a, "NULL",
                                   (vf - sqrt(vf**2 - 2*a*d))/a, (vf + sqrt(vf**2 - 2*a*d))/a, "NULL"]
                        except ValueError:
                            if (2*a*d + vi**2) < 0 and (vf**2 - 2*a*d) < 0:
                                tim = ["NULL", (vf - vi) / a, "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
                            elif (2*a*d + vi**2) < 0:
                                tim = ["NULL", (vf - vi) / a, "NULL", "NULL", "NULL", (vf - sqrt(vf**2 - 2*a*d))/a,
                                       (vf + sqrt(vf**2 - 2*a*d))/a, "NULL"]
                            elif (vf**2 - 2*a*d) < 0:
                                tim = ["NULL", (vf - vi) / a, (sqrt(2 * a * d + vi ** 2) - vi) / a,
                                       (-1 * sqrt(2 * a * d + vi ** 2) + vi) / a, "NULL", "NULL", "NULL", "NULL"]
                    else:
                        if (2 * a * d + vi ** 2) < 0 and (vf ** 2 - 2 * a * d) < 0:
                            tim = [(2 * d) / (vf - vi), (vf - vi) / a, "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
                        elif (2 * a * d + vi ** 2) < 0:
                            tim = [(2 * d) / (vf - vi), (vf - vi) / a, "NULL", "NULL", "NULL",
                                   (vf - sqrt(vf ** 2 - 2 * a * d)) / a, (vf + sqrt(vf ** 2 - 2 * a * d)) / a, "NULL"]
                        elif (vf ** 2 - 2 * a * d) < 0:
                            tim = [(2 * d) / (vf - vi), (vf - vi) / a, (sqrt(2 * a * d + vi ** 2) - vi) / a,
                                   (-1 * sqrt(2 * a * d + vi ** 2) + vi) / a, "NULL", "NULL", "NULL", "NULL"]
                if "Acceleration" not in var_values:
                    if vf != vi:
                        solution = tim[0]
                    else:
                        solution = "Error: divide by zero"
                elif "Displacement" not in var_values:
                    if a != 0:
                        solution = tim[1]
                    else:
                        solution = "Error: divide by zero"
                elif "Final Velocity" not in var_values:
                    if a != 0:
                        if (2*a*d + vi**2) >= 0:
                            solution = str(tim[2]) + " or " + str(tim[3])
                        else:
                            solution = "Error: square root of a negative"
                    else:
                        if vi != 0:
                            solution = tim[4]
                        else:
                            solution = "Error: divide by zero"
                elif "Initial Velocity" not in var_values:
                    if a != 0:
                        if (vf**2 - 2*a*d) >= 0:
                            solution = str(tim[5]) + " or " + str(tim[6])
                        else:
                            solution = "Error: square root of a negative"
                    else:
                        if vf != 0:
                            solution = tim[7]
                        else:
                            solution = "Error: divide by zero"
            elif "Acceleration" in solve:
                try:
                    accel = [(vf - vi) / t, 2 * (d - t * vi) / (t ** 2), (vf ** 2 - vi ** 2) / (2 * d),
                             -2 * (d - t * vf) / (t ** 2)]
                except ZeroDivisionError:
                    if t == 0 and d == 0:
                        accel = ["NULL", "NULL", "NULL", "NULL"]
                    elif t == 0:
                        accel = ["NULL", "NULL", (vf ** 2 - vi ** 2) / (2 * d), "NULL"]
                    elif d == 0:
                        accel = [(vf - vi) / t, 2 * (d - t * vi) / (t ** 2), "NULL", -2 * (d - t * vf) / (t ** 2)]
                if "Displacement" not in var_values:
                    if t != 0:
                        solution = accel[0]
                    else:
                        solution = "Error: divide by zero"
                elif "Final Velocity" not in var_values:
                    if t != 0:
                        solution = accel[1]
                    else:
                        solution = "Error: divide by zero"
                elif "Time" not in var_values:
                    if d != 0:
                        solution = accel[2]
                    else:
                        solution = "Error: divide by zero"
                elif "Initial Velocity" not in var_values:
                    if t != 0:
                        solution = accel[3]
                    else:
                        solution = "Error: divide by zero"
            solved = Label(frame, text=solve[0] + " = " + str(solution))
            solved.pack()


# The first frame, it shows buttons to allow the user to choose what variable to solve for
class ChooseSolve(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Choose one variable to solve for:")
        label.pack()
        for x in variables:
            picksolve = Button(self, text=x, command=lambda y=x: [controller.show_frame("PickVar"),
                                                                  controller.choosesolve(y, "PickVar")])
            picksolve.pack()


# The second frame, it shows the menu where the user can choose what variables they already have
class PickVar(Frame):

    def __init__(self, parent, controller):
        global onoff
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="You must choose three variables that you already know the values of.")
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Next",
                         command=lambda: [controller.show_frame("DefVar"), controller.var_entry("DefVar")])

        button1.pack(side="bottom", pady=20)


# The third frame, it holds the entry fields for the user to input their known values
class DefVar(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Define the values for your chosen variables.")
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Next",
                        command=lambda: [controller.show_frame("Solution"), controller.var_get("Solution")])
        button.pack(side="bottom", pady=20)


# The final frame, it shows the solution
class Solution(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller


# Runs the tkinter app
app = PhysCalc()
app.mainloop()