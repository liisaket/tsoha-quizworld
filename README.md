# tsoha-quizworld
<h2>Tietokantasovellus: Quiz-World (lopullinen palautus)</h2>

<h3>Lyhyesti:</h3>
Sovellukseni on Quiz-World: paikka, jossa voi vastata tietovisoihin ja mielipidekyselyihin.<br>
Ylläpitäjänä voi luoda uusia kyselyitä, sekä muokata tai poistaa olemassa olevia kyselyitä.<br>
Tilastoista voi tutkia tehtyjen kyselyiden tuloksia ja tilastoja.

<h3>Tarkemmin toiminnoista:</h3>
<ul>
 <li>Sovellukseen ensin rekisteröidytään tai kirjaudutaan sisään.</li>
<li>Sovelluksessa on kaksi käyttäjäroolia: (normaali) käyttäjä ja ylläpitäjä.</li>
<li>Jos rekisteröinnissä tai kirjautumisessa tapahtuu virhe, virheilmoitus näkyy nyt samalla sivulla sinisellä.</li>
<li>Jos yrittää manuaalisesti mennä sovelluksen sivuille (esim. /quiz/1) eikä ole kirjautunut sisään, virheilmoitus ("Et ole
 kirjautunut sisään") näkyy error-sivulla.</li>
<li>Kun sovellukseen on kirjautunut sisään, etusivulla lukee tervetuloa teksti ja lyhyesti tietoa sovelluksesta.</li>
<li>Sovelluksen yläosassa näkyy valikko: Home, Kyselyt, Tilastot, Asetukset. Niistä klikkaamalla pääsee navigoimaan sovelluksessa.</li>
<li>Home: sovelluksen etusivu</li>
<li>Kyselyt: sovelluksen tietovisat ja mielipidekyselyt (jos jompia kumpia kyselyitä on 0, kyselyn tyypin otsikon alla näkyy
  teksti "Sovelluksessa ei ole tällä hetkellä tietovisoja/mielipidekyselyitä"). Kyselyn voi tehdä vain kerran. Vastaamisen jälkeen näkee heti kyselyn tulokset (voi mennä myös   jälkikäteen tutkimaan niitä Tilastoista). Jos on ylläpitäjä, näkyy pieni ohjeteksti ja linkit "Luo uusi", "Muokkaa", "Poista".</li>
  <ul>
  <li>Luo uusi (kysely): ensin luodaan kyselyn pohja (aihe, kyselyn tyyppi, kuinka monta kysymystä ja vastausvaihtoehtoa), sitten
    luodaan itse kysely (sen kysymykset ja vastausvaihtoehdot ja tietovisoissa onko vastaus tosi/epätosi).
    (Tässä yksi asia, jota en saanut koodattua: se, että esim. jos on kirjoittanut kaikki kysymykset paitsi yhden, ja yrittää luoda kyselyn,
    tulee virheilmoitus ja kaikki edelliset tiedot unohtuvat. Vertaisarvioinneissa yksi ehdotus oli, että vanhat tiedot eivät unohtuisi (ei
    tarvitsisi kirjoittaa kaikkea uudelleen) mutta tosiaan en saanut tätä onnistumaan.)</li>
  <li>Muokkaa (kyselyä): valitse, mitä kyselyä haluat muokata (jos ei valitse mitään, tulee virheilmoitus samalle sivulle)
    -> pääsee muokkaamaan kyselyä. (Muokkauksessa yksi pieni asia mikä jäi korjaamatta: jos on monta vastausvaihtoehtoa,
    (kun kumittaa olemassa olevat vastausvaihtoehdot) numerot näkyy "väärin", pitäisi mennä esim. 1-3 aina per kysymys, mutta
    nyt ne näkyy esim. 1-12 jos vastausvaihtoehtoja on yhteensä 12. Tämä on kuitenkin aika pieni asia, sillä funktio toimii silti oikein
    ja esim. aivan uutta kyselyä luodessa numerot näkyvät oikein.)</li>
  <li>Poista (kysely): valitse, minkä kyselyn haluat poistaa (jos ei valitse mitään, tulee virheilmoitus samalle sivulle).</li>
 </ul>
<li>Tilastot: sivulla näkyy oma käyttäjätunnus ja rekisteröintiaika, sekä kuinka moneen kyselyyn on vastannut.
  Mielipidekyselyiden tilastoja voi tutkia ilman, että olisi vastannut kyseiseen kyselyyn (silloin sivulla näkyy
  asiasta ilmoitus ja linkki kyselyyn, sekä kyselyn tilastot). Tietovisan tuloksia voi tutkia vain, jos on vastannut kyseiseen kyselyyn.
  Jos yrittää nähdä tietovisan tulokset ilman, että on tehnyt kyselyn, tulee virheilmoitus samalle sivulle ja linkki kyselyyn.
  Tietovisan tuloksissa oikea vastaus näkyy lihavoituna ja vihreällä, ja käyttäjän oma valinta näkyy valitussa "pallerossa".
  Mielipidekyselyn tilastoissa näkyy kuinka monta kappaletta vastauksia on missäkin vaihtoehdossa.
  Uutena ominaisuutena nyt myös tietovisan tuloksissa näkyy kuinka monta kappaletta vastauksia on missäkin vaihtoehdossa!</li>
<li>Asetukset: sivulla näkyy oma käyttäjätunnus ja rekisteröintiaika. Sivulta pääsee poistamaan käyttäjätilin.</li>
 <ul>
  <li>Poista käyttäjä: ensin kysytään varmistus, ja jos sitä ei anna, samalle sivulle tulee virheilmoitus. "Poista käyttäjätili" poistaa
    käyttäjän tiedot sekä kirjauttaa käyttäjän ulos.</li>
 </ul>
<li>Csrf-suojaus on otettu huomioon.</li>
</ul>

Tässä osoitteessa oli sovellukseni:
https://tsoha-quizworld.herokuapp.com/</br>
[ei toiminnassa, koska Herokun palvelut eivät ole enää saatavilla]
