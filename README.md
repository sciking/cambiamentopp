# cambiamentopp
Cambiamento++, il linguaggio di programmazione del cambiamento

## Come funziona
Cambiamento++ è un semplice linguaggio di programmazione ispirato alle dinamiche del cosiddetto **Governo del Cambiamento**, in carica in Italia dal 1 giugno 2018, figlio di un'alleanza tra il Movimento 5 Stelle e la Lega - Salvini Premier.

## Visione generale

Il linguaggio adopera tre variabili principali ed effettua tra di esse le operazioni.

Accumulatore è la variabile **Conte**, le due variabili di lavoro sono **Salvini** e **Di Maio**. Tutte le operazioni binarie 
vengono effettuate tra Salvini e Di Maio e salvate in Conte.

Il codice viene eseguito in modo sequenziale da un **Contratto di Governo**, internamente definito come **CG**: Con le opportune istruzioni si puà mutare.

### Da Conte al lavoro
Per lavorare con i dati in Conte si possono mettere in Salvini e Di Maio con l'istruzione **VICEPREMIER nome_ministro**. Con le pseudoistruzioni speciali **MINISTRO SALVINI** e **MINISTRO DI MAIO** si inseriscono Salvini o Di Maio in Conte.

## Funzione principale
La funzione principale viene eseguita all'avvio del software ed è definita dal codice **ONOREVOLI COLLEGHI**

Seppur non essenziale è buona pratica segnalare ogni blocco logico di codice con **DISCUTIAMO IL DDL** oppure **INTERROGAZIONE A RISPOSTA SCRITTA** se il blocco restituisce qualcosa, seguito nella riga successiva dal nome del blocco, a libera scelta.

## I registri del linguaggio
Il linguaggio offre built-in otto GPR così denominati:
* R0: Costa
* R1: Grillo
* R2: Tria
* R3: Centinaio
* R4: Bongiorno
* R5: Toninelli
* R6: Lezzi
* R7: Fontana

I registri, di default, non sono inizializzati: Per farlo bisogna usare l'istruzione **MINISTRO nome_registro**.

Per poter operare con esse è necessario portarli nelle variabili di lavoro, con la sintassi'

**RUSPA nome_registro** per portare il registro in Salvini e Salvini nel registro

**ONESTÀ nome_registro** per portare il registro in Di Maio e Di Maio nel registro

L'operazione **CONTRATTO**, invece, scambia le variabili Salvini e Di Maio. 

## Operazioni matematiche

Il linguaggio supporta addizione, sottrazione, moltiplicazione, divisione, radice di N ed elevamento ad N.

### Addizione
Con il comando **LA GENTE È STANCA** il linguaggio eseguirà l'operazione **Conte = Salvini + Di Maio**
### Sottrazione
Con il comando **L'ONESTÀ ANDRÀ DI MODA** il linguaggio eseguirà l'operazione **Conte = Salvini - Di Maio**
### Moltiplicazione
Con il comando **BISOGNA PENSARE ALLA TRASPARENZA** il linguaggio eseguirà **Conte = Salvini * Di Maio**
### Divisione
Con il comando **BRUXELLES NON CI SPAVENTA** il linguaggio eseguirà **Conte = Salvini/Di Maio**
### Radice di N
Con il comando **PRIMA GLI ITALIANI** il linguaggio eseguirà **Conte == Di Maio√Salvini**
### Elevamento a N
Con il comando **IL REDDITO DI CITTADINANZA** il linguaggio eseguirà **Conte == Salvini^Di Maio**

## Aumenti notevoli
Il linguaggio possiede cinque operatori notevoli per ogni variabile di lavoro, essi modificano la variabile in modo predeterminato.

### Conte
* **IL PRESIDENTE DEL CONSIGLIO**: Conte = Conte/2
* **NON È NEL CONTRATTO**: Conte = 1/Conte
* **ABBIAMO SALVATO VITE**: Conte = Conte * 2
* **L'AVVOCATO DEL POPOLO**: Conte = Conte * 10
* **METTEREMO LA FIDUCIAA**: Conte = Conte^Conte
### Salvini
* **LA BOLDRINI**: Salvini = Salvini/2
* **LA LEVA OBBLIGATORIA**: Salvini = 1/Salvini
* **LA FLAT TAX**: Salvini = Salvini * 2
* **NESSUNO HA NOSTALGIA**: Salvini = Salvini * 10
* **BISOGNA EDUCARE**: Salvini = Salvini^Salvini
### Di Maio
* **IL LAVORO**: Di Maio = Di Maio/2
* **LA TAV**: Di Maio = 1/Di Maio
* **I DAZI**: Di Maio = Di Maio * 2
* **NESSUNO VUOLE USCIRE**: Di Maio = Di Maio * 10
* **L'EURO**: Di Maio = Di Maio^Di Maio

## Matematica avanzata
Il linguaggio supporta solo due funzioni di matematica avanzata, ossia il determinante e la logica booleana.

### Determinante
Con il comando **I MERCATI SE NE FARANNO UNA RAGIONE** si ottiene **Conte = Di Maio^2-4(Salvini * Conte)**. Per ragioni etiche l'interprete introduce un errore casuale nell'operazione, dato il rischio che venga usata in una disequazione, cosa disapprovata dal governo del cambiamento.

### Logica booleana
Dato che il governo dice sempre la verità esiste una sola variabile booleana, **CASALEGGIO**, perennemente settata a 1. Ovviamente è impossibile negarla in qualunque modo.

## Salti
Il linguaggio supporta i salti incondizionati e l'esecuzione condizionale.

### Salti incondizionati
Il salto incondizionato viene eseguito con l'istruzione **VOTIAMO IL PROGETTO DI LEGGE / numero_riga**, con / interruzione di riga, che modifica dunque il Governo del Cambiamento.

### Esecuzione condizionale
L'operazione **MATTARELLA FIRMA IL DECRETO** aumenta il GC di uno se **Conte** è minore o uguale a zero, quindi l'istruzione seguente viene eseguita se e solo se Conte è maggiore di zero.

## Input e output
### Input
Si possono inserire dati in Di Maio, Conte e Salvini con gli opportuni operatori **IL POPOLO CHIEDE nome_variabile**

### Output

Per ottenere in output il valore di una variabile si scrive **nome_variabile, LO VUOLE L'ITALIA**.

## Stringhe in R1

Si può usare R1 come registro per delle stringhe da stampare a video. L'inserimento avviene con un'istruzione su due righe ossia:

**BUONGIORNO AMICI**

**stringa da caricare, senza apici**

Per effettuare la stampa si scrive **CIAO AMICI**.
