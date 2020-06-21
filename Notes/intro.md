# Vorwort{#vorwort}

In --- diesem^[longnote1] Buch lernst[@Testref] du die Donaudaumpfschiffahrtsgesellschaftskapitän. Grundlagen zur Erstellung einer Joomla 4 Erweiterung. Du erstellst eine beispiel 

Anwendung ohne komplizierte Werkzeuge. Ich erkläre dir alles Notwendige --- von der Projekteinrichtung bis zur Veröffentlichung der Anwendung auf einem Webserver. Das Buch enthält Hinweise zu weiterführendem Lesematerial und Übungen am Ende jedes Kapitels. Nachdem du das Buch gelesen hast, hast du die Grundlagen, um deine eigene Erweiterung für Joomla 4 zu erstellen. Und, was heutzutage nicht unwichtig ist: Das Lernmaterial halte ich auf dem neuesten Stand.
Querverweis interner link
[hierhin](#foo)



Mit diesem Buch biete^[longnote2] ich dir eine Basis, bevor du in die vielen Möglichkeiten, die cryp&shy;to&shy;graphycryp&shy;to&shy;graphycryp&shy;to&shy;graphycryp&shy;to&shy;graphycryp&shy;to&shy;graphycryp&shy;to&shy;graphycryp&shy;to&shy;graphycryp&shy;to&shy;graphycryp&shy;to&shy;graphy die Community und das Ökosystem bereitstellen, eintauchst. Meine Erklärungen beinhalten nur wenige spezielle Werkzeuge, dafür aber viele Informationen über React selbst. Ich erkläre allgemeine Konzepte, Muster und Best Practice anhand einer realen Anwendung.

Wenn\
du die URL ansiehst, während du eine Komponente im Administrationsbereich verwendest, bemerkst du gegebenenfalls die Ansichts- und Layoutvariablen. Beispiel: `index.php?option=com_foos` `&view=foos&layout=default` weist uns an, die foos-Ansicht mit dem Standardlayout zu laden, sodass\
 `compon` `ents/com_foos/tmpl/foos/default.php` aufgerufen wird, wenn du dich im Front-End und `administrator/components/com_foos/tmpl/foos/default.php`, wenn du dich im Backend befindest.

Im Wesentlichen lernst du, eine eigene React-Anwendung von Grund auf neu zu erstellen, mit Funktionen wie Paginierung, clientseitiger und serverseitiger Suche und erweiterten Interaktionen wie Sortieren. Ich hoffe, dass meine Begeisterung für React und JavaScript dich ansteckt und dir so den Einstieg erleichtert.

## Über Astrid Günther

Dich interessiert wer ich bin? Darüber freue ich mich! Ich weiß nicht, welche Informationen du erwartest. Ich fange einmal an und hoffe, dass ich das Passende von mir preisgebe.

Seit 2017 arbeite ich selbständig. Vorher war ich 30 Jahre wohlbehütet im öffentlichen Dienst beschäftigt. Die letzten 20 in einer Sparkasse. Das war --- mit Abstand betrachtet --- nie das Richtige für mich. Hat mir aber, in einer Zeit, in der meine Tochter aufgewachsen ist, das Leben vereinfacht. Alles hat sein Gutes!

Ich fange vorne an: Ich habe 1969 das Licht der Welt erblickt und hatte eine unspektakuläre Kindheit. Nach dem Realschulabschluss habe ich von 1986 bis 1992 im mittleren Justizdienst gearbeitet. Während dieser Zeit habe ich nebenberuflich das Telekolleg II besucht und mit der Fachhochschulreife abgeschlossen. Von 1992 bis 1997 arbeitete ich im gehobenen Postdienst. Hier kam ich bei meiner Arbeit im IT – Betriebs- und Servicezentrum der Postdirektion Köln zum ersten Mal mit Computern in Berührung. 1997 wechselte ich in die EDV-Abteilung einer Sparkasse. Hier war ich bis 2017 angestellt --- unterbrochen durch Erziehungsurlaub --- erst als Systembetreuerin im Second Level Support und später als Programmiererin. Programmiert habe ich als Einzelkämpferin überwiegend in Java und PHP.

Um im IT-Bereich einen Berufsabschluss zu erlangen, habe ich von 1997 bis 2000 abends die berufsbildende Schule Wirtschaft besucht. Am Ende hatte ich die Erlaubnis, mich __staatlich geprüfte Betriebswirtin für Informationsverarbeitung__ zu nennen. Im Anschluss nahm ich 2000 bei der FernUniversität Hagen ein Informatik-Studium in Angriff, welches ich im März 2006 mit dem Abschluss __Master of Computer Science__ erfolgreich beendete. Im Studium habe ich hauptsächlich die objektorientierte Programmierung mit *Java* gelernt.

2007 habe ich die erste Website für eine Bekannte erstellt. Diese Arbeit forderte mich im Positiven. Ich habe daraufhin bei der Studiengemeinschaft Darmstadt den Kurs __Grafik-Designer/in PC (SGD)__ belegt und mit einer Prüfung beendet. Zunächst programmierte ich alles in PHP, später nutze ich Content Management System. *Wordpress* war kurz im Einsatz. Hängen geblieben sind wir bei *Joomla!*. Zur Zeit lege ich meinen Schwerpunkt auf statische System. Hier kommen *Gatsby* und *React* ins Spiel.

 Außerdem keimte in mir die Lust, mein Wissen selbst weiterzugeben. Ich habe erst für den *KnowWareVerlag*, später für *BookBoon* und heute als __SelfPublisherin__ Bücher geschrieben und veröffentlicht. Seit 2017 arbeite ich ausschließlich selbständig. Ich programmiere individuelle Webanwendungen, schreibe Fachliteratur im IT-Bereich und erstelle Websites.

*Warum schreibe und übersetzte ich?*

 Dafür gibt es mehrere Gründe. Einer meiner Antriebe ist, dass das Erstellen von Texten mich bereichert. Ja, ich dokumentiere für mich. Ich finde, dass das Aufschreiben von Gedanken mir hilft, den Wirbelwind der Informationen im Kopf zu ordnen. Außerdem bringe ich Sachverhalte zu Papier, weil ich weiß, dass andere Menschen davon profitieren --- so wie ich beim Lesen von Text fremder Autoren Nutzen ziehe. Egal ob Belletristik oder Fachliteratur.

Weitere Informationen über mich, Möglichkeiten zur Unterstützung oder Infos zu einer Zusammenarbeit findest du auf meiner [Website](https://www.astrid-guenther.de)^[https://www.astrid-guenther.de].

## FAQ

**Wie bekomme ich Updates?**

Ich informiere auf zwei Arten über Aktualisierungen meiner Inhalte. Erfahre Neuigkeiten per E-Mail, indem du [den Newsletter abonnierst](https://www.getrevue.co/profile/rwieruch) oder folge [mir auf Twitter](https://twitter.com/rwieruch). Unabhängig vom Kanal ist es mein Ziel, qualitativ hochwertige Inhalte zu teilen. Sobald du eine Benachrichtigung über eine Änderung erhalten hast, ist eine neue Version auf meiner Website verfügbar.

**Ist das Lernmaterial aktuell?**

Programmierbücher sind oft kurz nach ihrer Veröffentlichung schon veraltet. Da ich dieses Buch als Selfpublisher veröffentliche, ist es mir möglich, es bei Bedarf kurzfristig zu aktualisiere. Immer dann, wenn sich etwas ändert, werde ich das Buch überarbeiten und eine neue Version veröffentlichen.

**Kann ich eine digitale Kopie des Buches erhalten, wenn ich es bei Amazon gekauft habe?**

Erst nachdem du das Buch bei Amazon gekauft hast, stelltest du fest, dass das Buch auf meiner Website in einer digitalen Version verfügbar ist. Da ich Amazon als eine Möglichkeit verwende, für mich zu werben und Inhalte zu monetarisieren, danke ich dir für deine Unterstützung und lade dich ein, dich auf [meiner Website](https://www.robinwieruch.de/) anzumelden. Nachdem du dort ein Konto erstellt hast, schreibe mir eine E-Mail und füge eine Quittung von Amazon bei. Ich werde dann ein digitales Buch für dich freischalten. Mit einem Konto auf meiner Plattform hast du in Zukunft weiterhin Zugriff auf die neueste Version des Buches.

Wenn du ein gedrucktes Buch gekauft hast, notiere bitte deine Lernschritte im Buch. Ich habe mit Absicht die Printausgabe so gestaltet, dass größere Codefragmente genügend Platz bieten, um dir ausreichend Spielraum zum individuellen Arbeiten zu bieten.

**Wie kann ich beim Lesen des Buches Hilfe bekommen?**

Das Buch verbindet eine Gemeinschaft von Lernenden, die sich gegenseitig helfen und  Menschen, die mitlesen. Tritt dieser Community gerne bei. So erhältst du Hilfe. Oder du hilfst anderen. Das gegenseitige Unterstützen hilft dir und anderen dabei, Wissen zu verinnerlichen. Folge der Navigation zu den Kursen auf meiner [Website](https://www.robinwieruch.de/), melde dich dort an und navigiere zum Menüpunkt Community.

**Kann ich helfen, den Inhalt zu verbessern?**

Wenn du Feedback hast, schreibe mir gerne eine E-Mail und ich werde deine Vorschläge berücksichtigen. Erwarte bitte keine direkte Antwort von mir, denn das ist mir zeitlich nicht immer möglich. Wenn du dir ein Feedback wünschst, dann frage in der Community, siehe "Wie kann ich beim Lesen des Buches Hilfe bekommen?".

**Wie und wo melde ich einen Fehler?**

Wenn du einen Fehler im Code findest, melde dies bitte über Github. Am Ende jedes Abschnitts findest du eine URL zum aktuellen GitHub-Projekt. Bitte eröffne hier ein Issue. Ich bin dankbar für deine Hilfe!

**Wie unterstütze ich das Projekt idealerweise?**

Du findest meine Lektionen nützlich und möchtest einen Beitrag leisten? Dann suche bitte auf der [About-Seite meiner Website](https://www.robinwieruch.de/about/) nach Informationen darüber, welche Möglichkeiten es gibt, mich zu unterstützen. In jedem Fall ist hilfreich für potentielle Leser, wenn du darüber informierst, wie meine Bücher dir geholfen haben. Nur mit Unterstützung ist es mir möglich, weiterhin kostenloses Lernmaterial anzubieten.

**Was ist deine Motivation hinter dem Buch?**

Mir ist es wichtig, über aktuelle Themen zu berichten. Ich stoße oft online auf Websites, die nicht aktualisiert werden oder nur einen kleinen Teil eines Themas abdecken. Viele Menschen haben Schwierigkeiten, geeignetes Lernmaterial zu finden. Ich biete aktuelle Inhalte und hoffe, dass ich andere mit meinen Projekten unterstütze, indem ich ihnen Lernmaterial kostenlos zur Verfügung stelle und [etwas zurückgebe](https://www.robinwieruch.de/giving-back-by-learning-react/).

## Für wen ist dieses Buch?

**JavaScript-Anfänger**

JavaScript-Anfänger mit Grundkenntnissen in CSS und HTML: Wenn du die Webentwicklung während einer Ausbildung lernst und ein grundlegendes Verständnis für CSS und HTML hast, biete dir dieses Buch alles, was du zum Erlernen von React benötigst. Wenn du dich wackelig fühlst und der Meinung bist, dass dein JavaScript-Wissen lückenhaft ist, dann schließe diese Lücke, bevor du mit dem Buch fortfährst. Im Buch wirst du zusätzlich viele Hinweise und Links zu grundlegendem Wissen finden.

**JavaScript-Veteranen**

jQuery-JavaScript-Veteranen: Wenn du JavaScript früher ausgiebig mit jQuery, MooTools und Dojo verwendet hast, scheint die neue JavaScript-Ära überwältigend zu sein. Das grundlegende Wissen hat sich nicht geändert, es ist nach wie vor JavaScript und HTML unter der Haube --- daher hilft dieses Buch dir beim Einstieg in React.

**JavaScript-Enthusiasten**

JavaScript-Enthusiasten mit Kenntnissen in anderen modernen [SPA](https://de.wikipedia.org/wiki/Single-Page-Webanwendung)-Frameworks: Wenn du Erfahrungen mit Angular oder Vue gesammelt hast, wirst du zu Beginn auf viele Dinge stoßen, die anders sind. Aber: Alle diese Frameworks bauen auf derselben Grundlage auf --- JavaScript und HTML. Nach kurzem Umlernen wirst du dich schnell in React zurechtfinden.

**Nicht-JavaScript-Entwickler**

Wenn du eine andere Programmiersprache gelernt hast, bist du mit den verschiedenen Aspekten der Programmierung vertraut. Nachdem du dir die Grundlagen zu JavaScript, CSS und HTML angeeignet hast, wirst du React zusammen mit mir schnell lernen.

**Designer und UI/UX-Enthusiasten**

Arbeitest du im Bereich Design, Benutzerinteraktion oder Benutzererfahrung? Dann zögere nicht, dieses Buch in die Hand zu nehmen. Wenn du mit HTML und CSS vertraut bist, ist dies vorteilhaft. Nachdem du einige JavaScript-Grundlagen durchgearbeitet hast, wirst du die Inhalte dieses Buches verstehen. Heutzutage rücken UI und UX näher an die Implementierungsdetails heran. Es bringt dir Vorteile, wenn du weißt, wie die Dinge im Code funktionieren.

**Teamleiter oder Produktmanager**

Wenn du Teamleiter oder Produktmanager einer Entwicklungsabteilung bist, vermittelt dir dieses Buch eine Übersicht über alle wesentlichen Teile einer React-Anwendung. In jedem Abschnitt wird ein Konzept, ein Muster oder eine Technik erläutert. So wird Schritt für Schritt die Gesamtarchitektur aufgebaut und verbessert. Ergebnis ist eine fertige Anwendung, die alle wesentlichen Aspekte von React berücksichtigt.


