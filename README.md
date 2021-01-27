# RailNL

Bij RailNL is het de bedoeling om een zo efficiënt mogelijke lijnvoering te maken tussen alle intercitystations van Nederland. Een lijnvoering is een lijst van verschillende trajecten. Een traject bestaat dan weer uit een lijst met stations. De informatie die hiervoor nodig is zijn alle stations en hun x en y coördinaten en alle connecties tussen de stations met daarbij de tijd die het kost om de connectie te berijden. 


### Gebruik
Om een voorbeeld te genereren van een lijnvoering kan de volgende regel worden aangeroepen:
```
python main.py 
```
Vervolgens worden verschillende inputs gevraagd om te bepalen waar de lijnvoering voor moet worden gemaakt en wat de constraints zijn.
Holland of Nationaal?
Algoritme: Hillclimber of Simulated Annealing?
Tijdsframe: 120 of 180?
Aantal runs randomise?
Aantal runs volgend algoritme?
&nbsp;

### Inhoud van de repository:
#### code
In deze map staat de inhoudelijke code van het resultaten maken in 3 mappen opgedeeld.
##### algorithms 
Hierin staan de verschillende algoritmes die geimplementeerd zijn.
###### randomise.py 
Het randomise algoritme maakt alle trajecten willekeurig. Bij het maken van een traject wordt een willekeurige beginstation gekozen en van daar uit een willekeurige richting naar een volgend station. Dit gaat door totdat het tijdsframe bereikt is of het gekozen station doodlopend is.
###### hillclimber.py
De hillclimber algoritmes hebben als basis een willekeurige lijnvoering. Vervolgens zijn er twee opties: een hele trein aanpassen of een station van een trein. 
Voor optie 1 wordt steeds een traject uit de lijnvoering gepakt en vervangen door een ander traject wat willekeurig is gemaakt. Voor optie 2 wordt steeds uit een willekeurig traject het begin- of eindstations weggehaald. Bij het verwijderen van een beginstation wordt een random extra station aan het einde toegevoegd, bij het verwijderen van een eindstation wordt een random extra station aan het begin toegevoegd. Soms is het begin of eind van een traject doodlopend, dat betekent dat er geen station aan toegevoegd kan worden. 

De scores van de lijnvoering voor en na de vervanging worden berekend en vergeleken. Als de score met het nieuwe traject voor een betere score zorgt, is de vervanging definitief. Als het lager is, wordt de vervanging ongedaan gemaakt. Op die manier worden alle trajecten afgegaan voor ‘n’ aantal keer.
###### simulatedannealing.py
De simulated annealing algoritmes hebben als basis een willekeurige lijnvoering. Hier zijn dezelfde twee opties als bij hillclimber.

Aan het begin wordt een temperatuur vastgesteld, die temperatuur bepaalt of een verandering wordt geaccepteerd of niet. Het kan zijn dat een verslechtering wordt geaccepteerd. Dit gebeurt voor ‘n’ aantal keer.
&nbsp;

##### classes 
###### map.py
Hier worden de trajecten die samen een map vormen, gemaakt. Ook de kwaliteitsscore wordt hiervan berekend. Al deze informatie wordt samengevoegd en in een output bestand gezet. 
###### station.py
Aan de hand van de connections bestand worden alle stations met de daarbij behorende connecties geordend.  
&nbsp;

##### visualisation
Hier Dit bestand zorgt ervoor dat er een kaart van Nederland met daarbij de lijnvoering wordt gemaakt, passend bij de output. Een visualisatie maken kan even duren, zeker m
&nbsp;

#### data
Stationsinformatie over alle intercitystations in Holland en van heel Nederland.  
&nbsp;

#### docs
Het designdocument, een UML met daarin alle classes en algoritmes.  
&nbsp;

#### helpers
Hierin staat functies die heel algemeen zijn  
&nbsp;

#### results
De resultaten van de opdrachten behorend bij de RailNL case staan in deze map opgeslagen. 
&nbsp;

#### main.py
De main vraagt om input van de gebruiker. Er wordt eerst gevraagd met welke files de code gerund moet worden, Holland of Nationaal. Vervolgens mag de gebruiker zelf bepalen hoeveel iterations er worden gedaan. Daarna kies je voor een algoritme en heb je bij HillClimber en Simulated Annealing nog twee opties waar je uit kunt kiezen. Dan zal de code gaan runnen en word op het eind nog gevraagd of een visualisatie bij de lijnvoering moet worden gemaakt.
&nbsp;

#### output.csv
Een bestand die in een specifiek format, met header beginnend, de verschillende trajecten weergeeft die zijn gemaakt. Onderaan de lijst van trajecten staat de score weergegeven die de kwaliteit van de lijnvoering bepaald.  
&nbsp;

#### requirements
Om succesvol de code te draaien zijn in dit bestand alle benodigde packages op een rij gezet. Deze zijn te installeren via:
pip
```
pip install -r requirements.txt  
```
Conda
```
conda install --file requirements.txt 
```
&nbsp;