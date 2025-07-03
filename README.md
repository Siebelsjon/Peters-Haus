# Informatik Projekt
## Peters Haus
### Idee
Peters Haus ist ein Anomalie-Spiel, bei welchem der Spieler seine Maus bewegen kann und so einen kleinen ausschnitt des Spielbereich sieht und so unterschiede (=Anomalien) erkennen muss. Nicht bei jeden Level ist eine Anomalie enthalten, wenn dann sind diese Unterschiede meist subtil.

### Ausführung
Pro Level wird ein Raum geladen, dieser kann eine Anomalie enthalten, oder auch nicht, die Aufgabe des Spielers ist es Anomalien zu finden und zu melden. Mein Ziel hierbei war es die Anomalien einfach erweiterbar zu machen, dies habe ich durch das automatische auslesen einer Textdatei erreicht, es muss nur eine oder mehrere texturen dem entsprechenden Ordner hinzugefügt werden und die Textdatei dementsprechend erweitert werden, dies wird noch später genauer erklärt. Der Trick bei diesem Spiel ist jedoch, dass man nie den ganzen Bildschirm sieht sondern nur einen Ausschnitt den man mit der Maus verschieben kann, was es schwieriger macht.

### Spielanweisungen
Das Prgramm Peters haus.py muss geöffnet werden
Peters Haus: Wenn du eine Anomalie siehst drücke: A, wenn nicht dann: W. Du musst es fünfmal hintereinander richtig erraten um zu gewinnen, am anfang ist es immer keine Anomalie. 
Eine Anomalie ist wie folgt definiert: Es muss Abweichungen von dem am anfang gezeigten Raum geben
Das Easter-Egg kann durch drücken von folgenden Buchstaben geöffnet werden: pingu

### Hinzufügen von Anomalien
Wie oben schon erwähnt gehe ich hier auf das Hinzufügen von Anomalien ein. zuerst erstellt man die Anomalie als .png, daraufhin fügt man in der Textdatei in der nächsten Zeile den Namen des Bildes ein (Wichtig: mit der endung), daraufhin kann man Solids hinzufügen (hat aktuell noch keine Funktion, diese kann aber noch hinzugefügt werden. Als nächstest wird True (für Anomlie) eingetragen. Nun kommen die Argumente, dies ist ein Teil von dem ich kein Nutzen machen konnte, jedoch kann man damit Abläufe hinzufügen, das heißt, keine statische Anomalie, sondern eine Handlung. Als Beispiel: Am Anfang alles Normal -> Licht geht aus(Bildschirm wird Schwarz) -> Objekt verschoben.

### Credits
Credits für die Texturen gehen an Pedro


## Drachengames
### Wichtig
Trailer und Werbevideo sind im Release in /Media/Videos

### Idee
Das als Easter-Egg programmierte Spiel kann durch eine Tastenkombination von Peters Haus aus gestartet werden, das Spiel erinnert an eine billige Mischung zwischen SuperTux und dem einen Minispiel auf meinem Tablet.

### Ausführung
Über die Mindestanforderung hinaus werden zahlreiche Erweiterungen implementiert. Das verfügt über ein detailliertes Sounddesign mit hyperrealistischen Schrittgeräuschen auf dem Eis. Sowie einen Todesschrei, der den Moment des Untergangs atmosphärisch unterstreicht. Zudem wurde ein Bomben-Item (Schaufel-Feature) hinzugefügt, das einen zufälliges 2x2 Eisblock-Feld terminiert. Das Eis unter den Spielern zerbricht dabei nicht sofort, sondern durchläuft einen natürlichen Schmelzzyklus. Ergänzt wird das gesamte Spielerlebnis durch die tragende „RESET“ Funktion gefördert, die nach jedem Sturz beide Spieler zufällig auf dem Spielfeld neu positioniert, als auch den Boden erneut vereist. 

### Spielanweisung

__Spieler 1 Mario(blau):__

Fortbewegung = WASD

Bombe zünden = E



__Spieler 2 Peter (rot):__

Fortbewegung = Pfeiltasten

Bombe zünden = M 



__Allgemeine Inputs__

Reset Game = Enter

Spiel schließen = ALT + F4

## Dokumentation
Zuordnungen werden keine vorgenommen da wir immer zusammengearbeitet haben!

### Taskboard
![Taskboard1](https://github.com/user-attachments/assets/54f889de-5f32-4316-a89f-12c12378c419)
![Taskboard2](https://github.com/user-attachments/assets/50d80ac8-b6f3-4388-91e2-cd07066d2003)
![Taskboard3](https://github.com/user-attachments/assets/085533f3-0ca6-49b3-b49b-12351d5ccc17)
![Taskboard4](https://github.com/user-attachments/assets/9ae04a1d-5599-4530-938c-788160103974)
![Taskboard5](https://github.com/user-attachments/assets/4f59507e-c01c-4394-aa3e-d46ebd13ac4f)
![Taskboard6](https://github.com/user-attachments/assets/78c17114-2304-4d0a-a250-c5c5a0df931d)

### Code Erklärung
__Peters Haus__

![Peters Haus - Klassendiagramm](https://github.com/user-attachments/assets/c0833adf-8d2d-4df4-9861-590e608449b8)

__Drachengames__

![Drachengames - Klassendiagramm](https://github.com/user-attachments/assets/03f8f42d-ae3f-4496-937d-cb451de2df6c)


