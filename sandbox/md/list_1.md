# Lista 1. Zdarzenia i prawdopodobienstwo

Ta notatka ma byc materialem do nauki, wiec uzywamy normalnego zapisu matematycznego w Markdown.

## Idea przewodnia

W kazdym zadaniu najpierw odpowiadamy sobie na pytania:

1. Co jest pojedynczym wynikiem eksperymentu?
2. Czy kolejnosc ma znaczenie?
3. Czy losowania sa ze zwracaniem czy bez zwracania?
4. Czy wszystkie wyniki elementarne sa jednakowo prawdopodobne?
5. Czy przestrzen prob jest dyskretna, czy ciagla?

Dopiero potem zapisujemy przestrzen prob i liczymy prawdopodobienstwa.

## Zadanie 1. Rzut moneta

Moneta ma dwa mozliwe wyniki:

- $H$ - heads, czyli orzel
- $T$ - tails, czyli reszka

### 1. Jedno rzucenie

Przestrzen prob:

$$
\Omega_1 = \{H,T\}.
$$

Liczba wynikow elementarnych:

$$
|\Omega_1|=2.
$$

Wynik elementarny to jeden konkretny wynik jednego rzutu, na przyklad $H$.

### 2. Dwa rzuty

Tutaj kolejnosc ma znaczenie, wiec $HT$ i $TH$ to nie jest to samo.

Przestrzen prob:

$$
\Omega_2=\{(H,H),(H,T),(T,H),(T,T)\}.
$$

Liczba wynikow elementarnych:

$$
|\Omega_2|=2\cdot 2=4.
$$

Wynik elementarny to caly uporzadkowany opis dwoch rzutow, na przyklad $(H,T)$.

### 3. Trzy rzuty

Przestrzen prob:

$$
\Omega_3=\{
(H,H,H),(H,H,T),(H,T,H),(H,T,T),
(T,H,H),(T,H,T),(T,T,H),(T,T,T)
\}.
$$

Liczba wynikow elementarnych:

$$
|\Omega_3|=2^3=8.
$$

Wynik elementarny to jedna konkretna sekwencja trzech rzutow, na przyklad $(T,H,T)$.

### Wniosek

Dla $n$ rzutow moneta:

$$
|\Omega_n|=2^n,
$$

bo na kazdym kroku mamy 2 mozliwosci.

## Zadanie 2. Rzut kostka

Kostka szescienna daje wyniki $1,2,3,4,5,6$.

### 1. Jeden rzut

$$
\Omega_1=\{1,2,3,4,5,6\}.
$$

Liczba wynikow:

$$
|\Omega_1|=6.
$$

Wynik elementarny to liczba oczek, na przyklad $4$.

### 2. Dwa rzuty

Przestrzen prob:

$$
\Omega_2=\{(i,j)\colon i,j\in\{1,2,3,4,5,6\}\}.
$$

Nie trzeba wypisywac wszystkich 36 par, ale trzeba rozumiec, ze sa to wszystkie uporzadkowane pary.

Liczba wynikow:

$$
|\Omega_2|=6\cdot 6=36.
$$

Wynik elementarny to jedna konkretna para, na przyklad $(2,5)$.

### 3. Trzy rzuty

$$
\Omega_3=\{(i,j,k)\colon i,j,k\in\{1,2,3,4,5,6\}\}.
$$

Liczba wynikow:

$$
|\Omega_3|=6^3=216.
$$

Wynik elementarny to jedna konkretna trojka, na przyklad $(6,1,4)$.

### Wniosek

Dla $n$ rzutow kostka:

$$
|\Omega_n|=6^n.
$$

## Zadanie 3. Losowanie kart

Pracujemy na standardowej talii 52 kart. Wynikami sa konkretne karty, na przyklad $A\spadesuit$, $10\heartsuit$, $Q\diamondsuit$.

### 1. Jedna karta

Przestrzen prob:

$$
\Omega_1=\text{zbior wszystkich 52 kart z talii}.
$$

Liczba wynikow:

$$
|\Omega_1|=52.
$$

Wynik elementarny to jedna konkretna karta.

### 2. Dwie karty ze zwracaniem

