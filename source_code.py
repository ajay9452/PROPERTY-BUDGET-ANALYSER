import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import os
root=tk.Tk()

canvas = tk.Canvas(root, height = 800, width = 700) #give initial dimensions
canvas.pack()

frame1 = tk.Frame(root)
frame1.place(relheight = 0.1,relwidth = 1)
label1 = tk.Label(frame1, text = "WELCOME TO PROPERTY BUDGET ESTIMATOR", font='400', fg = 'WHITE', bg = '#34626c')
label1.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)

frame2 = tk.Frame(root)
frame2.place(rely = 0.1, relheight = 0.1, relwidth = 1)
label2 = tk.Label(frame2, text = "MARK YOUR REQUIREMENTS", font='400', fg = 'WHITE', bg = '#839b97')
label2.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)

frame3 = tk.Frame(root)
frame3.place(rely = 0.2, relheight = 0.3,relwidth = 1)

v1 = tk.BooleanVar()
checkbox1 = tk.Checkbutton(frame3, text = 'Lift', onvalue = 1, offvalue = 0, variable = v1, font = '50')
checkbox1.place(relx = 0.05, rely = 0.14, relheight = 0.166, relwidth = 0.2)

v2 = tk.BooleanVar()
ck2 = tk.Checkbutton(frame3, text = 'Car Parking', onvalue = 1, offvalue = 0, variable = v2, font = '50')
ck2.place(relx = 0.7, rely = 0.14, relheight = 0.166, relwidth = 0.2)

v3 = tk.BooleanVar()
ck3 = tk.Checkbutton(frame3, text = 'Power Backup', onvalue = 1, offvalue = 0, variable = v3, font = '50')
ck3.place(relx = 0.1052, rely = 0.3, relheight = 0.166, relwidth = 0.2)

v4 = tk.BooleanVar()
ck4 = tk.Checkbutton(frame3, text = 'Club House', onvalue = 1, offvalue = 0, variable = v4, font = '50')
ck4.place(relx=0.695,rely=0.3,relheight=0.166,relwidth=0.2)

v5 = tk.BooleanVar()
ck5 = tk.Checkbutton(frame3, text = 'Jogging Track', onvalue = 1, offvalue = 0, variable = v5, font = '50')
ck5.place(relx = 0.085, rely = 0.5, relheight = 0.166, relwidth = 0.25)

v6 = tk.BooleanVar()
ck6 = tk.Checkbutton(frame3, text = 'Gymnasium', onvalue = 1, offvalue = 0, variable = v6, font = '50')
ck6.place(relx=0.685,rely=0.5,relheight=0.166,relwidth=0.2)

v7 = tk.BooleanVar()
ck7 = tk.Checkbutton(frame3, text = 'Landscaped Garden', onvalue = 1, offvalue = 0, variable = v7, font = '50')
ck7.place(relx = 0.085, rely = 0.7, relheight = 0.166, relwidth = 0.3)

v8 = tk.BooleanVar()
ck8 = tk.Checkbutton(frame3, text = 'Swimming Pool', onvalue = 1, offvalue = 0, variable = v8, font = '50')
ck8.place(relx = 0.685, rely = 0.7, relheight = 0.166, relwidth = 0.25)

frame4 = tk.Frame(root)
frame4.place(relx = 0.1, rely = 0.5, relheight = 0.3, relwidth = 0.8)
label4 = tk.Label(frame4, text = "Number of bedrooms you want :", font = '50')
label4.place(relx = 0, rely = 0.05, relheight = 0.1, relwidth = 0.6)
e4 = tk.Entry(frame4, font = '50')
e4.place(relx = 0.63, rely = 0.05, relheight = 0.1, relwidth = 0.4)

label5 = tk.Label(frame4, text = "Minimum Budget:", font = '50')
label5.place(relx = 0, rely = 0.2, relheight = 0.1, relwidth = 0.6)
e5 = tk.Entry(frame4, font = '50')
e5.place(relx = 0.63, rely = 0.2, relheight = 0.1, relwidth = 0.4)

label6 = tk.Label(frame4, text = "Maximum Budget:", font = '50')
label6.place(relx = 0, rely = 0.35, relheight = 0.1, relwidth = 0.6)
e6 = tk.Entry(frame4, font = '50')
e6.place(relx = 0.63, rely = 0.35, relheight = 0.1, relwidth = 0.4)

def Display():
    df = pd.read_csv(r"C:\Mumbai.csv")

    NoOfBedrooms = int(e4.get())
    minimum = int(e5.get())
    maximum = int(e6.get())
    LiftAvailable = v1.get()
    CarParking = v2.get()
    PowerBackup = v3.get()
    ClubHouse = v4.get()
    JoggingTrack = v5.get()
    LandscapedGardens = v7.get()
    SwimmingPool = v8.get()
    Gymnasium = v6.get()

    if LiftAvailable:
        df = df.loc[df["LiftAvailable"] == 1]
    if CarParking:
        df = df.loc[df["CarParking"] == 1]
    if PowerBackup:
        df = df.loc[df["PowerBackup"] == 1]
    if ClubHouse:
        df = df.loc[df["ClubHouse"] == 1]
    if JoggingTrack:
        df = df.loc[df["JoggingTrack"] == 1]
    if SwimmingPool:
        df = df.loc[df["SwimmingPool"] == 1]
    if Gymnasium:
        df = df.loc[df["Gymnasium"] == 1]
    if LandscapedGardens:
        df = df.loc[df["LandscapedGardens"] == 1]

    df = df.loc[(df['Price'] <= maximum) & (df['Price'] >= minimum)]

    # Done
    plt.title("Number of Bedrooms v/s Price")
    plt.scatter(df['Price'],df.NoOfBedrooms,label='graph')
    plt.yticks([1,2,3,4])
    plt.xlabel('Price of bedrooms')
    plt.ylabel('No. of bedrooms')
    plt.show()

    df = df.loc[df["NoOfBedrooms"] == NoOfBedrooms]

    # Done
    x_1 = list(df.Area)
    y_1 = list(df.Price)
    plt.figure(figsize=(6,4))
    plt.scatter(x_1,y_1)
    plt.title("Area of rooms v/s Price of rooms")
    plt.xlabel('Area of flats')
    plt.ylabel('Price of flats')
    plt.show()

    # Done
    plt.title("No. of counts of flats in respective locations")
    plt.xlabel('Locations')
    plt.ylabel('Count')
    df['Location'].value_counts().plot(kind='bar',color='brown')
    plt.show()

    slices = []
    labels = []
    start = minimum
    it = 1000000

    while(start < maximum):
        if(start + it < maximum):
            slices.append(len(df.loc[(df['Price'] >= start) & (df['Price'] < start + it)].index))
            labels.append("{}-{}".format(start, start + it))
        else:
            slices.append(len(df.loc[(df['Price'] >= start) & (df['Price'] <= maximum)].index))
            labels.append("{}-{}".format(start, maximum))
        start += it

    plt.title("No. of rooms available in given range of prices")
    plt.pie(slices,labels = labels,autopct = '%.1f %%')
    plt.show()

frame5 = tk.Frame(root)
frame5.place(relx = 0.1, rely = 0.7, relheight = 0.1, relwidth = 0.8)
button=tk.Button(frame5,text="FIND",font='50',command=Display, bg = '#c6b497', fg = 'WHITE')
button.place(relx=0.3,rely=0.45,relheight=0.5,relwidth=0.4)

root.mainloop()
