Arduino + python + web sensor-plotting
======================================

Dette systemet består av 3 hovedkomponenter:

* ``arduino_reader/`` - Programvare som kjører på en arduino for å lese sensor-input, konvertere dette og videresende over serieport
* ``serial-to-*.py`` - Et knippe Python3-program som kjører fra en datamaskin, leser data fra en serieport og gjør ulike ting med det
  * ``serial-to-terminal.py`` - skriver de leste verdiene direkte til terminal
  * ``serial-to-plot.py`` - plotter verdiene ved hjelp av matplotlib (krever at matplotlib er tilgjengelig)
  * ``serial-to-file.py`` - skriver verdiene til en fil slik at de f.eks. kan brukes av ``plot.html``
* ``plot.html`` - Webside som leser inn datapunkter fra 1-4 filer og plotter de ut som en graf

Programmering av Arduino
----

Åpne prosjektet ``arduino_reader/`` i Arduino IDE2 og trykk "Upload". Obs; sikre at kortet er koblet korrekt til datamaskinen, og korrekt port er konfigurert i IDE2.


Kjøring av Python-script
----

``serial-to-file.py`` tar som kommandolinjeargumenter hvilken serieport den skal lese fra, hvilken baudrate dataene kommer på og hvilken fil den skal skrive resultatene til:

Avhengig av operativsystem og hvilken port det er tilkoblet så kan serieport variere.

For Windows er navnet typisk ``"COM"`` etterfulgt av et nummer. For WSL på Windows kan en finne tilsvarende port som ``"/dev/ttyS"`` etterfulgt av samme nummer. For macOS er denne ``/dev/tty.`` (TODO: Avklar).

F.eks: ``serial-to-file.py /dev/ttyS3 9600 results.txt``

``serial-to-terminal.py`` og ``serial-to-plot.py`` tar ingen argumenter ved kjøring, men er avhengige av at riktig serieport er angitt i koden.

Alle Python-scriptene er avhengig av Python3 og biblioteket [PySerial](https://pyserial.readthedocs.io/en/latest/shortintro.html).

``serial-to-plot.py`` er avhengig av [matplotlib](https://matplotlib.org/).

For å installere avhengigheter:

    pip3 install PySerial matplotlib




Visning av plot med plot.html
----

Plot-bibliotek: [Chart.js](https://www.chartjs.org/)

Ved å kjøre ``./launch_httpserver.sh`` vil det startes en enkel webserver som serverer gjeldende mappe som http://localhost:8080/

Dermed så ved å gå til [``http://localhost:8080/plot.html?file=results.txt``](http://localhost:8080/plot.html?file=results.txt) så skal resultatene fra målingene vises (gitt at de er lagret til ``results.txt``).

Du kan legge til flere plots som skal vises samtid ved å legge til ``&file=annenfil`` på slutten av URLen.

