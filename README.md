# RailNL

### Gebruik
Om een voorbeeld te genereren van een lijnvoering kan de volgende regel worden aangeroepen:
```python main.py runserver```

### Inhoud van de repository:
#### code
In deze map staat de inhoudelijke code van het resultaten maken in 3 mappen opgedeeld.
##### algorithms 
Hierin staan de verschillende algoritmes die geimplementeerd zijn.
###### randomise.py 
Het random algoritme kiest tijdens het maken van een traject steeds een willekeurige richting vanuit een bepaald station.
De resultaten die hier uit voort komen zijn dan ook niet 'slim'. 
##### classes 
###### map.py
Hier worden de trajecten die samene en map vormen gemaakt. Ook de kwaliteitsscore wordt hiervan berekend. Al deze informatie wordt samengevoegd en in een output bestand gezet. 

###### station.py
Aan de hand van he connections bestand worden alle stations met de daarbij behorende connecties geordend.

##### visualisation
###### visualise.py
Dit bestand zorgt ervoor dat er een kaart van Nederland met daarbij de lijnvoering wordt gemaakt.

#### data
##### Holland
Alleen stationinformatie over de de intercitystations in Noord- en Zuid-Holland. 
##### Nationaal
Stationsinformatie over alle intercitystations in heel Nederland.

#### docs
##### design.uxf
Het designdocument, een UML met daarin alle classes en algoritmes.

#### results
De resultaten van de opdrachten behorend bij de RailNL case staan in deze map opgeslagen. In `main.py` staat hoe elk van deze opdrachten tot stand zijn gekomen.

#### main.py
De main roept de bestanden aan met de inhoudelijke code om zo tot resultaten te komen. 

#### output.csv
Een bestand die in een specifiek format, met header beginnend, de verschillende trajecten weergeeft die zijn gemaakt. Onderaan de lijst van trajecten staat de score weergegeven die de kwaliteit van de lijnvoering bepaald.

#### requirements.txt
Om succesvol de code te draaien zijn in dit bestand alle benodigde packages op een rij gezet. 
```pip install -r requirements.txt```
