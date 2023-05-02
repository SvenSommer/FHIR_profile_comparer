# FHIR Profile Comparer

Dieses Projekt bietet ein Python-Script, das verwendet werden kann, um FHIR (Fast Healthcare Interoperability Resources) Profile zu vergleichen.

## Installation

Um das Script auszuführen, benötigen Sie Python 3.7 oder höher. Zusätzlich müssen die erforderlichen Abhängigkeiten installiert werden.

## Verwendung

### Bereitstellen der Dependencies

Im Ordner ./dependencies müssen alle für den Vergleich verwendeten FHIR-Abhängigkeiten hinterlegt sein.
Diese können z.B. mit
```bash
fhir install de.kbv.ita.erp 1.1.0
```
installiert und dann aus dem .fhir/packages Ordner kopiert werden.

### Schreiben der Transitionfiles

Für den Vergliech werden Transitionfiles benötigt, die angeben wie ein Profil in der alten und neuen Version heißt, bzw. ob es gelöscht oder neu hinzugekommen ist.

### Validator

Es muss ein Validator hinterlegt sein und in der compare_from_transitionfile.py entsprechend hinterlegt werden. Hier zu ist der Pfad anzugeben:

```python

validator_path = "/home/..."

```

### Vergleichen

Das Python-Script kann wie folgt verwendet werden:

```bash
python compare_from_transitionfile.py
```

Das Skript vergleicht nun mit Hilfe des Validators die Prfoile, wie sie in der Transitionfile angegeben sind.

### compress_result.py

Das Skript dient zur Erstellung einer Übersichtsseite, die die Ergebnisse eines Vergleichs von FHIR-Profilen darstellt. Es durchsucht ein Verzeichnis mit Vergleichsergebnissen und extrahiert aus jeder HTML-Datei eine Tabelle, die auf der Übersichtsseite angezeigt wird. Außerdem werden alle JSON-Dateien aus dem Vergleichsergebnisverzeichnis kopiert, während HTML-Dateien außer den üblichen Dateien in einem neuen Verzeichnis zusammengefasst werden. Das Skript erstellt schließlich eine neue HTML-Datei namens "index.html" im Verzeichnis "summary", die eine Übersicht über alle Vergleichsergebnisse und deren Tabellen enthält. Darüber hinaus kopiert das Skript auch das res-Verzeichnis, das alle erforderlichen Ressourcen (Bilder, CSS usw.) enthält, in das Verzeichnis "summary".

Das Python-Skript kann wie folgt verwendet werden:

```bash
python compress_result.py <directory_path>
```

`<directory_path>` ist der Pfad zum Verzeichnis, in dem sich die Ergebnisdateien des Profilvergleichs befinden. Das Skript durchsucht das Verzeichnis nach allen CSV-Dateien, kombiniert sie zu einer einzelnen Datei und speichert diese Datei im selben Verzeichnis.

### copy.py

Das `copy.py`-Skript in diesem Repository kann verwendet werden, um alle JSON-Dateien eines Verzeichnisses in ein anderes Verzeichnis zu kopieren.

Das Python-Skript kann wie folgt verwendet werden:

```bash
python copy.py <source_directory> <destination_directory>
```

`<source_directory>` ist das Verzeichnis, das die JSON-Dateien enthält, die kopiert werden sollen, und `<destination_directory>` ist das Verzeichnis, in das die JSON-Dateien kopiert werden sollen. Wenn das Zielverzeichnis nicht existiert, wird es automatisch erstellt.

Angenommen, Sie haben JSON-Dateien im Verzeichnis `/path/to/source` und möchten sie in das Verzeichnis `/path/to/destination` kopieren. Sie können das `copy.py`-Skript wie folgt ausführen:

```bash
python copy.py /path/to/source /path/to/destination
```

Das Skript kopiert alle JSON-Dateien aus dem Verzeichnis `/path/to/source` in das Verzeichnis `/path/to/destination`. Wenn das Zielverzeichnis nicht existiert, wird es automatisch erstellt.

## Beitragende

Dieses Projekt wurde von [Sven Sommer](https://github.com/SvenSommer) erstellt. Wenn Sie das Projekt verbessern möchten, können Sie gerne einen Pull Request erstellen oder mich kontaktieren.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der Datei `LICENSE`.