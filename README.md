Arduino + python + web sensor-plotting
======================================

Dette systemet består av 3 hovedkomponenter:

* ``arduino_reader/`` - Programvare som kjører på en arduino for å lese sensor-input, konvertere dette og videresende over serieport
* ``main.py`` - Python3-program som kjører fra en datamaskin, leser data fra en serieport og lagrer unna det den mottar til en lokal fil - en linje pr måling
* ``plot.html`` - Webside som leser inn datapunkter fra 1-4 filer og plotter de ut som en graf

Programmering av Arduino
----

Åpne prosjektet ``arduino_reader/`` i Arduino IDE2 og trykk "Upload". Obs; sikre at kortet er koblet korrekt til datamaskinen, og korrekt port er konfigurert i IDE2.


Kjøring av main.py
----

main.py tar som kommandolinjeargumenter hvilken serieport den skal lese fra, hvilken baudrate dataene kommer på og hvilken fil den skal skrive resultatene til:

Avhengig av operativsystem og hvilken port det er tilkoblet så kan serieport variere.

For Windows er navnet typisk ``"COM"`` etterfulgt av et nummer. For WSL på Windows kan en finne tilsvarende port som ``"/dev/ttyS"`` etterfulgt av samme nummer. For macOS er denne ``/dev/tty.`` (TODO: Avklar).

F.eks: ``main.py /dev/ttyS3 9600 results.txt``

main.py er avhengig av Python3 og biblioteket [PySerial](https://pyserial.readthedocs.io/en/latest/shortintro.html).


Visning av plot
----

Plot-bibliotek: [Chart.js](https://www.chartjs.org/)

Ved å kjøre ``./launch_httpserver.sh`` vil det startes en enkel webserver som serverer gjeldende mappe som http://localhost:8080/

Dermed så ved å gå til [``http://localhost:8080/plot.html?file=results.txt``](http://localhost:8080/plot.html?file=results.txt) så skal resultatene fra målingene vises (gitt at de er lagret til ``results.txt``).

Du kan legge til flere plots som skal vises samtid ved å legge til ``&file=annenfil`` på slutten av URLen.

