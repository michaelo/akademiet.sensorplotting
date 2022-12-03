Arduino + python + web sensor-plotting
======================================

Dette systemet består av 3 hovedkomponenter:

* ``arduino_reader/`` - Programvare som kjører på en arduino for å lese sensor-input, konvertere dette og videresende over serieport
* ``main.py`` - Python3-program som kjører fra en datamaskin, leser data fra en serieport og lagrer unna det den mottar til en lokal fil - en linje pr måling
* ``plot.html`` - Webside som leser inn datapunkter fra 1-4 filer og plotter de ut som en graf

Programmering av Arduino
----
TODO


Kjøring av main.py
----
TODO


Visning av plot
----
TODO



TODO
----
* Oppdater plot.html til å ta GET-argumenter for å angi hvilke datafiler som skal leses
* Oppdater main.py til å ta device, baud og output-fil som explisitte argumenter