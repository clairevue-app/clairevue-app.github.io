# -*- coding: utf-8 -*-
"""Contenu source des pages légales de PousseDedans, une entrée par langue.

Les .html du dossier sont GÉNÉRÉS depuis ce fichier par generer.py : les
modifier directement serait écrasé à la prochaine génération. Éditer ici,
puis relancer `python generer.py` à la racine du dépôt.

Avoir les 5 langues côte à côte dans un seul fichier rend les écarts de
contenu visibles d'un coup d'œil — le vrai risque sur des textes légaux
dupliqués n'est pas la faute de frappe, c'est qu'une langue prenne du
retard sur les autres sans que personne ne le voie.
"""

APP = "PousseDedans"
CONTACT = "clairevue.messagerie@gmail.com"
EDITEUR = "Clairevue"
MAJ = "27 septembre 2026"

LANGUES = ["fr", "en", "de", "es", "it"]

# Libellés de navigation communs aux deux documents.
NAV = {
    "fr": {"maj": "Dernière mise à jour", "retour": "Accueil Clairevue", "autre": "Conditions d'utilisation"},
    "en": {"maj": "Last updated", "retour": "Clairevue home", "autre": "Terms of use"},
    "de": {"maj": "Zuletzt aktualisiert", "retour": "Clairevue-Startseite", "autre": "Nutzungsbedingungen"},
    "es": {"maj": "Última actualización", "retour": "Inicio Clairevue", "autre": "Condiciones de uso"},
    "it": {"maj": "Ultimo aggiornamento", "retour": "Home Clairevue", "autre": "Termini di utilizzo"},
}
NAV_AUTRE_CONF = {
    "fr": "Politique de confidentialité",
    "en": "Privacy policy",
    "de": "Datenschutzerklärung",
    "es": "Política de privacidad",
    "it": "Informativa sulla privacy",
}

