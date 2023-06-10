# Engeto 2023 projekt 3

Třetí Python projekt - Akademie Engeto
## Popis projektu

Tento projekt slouží k získání výsledků z parlamentních voleb 2017 z webových stránek volby.cz.

## Instalace knihoven

Použité knihovny v tomto projektu jsou uloženy v souboru `requirements.txt.` 
Pro instalaci je vhodné použít nové virtuální prostředí v prostředí VS Code a pomocí terminálu nainstalovat knihovny příkazem:

`pip install -r requirements.txt`

## Spuštění projektu

Celý skript je uložen do souboru `election_scraper.py`. Pro spuštění projektu je třeba využít příkazového řádku v terminálu. Ke spuštění potřebujeme dva argumenty, první argument je URL adresa vybraného územního celku a druhý argument je název csv souboru, do kterého chceme uložit získaná data. Do terminálu musíme zadat příkaz:

`python election_scraper.py <URL adresa uzemniho celku> <nazev csv souboru pro zapsani>
`

## Příklad spuštěného projektu:
Pro ukázku si uvedeme  příklad jak spustit skript a jak vypadá následné spuštění programu.
Pokud chceme vědět například výsledky pro okres Prostějov, do terminálu zadáme:

```
python projekt3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "Prostejov_volby.csv"
```
Po správném spuštění nám program vypíše následující zprávy: 


```
Stahuji data z vybrané URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103

Ukládám výsledky do souboru: Prostejov_volby.csv

Data zapsaná úspěšně do tabulky
```

Částěčný výstup programu, který se zapíše do souboru:

```
kod obce, nazev obce, voliči v seznamu, vydané obálky, platné hlasy,...

589268,	Bedihošť, 834, 527, 524, 51, 0, 0, 28, 1, 13, 123, 2, 2, 14, 1, 0, 34, 0, 6, 140, 0, 0, 26, 0, 0, 0, 0, 82, 1
```

Při špatném zadání příkazu (špatná URL adresa, chybějící argument,...) se nám vypíše upozornění a program je ukončen:

```
Musíte zadat správnou URL adresu a název CSV souboru
---EXIT---
```
