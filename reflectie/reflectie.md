# De trojan

Deze trojan die momenteel bestaat uit vier modules is zodanig gemaakt dat hij makkelijk kan worden uitgebreid naar meerdere modules.

## Werking

Eens de trojan een host infecteerd, zal meteen de sys info module geactiveerd worden. Om vervolgens informatie te kunnen loggen zal er in de logs folder een nieuwe folder worden aangemaakt waarvan de naam een md5 hash is van het mac adres van de host, zodanig dat er voor elke unieke host een eigen log folder is. In deze folder wordt vervolgens een json bestand bijgehouden met de sys info en wordt er plaats gemaakt om informatie verkregen uit andere modules te loggen.

Om te weten welke module moet worden uitgevoerd, zal het programma een check uitvoeren om de willekeurige hoeveelheid tijd (momenteel tussen 30 en 60 seconden) door naar config.json te kijken in de root folder, de module die op dat moment dan daar staat zal worden uitgevoerd.

## Modules

Dit zijn de gebruikte modules:

- Sys info verzamelaar:
Deze verzamelt informatie over de geïnfecteerde host zoals operating system, versie, schrijfruimte, publiek ip adres, hostname, etc.

- Screenshotter:
Deze module maakt om de interval een screenshot en slaat deze op in bijhorende logs

- Keylogger:
Hiermee worden de keystroken van de gebruiker gelogt

- Netwerk analyseerder:
Het doel van deze module is om uit- en inkomend netwerkverkeer te bekijken