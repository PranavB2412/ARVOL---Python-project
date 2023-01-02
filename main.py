from tkinter import *

root = Tk()
root.config(bg='teal')
root.geometry("1600x800")
root.title("Area & Volume Calculator")

heading = Label(root, text="Hello Y'all!, Welcome to Area and Volume Calculator a.k.a ARVOL!", font=("Arial", 27, 'bold'),
                bg='black', fg='white')
heading.grid(row=0, column=2, padx=200)

shape1 = Label(root, text='Select a shape to compute its area:', font=("Arial", 24), bg='teal', fg='black')
shape1.grid(row=1, column=2, pady=20)


# shapes to calc area
def circle():
    new_window1 = Toplevel()
    new_window1.config(bg='white')
    new_window1.geometry("800x500")

    radius_label = Label(new_window1, text='Enter the radius of the circle: ', font="Arial", bg='white',
                         fg='black')
    radius_label.grid(row=0, column=1, padx=40, pady=10)
    radius = Entry(new_window1, width=10, borderwidth=5, font="Arial")
    radius.grid(row=0, column=2)

    def area_circle():
        if float(radius.get()) < 0:
            result1.config(text='Invalid Input!')
        else:
            area1 = 3.14 * float(radius.get()) * float(radius.get())
            result1.config(text=f'The area of the circle is {area1.__round__(2)} square units.')

    submit = Button(new_window1, text='Calculate Area', font="Arial", command=area_circle, bg='black', fg='white')
    submit.grid(row=1, column=1, pady=10)

    result1 = Label(new_window1, text='', font="Arial", bg='white', fg='black')
    result1.grid(row=2, column=1, pady=10, padx=20)

    exit_circle = Button(new_window1, text='Exit', font="Arial", command=new_window1.destroy, bg='red', fg='white')
    exit_circle.grid(row=1, column=2)


circle = Button(root, text='Circle', font="Arial", command=circle)
circle.grid(row=2, column=2, pady=5)


def triangle():
    new_window2 = Toplevel()
    new_window2.config(bg='white')
    new_window2.geometry("800x500")

    base_label = Label(new_window2, text='Enter the base of the triangle: ', font="Arial", bg='white', fg='black')
    base_label.grid(row=0, column=1, padx=40, pady=10)
    base = Entry(new_window2, width=10, borderwidth=5, font="Arial")
    base.grid(row=0, column=2)

    height_label = Label(new_window2, text='Enter the height of the triangle: ', font="Arial", bg='white', fg='black')
    height_label.grid(row=1, column=1, padx=40, pady=10)
    height = Entry(new_window2, width=10, borderwidth=5, font="Arial")
    height.grid(row=1, column=2)

    def area_triangle():
        if float(base.get()) < 0 or float(height.get()) < 0:
            result2.config(text='Invalid Input!')
        else:
            area2 = 0.5 * float(base.get()) * float(height.get())
            result2.config(text=f'The area of the circle is {area2.__round__(2)} square units.')

    submit = Button(new_window2, text='Calculate Area', font="Arial", command=area_triangle, bg='black', fg='white')
    submit.grid(row=2, column=1, pady=10)

    result2 = Label(new_window2, text='', font="Arial", bg='white', fg='black')
    result2.grid(row=3, column=1, pady=10, padx=20)

    exit_tri = Button(new_window2, text='Exit', font="Arial", command=new_window2.destroy, bg='red', fg='white')
    exit_tri.grid(row=2, column=2)


triangle = Button(root, text='Triangle', font="Arial", command=triangle)
triangle.grid(row=3, column=2, pady=5)


def square():
    new_window3 = Toplevel()
    new_window3.config(bg='white')
    new_window3.geometry("800x500")

    side_label = Label(new_window3, text='Enter the side of the square: ', font="Arial", bg='white', fg='black')
    side_label.grid(row=0, column=1, padx=40, pady=10)
    side = Entry(new_window3, width=10, borderwidth=5, font="Arial")
    side.grid(row=0, column=2)

    def area_square():
        if float(side.get()) < 0:
            result3.config(text='Invalid Input!')
        else:
            area3 = float(side.get()) * float(side.get())
            result3.config(text=f'The area of the square is {area3.__round__(2)} square units.')

    submit = Button(new_window3, text='Calculate Area', font="Arial", command=area_square, bg='black', fg='white')
    submit.grid(row=1, column=1, pady=10)

    result3 = Label(new_window3, text='', font="Arial", bg='white', fg='black')
    result3.grid(row=2, column=1, pady=10, padx=20)

    exit_square = Button(new_window3, text='Exit', font="Arial", command=new_window3.destroy, bg='red', fg='white')
    exit_square.grid(row=1, column=2)


