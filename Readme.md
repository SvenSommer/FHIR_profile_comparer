# FHIR Profile Comparer

Dieses Projekt bietet ein Python-Script, das verwendet werden kann, um FHIR (Fast Healthcare Interoperability Resources) Profile zu vergleichen. 

## Installation

Um das Script auszuführen, benötigen Sie Python 3.7 oder höher. Zusätzlich müssen die erforderlichen Abhängigkeiten installiert werden.

## Verwendung

Das Python-Script kann wie folgt verwendet werden:

```bash
python compare_profiles.py <path_to_profile_1> <path_to_profile_2>
```

Die beiden Profile müssen in JSON-Format vorliegen. Das Script vergleicht dann die Ressourcen-Definitionen und gibt eine Zusammenfassung der Unterschiede aus.

### compress_result.py

Das `compress_result.py`-Skript in diesem Repository kann verwendet werden, um die Ergebnisse eines FHIR-Profilvergleichs in eine einzelne CSV-Datei zu komprimieren.

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