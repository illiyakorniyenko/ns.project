from tkinter import *
import requests
import xmltodict


def vertrektijdenWin(): #Deze functie is ons venster waar je de naam van het station in kan voeren.
    newwin = Toplevel(root)
    newwin.configure(bg='#ffc917') #achtergrondkleur
    newwin.pack_propagate(0)
    newwin.geometry("800x600") #venstergrootte

    display = Label(newwin, text="Voer de naam van uw station in:", bg='#ffc917')
    display.pack()

    topFrame = Frame(newwin)
    topFrame.pack()

    stationnaam = Entry(newwin, bg='white', fg='black',) #input strook voor het aangeven van de stationnaam.
    stationnaam.pack(side=TOP)
    stationnaam.bind("<Return>", vertrektijden)

    photo = PhotoImage(file="ns.startscherm.png") #afbeelding ns logo.
    logo = Label(newwin, image=photo)
    logo.image = photo
    logo.pack()

    toolbar = Frame(newwin, bg='#003082') #onderste strook.

    nederlandsbutton = Button(toolbar, text='Nederlands', bg='#003082', fg='Black')
    photo = PhotoImage(file='nederland.png')
    kpn = photo.subsample(6, 6)
    nederlandsbutton.config(image=kpn, compound=TOP)
    nederlandsbutton.pack(side=LEFT, padx=2, pady=2)

    engelsbutton = Button(toolbar, text='English', bg='#003082', fg='Black')
    picture = PhotoImage(file='engels.png')
    kpe = picture.subsample(21, 21)
    engelsbutton.config(image=kpe, compound=TOP)
    engelsbutton.pack(side=LEFT, padx=2, pady=2)

    mastervisa = PhotoImage(file='mastervisa.png')

    kpa = mastervisa.subsample(5, 5)
    mastervisalabel = Label(toolbar, image=kpa, compound=TOP)
    mastervisalabel.pack(side=RIGHT, padx=2, pady=2)

    toolbar.pack(side=BOTTOM, fill=X)
    newwin.mainloop()


def vertrektijden(stationnaam): #het venster met de vertrektijden

    newwin = Toplevel(root)
    newwin.configure(bg='#ffc917')
    newwin.pack_propagate(0)
    newwin.geometry("800x600")

    display = Label(newwin, bg='#ffc917', fg="black", text="Dit zijn de vertrektijden op het gekozen station:")
    display.pack()

    topFrame = Frame(newwin)
    topFrame.pack()

    auth_details = ('illiya.korniyenko@student.hu.nl', 'Fn716EyB5F0QictFJSUdSoe9DKk2m0DNx54tdJTFmhb1gPNXaBhtsg') #inloggegevens voor de api.
    api_url = 'http://webservices.ns.nl/ns-api-avt?station='+ stationnaam.widget.get() #hier de link naar de vertrekkende tijden, het laatste deel van de link wordt aangevuld door wat de gebruiker in het vorig venster heeft ingevuld.

    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)


    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']: #uit het XML bestand pakken we alleen de tijden en de treinen, de rest hebben we niet nodig.
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:16] #alleen de 11 tot 16 letter van de string (de string begint met jaar > maand > dag, dat hebben we niet nodig, alleen uren en minuten.

        display = Label(newwin, bg="blue", fg="white", text='Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming)
        display.pack(fill=BOTH, expand=1,)

    toolbar = Frame(newwin, bg='#003082')

    nederlandsbutton = Button(toolbar, text='Nederlands', bg='#003082', fg='Black')
    photo = PhotoImage(file='nederland.png')
    kpn = photo.subsample(6, 6)
    nederlandsbutton.config(image=kpn, compound=TOP)
    nederlandsbutton.pack(side=LEFT, padx=2, pady=2)

    engelsbutton = Button(toolbar, text='English', bg='#003082', fg='Black')
    picture = PhotoImage(file='engels.png')
    kpe = picture.subsample(21, 21)
    engelsbutton.config(image=kpe, compound=TOP)
    engelsbutton.pack(side=LEFT, padx=2, pady=2)

    mastervisa = PhotoImage(file='mastervisa.png')

    kpa = mastervisa.subsample(5, 5)
    mastervisalabel = Label(toolbar, image=kpa, compound=TOP)
    mastervisalabel.pack(side=RIGHT, padx=2, pady=2)

    toolbar.pack(side=BOTTOM, fill=X)

    newwin.mainloop()

root = Tk()
root.configure(bg='#ffc917')
root.pack_propagate(0)
root.geometry("800x600")
photo = PhotoImage(file="ns.startscherm.png")
label = Label(image=photo,)
label.image = photo
label.pack()
topFrame = Frame(root)
topFrame.pack()

button = Button(topFrame, text='Actuele vertrektijden', bg='Black', fg='Black', height=3, width=17, command =vertrektijdenWin) #Dit is de knop die naar het vertrektijden venster doorverwijst.
button2 = Button(topFrame, text='Kopen los kaart', bg='#003082', fg='Black', height=3, width=17)
button3 = Button(topFrame, text='Kopen OV-chipkaart', bg='#003082', fg='Black', height=3, width=17)
button4 = Button(topFrame, text='Ik wil naar het buitenland', bg='#003082', fg='Black', height=3, width=18)

button.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

toolbar = Frame(root, bg='#003082')

nederlandsbutton = Button(toolbar, text='Nederlands', bg='#003082', fg='Black')
photo = PhotoImage(file='nederland.png')
kpn = photo.subsample(6, 6)
nederlandsbutton.config(image=kpn, compound=TOP)
nederlandsbutton.pack(side=LEFT, padx=2, pady=2)

engelsbutton = Button(toolbar, text='English', bg='#003082', fg='Black')
picture = PhotoImage(file='engels.png')
kpe = picture.subsample(21, 21)
engelsbutton.config(image=kpe, compound=TOP)
engelsbutton.pack(side=LEFT, padx=2, pady=2)


mastervisa = PhotoImage(file='mastervisa.png')

kpa = mastervisa.subsample(5, 5)
mastervisalabel = Label(toolbar, image=kpa, compound=TOP)
mastervisalabel.pack(side=RIGHT, padx=2, pady=2)


toolbar.pack(side=BOTTOM, fill=X)

root.mainloop()