CONFIDENTIALITE = {
"fr": {
"titre": "Politique de confidentialité",
"intro": f"{APP} (« l'application ») est une application de gestion des soins de plantes d'intérieur, éditée par {EDITEUR}. Cette page décrit quelles données sont traitées lorsque vous utilisez l'application.",
"sections": [
("Aucune collecte de données personnelles par Clairevue",
 f"<p>{APP} fonctionne entièrement <strong>hors ligne</strong>. Toutes les données que vous saisissez — maisons, espaces, plantes, historique de soins, notes, photos — sont stockées uniquement sur votre appareil, dans une base de données locale. Elles ne sont jamais envoyées à un serveur, ni à {EDITEUR}, ni à un tiers.</p><p>Il n'existe aucun compte utilisateur, aucune inscription, aucune authentification.</p>"),
("Export et sauvegarde",
 f"<p>L'application permet d'exporter vos données (maisons, plantes, photos, réglages) dans un fichier que vous choisissez d'enregistrer ou de partager vous-même. {EDITEUR} n'a accès à aucun de ces fichiers ; leur diffusion dépend entièrement de vos propres choix une fois le fichier créé.</p>"),
("Publicité (Google AdMob)",
 "<p>La version gratuite affiche des bannières publicitaires fournies par <strong>Google AdMob</strong>. AdMob peut collecter des identifiants publicitaires et des données techniques (type d'appareil, adresse IP approximative) afin d'afficher des publicités, éventuellement personnalisées selon vos réglages Android.</p><p>Ces données sont traitées par Google. Pour en savoir plus : <a href=\"https://policies.google.com/privacy\">politique de confidentialité de Google</a> et <a href=\"https://adssettings.google.com\">paramètres publicitaires</a>.</p><p>L'achat de la version complète retire définitivement ces publicités.</p>"),
("Achats intégrés (Google Play)",
 f"<p>L'achat unique proposé est traité entièrement par <strong>Google Play</strong>. {EDITEUR} ne reçoit ni ne stocke aucune information de paiement.</p>"),
("Notifications",
 "<p>Les rappels d'arrosage et d'engrais sont des notifications <strong>locales</strong>, planifiées par votre appareil à partir des données déjà présentes localement. Aucune donnée n'est envoyée à un serveur pour les générer.</p>"),
("Permissions demandées",
 "<ul><li><strong>Notifications</strong> : pour afficher les rappels de soin (refusables, l'app fonctionne sans).</li><li><strong>Alarmes et rappels</strong> : pour que le rappel se déclenche à l'heure choisie.</li><li><strong>Caméra / galerie</strong> : uniquement si vous ajoutez une photo à une plante. Les photos restent sur votre appareil.</li></ul>"),
("Enfants",
 "<p>L'application n'est pas spécifiquement destinée aux enfants et ne collecte sciemment aucune donnée les concernant.</p>"),
("Vos droits",
 f"<p>Puisqu'aucune donnée n'est stockée par {EDITEUR}, il n'y a rien à demander de supprimer de notre côté : la suppression se fait en désinstallant l'application, ou en supprimant une maison ou une photo dans l'application.</p>"),
("Modifications",
 "<p>Cette politique peut être mise à jour ; la date en haut de page indique la dernière révision.</p>"),
("Contact",
 f"<p>Pour toute question : <a href=\"mailto:{CONTACT}\">{CONTACT}</a></p>"),
]},

"en": {
"titre": "Privacy policy",
"intro": f"{APP} (\"the app\") is a houseplant care app published by {EDITEUR}. This page describes what data is processed when you use the app.",
"sections": [
("No personal data collected by Clairevue",
 f"<p>{APP} runs entirely <strong>offline</strong>. Everything you enter — homes, rooms, plants, care history, notes, photos — is stored only on your device, in a local database. It is never sent to a server, to {EDITEUR}, or to any third party.</p><p>There is no user account, no sign-up, no authentication.</p>"),
("Export and backup",
 f"<p>The app lets you export your data (homes, plants, photos, settings) to a file that you choose to save or share yourself. {EDITEUR} has no access to those files; what happens to them depends entirely on your own choices once the file is created.</p>"),
("Advertising (Google AdMob)",
 "<p>The free version displays banner ads provided by <strong>Google AdMob</strong>. AdMob may collect advertising identifiers and technical data (device type, approximate IP address) in order to show ads, possibly personalised according to your Android settings.</p><p>This data is processed by Google. For more information: <a href=\"https://policies.google.com/privacy\">Google's privacy policy</a> and <a href=\"https://adssettings.google.com\">ad settings</a>.</p><p>Purchasing the full version removes these ads permanently.</p>"),
("In-app purchases (Google Play)",
 f"<p>The one-off purchase is handled entirely by <strong>Google Play</strong>. {EDITEUR} neither receives nor stores any payment information.</p>"),
("Notifications",
 "<p>Watering and fertilising reminders are <strong>local</strong> notifications, scheduled by your device from data already stored locally. No data is sent to a server to generate them.</p>"),
("Permissions requested",
 "<ul><li><strong>Notifications</strong>: to show care reminders (can be denied, the app works without).</li><li><strong>Alarms and reminders</strong>: so the reminder fires at the time you chose.</li><li><strong>Camera / gallery</strong>: only if you add a photo to a plant. Photos stay on your device.</li></ul>"),
("Children",
 "<p>The app is not specifically aimed at children and knowingly collects no data about them.</p>"),
("Your rights",
 f"<p>Since no data is stored by {EDITEUR}, there is nothing to ask us to delete: removal happens by uninstalling the app, or by deleting a home or a photo within the app.</p>"),
("Changes",
 "<p>This policy may be updated; the date at the top of the page shows the last revision.</p>"),
("Contact",
 f"<p>For any question: <a href=\"mailto:{CONTACT}\">{CONTACT}</a></p>"),
]},

"de": {
"titre": "Datenschutzerklärung",
"intro": f"{APP} („die App“) ist eine App zur Pflege von Zimmerpflanzen, herausgegeben von {EDITEUR}. Diese Seite beschreibt, welche Daten bei der Nutzung der App verarbeitet werden.",
"sections": [
("Keine Erhebung personenbezogener Daten durch Clairevue",
 f"<p>{APP} funktioniert vollständig <strong>offline</strong>. Alle von dir eingegebenen Daten — Zuhause, Räume, Pflanzen, Pflegeverlauf, Notizen, Fotos — werden ausschließlich auf deinem Gerät in einer lokalen Datenbank gespeichert. Sie werden niemals an einen Server, an {EDITEUR} oder an Dritte gesendet.</p><p>Es gibt kein Benutzerkonto, keine Registrierung, keine Anmeldung.</p>"),
("Export und Sicherung",
 f"<p>Die App ermöglicht den Export deiner Daten (Zuhause, Pflanzen, Fotos, Einstellungen) in eine Datei, die du selbst speicherst oder teilst. {EDITEUR} hat keinen Zugriff auf diese Dateien; ihre Verbreitung hängt allein von deinen Entscheidungen ab.</p>"),
("Werbung (Google AdMob)",
 "<p>Die kostenlose Version zeigt Werbebanner von <strong>Google AdMob</strong>. AdMob kann Werbe-IDs und technische Daten (Gerätetyp, ungefähre IP-Adresse) erheben, um Werbung anzuzeigen, je nach deinen Android-Einstellungen ggf. personalisiert.</p><p>Diese Daten werden von Google verarbeitet. Mehr dazu: <a href=\"https://policies.google.com/privacy\">Datenschutzerklärung von Google</a> und <a href=\"https://adssettings.google.com\">Werbeeinstellungen</a>.</p><p>Der Kauf der Vollversion entfernt diese Werbung dauerhaft.</p>"),
("In-App-Käufe (Google Play)",
 f"<p>Der einmalige Kauf wird vollständig von <strong>Google Play</strong> abgewickelt. {EDITEUR} erhält und speichert keinerlei Zahlungsinformationen.</p>"),
("Benachrichtigungen",
 "<p>Gieß- und Düngeerinnerungen sind <strong>lokale</strong> Benachrichtigungen, die dein Gerät aus bereits lokal vorhandenen Daten plant. Es werden dafür keine Daten an einen Server gesendet.</p>"),
("Angeforderte Berechtigungen",
 "<ul><li><strong>Benachrichtigungen</strong>: zur Anzeige der Pflegeerinnerungen (ablehnbar, die App funktioniert auch ohne).</li><li><strong>Wecker und Erinnerungen</strong>: damit die Erinnerung zur gewählten Uhrzeit ausgelöst wird.</li><li><strong>Kamera / Galerie</strong>: nur wenn du einer Pflanze ein Foto hinzufügst. Fotos bleiben auf deinem Gerät.</li></ul>"),
("Kinder",
 "<p>Die App richtet sich nicht gezielt an Kinder und erhebt wissentlich keine Daten über sie.</p>"),
("Deine Rechte",
 f"<p>Da {EDITEUR} keine Daten speichert, gibt es bei uns nichts zu löschen: Die Löschung erfolgt durch Deinstallation der App oder durch Löschen eines Zuhauses oder Fotos in der App.</p>"),
("Änderungen",
 "<p>Diese Erklärung kann aktualisiert werden; das Datum oben auf der Seite zeigt die letzte Überarbeitung.</p>"),
("Kontakt",
 f"<p>Bei Fragen: <a href=\"mailto:{CONTACT}\">{CONTACT}</a></p>"),
]},

"es": {
"titre": "Política de privacidad",
"intro": f"{APP} («la aplicación») es una aplicación de cuidado de plantas de interior, editada por {EDITEUR}. Esta página describe qué datos se tratan cuando usas la aplicación.",
"sections": [
("Ningún dato personal recogido por Clairevue",
 f"<p>{APP} funciona completamente <strong>sin conexión</strong>. Todos los datos que introduces — casas, estancias, plantas, historial de cuidados, notas, fotos — se guardan únicamente en tu dispositivo, en una base de datos local. Nunca se envían a un servidor, ni a {EDITEUR}, ni a terceros.</p><p>No existe cuenta de usuario, ni registro, ni autenticación.</p>"),
("Exportación y copia de seguridad",
 f"<p>La aplicación permite exportar tus datos (casas, plantas, fotos, ajustes) a un archivo que tú decides guardar o compartir. {EDITEUR} no tiene acceso a esos archivos; su difusión depende enteramente de tus propias decisiones.</p>"),
("Publicidad (Google AdMob)",
 "<p>La versión gratuita muestra banners publicitarios de <strong>Google AdMob</strong>. AdMob puede recoger identificadores publicitarios y datos técnicos (tipo de dispositivo, dirección IP aproximada) para mostrar anuncios, posiblemente personalizados según tus ajustes de Android.</p><p>Estos datos los trata Google. Más información: <a href=\"https://policies.google.com/privacy\">política de privacidad de Google</a> y <a href=\"https://adssettings.google.com\">ajustes de anuncios</a>.</p><p>La compra de la versión completa elimina definitivamente estos anuncios.</p>"),
("Compras integradas (Google Play)",
 f"<p>La compra única se gestiona íntegramente mediante <strong>Google Play</strong>. {EDITEUR} no recibe ni almacena ningún dato de pago.</p>"),
("Notificaciones",
 "<p>Los recordatorios de riego y abono son notificaciones <strong>locales</strong>, programadas por tu dispositivo a partir de datos ya presentes localmente. No se envía ningún dato a un servidor para generarlos.</p>"),
("Permisos solicitados",
 "<ul><li><strong>Notificaciones</strong>: para mostrar los recordatorios de cuidado (puedes denegarlo, la app funciona igual).</li><li><strong>Alarmas y recordatorios</strong>: para que el recordatorio salte a la hora elegida.</li><li><strong>Cámara / galería</strong>: solo si añades una foto a una planta. Las fotos permanecen en tu dispositivo.</li></ul>"),
("Menores",
 "<p>La aplicación no está dirigida específicamente a menores y no recoge conscientemente ningún dato sobre ellos.</p>"),
("Tus derechos",
 f"<p>Dado que {EDITEUR} no almacena ningún dato, no hay nada que pedirnos que borremos: la eliminación se realiza desinstalando la aplicación, o borrando una casa o una foto dentro de ella.</p>"),
("Modificaciones",
 "<p>Esta política puede actualizarse; la fecha en la parte superior indica la última revisión.</p>"),
("Contacto",
 f"<p>Para cualquier duda: <a href=\"mailto:{CONTACT}\">{CONTACT}</a></p>"),
]},

"it": {
"titre": "Informativa sulla privacy",
"intro": f"{APP} (“l'applicazione”) è un'app per la cura delle piante da interno, pubblicata da {EDITEUR}. Questa pagina descrive quali dati vengono trattati quando usi l'applicazione.",
"sections": [
("Nessun dato personale raccolto da Clairevue",
 f"<p>{APP} funziona interamente <strong>offline</strong>. Tutti i dati che inserisci — case, stanze, piante, cronologia delle cure, note, foto — sono memorizzati solo sul tuo dispositivo, in un database locale. Non vengono mai inviati a un server, né a {EDITEUR}, né a terzi.</p><p>Non esiste alcun account utente, né registrazione, né autenticazione.</p>"),
("Esportazione e backup",
 f"<p>L'applicazione consente di esportare i tuoi dati (case, piante, foto, impostazioni) in un file che scegli tu stesso di salvare o condividere. {EDITEUR} non ha accesso a questi file; la loro diffusione dipende interamente dalle tue scelte.</p>"),
("Pubblicità (Google AdMob)",
 "<p>La versione gratuita mostra banner pubblicitari forniti da <strong>Google AdMob</strong>. AdMob può raccogliere identificatori pubblicitari e dati tecnici (tipo di dispositivo, indirizzo IP approssimativo) per mostrare annunci, eventualmente personalizzati in base alle tue impostazioni Android.</p><p>Questi dati sono trattati da Google. Per saperne di più: <a href=\"https://policies.google.com/privacy\">informativa sulla privacy di Google</a> e <a href=\"https://adssettings.google.com\">impostazioni annunci</a>.</p><p>L'acquisto della versione completa rimuove definitivamente questa pubblicità.</p>"),
("Acquisti in-app (Google Play)",
 f"<p>L'acquisto una tantum è gestito interamente da <strong>Google Play</strong>. {EDITEUR} non riceve né conserva alcuna informazione di pagamento.</p>"),
("Notifiche",
 "<p>I promemoria di irrigazione e concimazione sono notifiche <strong>locali</strong>, pianificate dal tuo dispositivo a partire da dati già presenti localmente. Nessun dato viene inviato a un server per generarli.</p>"),
("Autorizzazioni richieste",
 "<ul><li><strong>Notifiche</strong>: per mostrare i promemoria di cura (puoi rifiutare, l'app funziona lo stesso).</li><li><strong>Sveglie e promemoria</strong>: perché il promemoria scatti all'ora scelta.</li><li><strong>Fotocamera / galleria</strong>: solo se aggiungi una foto a una pianta. Le foto restano sul tuo dispositivo.</li></ul>"),
("Minori",
 "<p>L'applicazione non è specificamente rivolta ai minori e non raccoglie consapevolmente alcun dato che li riguardi.</p>"),
("I tuoi diritti",
 f"<p>Poiché {EDITEUR} non memorizza alcun dato, non c'è nulla da chiederci di cancellare: la rimozione avviene disinstallando l'applicazione, o eliminando una casa o una foto al suo interno.</p>"),
("Modifiche",
 "<p>Questa informativa può essere aggiornata; la data in alto indica l'ultima revisione.</p>"),
("Contatto",
 f"<p>Per qualsiasi domanda: <a href=\"mailto:{CONTACT}\">{CONTACT}</a></p>"),
]},
}

