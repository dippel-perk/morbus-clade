## Morbus Clade

A proof of concept for scaling up Sars-Covid-2 testing in Germany. 
Developed as part of the [WirVsWirus](https://wirvsvirushackathon.org/) Hackathon. 
A running demo can be found [here](https://sars-cov2-testing.herokuapp.com/).

### Installation
The website is developed with the django framework.

1. Clone the repository.

2. Install the required dependencies with

    ``pip install -r requirements.txt``

3. Execute the database migrations:

    ``python manage.py migrate``

4. load some initial data into the database
    ``python manage.py loaddata health_system``

5. _optional_: load some dummy fake data for tested persons:
    ``python manage.py loaddata base_data``


### Run

Exceute `python manage.py runserver` to start the webserver.


The follwong text includes the project descirption in German.



## Inspiration

Mit einem exponentiellen Wachstum von Infizierten in dieser Krise, werden schon bald alle Gesundheitsämter in Deutschland keine Kapazitäten mehr haben, um die Testprozesse gewissenhaft und schnell zu organisieren. Unsere Plattform setzt genau an diesem Problem an und hilft den Teststationen Corona Tests schnell durchzuführen sowie Auswertungen und Anfragen des Gesundheitsamts automatisch zu versenden und auszuwerten.

## Aufbau der Seite
Die Seite ist in zwei Bereiche aufgeteilt. Im öffentlichen Bereich können Bürger sich für Tests registrieren und Informationen über das Konzept der Seite einsehen. Der Bereich vom Gesundheitsamt ist nur mit Zugangsdaten erreichbar und bietet eine Übersicht über alle getesteten Personen. Informationen zu Zugangsdaten können auf der Hilfsseite von der Demo gefunden werden.

## Wie soll die Plattform funktionieren?
In diesem Abschnitt wird erläutert, wie die Plattform funktionieren soll, sobald sie **vollständig** implementiert wurde.
### Sich testen lassen
Bürger können weiterhin entscheiden, ob sie sich online oder offline testen lassen möchten. Der online Test mit _Morbus Clade_ bringt jedoch mehrere Vorteile für diejenigen, die eine E-Mail-Adresse besitzen.

Wenn ein Bürger von einem Arzt einen Test verschrieben bekommt, meldet er sich bei der Seite mit einer E-Mail-Adresse an. Die E-Mail-Adresse ist das Hauptkommunikationsmedium im weiteren Prozess. Auf der Startseite befindet sich eine Karte mit Teststationen in der Region, die der Bürger kontaktieren kann. Wenn der Bürger sich nun zu einer Teststation begibt, zeig er vor der Abstrichentnahme den QR-Code, den er/sie nach der Registrierung zugesandt bekommen hat. Die Teststation kann so ohne weitere Datenerfassung direkt eine Probe mit dem Bürger verknüpfen.

Nachdem das Testlabor den Abstrich geprüft hat, wird sie anhand der Identifikationsnummer auf der Probe den Status des Tests für den jeweiligen Bürger auf positiv oder negativ setzen. Sobald die Ergebnisse eingetragen wurden, erhält der Bürger eine E-Mail mit einem Link zur Plattform. Sollte der Bürger positiv getestet worden sein, kann er direkt über diesen Link seine Kontaktpersonen eintragen sowie Aufenthaltsorte auf einer Karte markieren.

### Übersicht vom Gesundheitsamt
Gesundheitsämter, Teststationen und Labore besitzen gesonderte Benutzeraccounts, um Testanfragen zu stellen, Testergebnisse zu aktualisieren sowie Daten von Bürgern einzusehen und zu aggregieren. 

Im Benutzeraccount des Gesundheitsamts werden alle Tests, die von Teststationen in ihrem Bereich erfasst wurden in einer Zusammenfassung angezeigt. Zu jedem (neuen) positiv getesteten Bürger können direkt alle Informationen wie Kontaktpersonen oder Aufenthaltsorte angezeigt werden. Eine aggregierte Ansicht der Aufenthaltsorte erlaubt es dem Gesundheitsamt bestimmte Risikogebiete bzw. Orte an denen sich viele Infizierte aufgehalten haben in einer gesonderten Meldung an die Bürger weiterzugeben. Weiterhin könnten Auswertungen zu Altersgruppen, Anzahl der Kontaktpersonen etc. anhand der Daten automatisch generiert werden. Eine Teilautomatisierte Weiterleitung von Daten an offizielle Stellen wie das RKI sind ebenfalls möglich.

Gesundheitsämter können weitere Labore und Teststationen anlegen. Diese Benutzeraccounts haben als einzige die Berechtigung einen neuen Test anzulegen bzw. den Status eines Tests zu ändern. Das Anlegen und die Statusänderung eines Tests kann automatisch durch das Scannen des QR-Codes (beispielsweise mit einer App) geschehen.

## Das haben wir implementiert

Als Proof of Concept haben wir eine Plattform mit grundlegender Funktionalität erstellt. Die Seite ist momentan noch nicht für Mobilgeräte optimiert (wir bitten um Nachsicht aufgrund der Zeit). Wir haben eine Menge Daten generiert und in die dahinterliegende Datenbank eingespeist. Die Daten könnten unter Umständen teilweise keinen Sinn ergeben.

Wir haben auf der Demo Seite eine Hilfe erstellt, die den Besucher durch die Funktionen der Demo führt. Die Punkte listen wir im Folgenden auf:

### Aus Sicht des Bürgers
Der Bürger besucht die Hauptseite und kann sich dort für einen Test registrieren. Der Ablauf ist wie folgt:

#### 1. Testanmeldung
Begib dich zunächst auf die Testanmeldungs-Seite.

#### 2. Formular ausfüllen

Fülle nun das unten stehende Formular. Damit wirst du für einen bevorstehenden Test registriert. Bitte beachte, dass momentan noch  **keine**  E-Mails versendet werden. Deshalb wirst du direkt zum QR-Code weitergeleitet.

#### 3. Testsimulation

Auf der folgenden Seite befinden sich deine persönlichen Informationen und ein QR-Code. Nun würdest du zur nächstgelegenen Teststation fahren und dort den QR-Code vorzeigen. Das medizinische Personal würde deinen Code scannen und mit der abgegebenen Probe verknüpfen. Um diesen Vorgang in der Demo zu simulieren, drücke einfach den Button im Header der Seite.

#### 4. Warten auf das Ergebnis

Nach Abgeben der Probe an der Teststation, muss man normalerweise das Ergebnis warten. Auf der Website kann man sehen an welcher Teststation die Probe abgegeben wurde und welches Testlabor die Probe auswertet. Sobald das Testlabor die Probe getestet hat, trägt sie das Ergebnis ein und der Bürger bekommt eine Mail mit dem Link zu seinem Testergebnis. Die Analyse der Probe kann in der Demo mit einem Klick auf das jeweilige Testergebnis simuliert werden.

#### 5. Kontaktpersonen hinzufügen

Wenn das Testergebnis positiv war, soll der Bürger seine Kontaktpersonen in ein Formular eintragen. Durch Aufrufen des Links aus der E-Mail öffnet sich eine Seite auf der Kontaktpersonen hinzugefügt werden können. Da wir noch keine E-Mails versenden, wird diese Seite in der Demo automatisch geöffnet, nachdem man das Testergebnis als "positiv" markiert hat.

#### 6. Daten der Kontaktperson angeben

Beim Hinzufügen der Kontaktperson werden die Kontaktdaten der jeweiligen Person angegeben. Weiterhin soll die Intensität des Kontaktes und eine kleine Beschreibung hinzugefügt werden, die die Art des Kontaktes beschreibt.

### Aus Sicht des Gesundheitsamtes

#### 1. Login

Um auf die Verwaltungsseite eines Gesundheitsamtes zuzugreifen, muss man sich zunächst anmelden. Der Link zum Login befindet sich im Footer jeder Seite. Man kann sich mit dem Demo-Account "gesundheitsamt-braunschweig" und dem Passwort "test" einloggen.

#### 2. Übersicht

Nach dem Login gibt es für das Gesundheitsamt eine Übersicht über alle getesteten Personen. Diese Liste kann nach bestimmten Kriterien gefiltert werden. In Zukunft wird es auch noch möglich sein aggregierte Statistiken über die einzelnen Testpersonen einzusehen. Durch Klicken auf eine Testperson gelangt man zur Detailansicht.

#### 3. Detailansicht

In der Detailansicht können die Kontaktdaten und Testergebnisse zu einer Person sowie dessen Kontaktpersonen eingesehen werden.

## Was kommt als Nächstes?
Zuerst werden grundlegende Funktionen, wie der E-Mail Versand und ein Benutzermanagement von Gesundheitsämtern, Laboren und Teststationen benötigt. So können Benutzer momentan noch nicht dynamisch erstellt werden.
Im Anschluss sollte über eine Verschlüsselung der Nutzerdaten nachgedacht werden. Denkbar wäre, dass Gesundheitsämter Schlüssel besitzen, mit denen die Daten der Bürger aus einem bestimmten Gebiet symmetrisch verschlüsselt abgelegt werden können. So würden Daten geschützt sein selbst, wenn ein Unbefugter Zugriff auf den Server erhält.
Als Nächstes werden weitere Features der Plattform, wie eine verbesserte Evaluation der registrierten Fälle und die Möglichkeit bei einem positiven Test, seine zuletzt besuchten Orte auf einer Karte zu markieren eingebaut. Mithilfe dieser Daten kann eine Vielzahl von Diagrammen erstellt werden.

Natürlich muss neben diesen Prozessen eine Akquise von Gesundheitsämtern laufen und Werbung für die Plattform erstellt werden, damit möglichst viele Bürger, die über eine E-Mail-Adresse verfügen, die Plattform auch nutzen können. Nachdem Datenschutzrechtliche fragen geklärt werden, muss evaluiert werden, ob man das Tool für einzelne Anwendungsfälle von bestimmten Ämtern auf dedizierten Servern aufsetzt oder eine Plattform für ganz Deutschland anbietet.

## Über Uns
Wir haben das Projekt am Freitagabend gestartet und etwa 48h sehr intensiv daran gearbeitet. "Wir", sind Jonas Dippel (22) von der TU Berlin und Michael Perk (23) von der TU Braunschweig. Als Informatikstudenten sind wir natürlich immer auf der Suche nach Softwarelösungen für aktuelle Probleme. Der Hackathon war ein schöner Anlass diesen Tatendrang eine Bühne zu geben.
