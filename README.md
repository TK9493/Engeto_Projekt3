# Engeto 2021 projekt 3

Třetí Python projekt do Python Akademie na Engetu

## Popis projektu

Tento projekt slouží k získání výsledků z parlamentních voleb 2017z webových stránek volby.cz.

## Instalace knihoven

Použité knihovny v tomto projektu jsou uloženy v souboru `requirements.txt.` 
Pro instalaci je vhodné použít nové virtuální prostředí v prostředí PyCharm a pomocí terminálu nainstalovat knihovny příkazem:

`pip install -r requirements.txt`

## Spuštění projektu

Celý skript je uložen do souboru `election_scraper.py`. Pro spuštění projektu je třeba využít příkazového řádku v terminálu. Ke spuštění je třeba dvou argumentů, první argument je URL adresa vybraného územního celku a druhý argument je název csv souboru, do kterého chceme uložit získaná data. Do terminálu tedy zadáme příkaz:

`python projekt3.py <URL adresa uzemniho celku> <nazev csv souboru pro zapsani>
`

## Praktický příklad spuštěného projektu:
Pro ukázku si uvedeme praktický příklad jak spustit skript a jak vypadá následné spuštění programu.
Zajímají nás třeba výsledky pro okres Prostějov, do terminálu se tedy zadá:

```
python projekt3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "vysledky_prostejov.csv"
```
Po úspěšném spuštění nám program vypíše následující zprávy: 


```
Stahuji data z vybrané URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103

Ukládám výsledky do souboru: vysledky_prostejov.csv

Data zapsaná úspěšně do tabulky
```

Částěčný výstup programu, který se zapíše do souboru:

```
kod obce, nazev obce, voliči v seznamu, vydané obálky, platné hlasy,...

589268,	Bedihošť, 834, 527, 524, 51, 0, 0, 28, 1, 13, 123, 2, 2, 14, 1, 0, 34, 0, 6, 140, 0, 0, 26, 0, 0, 0, 0, 82, 1
```

Při nesprávném zadání příkazu (špatná URL adresa, chybějící argument,...) se nám vypíše upozornění a program je zastaven:

```
Musíte zadat správnou URL adresu a název CSV souboru
---EXIT---
```
