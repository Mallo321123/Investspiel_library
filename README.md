# Features

## Trading

Alle bereits initialisierten crypto währungen und aktien können gehandelt werden

## Lesen wichtiger informationen

Man kann auch dinge wie kontostand oder besitz einer aktie auslesen

# Installation

## use prebuild library

1. downloade den neusten release

2. führe aus:
   ```
   pip install /path/to/.whl
   ```

## Build it yourself

1. Clone das Repro

2. navigiere zum installations ordner

3. führe aus:
   ```
   python3 -m build
   ```

5. führe aus:
   ```
   pip install dist/*.whl
   ```

# usage

# initialisation

1. import der Bibliothek
```
   from investspielapi.Config import Config
   from investspielapi.Trade import Trade
   from investspielapi.Read import Read
```

2. Initialisieren

   Für diesen schritt braucht man einen session cookie, man kann ihn am besten aus Firefox exportieren.

   um sich die config zu gennerieren, braucht man nur vollgende zeile einfügen:
```
   conf = Config(cookieconsent, ssid, cookie, "**acountid**")
```
   hierbei sollte man cookieconsent und ssid durch den CookieConsent und die EQSESSID ersetzten

   die accountid bekommt man aus der browser debug konsole, wenn man sein depot betritt. (Automatisches auslesen ToDo)
   
3. wenn man nur lesen möchte, muss man nur das read modul initialisieren.
   ```
   Read = Read(conf)
   ```

4. wenn man auch traden will, braucht man auch das trade modul.
   ```
   Trade = Trade(conf)
   ```
   
5. Ab Jetzt ist alles einsatzbereit, und kann genutzt werden
