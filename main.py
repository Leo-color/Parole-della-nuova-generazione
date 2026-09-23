
meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "BRO": "un amico",
            "GIF": "immagine in movimento per pochi secondi"
            }
for i in range (5):
                parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")



if parola in meme_dict.keys():
    print(meme_dict[parola])
    # Cosa fare se la parola è stata trovata?
else:
    print("riprova")
    # Cosa fare se la parola non è stata trovata?
