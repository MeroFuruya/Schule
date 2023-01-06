tel = {
    "arbeit": {"Jan": "50", "Mark": "81"}, 
    "private": {"Julia": "0151438924", "Mark": "016932834"}
}

# Ändere nachträglich die interne Durchwahl von Mark zu 80.
tel["arbeit"]["Mark"] = "80"

# Lösche die Eintrag von Julia inkl. Handynummer
tel["private"].pop("Julia")

# Ändere den Namen Mark im privaten Bereich in "Murad"
tel["private"]["Murad"] = tel["private"]["Mark"]
tel["private"].pop("Mark")

print(tel)

