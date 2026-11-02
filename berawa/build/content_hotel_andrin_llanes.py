# Contenido de la demo Hotel Andrín (Andrín, Llanes) (es/en/fr/de). Hechos de hotelandrin.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Apartamentos 1, 2 y 3','Apartamentos 4 y 5','Apartamentos 6 y 8'],'en':['Apartments 1, 2 and 3','Apartments 4 and 5','Apartments 6 and 8'],'fr':['Appartements 1, 2 et 3','Appartements 4 et 5','Appartements 6 et 8'],'de':['Apartments 1, 2 und 3','Apartments 4 und 5','Apartments 6 und 8']}
RD={
'es':['En planta baja, para 2 adultos y 2 niños, con terraza a un pequeño jardín, baño completo, cocina y salón.','Para 4 personas, con dos amplias habitaciones, baño completo, cocina y salón.','Para 4 personas, con dos habitaciones, cada una con su propio baño, cocina y salón.'],
'en':['On the ground floor, for 2 adults and 2 children, with a terrace onto a small garden, full bathroom, kitchen and living room.','For 4 people, with two large bedrooms, full bathroom, kitchen and living room.','For 4 people, with two bedrooms, each with its own bathroom, kitchen and living room.'],
'fr':['En rez-de-chaussée, pour 2 adultes et 2 enfants, avec terrasse sur un petit jardin, salle de bains complète, cuisine et salon.','Pour 4 personnes, avec deux grandes chambres, salle de bains complète, cuisine et salon.','Pour 4 personnes, avec deux chambres ayant chacune sa salle de bains, cuisine et salon.'],
'de':['Im Erdgeschoss, für 2 Erwachsene und 2 Kinder, mit Terrasse zu einem kleinen Garten, komplettem Bad, Küche und Wohnzimmer.','Für 4 Personen, mit zwei großen Schlafzimmern, komplettem Bad, Küche und Wohnzimmer.','Für 4 Personen, mit zwei Schlafzimmern mit jeweils eigenem Bad, Küche und Wohnzimmer.']}
ART={
'hero':('waves',1611,['#14303a','#4f9aa8','#dcefef','#3f6f78','#2a525b','#0e2228']),
'intro':('hills',1612,['#eef3ea','#dce8d2','#8fb07a','#6f8a60','#516847','#33442c']),
'r1':('hills',1621,['#eef3ea','#dce8d2','#8fb07a','#6f8a60','#516847','#33442c']),
'r2':('columns',1622,['#f2f5f4','#f9fbfa','#2f6b74','#55615f','#22302f']),
'r3':('skyline',1623,['#14303a','#5aa4b1','#e2f2f2','#477a83','#2f5a63','#0e2228']),
'g1':('waves',1631,['#14303a','#4f9aa8','#dcefef','#3f6f78','#2a525b','#0e2228']),
'g2':('hills',1632,['#eef3ea','#dce8d2','#8fb07a','#6f8a60','#516847','#33442c']),
'g3':('arches',1633,['#f2f5f4','#d7e6e6','#2f6b74','#55615f','#22302f']),
'g4':('skyline',1634,['#14303a','#5aa4b1','#e2f2f2','#477a83','#2f5a63','#0e2228'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Andrín · Apartamentos en Andrín, Llanes, a 400 m de la playa',see_rooms='Ver apartamentos',hero_k='Andrín · Llanes · Asturias',hero_t='Apartamentos en Andrín, a 400 m de la playa',hero_s='Una zona muy tranquila, junto a la senda costera y el campo de golf municipal, a menos de 5 minutos de Llanes.',
 intro_t='Como en casa, en el Oriente de Asturias',intro_p1='Siete apartamentos modernos y acogedores, cuidados hasta el último detalle, con wifi en todo el hotel, jardín, terraza exterior y aparcamiento privado.',
 intro_p2='A menos de 5 minutos de Llanes y de más de 20 playas del Oriente de Asturias, como Andrín, Gulpiyuri, Torimbia o Cuevas del Mar.',
 stats=['7 apartamentos','A 400 m de la playa','Parking gratis','WiFi gratis'],nav_rooms='Apartamentos',rooms_t='Apartamentos',rooms_s='Con cocina completa, lavavajillas, lavadora, cafetera, microondas, calefacción, televisión, bañera y secador.',
 svcs=['Parking privado gratuito','WiFi gratis en todo el hotel','Jardín y terraza exterior','Rutas en bicicleta guiadas y gratuitas','Información turística y ayuda para organizar actividades','Campo de golf municipal «La Cuesta» al lado'],
 loc_p='Andrín, s/n · 33596 Llanes (Asturias). Teléfonos: 985 417 453 · 638 004 162. Correo: info@hotelandrin.com.',
 chips=['¿Qué apartamentos tenéis?','¿Tenéis parking?','¿Está cerca la playa?','¿Cómo reservo?']),
'en':dict(title='Hotel Andrín · Apartments in Andrín, Llanes, 400 m from the beach',see_rooms='See apartments',hero_k='Andrín · Llanes · Asturias',hero_t='Apartments in Andrín, 400 m from the beach',hero_s='A very quiet area by the coastal path and the municipal golf course, less than 5 minutes from Llanes.',
 intro_t='At home in eastern Asturias',intro_p1='Seven modern, cosy apartments, cared for down to the last detail, with wifi throughout, garden, outdoor terrace and private parking.',
 intro_p2='Less than 5 minutes from Llanes and more than 20 beaches of eastern Asturias, such as Andrín, Gulpiyuri, Torimbia and Cuevas del Mar.',
 stats=['7 apartments','400 m from the beach','Free parking','Free WiFi'],nav_rooms='Apartments',rooms_t='Apartments',rooms_s='With full kitchen, dishwasher, washing machine, coffee maker, microwave, heating, TV, bathtub and hairdryer.',
 svcs=['Free private parking','Free WiFi throughout','Garden and outdoor terrace','Free guided bike routes','Tourist information and help organising activities','«La Cuesta» municipal golf course next door'],
 loc_p='Andrín, s/n · 33596 Llanes (Asturias). Phones: +34 985 417 453 · +34 638 004 162. Email: info@hotelandrin.com.',
 chips=['Which apartments do you have?','Do you have parking?','Is the beach close?','How do I book?']),
'fr':dict(title='Hotel Andrín · Appartements à Andrín, Llanes, à 400 m de la plage',see_rooms='Voir les appartements',hero_k='Andrín · Llanes · Asturies',hero_t='Appartements à Andrín, à 400 m de la plage',hero_s='Un coin très calme, près du sentier côtier et du golf municipal, à moins de 5 minutes de Llanes.',
 intro_t='Comme chez soi, dans l’est des Asturies',intro_p1='Sept appartements modernes et chaleureux, soignés jusque dans les moindres détails, avec wifi partout, jardin, terrasse extérieure et parking privé.',
 intro_p2='À moins de 5 minutes de Llanes et de plus de 20 plages de l’est des Asturies, comme Andrín, Gulpiyuri, Torimbia ou Cuevas del Mar.',
 stats=['7 appartements','À 400 m de la plage','Parking gratuit','WiFi gratuit'],nav_rooms='Appartements',rooms_t='Appartements',rooms_s='Avec cuisine équipée, lave-vaisselle, lave-linge, cafetière, micro-ondes, chauffage, télévision, baignoire et sèche-cheveux.',
 svcs=['Parking privé gratuit','WiFi gratuit partout','Jardin et terrasse extérieure','Balades à vélo guidées et gratuites','Infos touristiques et aide pour organiser des activités','Golf municipal «La Cuesta» à côté'],
 loc_p='Andrín, s/n · 33596 Llanes (Asturies). Téléphones : +34 985 417 453 · +34 638 004 162. E-mail : info@hotelandrin.com.',
 chips=['Quels appartements avez-vous ?','Avez-vous un parking ?','La plage est-elle proche ?','Comment réserver ?']),
'de':dict(title='Hotel Andrín · Apartments in Andrín, Llanes, 400 m vom Strand',see_rooms='Apartments ansehen',hero_k='Andrín · Llanes · Asturien',hero_t='Apartments in Andrín, 400 m vom Strand',hero_s='Eine sehr ruhige Gegend am Küstenweg und am städtischen Golfplatz, weniger als 5 Minuten von Llanes.',
 intro_t='Wie zu Hause im Osten Asturiens',intro_p1='Sieben moderne, gemütliche Apartments, bis ins Detail gepflegt, mit WLAN im ganzen Haus, Garten, Außenterrasse und Privatparkplatz.',
 intro_p2='Weniger als 5 Minuten von Llanes und von über 20 Stränden im Osten Asturiens, etwa Andrín, Gulpiyuri, Torimbia oder Cuevas del Mar.',
 stats=['7 Apartments','400 m zum Strand','Kostenloser Parkplatz','Kostenloses WLAN'],nav_rooms='Apartments',rooms_t='Apartments',rooms_s='Mit voll ausgestatteter Küche, Geschirrspüler, Waschmaschine, Kaffeemaschine, Mikrowelle, Heizung, Fernseher, Badewanne und Föhn.',
 svcs=['Kostenloser Privatparkplatz','Kostenloses WLAN im ganzen Haus','Garten und Außenterrasse','Kostenlose geführte Radtouren','Touristeninfos und Hilfe bei der Planung von Aktivitäten','Städtischer Golfplatz «La Cuesta» nebenan'],
 loc_p='Andrín, s/n · 33596 Llanes (Asturien). Telefon: +34 985 417 453 · +34 638 004 162. E-Mail: info@hotelandrin.com.',
 chips=['Welche Apartments gibt es?','Gibt es einen Parkplatz?','Ist der Strand in der Nähe?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
BOOK=dict(mode='mail',email='info@hotelandrin.com')
D=dict(name='Hotel Andrín',ac='#14303a',ac2='#2f6b74',ac2_a11y='#285d65',book=BOOK,around=[],foot=FOOT,
 address='Andrín, s/n · 33596 Llanes',phones=['+34 985 417 453','+34 638 004 162'],emails=['info@hotelandrin.com'],maps='Hotel Andrín, Andrín, 33596 Llanes, Asturias',t=T)
META=dict(repo='demo-hotel-andrin-llanes',name='Hotel Andrín',legal_name='DIOLTUR, S. L., NIF B33661067, nombre comercial Hotel Andrín (aviso legal de su web)',registry_ids=['B33661067'],
 url='https://hotelandrin.com/',domain='hotelandrin.com',municipality='Llanes',province='Asturias',sector='hotel rural de apartamentos en Andrín, Llanes',
 read_at='2026-11-02T10:49:00+01:00',created_at='2026-11-02T10:48:00+01:00',built_at='2026-11-02T11:20:00+01:00',audit_date='2026-11-02T10:49:00+01:00',
 rating=dict(value=4.7,coincide=['tel','web'],date='2026-10-30',url='https://www.google.com/maps/search/Hotel+Rural+Andrin+Llanes'),
 book=dict(mode='mail',url='mailto:info@hotelandrin.com',note='sin motor de reservas: los botones Reservar de su pagina /precios/ no llevan a ningun sitio (href="#") y su contacto da telefono y correo. Los botones Reservar de la demo abren un correo a info@hotelandrin.com y los telefonos reales 985 417 453 y 638 004 162 van en tel: (mismo criterio que San Martin, Nastasi y Lupercas).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué apartamentos tenéis?','K01'),('¿Qué tienen los apartamentos?','K02'),('¿Tenéis parking?','K03'),('¿Está cerca la playa?','K04'),('¿Hay wifi?','K05'),('¿Dónde estáis?','K06'),('¿Cómo reservo?','K07'),('¿Podéis confirmarme disponibilidad para mañana?','K07'),('¿Hacéis rutas en bicicleta?','K08'),('¿Hay campo de golf cerca?','K09'),('¿Qué actividades se pueden hacer?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Cómo llego desde Oviedo?','K12'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which apartments do you have?','K01'),('What do the apartments include?','K02'),('Do you have parking?','K03'),('Is the beach close?','K04'),('Is there wifi?','K05'),('Where are you?','K06'),('How do I book?','K07'),('Can you confirm availability for tomorrow?','K07'),('Do you organise bike routes?','K08'),('Is there a golf course nearby?','K09'),('What activities can I do?','K10'),('What is your phone number?','K11'),('How do I get there from Oviedo?','K12'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quels appartements avez-vous ?','K01'),('Que comprennent les appartements ?','K02'),('Avez-vous un parking ?','K03'),('La plage est-elle proche ?','K04'),('Y a-t-il le wifi ?','K05'),('Où êtes-vous ?','K06'),('Comment réserver ?','K07'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K07'),('Organisez-vous des balades à vélo ?','K08'),('Y a-t-il un golf à proximité ?','K09'),('Quelles activités peut-on faire ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Comment venir depuis Oviedo ?','K12'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Apartments gibt es?','K01'),('Was bieten die Apartments?','K02'),('Gibt es einen Parkplatz?','K03'),('Ist der Strand in der Nähe?','K04'),('Gibt es WLAN?','K05'),('Wo liegt das Haus?','K06'),('Wie kann ich buchen?','K07'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K07'),('Organisieren Sie Radtouren?','K08'),('Gibt es einen Golfplatz in der Nähe?','K09'),('Welche Aktivitäten kann man machen?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Wie komme ich von Oviedo hin?','K12'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
