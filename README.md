# platynui.sut

[![PyPI - Version](https://img.shields.io/pypi/v/platynui-sut.svg)](https://pypi.org/project/platynui-sut)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/platynui-sut.svg)](https://pypi.org/project/platynui-sut)

-----

## Overview

`platynui-sut` ist eine kleine PySide6-Anwendung, die zeigt, wie eine durch Qt
Designer erzeugte Oberfläche über Python mit Logik versehen wird. Das Projekt
liefert eine einfache Main-Window-Demo samt vorkonfigurierten Hatch-Skripten
zum Starten, Testen und Bauen.

## Features

- Qt-Designer-UI (`mainwindow.ui`) mit automatisch generiertem Python-Wrapper.
- Beispiel für Signal/Slot-Verbindungen: Ein Button aktualisiert ein Label.
- Hatch-Skripte für Entwicklungsaufgaben (Starten, Testen, Bauen).
- Bereitstellung als installierbares Python-Paket über PyPI.

## Table of Contents

- [Installation](#installation)
- [Benutzung](#benutzung)
- [Entwicklung](#entwicklung)
- [License](#license)

## Installation

```console
pip install platynui-sut
```

Die Runtime-Abhängigkeiten (u. a. `PySide6`) werden automatisch mitinstalliert.

## Benutzung

### Demo-Fenster starten

```console
python -m platynui_sut.main
```

Alternativ können Sie innerhalb einer Hatch-Shell den Shortcut verwenden:

```console
hatch run start
```

Nach dem Start erscheint das Hauptfenster. Sobald Sie auf den Button klicken,
ändert sich die Beschriftung des Labels auf einen Begrüßungstext.

### Eigenständiges Binary bauen

```console
hatch run build
```

Die erzeugte ausführbare Datei finden Sie anschließend im Unterverzeichnis
`dist/`.

## Entwicklung

1. Abhängigkeiten installieren (empfohlen via [Hatch](https://hatch.pypa.io/)):
   ```console
   hatch shell
   ```
2. Tests ausführen:
   ```console
   hatch run test
   ```
   oder direkt mit `pytest`:
   ```console
   pytest
   ```
3. Statische Typprüfung (optional):
   ```console
   hatch run types:check
   ```

## License

`platynui-sut` wird unter den Bedingungen der
[MIT-Lizenz](https://spdx.org/licenses/MIT.html) veröffentlicht.