square = Button(root, text='Square', font="Arial", command=square)
square.grid(row=4, column=2, pady=5)


def rectangle():
    new_window4 = Toplevel()
    new_window4.config(bg='white')
    new_window4.geometry("800x500")

    length_rect = Label(new_window4, text='Enter the length of the rectangle: ', font="Arial", bg='white', fg='black')
    length_rect.grid(row=0, column=1, padx=40, pady=10)
    length1 = Entry(new_window4, width=10, borderwidth=5, font="Arial")
    length1.grid(row=0, column=2)

    breadth_label = Label(new_window4, text='Enter the breadth of the rectangle: ', font="Arial", bg='white',
                          fg='black')
    breadth_label.grid(row=1, column=1, padx=40, pady=10)
    breadth1 = Entry(new_window4, width=10, borderwidth=5, font="Arial")
    breadth1.grid(row=1, column=2)

    def area_rectangle():
        if float(length1.get()) < 0 or float(breadth1.get()) < 0:
            result4.config(text='Invalid Input!')
        else:
            area4 = float(length1.get()) * float(breadth1.get())
            result4.config(text=f'The area of the rectangle is {area4.__round__(2)} square units.')

    submit = Button(new_window4, text='Calculate Area', font="Arial", command=area_rectangle, bg='black', fg='white')
    submit.grid(row=2, column=1, pady=10)

    result4 = Label(new_window4, text='', font="Arial", bg='white', fg='black')
    result4.grid(row=3, column=1, pady=10, padx=20)

    exit_rect = Button(new_window4, text='Exit', font="Arial", command=new_window4.destroy, bg='red', fg='white')
    exit_rect.grid(row=2, column=2)


rectangle = Button(root, text='Rectangle', font="Arial", command=rectangle)
rectangle.grid(row=5, column=2, pady=5)

shape2 = Label(root, text='Select a shape to compute its volume:', font=("Arial", 24), bg='teal')
shape2.grid(row=6, column=2, pady=20)


# shapes to calc volume
def sphere():
    new_window5 = Toplevel()
    new_window5.config(bg='white')
    new_window5.geometry("800x500")

    radius_sphere = Label(new_window5, text='Enter the radius of the sphere: ', font="Arial", bg='white', fg='black')
    radius_sphere.grid(row=0, column=1, padx=40, pady=10)
    radius2 = Entry(new_window5, width=10, borderwidth=5, font="Arial")
    radius2.grid(row=0, column=2)

    def vol_sphere():
        if float(radius2.get()) < 0:
            result5.config(text='Invalid Input!')
        else:
            vol1 = (4 / 3) * 3.14 * float(radius2.get()) ** 3
            result5.config(text=f'The volume of the sphere is {vol1.__round__(2)} cubic units.')

    submit = Button(new_window5, text='Calculate Volume', font="Arial", command=vol_sphere, bg='black', fg='white')
    submit.grid(row=1, column=1, pady=10)

    result5 = Label(new_window5, text='', font="Arial", bg='white', fg='black')
    result5.grid(row=2, column=1, pady=10, padx=20)

    exit_sphere = Button(new_window5, text='Exit', font="Arial", command=new_window5.destroy, bg='red', fg='white')
    exit_sphere.grid(row=1, column=2)


sphere = Button(root, text='Sphere', font="Arial", command=sphere)
sphere.grid(row=7, column=2, pady=5)


