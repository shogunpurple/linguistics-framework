# 🌐 Linguistics Framework Español 🇪🇸


![Screenshot 2021-04-07 at 20 47 43](https://user-images.githubusercontent.com/11256663/113925103-83870880-97e2-11eb-9ca0-9e800a9065c5.png)

LFE is a simple, clean and functional self-hostable language learning application for adding Spanish verbs and vocabulary to your Anki decks. It is best used as a companion app during Spanish listening practice, allowing you to save words and verbs you don’t know and review them later, complete with definitions and examples.

See the demo video below for an idea of how LFE works.

https://user-images.githubusercontent.com/11256663/113925488-f8f2d900-97e2-11eb-9582-d741cf64d3da.mp4

Once words are saved, you can review them in your Anki decks as normal!

## Stack
LFE is a python flask application with a svelte frontend with Tailwind CSS. The application makes HTTP requests to SpanishDict.com to retrieve Spanish translations, verb conjugations and example phrases, writing them to your Anki Deck so you can review them at a later date.

## Setup
To start using LFE, you need to have some dependencies in installed on your machine.
- Docker
- Anki

### Setup Anki
You must have the Anki app running on your machine or a VM. You can install it [here](https://apps.ankiweb.net/).

Once you have set up Anki you need to create two decks.
- Spanish Vocabulary
- Spanish Verbs

#### Anki Connect
In order to allow LFE to integrate with your Anki installation, you must install the **Anki Connect** add on. This will expose an API allowing you to create cards, decks and more through HTTP calls.

Get it here:
[https://github.com/FooSoft/anki-connect](https://github.com/FooSoft/anki-connect)

#### (Optional) Anki Auto Sync
This is a very useful extension for auto syncing your Anki decks. This comes in especially useful if you are running your Anki installation on a separate server or VM, and you don’t want to have to manually sync changes to the web from your other server.
[Anki Autosync Plugin](https://ankiweb.net/shared/info/1726633659)

### Setup LFE
Run the LFE docker container using the following command:

```bash
docker run -it -p 3001:3001 -d shogunpurple/linguistics-framework-espanol
```

Visit port 3001 and you should see the UI.

## Using LFE
There are two types of words/phrases you can enter into LFE - verbs and vocabulary.

### Verbs
Input the **Spanish infinitive** of the verb you want to add. For example the verb “to send” in Spanish is **enviar.** Here’s how you would add enviar in the present tense. Once added, every conjugation of that verb for the tense you chose will be added to your anki deck as a new card.

https://www.loom.com/share/40c1401f4f694ac6aa4fd8feb101c52b

### Vocabulary
Vocabulary is simple - you just enter the Spanish word you want to save, choose vocabulary and click save. Here’s an example below with the Spanish word for "plate" which is **plato**.

https://www.loom.com/share/5b381c3495284a4d87d360c168c37d0e

## Configuration
The only piece of configuration that LFE accepts is the `ANKI_CONNECT_URL` environment variable. This defaults to `http://localhost:8765`. If you want to use something different, the best way would be to pass the new environment variable as part of your `docker run` command.


```bash
docker run -it -p 3001:3001 -e ANKI_CONNECT_URL=http://192.168.1.251:8765/ -d shogunpurple/linguistics-framework-espanol
```
