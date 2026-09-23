meme_dict = {
    "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
    "LOL": "Una risposta comune a qualcosa di divertente",
    "BRO": "Un amico",
    "GIF": "Immagine in movimento per pochi secondi"
}

for i in range(5):
    parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

    if parola in meme_dict:
        print(meme_dict[parola])
    else:
        print("Riprova")
