# RailNL

Bij RailNL is het de bedoeling om een zo efficiënt mogelijke lijnvoering te maken tussen alle intercitystations van Nederland of Holland. Een lijnvoering is een lijst van verschillende trajecten. Een traject bestaat dan weer uit een lijst met stations. De informatie die hiervoor nodig is zijn alle stations en hun x en y coördinaten en alle connecties tussen de stations met daarbij de tijd die het kost om de connectie te berijden. 
Om de kwaliteit van de lijnvoering te bepalen wordt rekening gehouden met het aantal bereden connecties. Het aantal trajecten die je hebt opgesteld, dus het aantal treinen dat rijdt. Het aantal minuten wat alle treinen in totaal samen rijden.
De uitdaging is om zoveel mogelijk connecties te berijden met zo min mogelijk trajecten in zo min mogelijk tijd.



### Gebruik
Om een voorbeeld te genereren van een lijnvoering kan de volgende regel worden aangeroepen:
```
python main.py 
```
Vervolgens worden verschillende inputs gevraagd om te bepalen waar de lijnvoering voor moet worden gemaakt en wat de constraints zijn.
Bestand: Holland of Nationaal?
Aantal iteraties?
Algoritme: Randomise, Hillclimber of Simulated Annealing?
Voor Hillclimber en Simulated Annealing:
Verandering: een hele trein of stations?
Voor Simulated Annealing:
Temperatuur: zelf bedacht temperatuur of zelf bepaalde temperatuur?
Visualisatie?

&nbsp;

### Inhoud van de repository:
#### code
In deze map staat de inhoudelijke code van het resultaten maken in 3 mappen opgedeeld.
##### algorithms 
Hierin staan de verschillende algoritmes die geimplementeerd zijn. Randomise, HillClimber en Simulated Annealing.
###### randomise.py 
Het randomise algoritme maakt een lijnvoering waarbij alle trajecten willekeurig zijn. Bij het maken van een traject wordt een willekeurige beginstation gekozen en van daar uit een willekeurige richting naar een volgend station. Er worden steeds nieuwe stations aan het traject toegevoegd totdat het tijdsframe bereikt is of het gekozen station doodlopend is. Het aantal trajecten dat wordt gemaakt is ook willekeurig.
###### hillclimber.py
De hillclimber algoritmes hebben als basis een willekeurige lijnvoering. Vervolgens zijn er twee opties: een hele trein aanpassen of een station van een trein. 
Voor optie 1 wordt steeds een traject uit de lijnvoering gepakt en vervangen door een ander traject die willekeurig is gemaakt. Voor optie 2 wordt steeds uit een willekeurig traject gekozen, daarbij wordt het begin- of eindstations weggehaald. Als een station wordt weggehaald aan het begin, wordt een random extra station aan het einde toegevoegd. Bij het verwijderen van een eindstation wordt een random extra station aan het begin toegevoegd. De plaats van verwijdering en toevoeging van stations wordt gebaseerd op of het eind of begin van een traject doodlopend is, dat betekent dat er geen station aan toegevoegd kan worden. Dan wordt dus aan de andere zijde een station toegevoegd.

De scores van de lijnvoering voor en na de vervanging worden berekend en vergeleken. Als de score met het nieuwe traject voor een betere score zorgt, is de vervanging definitief. Als het lager is, wordt de vervanging ongedaan gemaakt. Op die manier worden alle trajecten afgegaan voor ‘n’ aantal keer.
###### simulatedannealing.py
De simulated annealing algoritmes hebben als basis een willekeurige lijnvoering. Hier zijn dezelfde twee opties als bij hillclimber.

#################iets meer over temperatuur################Aan het begin wordt een temperatuur vastgesteld, die temperatuur bepaalt of een verandering wordt geaccepteerd of niet. Het kan zijn dat een verslechtering wordt geaccepteerd. Dit gebeurt voor ‘n’ aantal keer.
&nbsp;

##### classes 
###### map.py
Hier worden de trajecten die samen een map vormen, gemaakt. Ook de kwaliteitsscore wordt hiervan berekend. Al deze informatie wordt samengevoegd en in een output bestand gezet. De outputs zijn te vinden in de map 'results'.
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
De resultaten van de opdrachten behorend bij de RailNL case staan in deze map opgeslagen. Daarnaast komen de output files in deze map terecht. Output1 weergeeft de willekeurige lijnvoering, output2 weergeeft de verbeterde lijnvoering. Zo is te zien wat hoe de lijnvoering verandert is door de algoritmes.
&nbsp;

#### main.py
Om de algoritmes te runnen is er main.py. De main vraagt om input van de gebruiker. 
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