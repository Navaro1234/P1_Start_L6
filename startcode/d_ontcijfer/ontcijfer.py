def ontcijfer(tekst, toegelaten_tekens):
    boodschap = ""
    for teken in tekst:
        if teken in toegelaten_tekens:
            boodschap += teken
            # boodschap = boodschap + teken
    return boodschap
