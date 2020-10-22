'''Python program to  create a simple GUI calculator using Tkinter'''

from tkinter import *

# globally declare the expression variable (i.e. calculator display contents)
expression = ""


def press(num):
    '''Function to update expression in the text entry box on pressing a button'''
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


def equalpress():
    '''Function to evaluate the final expression'''

    # Try and except statement for handling errors (zero division etc.)
    try:
        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
        equation.set(total)

        # initialize the expression variable with empty str
        expression = ""

    # except for errors
    except:
        equation.set(" error ")
        expression = ""


def clear():
    """remove text in text entry box"""

    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    '''Driver code'''

    # initialize a GUI window
    gui = Tk()

    # background color of GUI window
    gui.configure(background="light green")

    # title of GUI window
    gui.title("Simple Calculator")

    # size of GUI window
    gui.geometry("320x220")

    # instantiate StringVar() object
    equation = StringVar()

    # text entry box containing expression text
    expression_field = Entry(gui, textvariable=equation)

    # place widgets in grid structure that can be referenced as row/column
    expression_field.grid(columnspan=5, ipadx=100)

    # initial equation in expression field
    equation.set('enter your expression')

    # create buttons on grid. When pressing, the 'press' function with button's contents is executed.
    button_height = 2
    button_width = 10

    button1 = Button(gui, text=' 1 ', fg='black', bg='red', command=lambda: press(1),
                     height=button_height, width=button_width)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red', command=lambda: press(2),
                     height=button_height, width=button_width)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red', command=lambda: press(3),
                     height=button_height, width=button_width)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red', command=lambda: press(4),
                     height=button_height, width=button_width)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red', command=lambda: press(5),
                     height=button_height, width=button_width)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red', command=lambda: press(6),
                     height=button_height, width=button_width)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red', command=lambda: press(7),
                     height=button_height, width=button_width)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red', command=lambda: press(8),
                     height=button_height, width=button_width)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red', command=lambda: press(9),
                     height=button_height, width=button_width)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red', command=lambda: press(0),
                     height=button_height, width=button_width)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red', command=lambda: press("+"),
                  height=button_height, width=button_width)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red', command=lambda: press("-"),
                   height=button_height, width=button_width)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red', command=lambda: press("*"),
                      height=button_height, width=button_width)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red', command=lambda: press("/"),
                    height=button_height, width=button_width)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red', command=equalpress,
                   height=button_height, width=button_width)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red', command=clear,
                   height=button_height, width=button_width)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='red', command=lambda: press('.'),
                     height=button_height, width=button_width)
    Decimal.grid(row=6, column=0)

    # start the GUI
    gui.mainloop()