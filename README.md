# Ortus Mājasdarbu Paziņotāja Bots
Šis repozitorijs satur Python skriptu, kas automatizē Ortus mājasdarbu pārbaudes un lietotāju informēšanu par pašreizējiem mājasdarbiem. Skripts izmanto Selenium tīmekļa automatizācijai un Telebot integrācijai ar Telegram.
## Kā Tas Darbojas
### Telegram Bota iestatīšana:
Izveidojiet jaunu Telegram botu un iegūstiet bot token.
> Ttelegramā sāciet dialogu ar BotFather, ierakstiet /newbot, pēc tam piešķiriet savam robotam vārdu, pēc tam
 ierakstiet komandu /token un atlasiet savu botu, lai saņemtu tokenu.
> Ierakstiet tokenu 10. rindā pēdiņās.
### Akreditācijas faila izveide:
Ievietojiet failā ar nosaukumu data.txt Ortus pieteikšanās akreditāciju šādā formātā:
```
Lietotājvārds
jūsu_parole
```
## Atkarību Instalēšana:
```
pip install -r requirements.txt
```
## Koda Izpilde:
```
python python.py
```
Pēc tam nosūtam /start komandu savam Telegram botam.
## Automatizētais Process:
1) Izmantojot selenium bibliotēku skripts automatizē Ortus ieejas procesu, izmantojot sniegtos datus.
2) Tas navigē uz sadaļu 'Studentiem', un pēc tam uz saiti 'estudijas.rtu.lv'.
3) Izmantojot bibliotēku BeautifulSoup, tas izvelk informāciju par pašreizējiem mājasdarbiem.
4) Katram mājasdarbam tiek nosūtīts Telegram ziņojums ar kursa nosaukumu un aktivitātes virsrakstu un linku, izmantojot telebot library.
## Koda Izskaidrojums
Skripts izmanto Selenium, lai automatizētu tīmekļa mijiedarbību ar Ortus.
Telebot tiek izmantots, lai mijiedarbotos ar Telegram.
/start komanda aktivizē skriptu.
Skripts nolasa Ortus pieteikšanās akreditāciju no data.txt faila.
Tam tiek izmantots bezgalvains Chrome mājasdarbu iegūšanai, padarot procesu neredzamu lietotājam.
Izmantojot BeautifulSoup, tiek izanalizēts lapas kods, lai izgūtu informāciju par mājasdarbiem.
Par katru mājasdarbu tiek sūtīts Telegram ziņojums, lai informētu lietotāju.

## Programmas izpildes demonstrēšana
Noklikšķinot uz tālāk esošās saites, jūs varat redzēt programmu darbībā
Links: https://drive.google.com/file/d/1jGZbJoF2KgWhKtQxEaNgI_zDJ-270cUf/view?usp=drive_link
