import tkinter as tk
from tkinter import font

def hesapla():
    ms1_entry = float(girdiler[0].get())
    ms2_entry = float(girdiler[1].get())
    gol_entry = float(girdiler[2].get())
    ev_son_entry = float(girdiler[3].get())
    dep_son_entry = float(girdiler[4].get())
    ev_sakat_def_entry = float(girdiler[5].get())
    ev_sakat_ort_entry = float(girdiler[6].get())
    ev_sakat_for_entry = float(girdiler[7].get())
    dep_sakat_def_entry = float(girdiler[8].get())
    dep_sakat_ort_entry = float(girdiler[9].get())
    dep_sakat_for_entry = float(girdiler[10].get())
    ev_son_bes_at_entry = float(girdiler[11].get())
    ev_son_bes_yiyilen_entry = float(girdiler[12].get())
    dep_son_bes_at_entry = float(girdiler[13].get())
    dep_son_bes_yiyilen_entry = float(girdiler[14].get())
    ev_son_mac_gun = float(girdiler[15].get())
    dep_son_mac_gun = float(girdiler[16].get())

    home_at = 0.2
    dep_at = 0

    if gol_entry <= 1.60:
        home_at += 0.25
        dep_at += 0.25

    if ms1_entry <= 1.80:
        if ms1_entry <= 1.40:
            home_at += 1.25
        else:
            home_at += 0.75

    if ms2_entry <= 1.80:
        if ms2_entry <= 1.40:
            dep_at += 1.25
        else:
            dep_at += 0.75

    ev_son = ev_son_entry / 4
    dep_sakat_def = dep_sakat_def_entry / 3.5
    dep_sakat_ort = dep_sakat_ort_entry / 3.5
    ev_sakat_for = ev_sakat_for_entry / 3.5
    ev_son_bes_at = ev_son_bes_at_entry / 25
    ev_son_bes_yiyilen = ev_son_bes_yiyilen_entry / 25
    home_cikarilacak = 1 - (ev_son_mac_gun / 11)

    dep_son = dep_son_entry / 4
    ev_sakat_def = ev_sakat_def_entry / 3.5
    ev_sakat_ort = ev_sakat_ort_entry / 3.5
    dep_sakat_for = dep_sakat_for_entry / 3.5
    dep_son_bes_at = dep_son_bes_at_entry / 25
    dep_son_bes_yiyilen = dep_son_bes_yiyilen_entry / 25
    dep_cikarilacak = 1 - (dep_son_mac_gun / 11)

    ev_ekle = ev_son + dep_sakat_def + dep_sakat_ort + ev_son_bes_at + dep_son_bes_yiyilen
    ev_cikar = ev_sakat_for + home_cikarilacak
    dep_ekle = dep_son + ev_sakat_def + ev_sakat_ort + dep_son_bes_at + ev_son_bes_yiyilen
    dep_cikar = dep_sakat_for + dep_cikarilacak

    home_at += ev_ekle - ev_cikar
    dep_at += dep_ekle - dep_cikar

    if gol_entry > 2.15:
        home_at -= 1
        dep_at -= 1

    toplam_gol = home_at + dep_at
    if gol_entry > 1.60:
        if toplam_gol > 3:
            home_at = home_at - 1.75
            dep_at = dep_at - 1.75

    home_eklencek = ev_son_mac_gun / 10
    home_at = home_at + home_eklencek

    dep_eklencek = dep_son_mac_gun / 10
    dep_at = dep_at + dep_eklencek

    if home_at < 0 or dep_at < 0:
        home_at += 0.25
        dep_at += 0.25
        if home_at < 0 or dep_at < 0:
            home_at += 0.25
            dep_at += 0.25

    sonuc.config(text=f"[{home_at:.1f} - {dep_at:.1f}]")

pencere = tk.Tk()
pencere.title("Match Score")
buyuk_font = font.Font(size=16)
orta_font = font.Font(size=13)
girdiler = []

etiket = tk.Label(pencere, text="Home Odd", bg="gray")
etiket.grid(column=1, row=1, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=2, row=1, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="                                                                     Away Odd", bg="gray")
etiket.grid(column=5, row=1, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=6, row=1, padx=5, pady=5)
girdiler.append(giris)


etiket = tk.Label(pencere, text="2,5 Over Odd", bg="gray")
etiket.grid(column=1, row=2, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=2, row=2, padx=5, pady=5)
girdiler.append(giris)


etiket = tk.Label(pencere, text="Previous Match / Home Goal", bg="gray")
etiket.grid(column=1, row=3, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=2, row=3, padx=5, pady=5)
girdiler.append(giris)


etiket = tk.Label(pencere, text="                                               Previous Match / Away Goal", bg="gray")
etiket.grid(column=5, row=3,padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=6, row=3, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="Home Missing Defender", bg="gray")
etiket.grid(column=1, row=4, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=2, row=4, padx=5, pady=5)
girdiler.append(giris)


etiket = tk.Label(pencere, text="Home Missing Midfielder", bg="gray")
etiket.grid(column=1, row=5, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=2, row=5, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="Home Missing Forward", bg="gray")
etiket.grid(column=1, row=6, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=2, row=6, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="                                                      Away Missing Defender", bg="gray")
etiket.grid(column=5, row=4, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=6, row=4, padx=5, pady=5)
girdiler.append(giris)


etiket = tk.Label(pencere, text="                                                    Away Missing Midfielder", bg="gray")
etiket.grid(column=5, row=5, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=6, row=5, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="                                                     Away Missing Forward", bg="gray")
etiket.grid(column=5, row=6, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=6, row=6, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="Home Goal Scored (Last 5)", bg="gray")
etiket.grid(column=1, row=7, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=2, row=7, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="Home Conceded Goal (Last 5)", bg="gray")
etiket.grid(column=1, row=8, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=2, row=8, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="                                                 Away Goal Scored (Last 5)", bg="gray")
etiket.grid(column=5, row=7, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=6, row=7, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="                                              Away Conceded Goal (Last 5)", bg="gray")
etiket.grid(column=5, row=8, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=6, row=8, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="How Many Day Home Last Match", bg="gray")
etiket.grid(column=1, row=9, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=2, row=9, padx=5, pady=5)
girdiler.append(giris)

etiket = tk.Label(pencere, text="                                                    How Many Day Away Last Match ", bg="gray")
etiket.grid(column=5, row=9, padx=5, pady=5)
giris = tk.Entry(pencere, bd=3, relief="ridge", bg="white")
giris.grid(column=6, row=9, padx=5, pady=5)
girdiler.append(giris)

hesapla_dugme = tk.Button(pencere, text="CALCULATE", command=hesapla, bd=3, relief="ridge", bg="white", font=orta_font)
hesapla_dugme.grid(row=19, column=3, columnspan=2, padx=5, pady=5)

sonuc = tk.Label(pencere, text="[Match Score]", font=buyuk_font, bg="gray")
sonuc.grid(row=19, column=4, columnspan=2, padx=5, pady=5)

pencere.configure(background="gray")

pencere.mainloop()