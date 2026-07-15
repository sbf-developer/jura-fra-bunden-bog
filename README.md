# Jura fra bunden

En dansk, selvstændig introduktionsbog om jura. Bogen er skrevet til læsere uden juridisk forhåndsviden, men bevarer den juridiske disciplin ved at skelne mellem regler, fortolkning, bevis, vurdering og konkrete råd.

## Indhold

- `main.tex` - hovedfilen og bogens design
- `chapters/` - bogens kapitler og appendices
- `figures/` - genbrugelige TikZ-figurer
- `references.bib` - bibliografisk database
- `scripts/` - små kontrolscripts
- `output/pdf/` - den byggede PDF

## Byg bogen

Kræver en TeX-installation med XeLaTeX, BibTeX og de pakker, der bruges i `main.tex`.

```bash
make
python3 scripts/check_book.py
```

Hvis der skal bygges fra en ren mappe:

```bash
make clean
make
```

## Afgrænsning

Bogen tager udgangspunkt i dansk ret og forklarer, hvordan EU-retten og Den Europæiske Menneskerettighedskonvention påvirker den danske retsorden. Den er introduktionsstof og ikke konkret juridisk rådgivning. Love, praksis og myndighedsvejledninger kan ændre sig; ved en konkret sag skal den gældende tekst og eventuel professionel rådgivning altid kontrolleres.

## Redaktionsnotat

Kildelinks i bogen peger primært på Retsinformation, EUR-Lex, Den Europæiske Menneskerettighedsdomstol, Datatilsynet og Domstolene. Kilderne er kontrolleret 15. juli 2026. Referencer til bestemte paragraffer er illustrative og må ikke læses som en udtømmende gengivelse af gældende ret.
