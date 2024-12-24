EV Laddning (Electric Vehicle Charging)
Det här är en webbaserad applikation för att simulera laddning av ett elfordon (EV). Applikationen använder Flask som backend och en enkel HTML/JavaScript frontend för att visualisera batterinivån och interagera med användaren.

Funktioner
Laddning av batteri: Ladda upp batterinivån till en vald nivå (80% eller 100%).
Elpris per timme: Simulera elprisvariationer per timme.
Hushållsförbrukning: Simulera hushållens elförbrukning per timme.
Laddningsinformation: Visa information om laddningens status, inklusive starttid och när laddningen sker med det lägsta elpriset.
Installation
Förutsättningar
För att köra projektet lokalt behöver du följande:

Python 3.x
Flask
Flask-CORS
Steg för att köra projektet
Klona repositoryn:

bash
Copy code
git clone https://github.com/ditt-repo/ev-laddning.git
cd ev-laddning
Installera beroenden: Installera Flask och Flask-CORS med pip:

bash
Copy code
pip install flask flask-cors
Kör backend-servern: Starta Flask-servern:

bash
Copy code
python app.py
Öppna frontend: Efter att servern har startat kan du öppna webbsidan genom att navigera till http://localhost:5000 i din webbläsare.

API Endpoints
GET /priceperhour: Hämtar simulerade elpriser per timme (24 timmar).
GET /household_consumption: Hämtar simulerad hushållsförbrukning per timme (24 timmar).
POST /charge: Startar laddning till en specificerad nivå (t.ex. 80% eller 100%).
GET /get_battery_level: Hämtar den aktuella batterinivån.
Frontend
Frontend är byggt med HTML, CSS och JavaScript och använder fetch-API för att hämta data från backend.

Visar batterinivå: Uppdaterar batteriets nivå visuellt när laddningen pågår.
Elpris och hushållsförbrukning: Visar elpriser och hushållens förbrukning per timme.
Interaktiv laddning: Användaren kan starta och stoppa laddning.
Teknologier
Backend: Python, Flask, Flask-CORS
Frontend: HTML, CSS, JavaScript
API: JSON för dataöverföring mellan frontend och backend.
Bygg och Underhåll
Uppdatera batterinivån och elpriserna genom att justera backend-koden.
Anpassa gränssnittet och interaktionen på frontend för att möta nya krav.
Licens
Detta projekt är licensierat under MIT-licensen. Se LICENSE-filen för mer information.