CONDITIONS = {
"fr": {
"titre": "Conditions d'utilisation",
"intro": f"En installant et en utilisant {APP} (« l'application »), vous acceptez les conditions décrites ci-dessous.",
"sections": [
("Objet de l'application",
 f"<p>{APP} est un outil d'aide personnelle pour suivre l'entretien de plantes d'intérieur. Ce n'est pas un service professionnel d'horticulture ni de médecine vétérinaire.</p>"),
("!Conseils de culture",
 "Les recommandations de soin (fréquence d'arrosage, d'engrais, exposition) sont des <strong>indications générales</strong>, fondées sur des données publiques moyennes par espèce. Elles ne remplacent ni l'observation de votre plante réelle ni l'avis d'un professionnel. L'application ne garantit pas la survie de vos plantes."),
("!Toxicité pour les animaux",
 "Les indications de toxicité sont fournies <strong>à titre purement informatif</strong> et ne constituent en aucun cas un avis vétérinaire. En cas d'ingestion réelle ou suspectée, contactez immédiatement un vétérinaire ou un centre antipoison animalier — ne vous fiez jamais uniquement à l'application en situation d'urgence."),
("Contenu ajouté par l'utilisateur",
 "<p>Vous pouvez ajouter vos propres plantes au catalogue local. Ce contenu reste strictement local à votre appareil : il n'est ni partagé, ni vérifié, ni validé par qui que ce soit. Vous êtes seul responsable de l'exactitude des informations saisies.</p>"),
("Absence de sauvegarde automatique",
 "<p>L'application fonctionne hors ligne et ne sauvegarde vos données sur aucun serveur. Si vous désinstallez l'application, changez de téléphone, ou perdez votre appareil <strong>sans avoir exporté une sauvegarde au préalable</strong>, toutes vos données seront <strong>définitivement perdues</strong>. Il vous appartient d'effectuer des sauvegardes régulières via la fonction prévue à cet effet.</p>"),
("Achat intégré",
 "<p>L'application propose un achat unique optionnel qui retire la publicité et débloque des fonctionnalités supplémentaires. Cet achat est traité par Google Play ; les remboursements suivent la politique de Google Play.</p>"),
("Fourniture « en l'état »",
 "<p>L'application est fournie « telle quelle », sans garantie d'aucune sorte. L'éditeur ne peut être tenu responsable d'un dommage direct ou indirect résultant de son utilisation, dans la mesure permise par la loi applicable.</p>"),
("Droit applicable",
 "<p>Ces conditions sont régies par le droit français.</p>"),
("Contact",
 f"<p>Pour toute question : <a href=\"mailto:{CONTACT}\">{CONTACT}</a></p>"),
]},

"en": {
"titre": "Terms of use",
"intro": f"By installing and using {APP} (\"the app\"), you accept the terms described below.",
"sections": [
("Purpose of the app",
 f"<p>{APP} is a personal tool for tracking houseplant care. It is not a professional horticultural or veterinary service.</p>"),
("!Care advice",
 "Care recommendations (watering and fertilising frequency, light exposure) are <strong>general indications</strong>, based on average public data per species. They replace neither observing your actual plant nor professional advice. The app does not guarantee your plants' survival."),
("!Toxicity to animals",
 "Toxicity information is provided <strong>for information only</strong> and does not constitute veterinary advice. If ingestion is suspected or confirmed, contact a vet or an animal poison control centre immediately — never rely on the app alone in an emergency."),
("User-added content",
 "<p>You may add your own plants to the local catalog. That content stays strictly local to your device: it is neither shared, nor reviewed, nor validated by anyone. You alone are responsible for the accuracy of what you enter.</p>"),
("No automatic backup",
 "<p>The app works offline and stores your data on no server. If you uninstall the app, change phones, or lose your device <strong>without having exported a backup first</strong>, all your data will be <strong>permanently lost</strong>. Making regular backups through the built-in function is your responsibility.</p>"),
("In-app purchase",
 "<p>The app offers an optional one-off purchase that removes ads and unlocks extra features. It is handled by Google Play; refunds follow Google Play's policy.</p>"),
("Provided \"as is\"",
 "<p>The app is provided \"as is\", without warranty of any kind. The publisher cannot be held liable for any direct or indirect damage resulting from its use, to the extent permitted by applicable law.</p>"),
("Governing law",
 "<p>These terms are governed by French law.</p>"),
("Contact",
 f"<p>For any question: <a href=\"mailto:{CONTACT}\">{CONTACT}</a></p>"),
]},

"de": {
"titre": "Nutzungsbedingungen",
"intro": f"Mit der Installation und Nutzung von {APP} („die App“) akzeptierst du die nachstehenden Bedingungen.",
"sections": [
("Zweck der App",
 f"<p>{APP} ist ein persönliches Hilfsmittel zur Pflege von Zimmerpflanzen. Es ist kein professioneller Gartenbau- oder tiermedizinischer Dienst.</p>"),
("!Pflegehinweise",
 "Die Pflegeempfehlungen (Gieß- und Düngehäufigkeit, Lichtbedarf) sind <strong>allgemeine Anhaltspunkte</strong> auf Basis öffentlicher Durchschnittswerte je Art. Sie ersetzen weder die Beobachtung deiner tatsächlichen Pflanze noch fachlichen Rat. Die App garantiert das Überleben deiner Pflanzen nicht."),
("!Giftigkeit für Tiere",
 "Angaben zur Giftigkeit dienen <strong>ausschließlich der Information</strong> und stellen keine tierärztliche Beratung dar. Bei tatsächlicher oder vermuteter Aufnahme wende dich sofort an eine Tierärztin, einen Tierarzt oder eine Giftnotrufzentrale — verlasse dich im Notfall niemals allein auf die App."),
("Von Nutzenden hinzugefügte Inhalte",
 "<p>Du kannst eigene Pflanzen zum lokalen Katalog hinzufügen. Diese Inhalte bleiben strikt lokal auf deinem Gerät: Sie werden weder geteilt noch geprüft noch von irgendjemandem freigegeben. Für die Richtigkeit bist allein du verantwortlich.</p>"),
("Keine automatische Sicherung",
 "<p>Die App arbeitet offline und speichert deine Daten auf keinem Server. Wenn du die App deinstallierst, das Telefon wechselst oder dein Gerät verlierst, <strong>ohne zuvor eine Sicherung exportiert zu haben</strong>, gehen alle deine Daten <strong>endgültig verloren</strong>. Regelmäßige Sicherungen über die vorgesehene Funktion liegen in deiner Verantwortung.</p>"),
("In-App-Kauf",
 "<p>Die App bietet einen optionalen einmaligen Kauf, der Werbung entfernt und zusätzliche Funktionen freischaltet. Er wird über Google Play abgewickelt; Rückerstattungen richten sich nach den Richtlinien von Google Play.</p>"),
("Bereitstellung „wie besehen“",
 "<p>Die App wird „wie besehen“ bereitgestellt, ohne jegliche Gewährleistung. Der Herausgeber haftet nicht für direkte oder indirekte Schäden aus der Nutzung, soweit gesetzlich zulässig.</p>"),
("Anwendbares Recht",
 "<p>Diese Bedingungen unterliegen französischem Recht.</p>"),
("Kontakt",
 f"<p>Bei Fragen: <a href=\"mailto:{CONTACT}\">{CONTACT}</a></p>"),
]},

"es": {
"titre": "Condiciones de uso",
"intro": f"Al instalar y utilizar {APP} («la aplicación»), aceptas las condiciones descritas a continuación.",
"sections": [
("Objeto de la aplicación",
 f"<p>{APP} es una herramienta de ayuda personal para el seguimiento del cuidado de plantas de interior. No es un servicio profesional de horticultura ni de medicina veterinaria.</p>"),
("!Consejos de cultivo",
 "Las recomendaciones de cuidado (frecuencia de riego y abono, exposición a la luz) son <strong>indicaciones generales</strong>, basadas en datos públicos medios por especie. No sustituyen ni la observación de tu planta real ni el criterio de un profesional. La aplicación no garantiza la supervivencia de tus plantas."),
("!Toxicidad para los animales",
 "La información sobre toxicidad se facilita <strong>a título meramente informativo</strong> y no constituye en ningún caso un consejo veterinario. En caso de ingestión real o sospechada, contacta inmediatamente con un veterinario o un centro toxicológico veterinario — nunca te fíes solo de la aplicación en una urgencia."),
("Contenido añadido por el usuario",
 "<p>Puedes añadir tus propias plantas al catálogo local. Ese contenido permanece estrictamente local en tu dispositivo: no se comparte, ni se verifica, ni lo valida nadie. Eres el único responsable de la exactitud de lo que introduces.</p>"),
("Ausencia de copia de seguridad automática",
 "<p>La aplicación funciona sin conexión y no guarda tus datos en ningún servidor. Si desinstalas la aplicación, cambias de teléfono o pierdes tu dispositivo <strong>sin haber exportado antes una copia de seguridad</strong>, todos tus datos se perderán <strong>definitivamente</strong>. Realizar copias periódicas mediante la función prevista es responsabilidad tuya.</p>"),
("Compra integrada",
 "<p>La aplicación ofrece una compra única opcional que elimina la publicidad y desbloquea funciones adicionales. La gestiona Google Play; los reembolsos siguen su política.</p>"),
("Suministro «tal cual»",
 "<p>La aplicación se suministra «tal cual», sin garantía de ningún tipo. El editor no será responsable de daños directos o indirectos derivados de su uso, en la medida permitida por la ley aplicable.</p>"),
("Ley aplicable",
 "<p>Estas condiciones se rigen por el derecho francés.</p>"),
("Contacto",
 f"<p>Para cualquier duda: <a href=\"mailto:{CONTACT}\">{CONTACT}</a></p>"),
]},

"it": {
"titre": "Termini di utilizzo",
"intro": f"Installando e utilizzando {APP} (“l'applicazione”), accetti i termini descritti di seguito.",
"sections": [
("Oggetto dell'applicazione",
 f"<p>{APP} è uno strumento di supporto personale per seguire la cura delle piante da interno. Non è un servizio professionale di orticoltura né di medicina veterinaria.</p>"),
("!Consigli di coltivazione",
 "Le raccomandazioni di cura (frequenza di irrigazione e concimazione, esposizione alla luce) sono <strong>indicazioni generali</strong>, basate su dati pubblici medi per specie. Non sostituiscono né l'osservazione della tua pianta reale né il parere di un professionista. L'applicazione non garantisce la sopravvivenza delle tue piante."),
("!Tossicità per gli animali",
 "Le indicazioni sulla tossicità sono fornite <strong>a puro titolo informativo</strong> e non costituiscono in alcun caso un parere veterinario. In caso di ingestione reale o sospetta, contatta immediatamente un veterinario o un centro antiveleni per animali — non affidarti mai alla sola applicazione in un'emergenza."),
("Contenuti aggiunti dall'utente",
 "<p>Puoi aggiungere le tue piante al catalogo locale. Questi contenuti restano strettamente locali sul tuo dispositivo: non sono condivisi, né verificati, né validati da nessuno. Sei l'unico responsabile dell'esattezza di quanto inserisci.</p>"),
("Assenza di backup automatico",
 "<p>L'applicazione funziona offline e non salva i tuoi dati su alcun server. Se disinstalli l'applicazione, cambi telefono o perdi il dispositivo <strong>senza aver prima esportato un backup</strong>, tutti i tuoi dati andranno <strong>definitivamente persi</strong>. Effettuare backup regolari tramite l'apposita funzione è responsabilità tua.</p>"),
("Acquisto in-app",
 "<p>L'applicazione propone un acquisto una tantum facoltativo che rimuove la pubblicità e sblocca funzioni aggiuntive. È gestito da Google Play; i rimborsi seguono la politica di Google Play.</p>"),
("Fornitura “così com'è”",
 "<p>L'applicazione è fornita “così com'è”, senza garanzie di alcun tipo. L'editore non è responsabile per danni diretti o indiretti derivanti dal suo utilizzo, nei limiti consentiti dalla legge applicabile.</p>"),
("Legge applicabile",
 "<p>Questi termini sono regolati dal diritto francese.</p>"),
("Contatto",
 f"<p>Per qualsiasi domanda: <a href=\"mailto:{CONTACT}\">{CONTACT}</a></p>"),
]},
}
