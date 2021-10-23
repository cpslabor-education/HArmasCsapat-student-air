# HArmasCsapat-student-air
HármasCsapat csapat - Autonóm és Intelligens Robotok 2021 ősz kurzus
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<HTML>
<HEAD>
<META http-equiv="Content-Type" content="text/html; charset=iso-8859-2">

</HEAD>
<BODY bgcolor=white>



<H1>1.Labor</H1>

<H2>Csapat által elkészített LEGO robot:</H2>

<IMG src="https://raw.githubusercontent.com/robotlabor-education/HArmasCsapat-student-air/main/K%C3%A9pek/1.png"> <IMG src="https://raw.githubusercontent.com/robotlabor-education/HArmasCsapat-student-air/main/K%C3%A9pek/2.png">

<H2>Felhasznált fő építőelemek:</H2>
<UL>
<LI>Szenzorok: giroszkóp a robot kerekeinek tengelye körüli elfordulás mérésére
<LI>Aktuátorok: két darab DC villanymotor a kerekek meghajtására
<LI>Vezérlő modul
<LI>Golyós görgő egyensúlyi stabilitás és borulási védelem szempontjából
</UL>

<H2>Elkészítés szempontjai</H2>
<P>A feladat egy tetszőleges differenciális robot elkészítése volt, ami az jelenti, hogy a robot két
hajtott kerékkel kell, hogy rendelkezzen és mozgását ezen két kerék forgási sebessége
közötti differencia adja meg. Ezt a fő szempontot szemelőtt tartva a csapat alapvető ötlete a
robot működésével kapcsolatban az volt, hogy a robot a két kerekének tengely vonalán
egyensúlyozza magát a talajra merőleges pozíció megtartásával, és ezt a helyzetet
megtartva haladjon minden irányban. Ennek kivitelezése érdekében szükség van a robot
kerekeinek tengelye körüli szögelfordulás mérésére. Erre egy giroszkópot használtunk fel.
Az egyensúlyozás megvalósítása érdekében fontos volt, még hogy a robot súlypontja a
lehető legközelebb helyezkedjen el kerekeinek tengely vonalához. Mivel a vezérlőegység
nagy tömeggel rendelkezik a felhasznált giroszkópot a motorokat és az egyéb alkatrészeit a
robotnak a kerekek tengelyének ellentétes oldalára próbáltuk felszerelni. A stabilitás
érdekében felszereltünk keresztmerevítőket is. Az egyensúlyozást megvalósító szabályozás
beállításához fontos, hogy jól lássuk a kerék elfordulását ezért felszereltünk az oldalukra a
képen látható díszelemeket. Ha esetleg a robot eldőlne a szenzor védelmére felszereltük a
képen látható görgőt, ami emelett segít a robot tömegközéppontjának beállításánál is.</P>

<H2>Felmerülő problémák:</H2>
<UL>
<LI>Mint kiderül a giroszkóp nem az összes tengelye körüli elfordulást méri, hanem csak
a rajta jelölt kiválasztott tengelyét. Ezért a felszereléskor orientációja nem volt
mindegy. Így a felfogatáson kissé el kellet gondolkodnunk és végül feladnunk az
esztétikából egy keveset. Emellet a szenzor stabil felfogatása is fontos volt, mivel ha
az elmozdul az egyensúlyozást irányító szabályozás is félre mehet.
<LI>A vezérlőegység a többi LEGO elemhez képest meglehetősen nehéz, ezért a robot
tömegközéppontját nagyban befolyásolja. Ezért figyelnünk kellett, hogy a többi
felszerelt alkatrész egyensúlyozza azt.
</UL>

<H2>Javítási ötletek</H2>
<UL>
<LI>Mivel a vezérlőegység rendelkezik kijelzővel és vezérlő gombokkal célszerű lenne
azt megfordítani, így könnyebben hozzáférhetőek lennének ezek is.
<LI>A szenzorokat és a motorokat a vezérlő egységgel összekötő vezetékek
esztétikusabb elvezetése
<LI>A felszerelt görgő helyett akár tehetnénk még egy szenzort, ezzel bővítve a robot
tudását.
</UL>

  <H1>2.Labor</H1>

<H2>Feladat:</H2>
<P>Az előző alkalommal elkészített differenciális robot befejezése, tovább fejlesztése.
A Lego Mindstorms EV3 alkalmazással csatlakozás a robot vezérlőjéhez és a robot
építéséhez felhasznált aktuátorok és szenzorok működésének ellenőrzése. A robot
mozgásának tesztelése.</P>

<H2>Csapat robotja a módosítások után:</H2>
<center><IMG src="https://raw.githubusercontent.com/robotlabor-education/HArmasCsapat-student-air/main/K%C3%A9pek/4.png"> <IMG src="https://raw.githubusercontent.com/robotlabor-education/HArmasCsapat-student-air/main/K%C3%A9pek/3.png"></center>

<H2>Elvégzett módosítások:</H2>
<UL>
<LI>Megfordítottuk a vezérlőegységet, ami így jobban hozzáférhető és a kijelző is jobban
látszik.
<LI>Leszereltük a golyós görgőt, mivel ha a robotnak szüksége lenne rá lényegében
értelmét vesztené az egyensúlyozás koncepciója.
<LI>Helyette előre és hátulra is kinyúló védelmi elemeket szereltünk a képernyő és a
giroszkóp szenzor megóvása érdekében.
<LI>A robot hátuljára (amint az alsó képeken látszik is) kábel sorolót szereltünk, hogy a
vezetékek ne érjenek a talajhoz és esztétikailag is rendezettebben nézzenek ki.
</UL>

<H2>A feltöltött első programunk:</H2>
<P>A csapat által elsőnek feltöltött program a motorok és a giroszkóp szenzor működésének
megismerésére szolgált számunkra. Megismerkedtünk a Lego Mindstorms EV3
programozási felülettel. Megfigyeltük, hogy a giroszkóp milyen pontossággal és milyen
stabilan méri a robot elfordulási szögét. Majd a szenzor adatok felhasználásával egy nagyon
egyszerű, az egyensúlyozás megvalósítására alkalmatlan, if statementekből álló programot
írtunk. A lényeg annyi volt, hogy megtaláljuk a robot súlypontját, majd az ettől való
eltéréseket figyeltük a giroszkóppal. Ha egy két fokkal dőlni kezdett a robot ellen próbáltunk
tartani a motorokkal. Megfigyeltük a motorok által kifejtett nyomatékot és próbáltuk
optimálisra állítani. Ezzel a módszerrel természetesen nem tartotta meg a robot stabilan az
egyensúlyát, de volt amikor egészen közel állt és a súlypontja körül dülöngélt oda-vissza.
Ennek kiküszöbölésére természetesen egy megfelelő szabályozó megírására lesz
szükségünk.</P>

<H2>Felmerülő problémák:</H2>
<UL>
<LI>A végrehajtott módosításokkal, főleg a vezérlő megfordításával és a golyós görgő
leszerelésével a robot súlypontja kissé hátra tolódott, így az egyensúlyozás
megvalósítása kissé nehézkesebb lesz.
<LI>A Lego szoftver eddig általunk megismert részével nem tudjuk, hogyan kivitelezhető
egy szabályozás megvalósítása. Feltételezzük, hogy erre majd python nyelvben lesz
lehetőségünk.
</UL>
  
</BODY>
</HTML>