Po pierwszym losowaniu karta wraca do talii, wiec przy drugim losowaniu znow mamy 52 mozliwosci.

$$
\Omega_2=\{(c_1,c_2)\colon c_1,c_2 \text{ sa kartami z talii}\}.
$$

Liczba wynikow:

$$
|\Omega_2|=52\cdot 52=2704.
$$

Wynik elementarny to uporzadkowana para kart, na przyklad $(A\heartsuit,7\clubsuit)$.

### 3. Dwie karty bez zwracania

Po pierwszym losowaniu karta nie wraca do talii, wiec przy drugim losowaniu zostaje 51 mozliwosci.

$$
\Omega_2'=\{(c_1,c_2)\colon c_1\neq c_2\}.
$$

Liczba wynikow:

$$
|\Omega_2'|=52\cdot 51=2652.
$$

Wynik elementarny to uporzadkowana para dwoch roznych kart.

### Najwazniejsza roznica

- ze zwracaniem: mozna wylosowac te sama karte drugi raz
- bez zwracania: nie mozna

To od razu zmienia liczbe wynikow elementarnych i pozniejsze prawdopodobienstwa.

## Zadanie 4. Pogoda w ciagu tygodnia

Kazdego dnia sa trzy mozliwe stany:

- $S$ - sunny
- $C$ - cloudy
- $R$ - rainy

### 1. Jeden dzien

$$
\Omega_1=\{S,C,R\}.
$$

Liczba wynikow:

$$
|\Omega_1|=3.
$$

### 2. Dwa dni

$$
\Omega_2=\{(x,y)\colon x,y\in\{S,C,R\}\}.
$$

Liczba wynikow:

$$
|\Omega_2|=3^2=9.
$$

### 3. Siedem dni

$$
\Omega_7=\{(x_1,x_2,x_3,x_4,x_5,x_6,x_7)\colon x_i\in\{S,C,R\}\}.
$$

Liczba wynikow:

$$
|\Omega_7|=3^7=2187.
$$

Wynik elementarny to caly tygodniowy zapis pogody, na przyklad

$$
(S,C,R,R,S,C,S).
$$

## Zadanie 5. Igla Buffona

To jest pierwsze zadanie, w ktorym przestrzen prob nie jest dyskretna.

W poprzednich zadaniach wynikami byly pojedyncze symbole lub skonczone ciagi symboli. Tutaj wynik eksperymentu opisujemy przez wielkosci geometryczne.

### 1. Co determinuje wynik rzutu?

Jedno polozenie igly mozna opisac przez:

- $x$ - odleglosc srodka igly od najblizszej linii
- $\theta$ - kat miedzy igla a liniami

Korzystajac z symetrii, mozemy przyjac:

$$
x\in\left[0,\frac d2\right],\qquad \theta\in\left[0,\frac\pi2\right].
$$

### 2. Przestrzen prob

$$
\Omega=\left\{(x,\theta)\colon 0\le x\le \frac d2,\ 0\le \theta\le \frac\pi2\right\}.
$$

Jest to prostokat w ukladzie wspolrzednych $(x,\theta)$.

### 3. Dlaczego przestrzen jest ciagla?

Bo $x$ i $\theta$ nie przyjmuja tylko kilku wartosci, ale dowolne wartosci z przedzialow. Mamy wiec nieskonczenie wiele wynikow elementarnych.

## Zadanie 6. Zdarzenia i prawdopodobienstwa dla monety

Moneta jest uczciwa, wiec wszystkie wyniki elementarne sa rownie prawdopodobne.

### 1. Prawdopodobienstwa wynikow elementarnych

Dla jednego rzutu:

$$
P(H)=\frac12,\qquad P(T)=\frac12.
$$

Dla dwoch rzutow:

$$
P((H,H))=P((H,T))=P((T,H))=P((T,T))=\frac14.
$$

Dla trzech rzutow kazdy z 8 wynikow ma prawdopodobienstwo

$$
\frac18.
$$

### Jeden rzut

#### Zdarzenie $A_1$ - wypada orzel

$$
A_1=\{H\},\qquad P(A_1)=\frac12.
$$

#### Zdarzenie $B_1$ - wypada reszka

