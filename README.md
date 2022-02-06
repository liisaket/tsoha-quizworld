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
- Sovelluksen etusivulla (kun on kirjautuneena sisään) näkyy kuinka monta kyselyä on olemassa, ja linkit niihin.
- Käyttäjä voi vastata kyselyihin, ja sen jälkeen näkee kyselyn tulokset (pitää vielä muokata results.html sivua, että tietovisan tuloksissa
  näkyy mikä oli oikea vastaus).
- Olen tyytyväinen ulkonäköön ja sovellus toimii jo aika hyvin.

https://tsoha-quizworld.herokuapp.com/

En saanut vielä sovellusta näkymään Herokussa (heroku komentorivi ei toimi jostain syystä, ja Herokun manuaalinen käyttäminen selaimessa
on vielä aika hankalaa.), mutta otin näyttökuvia sovelluksesta:

![Näyttökuva 2022-02-06 225729](https://user-images.githubusercontent.com/95650016/152701380-23fedc90-2727-4b6f-b2a9-dbbe532f0a5b.png)

![rekisteröinti](https://user-images.githubusercontent.com/95650016/152701383-1ccce6ec-e9ff-4d2b-abf7-3627fd91d6d7.png)

![Näyttökuva 2022-02-06 225833](https://user-images.githubusercontent.com/95650016/152701391-187286c1-aef7-4f32-ae9d-d416746d11f3.png)

![Näyttökuva 2022-02-06 225911](https://user-images.githubusercontent.com/95650016/152701405-a654535e-902d-4830-acb3-3380ec8742f2.png)

![Näyttökuva 2022-02-06 225946](https://user-images.githubusercontent.com/95650016/152701408-5d8c4fb5-a8bc-40cc-a849-a3b80a78a85b.png)

![Näyttökuva 2022-02-06 230016](https://user-images.githubusercontent.com/95650016/152701416-48205587-8774-42eb-b29e-6f899d41a8be.png)

![Näyttökuva 2022-02-06 230031](https://user-images.githubusercontent.com/95650016/152701426-6e22a272-0cae-4ac3-9643-d3139b01efbf.png)

![Näyttökuva 2022-02-06 230047](https://user-images.githubusercontent.com/95650016/152701429-df17fb80-0126-40ab-97ca-5c13b1e73f2d.png)

![Näyttökuva 2022-02-06 230111](https://user-images.githubusercontent.com/95650016/152701436-35b58eff-3b93-4afa-a547-c15a03bfe7a5.png)

![Näyttökuva 2022-02-06 230135](https://user-images.githubusercontent.com/95650016/152701450-1f412bff-7f30-4f43-b6ed-878c6adc8c22.png)

![Näyttökuva 2022-02-06 230230](https://user-images.githubusercontent.com/95650016/152701455-94336bc9-1c3c-4b8b-acc7-c67aca92ebf1.png)

![Näyttökuva 2022-02-06 230246](https://user-images.githubusercontent.com/95650016/152701471-acb13c7e-cfea-4443-8e9a-892898fafa81.png)

![Näyttökuva 2022-02-06 231050](https://user-images.githubusercontent.com/95650016/152701501-8cee3f86-a5f1-4a4c-9326-28dc198e43d4.png)
