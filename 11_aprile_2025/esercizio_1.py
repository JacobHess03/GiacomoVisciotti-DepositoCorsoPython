
import requests


# Ciclo per inserire il numero di giorni e fare richieste meteo
while True:
    print("---MENU---")
    scelta = int(input("Scegli l'opzione: \n1.Visualizza meteo\n2.Esci\n"))
    match scelta:
        case 1:
            # Inserimento città
            city = input("Inserisci il nome della città per cui vuoi visualizzare le informazioni: ").strip().lower()

            # URL CORRETTO per la geocodifica (restituisce latitudine e longitudine)
            url_1 = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=it&format=json"
            response_1 = requests.get(url_1)
            dizionario_1 = response_1.json()

            # Controlla che ci siano risultati
            if "results" not in dizionario_1 or not dizionario_1["results"]:
                print("Nessun risultato trovato per la città inserita.")
                exit()

            # Prendi latitudine e longitudine
            latitude = dizionario_1["results"][0]["latitude"] # results -> [0] -> latitude
            longitude = dizionario_1["results"][0]["longitude"] # results -> [0] -> longitude
            num_days = int(input("Inserisci il numero di giorni per cui vuoi visualizzare le info (1g, 3g, 7g): ").strip())
            if num_days != 1 and num_days != 3 and num_days != 7:
                print("Inserisci un numero valido.")
                continue
        

            # URL della previsione
            url_2 = (
                f"https://api.open-meteo.com/v1/forecast?"
                f"latitude={latitude}&longitude={longitude}"
                f"&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_mean,wind_speed_10m_max"
                f"&forecast_days={num_days}&timezone=Europe%2FRome"
            )


            response_2 = requests.get(url_2)
            dati_meteo = response_2.json()

            if "daily" in dati_meteo:
                print("\nPrevisioni giornaliere:")
                for i in range(num_days):
                    giorno = dati_meteo["daily"]["time"][i] # daily -> time -> 1 giorno, 2 giorno, 3 giorno ... i giorni
                    temp_max = dati_meteo["daily"]["temperature_2m_max"][i]
                    temp_min = dati_meteo["daily"]["temperature_2m_min"][i]
                    pioggia = dati_meteo["daily"]["precipitation_probability_mean"][i]
                    vento = dati_meteo["daily"]["wind_speed_10m_max"][i]
                    print(f"- {giorno}: Max: {temp_max}°C, Min: {temp_min}°C, Pioggia (media): {pioggia}%, Vento: {vento}km/h")
            else:
                print("Nessun dato meteo disponibile.")


        case 2:
            print("Uscita programma...")
            break
