# Sistem-de-recunoastere-a-amprentelor-digitale
Un sistem biometric de recunoastere a amprentelor digitale este organizat in patru etape principale: 
introducerea amprentelor
extragerea caracteristicilor amprentelor
etapa de comparare cu setul de amprente din baza de date(comparaţii de tipul 1: N)
ultima etapa aceea de a decide daca existao potrivire cu o inregistrare din setul de date. 

În figura următoare este prezentată schema logică și structura proiectului. Este ilustrată, de asemenea,
adaugarea unei noi amprente în baza de date și ștergerea unei înregistrări.

![image](https://github.com/ddaci/Recunoastere_amprenta_digitala/assets/148542192/b6c8da89-8707-4525-b1e6-acb9a7b9af58)



Interfața grafica a aplicatiei(GUI) este construita cu ajutorul bibliotecii Tkinter și arată așa:

![1](https://github.com/ddaci/Recunoastere_amprenta_digitala/assets/148542192/69f31409-ada8-4967-bf18-71a3445c7dd7)


Am definit trei cadre (frame1, frame2, frame3) pentru organizarea interfeței grafice și am încărcat
imagini de fundal pentru fiecare cadru. Frame 1 este partea care conține logo-ul si frame 2 este 
partea care conține cele 4 butoane mai sus menționate. Frame 3 permite afișarea rezultatului căutarii
amprentei in baza de date și conține și 2 butoane, butonul Înapoi care permite revenirea la frame 2 
și butonul de Ieșire din aplicație. Fiecare din cele 6 butoane din aplicație are implementată funcționalitatea hover.

Detectia minutiilor utilizand algoritmul SIFT
Cea mai incontestabilă caracteristică constituțională a amprentei digitale este modelul său de creste,
margini și bifurcații(minutiile). Aceste caracteristici sunt folosite pentru a compara o amprentă
digitală cu altele. Există mai multe algoritmi pentru detectarea caracteristicilor. În ceea ce privește
recunoașterea amprentelor digitale, se pot  implementa algoritmi precum Scale-Invariant Feature Transform (SIFT),
algoritmul Speeded-Up Robust Features (SURF), algoritmul Oriented FAST Rotated BRIEF (ORB) și algoritmul 
Binary Robust Invariant Scalable Keypoints (BRISK).
SIFT este un algoritm utilizat în prelucrarea imaginilor și recunoașterea de obiecte. Acest algoritm 
a fost dezvoltat pentru a detecta și extrage caracteristici distinctive din imagini, caracteristici
care sunt invariant la schimbarea scară sau la rotație. Aceste caracteristici sunt esențiale pentru 
compararea și potrivirea obiectelor în imagini, indiferent de variațiile de perspectivă, iluminare 
sau distorsiuni. Punctele-cheie identificate de SIFT sunt selectate astfel încât să fie reprezentative 
și distinctive pentru obiectele din imagine. 

Algoritmul SIFT urmează câțiva pași cheie:
•Detectarea extremităților în spațiu-scală: Algoritmul utilizează funcții Gaussian pentru
a identifica puncte de interes potențiale din imagine, care sunt invariant la schimbarea scară și rotație.
•Localizarea punctelor-cheie: Se determină locația și scala fiecărui punct-cheie identificat în etapa 
anterioară. Atribuirea orientării: Se atribuie o orientare fiecărui punct-cheie bazat pe direcțiile locale 
ale gradientului imaginii.
•Crearea descriptorului: Pentru fiecare punct-cheie, se creează un descriptor care reprezintă direcțiile 
gradientului într-o zonă înconjurătoare. Acești descriptori sunt utilizați pentru a compara și potrivi obiecte 
sau caracteristici în imagini, ceea ce face SIFT extrem de util pentru recunoașterea de obiecte, urmărirea 
obiectelor și alte aplicații de prelucrare a imaginilor.

Potrivirea amprentelor cu FLANN Matcher
Potrivirea caracteristicilor este o etapă in care se calculeaza scorul de similaritate între două imagini
folosind caracteristicile și descriptorii lor detectați. În OpenCV, acest scor de similaritate este definit 
ca distanța dintre două imagini, cu cât valoarea distanței este mai mică, cu atât imaginea este mai similară,
și invers. Acest scor de similaritate este apoi verificat folosind o valoare de prag pentru a determina dacă 
imaginea este o potrivire sau nu.
Fast Library for Approximate Nearest Neighbors Matcher (FLANN Matcher) este un component al bibliotecii FLANN.
FLANN Matcher folosește o serie de algoritmi optimizați pentru a găsi cei mai apropiați vecini în seturile 
de date mari. Algoritmii principali utilizați în FLANN Matcher sunt arborele ierarhic k-means și arborele k-d randomizat. 
FLANN Matcher este cunoscut pentru viteza sa în găsirea vecinilor apropiați, în special în seturi de date mari,
ceea ce îl face potrivit pentru aplicații în care timpul de răspuns este critic.


![2](https://github.com/ddaci/Recunoastere_amprenta_digitala/assets/148542192/5dccf0c6-db21-4919-a33a-1e7a11581abe)

Setul de date pentru amprentele Sokoto Coventry (SOCOFing), este o bază de date biometrică cu amprente 
digitale creată în scopuri de cercetare academică.
SOCOFing este format din 6.000 de imagini ale amprentelor digitale. Numele inregistrărilor(ale imaginilor de amrente), 
conține atribute unice, cum ar fi etichetele pentru gen(feminin sau masculin), mâna(stânga sau dreapta) și numele degetului. 
Setul de date conține si versiunile alterate sintetic ale amprentelor originale. Alterarea imaginilor a fost 
făcută prin ștergere a unor zone de imagine, prin rotație centrală și tăietură în formă de "z".