def cuboid():
    new_window6 = Toplevel()
    new_window6.config(bg='white')
    new_window6.geometry("800x500")

    length_label = Label(new_window6, text='Enter the length of the cuboid: ', font="Arial", bg='white', fg='black')
    length_label.grid(row=0, column=1, padx=40, pady=10)
    length = Entry(new_window6, width=10, borderwidth=5, font="Arial")
    length.grid(row=0, column=2)

    breadth_label = Label(new_window6, text='Enter the breadth of the cuboid: ', font="Arial", bg='white', fg='black')
    breadth_label.grid(row=1, column=1, padx=40, pady=10)
    breadth = Entry(new_window6, width=10, borderwidth=5, font="Arial")
    breadth.grid(row=1, column=2)

    height_label = Label(new_window6, text='Enter the height of the cuboid: ', font="Arial", bg='white', fg='black')
    height_label.grid(row=2, column=1, padx=40, pady=10)
    height = Entry(new_window6, width=10, borderwidth=5, font="Arial")
    height.grid(row=2, column=2)

    def vol_cuboid():
        if float(length.get()) < 0 or float(breadth.get()) < 0 or float(height.get()) < 0:
            result6.config(text='Invalid Input!')
        else:
            vol2 = float(length.get()) * float(breadth.get()) * float(height.get())
            result6.config(text=f'The volume of the cuboid is {vol2.__round__(2)} cubic units.')

    submit = Button(new_window6, text='Calculate Volume', font="Arial", command=vol_cuboid, bg='black', fg='white')
    submit.grid(row=3, column=1, pady=10)

    result6 = Label(new_window6, text='', font="Arial", bg='white', fg='black')
    result6.grid(row=4, column=1, pady=10, padx=20)

    exit_cuboid = Button(new_window6, text='Exit', font="Arial", command=new_window6.destroy, bg='red', fg='white')
    exit_cuboid.grid(row=3, column=2)


cuboid = Button(root, text='Cuboid', font="Arial", command=cuboid)
cuboid.grid(row=8, column=2, pady=5)


def cube():
    new_window7 = Toplevel()
    new_window7.config(bg='white')
    new_window7.geometry("800x500")

    side2 = Label(new_window7, text='Enter the side of the cube: ', font="Arial", bg='white', fg='black')
    side2.grid(row=0, column=1, padx=40, pady=10)
    side_cube = Entry(new_window7, width=10, borderwidth=5, font="Arial")
    side_cube.grid(row=0, column=2)

    def vol_cube():
        if float(side_cube.get()) < 0:
            result7.config(text='Invalid Input!')
        else:
            vol3 = float(side_cube.get()) ** 3
            result7.config(text=f'The volume of the cube is {vol3.__round__(2)} cubic units.')

    submit = Button(new_window7, text='Calculate Volume', font="Arial", command=vol_cube, bg='black', fg='white')
    submit.grid(row=1, column=1, pady=10)

    result7 = Label(new_window7, text='', font="Arial", bg='white', fg='black')
    result7.grid(row=2, column=1, pady=10, padx=20)

    exit_cube = Button(new_window7, text='Exit', font="Arial", command=new_window7.destroy, bg='red', fg='white')
    exit_cube.grid(row=1, column=2)


cube = Button(root, text='Cube', font="Arial", command=cube)
cube.grid(row=9, column=2, pady=5)


def cylinder():
    new_window8 = Toplevel()
    new_window8.config(bg='white')
    new_window8.geometry("800x500")

    base_radius = Label(new_window8, text='Enter the base radius of the cylinder: ', font="Arial", bg='white',
                        fg='black')
    base_radius.grid(row=0, column=1, padx=40, pady=10)
    radius_cyl = Entry(new_window8, width=10, borderwidth=5, font="Arial")
    radius_cyl.grid(row=0, column=2)

    height_cyl = Label(new_window8, text='Enter the height of the cylinder: ', font="Arial", bg='white', fg='black')
    height_cyl.grid(row=1, column=1, padx=40, pady=10)
    height2 = Entry(new_window8, width=10, borderwidth=5, font="Arial")
    height2.grid(row=1, column=2)

    def vol_cylinder():
        if float(radius_cyl.get()) < 0 or float(height2.get()) < 0:
            result8.config(text='Invalid Input!')
        else:
            vol4 = 3.14 * float(radius_cyl.get()) * float(radius_cyl.get()) * float(height2.get())
            result8.config(text=f'The volume of the cylinder is {vol4.__round__(2)} cubic units.')

    submit = Button(new_window8, text='Calculate Volume', font="Arial", command=vol_cylinder, bg='black', fg='white')
    submit.grid(row=2, column=1, pady=10)

    result8 = Label(new_window8, text='', font="Arial", bg='white', fg='black')
    result8.grid(row=3, column=1, pady=10, padx=20)

    exit_cyl = Button(new_window8, text='Exit', font="Arial", command=new_window8.destroy, bg='red', fg='white')
    exit_cyl.grid(row=2, column=2)


cylinder = Button(root, text='Cylinder', font="Arial", command=cylinder)
cylinder.grid(row=10, column=2, pady=5)

exit_button = Button(root, text='Exit', command=quit, bg='red', fg='white', font=("Arial", 25))
exit_button.grid(row=12, column=2, padx=50, pady=20)

mainloop()