$$
B_1=\{T\},\qquad P(B_1)=\frac12.
$$

#### Zdarzenie $C_1$ - nie wypada reszka

To po prostu znaczy: wypada orzel.

$$
C_1=\{H\},\qquad P(C_1)=\frac12.
$$

### Dwa rzuty

$$
\Omega_2=\{(H,H),(H,T),(T,H),(T,T)\}.
$$

#### Zdarzenie $A_2$ - dokladnie jeden orzel

$$
A_2=\{(H,T),(T,H)\},\qquad P(A_2)=\frac24=\frac12.
$$

#### Zdarzenie $B_2$ - co najmniej jeden orzel

$$
B_2=\{(H,H),(H,T),(T,H)\},\qquad P(B_2)=\frac34.
$$

Mozna tez szybciej przez dopelnienie:

$$
P(B_2)=1-P((T,T))=1-\frac14=\frac34.
$$

#### Zdarzenie $C_2$ - oba rzuty takie same

$$
C_2=\{(H,H),(T,T)\},\qquad P(C_2)=\frac24=\frac12.
$$

### Trzy rzuty

#### Zdarzenie $A_3$ - dokladnie dwa orly

$$
A_3=\{(H,H,T),(H,T,H),(T,H,H)\},\qquad P(A_3)=\frac38.
$$

#### Zdarzenie $B_3$ - co najmniej jedna reszka

Najwygodniej liczyc przez dopelnienie:

$$
P(B_3)=1-P((H,H,H))=1-\frac18=\frac78.
$$

#### Zdarzenie $C_3$ - wszystkie trzy rzuty takie same

$$
C_3=\{(H,H,H),(T,T,T)\},\qquad P(C_3)=\frac28=\frac14.
$$

#### Przykladowe dodatkowe zdarzenie

Niech

$$
D_3=\text{zdarzenie "pierwszy i trzeci rzut sa takie same"}.
$$

Wyniki sprzyjajace:

$$
(H,H,H),\ (H,T,H),\ (T,H,T),\ (T,T,T).
$$

Zatem

$$
P(D_3)=\frac48=\frac12.
$$

## Zadanie 7. Zdarzenia i prawdopodobienstwa dla kostki

Kazdy wynik elementarny dla uczciwej kostki ma takie samo prawdopodobienstwo.

### 1. Prawdopodobienstwa wynikow elementarnych

- w $\Omega_1$: kazdy wynik ma prawdopodobienstwo $\frac16$
- w $\Omega_2$: kazda uporzadkowana para ma prawdopodobienstwo $\frac1{36}$
- w $\Omega_3$: kazda uporzadkowana trojka ma prawdopodobienstwo $\frac1{216}$

### Jeden rzut

#### $A_1$ - wynik parzysty

$$
A_1=\{2,4,6\},\qquad P(A_1)=\frac36=\frac12.
$$

#### $B_1$ - wynik wiekszy od 4

$$
B_1=\{5,6\},\qquad P(B_1)=\frac26=\frac13.
$$

#### $C_1$ - wynik co najwyzej 3

$$
C_1=\{1,2,3\},\qquad P(C_1)=\frac36=\frac12.
$$

### Dwa rzuty

#### $A_2$ - suma wynikow rowna 7

Pary sprzyjajace:

$$
(1,6),(2,5),(3,4),(4,3),(5,2),(6,1).
$$

Jest ich 6, wiec

$$
P(A_2)=\frac6{36}=\frac16.
$$

#### $B_2$ - oba wyniki sa takie same

$$
(1,1),(2,2),(3,3),(4,4),(5,5),(6,6).
$$

Zatem

$$
P(B_2)=\frac6{36}=\frac16.
$$

#### $C_2$ - suma co najmniej 10

Mozliwe sumy to $10,11,12$.

- suma $10$: $(4,6),(5,5),(6,4)$
- suma $11$: $(5,6),(6,5)$
- suma $12$: $(6,6)$

Razem 6 wynikow, wiec

$$
P(C_2)=\frac6{36}=\frac16.
$$

### Trzy rzuty

#### $A_3$ - suma rowna 10

Szukamy wszystkich uporzadkowanych trojek o sumie $10$. Najlatwiej policzyc najpierw typy nieuporzadkowane:

- $1,3,6$ - daje $3!=6$ permutacji
- $1,4,5$ - daje $6$ permutacji
- $2,2,6$ - daje $\frac{3!}{2!}=3$ permutacje
- $2,3,5$ - daje $6$ permutacji
- $2,4,4$ - daje $3$ permutacje
- $3,3,4$ - daje $3$ permutacje

Razem:

$$
6+6+3+6+3+3=27.
$$

Zatem

$$
P(A_3)=\frac{27}{216}=\frac18.
$$

#### $B_3$ - dokladnie dwa rzuty daja te sama liczbe

To znaczy:

- jedna liczba pojawia sie dwa razy
- trzecia jest inna

Liczymy etapami:

1. wybieramy liczbe powtorzona - $6$ sposobow
2. wybieramy liczbe pojedyncza - $5$ sposobow
3. wybieramy pozycje tej pojedynczej liczby - $3$ sposoby

Czyli:

$$
6\cdot 5\cdot 3=90.
$$

Wobec tego:

$$
P(B_3)=\frac{90}{216}=\frac5{12}.
$$

#### $C_3$ - wyniki zawieraja dwie dwojki i jedna trojke

$$
(2,2,3),\ (2,3,2),\ (3,2,2).
$$

Sa 3 wyniki sprzyjajace, wiec

$$
P(C_3)=\frac3{216}=\frac1{72}.
$$

#### Przykladowe dodatkowe zdarzenie

Niech

$$
D_3=\text{zdarzenie "suma trzech rzutow jest parzysta"}.
$$

Suma jest parzysta, gdy liczba nieparzystych wynikow jest parzysta, czyli:

- albo 0 wynikow nieparzystych
- albo 2 wyniki nieparzyste

Na kostce mamy 3 liczby parzyste i 3 nieparzyste.

Liczba wynikow sprzyjajacych:

- wszystkie 3 parzyste: $3^3=27$
- dokladnie 2 nieparzyste i 1 parzysta: $\binom32\cdot 3^2\cdot 3=3\cdot 9\cdot 3=81$

Razem:

$$
27+81=108.
$$

Zatem

$$
P(D_3)=\frac{108}{216}=\frac12.
$$

## Zadanie 8. Zdarzenia i prawdopodobienstwa przy losowaniu kart

### 1. Prawdopodobienstwa wynikow elementarnych

- w $\Omega_1$: kazda karta ma prawdopodobienstwo $\frac1{52}$
- w $\Omega_2$ ze zwracaniem: kazda uporzadkowana para ma prawdopodobienstwo $\frac1{2704}$
- w $\Omega_2'$ bez zwracania: kazda uporzadkowana para roznych kart ma prawdopodobienstwo $\frac1{2652}$

### Jedna karta

#### $A_1$ - karta jest kierem

W talii jest 13 kierow, wiec

$$
P(A_1)=\frac{13}{52}=\frac14.
$$

#### $B_1$ - karta jest krolem

W talii sa 4 krole, wiec

$$
P(B_1)=\frac4{52}=\frac1{13}.
$$

#### $C_1$ - karta nie jest figura

Figury to $J,Q,K$, czyli 3 rangi, po 4 karty kazda. Lacznie 12 kart figur.

Nie-figur jest:

$$
52-12=40.
$$

Zatem

$$
P(C_1)=\frac{40}{52}=\frac{10}{13}.
$$

### Dwie karty ze zwracaniem

#### $A_2$ - obie karty sa kierami

Losowania sa niezalezne, wiec

$$
P(A_2)=\left(\frac{13}{52}\right)^2=\left(\frac14\right)^2=\frac1{16}.
$$

#### $B_2$ - obie karty maja ten sam rang

Po wylosowaniu pierwszej karty druga musi miec ten sam rang. Dla dowolnej pierwszej karty istnieja 4 takie karty w talii, bo losujemy ze zwracaniem i ta sama karta tez moze wypasc ponownie.

$$
P(B_2)=\frac4{52}=\frac1{13}.
$$

#### $C_2$ - co najmniej jedna karta jest asem

Najwygodniej przez dopelnienie:

$$
P(C_2)=1-\left(\frac{48}{52}\right)^2
=1-\left(\frac{12}{13}\right)^2
=1-\frac{144}{169}
=\frac{25}{169}.
$$

### Dwie karty bez zwracania

#### $A_3$ - obie karty sa kierami

$$
P(A_3)=\frac{13}{52}\cdot\frac{12}{51}=\frac1{17}.
$$

#### $B_3$ - obie karty maja ten sam rang

Po pierwszej karcie zostaja 51 kart, z czego tylko 3 maja ten sam rang, wiec

$$
P(B_3)=\frac3{51}=\frac1{17}.
$$

#### $C_3$ - jedna karta jest krolem, druga dama, w dowolnej kolejnosci

Mamy 4 krole i 4 damy.

Mozliwe uklady uporzadkowane:

- najpierw krol, potem dama
- najpierw dama, potem krol

Liczba wynikow sprzyjajacych:

$$
4\cdot 4\cdot 2=32.
$$

Liczba wszystkich wynikow:

$$
52\cdot 51=2652.
$$

Zatem

$$
P(C_3)=\frac{32}{2652}=\frac8{663}.
$$

#### Przykladowe dodatkowe zdarzenie

Niech

$$
D_3=\text{zdarzenie "obie karty sa czerwone"}.
$$

W talii sa 26 kart czerwonych, wiec

$$
P(D_3)=\frac{26}{52}\cdot\frac{25}{51}=\frac{25}{102}.
$$

## Zadanie 9. Zdarzenia i prawdopodobienstwa dla tygodniowej pogody

Kazdy dzien jest niezalezny i ma trzy rowno prawdopodobne stany:

$$
P(S)=P(C)=P(R)=\frac13.
$$

Wynik tygodniowy to ciag 7 symboli z $S,C,R$.

### $A$ - caly weekend jest sloneczny

Zakladamy, ze chodzi o sobote i niedziele.

Potrzebujemy:

- sobota $S$
- niedziela $S$

Pozostale dni sa dowolne, wiec

$$
P(A)=\left(\frac13\right)^2=\frac19.
$$

### $B$ - sroda, czwartek i piatek sa deszczowe

$$
P(B)=\left(\frac13\right)^3=\frac1{27}.
$$

### $C$ - co najmniej jeden dzien jest sloneczny

To klasyczny przypadek dla dopelnienia.

Latwiej policzyc, ze nie ma ani jednego dnia slonecznego. Wtedy kazdego dnia mamy tylko $C$ albo $R$, czyli prawdopodobienstwo $\frac23$.

$$
P(C)=1-\left(\frac23\right)^7
=1-\frac{128}{2187}
=\frac{2059}{2187}.
$$

### $D$ - ani jednego deszczowego dnia

Kazdego dnia dopuszczalne sa tylko $S$ albo $C$, wiec

$$
P(D)=\left(\frac23\right)^7=\frac{128}{2187}.
$$

### $E$ - dokladnie dwa dni sa sloneczne

To jest model dwumianowy:

- wybieramy 2 dni sloneczne sposrod 7
- na tych dniach mamy $S$
- na pozostalych 5 dniach mamy "nie-$S$", czyli $C$ albo $R$

Zatem

$$
P(E)=\binom72\left(\frac13\right)^2\left(\frac23\right)^5
=21\cdot \frac19\cdot \frac{32}{243}
=\frac{672}{2187}
=\frac{224}{729}.
$$

#### Przykladowe dodatkowe zdarzenie

Niech

$$
F=\text{zdarzenie "dokladnie jeden dzien jest deszczowy"}.
$$

Wtedy

$$
P(F)=\binom71\cdot \frac13\cdot \left(\frac23\right)^6
=7\cdot \frac13\cdot \frac{64}{729}
=\frac{448}{2187}.
$$

## Zadanie 10. Zdarzenia i prawdopodobienstwa w eksperymencie igly Buffona

Zakladamy:

- $L\le d$
- $X$ jest jednostajny na $\left[0,\frac d2\right]$
- $\theta$ jest jednostajny na $\left[0,\frac\pi2\right]$
- $X$ i $\theta$ sa niezalezne

To oznacza, ze na prostokacie

