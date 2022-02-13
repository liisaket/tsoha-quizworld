# tsoha-quizworld
Tietokantasovellus

- Sovellukseni on Quiz-World: paikka, jossa voi vastata erilaisiin kyselyihin (tietovisoihin tai mielipidekyselyihin).
- Sovellukseen pitää kirjautua sisään, jotta kyselyt voi nähdä.
- Sovellukseen voi rekisteröityä, käyttärooleja on 2 (normaali käyttäjä ja ylläpitäjä).
- Ylläpitäjä voi luoda uusia kyselyitä.
- Kun on kirjautunut sisään, voi vastata kyselyihin tai tutkia tilastoja.
- Tietovisan kysymyksissä on aina edes yksi oikea vastaus, mutta mielipidekyselyssä mikä tahansa vastaus on oikein.
- Tilastot: kuinka moneen kyselyyn käyttäjä on vastannut, tietovisat: kuinka moni vastaus on mennyt oikein/väärin,
            mielipidekyselyt: kuinka monta kappaletta vastauksia on jokaiselle vastausvaihtoehdolle.
            (Esim. Paras vuodenaika: Kevät: 1 kpl, Kesä: 5 kpl, Syksy: 0 kpl, Talvi: 2 kpl)

Nykyinen tilanne:
- Sovellukseen voi kirjautua sisään ja rekisteröityä, joko normaalina käyttäjänä tai ylläpitäjänä.
- Ylläpitäjä voi luoda uuden kyselyn: joko tietovisan, jossa on oikeita tai vääriä vastauksia, tai mielipidekyselyn,
  jossa ei ole vääriä vastauksia. Ensin kyselylle luodaan pohja (kyselyn tyyppi, aihe, montako kysymystä ja vastausvaihtoehtoa) ja
  sitten luodaan itse kysely (sen kysymykset ja vastausvaihtoehdot).
- Kun on kirjautunut sisään, etusivulla näkyy "valikko": Home, Kyselyt, Tilastot, (ja jos on ylläpitäjä niin Luo uusi kysely).
  Linkeistä painamalla pääsee sivuille:
- Home-linkistä pääsee etusivulle.
- Kyselyt-linkistä pääsee kyselyt-sivulle näkyy sovelluksen kaikki tietovisat ja mielipidekyselyt, joita painamalla
  pääsee suorittamaan kyselyitä.
- Tilastot-linkistä pääsee tilastoihin, jossa näkyy käyttäjän nimi ja aika, jolloin käyttäjä rekisteröityi sovellukseen. Siellä näkyy myös kyselyt, joita painamalla
  pääsee tutkimaan kyselyiden tuloksia.
- Käyttäjä voi vastata kyselyihin, ja sen jälkeen näkee kyselyn tulokset. Tietovisan tuloksissa oikea vastaus näkyy vihreänä ja lihavoituna,
  ja käyttäjän oma valinta näkyy valitussa "pallerossa". Mielipidekyselyissä näkyy kuinka monta kappaletta vastauksia on missäkin vaihtoehdossa.
- Myös virheihin on kiinnitetty huomiota, esim. jos kyselylle ei anna nimeä, hypätään Virhe-sivulle, jossa kerrotaan mikä meni pieleen, yms.
- Palaa takaisin- nappulasta pääsee aina takaisin edelliselle sivulle.
- Olen tyytyväinen ulkonäköön ja sovellus toimii jo aika hyvin.

Tässä osoitteessa on toimiva sovellukseni:
https://tsoha-quizworld.herokuapp.com/

Tällä ylläpitäjä-käyttäjällä voi luoda uusia kyselyitä (saa myös luoda oman ylläpitäjä-käyttäjän):
- tunnus: admin
- salasana: admin123
