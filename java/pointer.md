# Pointer spiegati

---

Supponiamo di avere un albergo da 100 posti.

Immaginiamo che io, `Luca`, di `20` anni, vado in questo albergo e chiedo una stanza.
La reception mi chiede nome, ed età, e mi da la prima stanza libera (la 1).

Questo corrisponde in java a fare
```java
new Persona("Luca", 20);
```
e quindi sto registrando un nuovo `Pointer` nel mio albergo

La chiave, che mi viene data, è la `variabile`.
La variabile non è altro che una chiave,
con su scritto "1" che mi dice che quella chiave è proprio per la stanza numero 1,
in cui troverò la persona chiamata `Luca` che ha `20` anni.

Quando quindi andiamo a creare una variabile, ad esempio così:

```java
Persona laMiaVariabile = new Persona("Luca", 20);
```

Stiamo sia registrando un pointer,
che creando una "chiave" che punta a quel pointer e che ha nome `laMiaVariabile`

Quando riassegniamo un valore alla variabile, come ad esempio
```java
Persona laMiaVariabile = new Persona("Luca", 20); //Creazione della variabile

laMiaVariabile = new Persona("Mario", 36); //Cambio di valore
```

Non stiamo modificando un oggetto,
ma stiamo solo dicendo alla "Chiave" di cambiare stanza a cui puntare

**Il primo pointer che abbiamo registrato non viene eliminato,
fino a che il Garbage Collector non si occupa di eliminarlo**

## Controllo dei valori

Mettiamo ora che nell'albergo arrivi un secondo Luca, sempre di 20 anni.

Quando si registra nell'albergo, le informazioni sono identiche,
ma gli verrà assegnata un altra stanza perché la numero 1 è occupata.

**Di conseguenza, due oggetti uguali possono avere pointer diversi**

A questo punto, se io, Luca di 20 anni mi trovo nella stanza 1, mentre l'altro Luca,
sempre di 20 anni si trova nella stanza 2 la condizione:

```java
Persona variabile1 = new Persona("Luca", 20);
Persona variabile2 = new Persona("Luca", 20);

boolean condizione = variabile1 == variabile2; //False
```

Sarà falsa. Poiché i pointer sono diversi.

Di conseguenza, ci viene in aiuto il metodo base `Object::equals`.

Se nella nostra classe `Persona`, andiamo a estendere il metodo `equals`:

```java
public class Persona {
	private final String nome;
	private final int età;
    
	public Persona(String nome, int età) {
		this.nome = nome;
		this.età = età;
	}
    
	@Override
	public boolean equals(Object obj) {
		//Qui eseguiamo qualcosa per controllare
	}
}
```

Da dentro possiamo controllare dei valori

```java
@Override
public boolean equals(Object obj) {
    // Controlliamo se l'oggetto con cui stiamo facendo il controllo
    // è sempre di tipo "Persona"
    if(obj instanceof Persona persona2) {
        // Controlliamo che nome e età siano uguali
        return this.nome.equals(persona2.nome) && this.età == persona2.età;
    } else {
        // Se non è di tipo persona, torniamo a controllare i pointer
        // come da metodo originale
        return super.equals(obj);
    }
}
```

## Attenzione

Per controllare se i nostri due oggetti sono uguali, dobbiamo usare `equals`,
poiché `==` farà il controllo dei pointer.

**Le tipi di variabile primitiva, come `int`,
non sono veri e propri oggetti ed è per questo del tutto normale compararli con `==`**