$$
\left[0,\frac d2\right]\times \left[0,\frac\pi2\right]
$$

kazdy obszar ma prawdopodobienstwo proporcjonalne do swojego pola.

Pole calej przestrzeni prob wynosi

$$
\frac d2\cdot \frac\pi2=\frac{d\pi}{4}.
$$

### Warunek przeciecia linii

Igla przetnie linie wtedy i tylko wtedy, gdy

$$
X\le \frac L2\sin\theta.
$$

To jest kluczowy warunek calego zadania.

### $A$ - igla przecina jedna z linii

Szukamy pola pod wykresem

$$
x=\frac L2\sin\theta.
$$

Zatem

$$
P(A)=\frac{1}{d\pi/4}\int_0^{\pi/2}\frac L2\sin\theta\, d\theta.
$$

Liczymy:

$$
P(A)=\frac{4}{d\pi}\cdot \frac L2\int_0^{\pi/2}\sin\theta\, d\theta
=\frac{4}{d\pi}\cdot \frac L2\cdot 1
=\frac{2L}{\pi d}.
$$

To jest klasyczny wzor Buffona.

### $B$ - igla nie przecina zadnej linii

To dopelnienie zdarzenia $A$, wiec

$$
P(B)=1-\frac{2L}{\pi d}.
$$

### $C$ - kat jest mniejszy niz $\frac\pi6$

Poniewaz $\theta$ ma rozklad jednostajny na $\left[0,\frac\pi2\right]$, liczymy po dlugosci przedzialu:

$$
P(C)=\frac{\pi/6}{\pi/2}=\frac13.
$$

### $D$ - srodek igly lezy blizej niz $\frac d4$ od najblizszej linii

Poniewaz $X$ jest jednostajny na $\left[0,\frac d2\right]$,

$$
P(D)=\frac{d/4}{d/2}=\frac12.
$$

### $E$ - igla przecina linie i jednoczesnie ma kat wiekszy niz $\frac\pi4$

Musimy polaczyc dwa warunki:

- $\theta>\frac\pi4$
- $X\le \frac L2\sin\theta$

Zatem

$$
P(E)=\frac{4}{d\pi}\int_{\pi/4}^{\pi/2}\frac L2\sin\theta\, d\theta.
$$

Liczymy calke:

$$
\int_{\pi/4}^{\pi/2}\sin\theta\, d\theta
=[-\cos\theta]_{\pi/4}^{\pi/2}
=1-\frac{\sqrt2}{2}.
$$

Wobec tego

$$
P(E)=\frac{2L}{\pi d}\left(1-\frac{\sqrt2}{2}\right).
$$

#### Przykladowe dodatkowe zdarzenie

Niech

$$
F=\text{zdarzenie "igla przecina linie i ma kat mniejszy niz }\frac\pi6\text{"}.
$$

Wtedy

$$
P(F)=\frac{4}{d\pi}\int_0^{\pi/6}\frac L2\sin\theta\, d\theta.
$$

Po obliczeniu:

$$
P(F)=\frac{2L}{\pi d}\left(1-\frac{\sqrt3}{2}\right).
$$

## Co warto zapamietac z calej listy

1. Najpierw budujemy przestrzen prob, dopiero potem liczymy prawdopodobienstwa.
2. Gdy wyniki elementarne sa rowno prawdopodobne, korzystamy ze wzoru

$$
P(A)=\frac{|A|}{|\Omega|}.
$$

3. W zadaniach wieloetapowych bardzo wazne jest, czy kolejnosc ma znaczenie.
4. W losowaniach kart kluczowa jest roznica miedzy losowaniem ze zwracaniem i bez zwracania.
5. Zdarzenia typu "co najmniej jedno" bardzo czesto najlatwiej liczy sie przez dopelnienie.
6. Nie kazda przestrzen prob jest dyskretna. W geometrii prawdopodobienstwa, jak przy igle Buffona, liczymy przez pola i calki.

## Szybka mapa metod

- moneta, kostka, karty: liczenie wynikow elementarnych
- "dokladnie $k$ sukcesow": schemat kombinatoryczny albo dwumianowy
- "co najmniej jedno": dopelnienie
- modele geometryczne: opis obszaru i liczenie pola

