tel = {
    "arbeit": {"Jan": "50", "Mark": "81"}, 
    "private": {"Julia": "0151438924", "Mark": "016932834"}
}

len(tel)  # 2
len(tel["arbeit"])  # 2
tel["arbeit"].get("Mark")  # 81
"Jan" in tel["arbeit"]  # True
list(tel["private"].values())  # ["0151438924", "016932834"]
tel["private"].copy()  # {'Julia': '0151438924', 'Mark': '016932834'}


