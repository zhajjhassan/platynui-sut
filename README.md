# PlatynUI SUT – Qt Widgets Showcase
Ein TestSystem für die  [PlatynUI](https://github.com/imbus/robotframework-PlatynUI)
Ein plattformübergreifendes **PySide6-Projekt**, das eine moderne Qt-UI demonstriert (Controls, ListView, TableView, TextEdit).


---

## Voraussetzungen

- **Python ≥ 3.10** (empfohlen 3.12 oder 3.13)  
- **Hatch** installiert  
  ```bash
  pip install hatch
  ```
- Optional: **Qt Designer** (z. B. über Qt Installer)

---

## Installation

Klonen oder herunterladen, dann im Projekt-Root:

```bash
hatch env create
```

Hatch erstellt automatisch die virtuelle Umgebung und installiert alle Dependencies 

---

## Starten der Anwendung

```bash
hatch run start
```

Dieser Befehl:
- aktiviert die Hatch-Umgebung  
- startet `python -m platynui_sut.main`  
- öffnet das Hauptfenster der Widgets-Gallery  

---



## Häufige Befehle (Hatch-Skripte)

| Zweck | Befehl | Beschreibung |
|-------|---------|---------------|
| App starten | `hatch run start` | Startet GUI |
| Tests ausführen | `hatch run test` | Führt Pytest aus |
| Build-Artefakt (EXE) | `hatch run build` | Erstellt Single-File App mit PyInstaller |
| UI-Dateien konvertieren | `pyside6-uic ui/controls_page.ui -o ui/ui_controls_page.py` | Übersetzt Designer-XML → Python |

---

## Beispiel: Projekt bauen

```bash
hatch run build
```

Ergebnis: eine ausführbare Datei (z. B. `platynui_sut.exe`) im `dist/`-Verzeichnis.  
PyInstaller wird dabei über das Hatch-Skript ausgeführt.

---

## Nützliche Hinweise

 
- **Editable UI-Workflow:**  
  1. `.ui`-Datei im Designer öffnen  
  2. Änderungen speichern  
  3. mit `pyside6-uic` neu generieren  

---

## Beispiel: manuell im Hatch-Shell

```bash
hatch shell
python -m platynui_sut.main
```

---

TODOs

* RadioButtons
* Menu/MenuItems
* Tabs
* Tree
* Toolbar
* QML
* uv statt hatch 
