# tsoha-quizworld
Tietokantasovellus

- Sovellukseni on Quiz-World: paikka, jossa voi vastata erilaisiin kyselyihin (tietovisoihin tai mielipidekyselyihin)
- Sovellukseen voi rekisteröityä ja kirjautua sisään
- Käyttäjärooleja on kaksi: normaali käyttäjä ja ylläpitäjä
- Ylläpitäjä voi luoda uusia kyselyitä, sekä muokata ja poistaa olemassa olevia kyselyitä
- Normaali käyttäjä voi vastata kyselyihin ja tutkia niiden tuloksia ja tilastoja
- Tilastoissa voit tutkia vastanneesi tietovisan tuloksia, sekä mielipidekyselyiden tilastoja (ne näkee, ilman että olisi vastannut kyseiseen kyselyyn)

Nykyinen tilanne:
- Rekisteröityminen ja kirjautuminen toimii
- Ylläpitäjä voi luoda, muokata ja poistaa kyselyitä
- Kyselyn luomisessa ensin luodaan pohja (kyselyn tyyppi, aihe, kysymysten ja vastausvaihtoehtojen määrä) ja sitten itse kysely (sen kysymykset ja vastausvaihtoehdot ja tietovisassa onko vastaus tosi/epätosi)
 - Jos kyselyn luomisen aikana tulee virheitä, ne ilmoitetaan samalla sivulla/lomakkeessa (ennen hypättiin "error" sivulle)
- Kun on kirjautunut sisään, etusivulla kerrotaan sovelluksesta ja ylhäällä löytyy valikko: Home, Kyselyt, Tilastot, Asetukset (linkit sivuille)
- Home: sovelluksen etusivu
- Kyselyt: sivulla näkyy sovelluksen kaikki tietovisat ja mielipidekyselyt, linkkiä painamalla pääsee suorittamaan kyseistä kyselyä. Jos on ylläpitäjä, sivulla näkyy myös kuvaileva (ohje)teksti ja linkit "Luo uusi", "Muokkaa" ja "Poista".
  - Luo uusi: luo uusi kysely
  - Muokkaa: valitse mitä kyselyä haluat muokata
  - Poista: valitse minkä kyselyn haluat poistaa
- Tilastot: sivulla näkyy käyttäjän nimi ja rekisteröitymisaika, sekä kyselyt, joita painamalla pääsee tutkimaan kyseisen kyselyn tuloksia/tilastoja.
- Käyttäjä voi vastata kerran kyselyihin, vastaamisen jälkeen näkee suoraan kyselyn tulokset, mutta niitä voi myös jälkikäteen mennä tutkimaan Tilastoista.
- Tietovisan tuloksissa oikea vastaus näkyy vihreänä ja lihavoituna ja käyttäjän oma valinta näkyy valitussa "pallerossa". Mielipidekyselyiden tilastoissa näkyy kuinka monta kappaletta vastauksia on missäkin vaihtoehdossa.
- Asetukset: tämä sivu ei ole vielä toiminnassa, mutta ideana on, että käyttäjä pystyy poistamaan oman käyttäjänsä täältä.

Tässä osoitteessa on toimiva sovellukseni:
https://tsoha-quizworld.herokuapp.com/
