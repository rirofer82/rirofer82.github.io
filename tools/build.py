"""Genera las páginas de la web: index.html (portada), privacy/index.html (política común a todas las apps)
y una página por app (deepdoku/index.html).

Los textos de cada idioma (es, en, fr, pt) están aquí abajo; cada página lleva los cuatro y
assets/js/lang.js enseña el del navegador (o el que elija el visitante).

  python3 tools/build.py

Para publicar: commit y push a main; GitHub Pages sirve la rama main tal cual.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ['es', 'en', 'fr', 'pt']
NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'pt': 'Português'}
EMAIL = 'rr2apps@gmail.com'
DEV = 'RRF-APPS'
PLAY_URL = 'https://play.google.com/store/apps/details?id=io.github.rirofer82.deepdoku'
PLAY_LIVE = False          # cámbialo a True cuando Deepdoku esté publicado en Google Play
UPDATED = {'es': '11 de noviembre de 2026', 'en': '11 November 2026', 'fr': '11 novembre 2026', 'pt': '11 de novembro de 2026'}

UI = {
    'nav_apps': {'es': 'Apps', 'en': 'Apps', 'fr': 'Applis', 'pt': 'Apps'},
    'nav_privacy': {'es': 'Privacidad', 'en': 'Privacy', 'fr': 'Confidentialité', 'pt': 'Privacidade'},
    'contact': {'es': 'Contacto', 'en': 'Contact', 'fr': 'Contact', 'pt': 'Contato'},
    'play': {'es': 'Descargar en Google Play', 'en': 'Get it on Google Play', 'fr': 'Disponible sur Google Play', 'pt': 'Disponível no Google Play'},
    'soon': {'es': 'Muy pronto en Google Play', 'en': 'Coming soon to Google Play', 'fr': 'Bientôt sur Google Play', 'pt': 'Em breve no Google Play'},
    'privacy': {'es': 'Política de privacidad', 'en': 'Privacy policy', 'fr': 'Politique de confidentialité', 'pt': 'Política de privacidade'},
}

HOME = {
    'title': {'es': 'RRF-APPS', 'en': 'RRF-APPS', 'fr': 'RRF-APPS', 'pt': 'RRF-APPS'},
    'h1': {'es': 'Juegos y utilidades <span>para tu móvil</span>', 'en': 'Games and tools <span>for your phone</span>',
           'fr': 'Jeux et outils <span>pour ton mobile</span>', 'pt': 'Jogos e utilitários <span>para o seu celular</span>'},
    'lead': {'es': 'RRF-APPS es un desarrollador independiente de Madrid. Hago juegos cortos para el móvil con reglas que se entienden en un minuto.',
             'en': 'RRF-APPS is an independent developer from Madrid. I make short mobile games with rules you learn in a minute.',
             'fr': 'RRF-APPS est un développeur indépendant basé à Madrid. Je crée des jeux mobiles courts, avec des règles qu\'on comprend en une minute.',
             'pt': 'RRF-APPS é um desenvolvedor independente de Madri. Faço jogos curtos para celular, com regras que você aprende em um minuto.'},
    'apps': {'es': 'Apps', 'en': 'Apps', 'fr': 'Applis', 'pt': 'Apps'},
    'dd_short': {'es': 'Puzzle de lógica: encuentra las parejas de animales en el fondo del mar.',
                 'en': 'Logic puzzle: find the pairs of deep-sea animals hiding on the ocean floor.',
                 'fr': 'Puzzle de logique : trouve les paires d\'animaux cachées au fond de la mer.',
                 'pt': 'Quebra-cabeça de lógica: encontre os pares de animais no fundo do mar.'},
    'dd_tag': {'es': 'Puzzle · Próximamente', 'en': 'Puzzle · Coming soon', 'fr': 'Puzzle · Bientôt', 'pt': 'Quebra-cabeça · Em breve'},
}

DD = {
    'title': {'es': 'Deepdoku: Parejas del abismo', 'en': 'Deepdoku: Pairs of the Abyss', 'fr': 'Deepdoku : paires des abysses', 'pt': 'Deepdoku: Pares do abismo'},
    'tag': {'es': 'Parejas del abismo', 'en': 'Pairs of the abyss', 'fr': 'Les paires des abysses', 'pt': 'Pares do abismo'},
    'lead': {'es': 'Baja al fondo del mar y encuentra las parejas de animales que se esconden en cada zona. Un puzzle de lógica nuevo, con reglas que se entienden en un minuto y niveles que dan mucho que pensar.',
             'en': 'Dive to the bottom of the sea and find the pairs of animals hiding in every zone. A new logic puzzle with rules you learn in a minute and levels that really make you think.',
             'fr': 'Plonge au fond de la mer et trouve les paires d\'animaux cachées dans chaque zone. Un nouveau puzzle de logique, avec des règles qu\'on comprend en une minute et des niveaux qui font vraiment réfléchir.',
             'pt': 'Mergulhe até o fundo do mar e encontre os pares de animais escondidos em cada zona. Um quebra-cabeça de lógica novo, com regras que você aprende em um minuto e níveis que fazem pensar de verdade.'},
    'rules_h': {'es': 'Tres reglas', 'en': 'Three rules', 'fr': 'Trois règles', 'pt': 'Três regras'},
    'rules': {
        'es': ['Cada <b>zona de color</b> esconde <b>una pareja</b>: dos animales pegados, lado con lado.', 'Los <b>números</b> de los bordes dicen cuántos animales hay en cada fila y columna.', 'Las parejas <b>no se tocan</b> entre sí, ni siquiera en diagonal.'],
        'en': ['Each <b>coloured zone</b> hides <b>one pair</b>: two animals side by side.', 'The <b>numbers</b> on the edges tell how many animals are in each row and column.', 'Pairs <b>never touch</b> each other, not even diagonally.'],
        'fr': ['Chaque <b>zone de couleur</b> cache <b>une paire</b> : deux animaux collés, côte à côte.', 'Les <b>nombres</b> sur les bords indiquent combien d\'animaux il y a dans chaque ligne et colonne.', 'Les paires <b>ne se touchent pas</b>, même en diagonale.'],
        'pt': ['Cada <b>zona colorida</b> esconde <b>um par</b>: dois animais grudados, lado a lado.', 'Os <b>números</b> nas bordas dizem quantos animais há em cada linha e coluna.', 'Os pares <b>não se tocam</b>, nem na diagonal.'],
    },
    'more_h': {'es': 'De la superficie a la fosa', 'en': 'From the surface to the trench', 'fr': 'De la surface à la fosse', 'pt': 'Da superfície até a fossa'},
    'more': {
        'es': ['30 niveles en seis zonas de profundidad, de 4×4 a 8×8, todos con una única solución que se encuentra solo con lógica.', '3 burbujas de oxígeno por nivel: cada animal mal colocado gasta una.', 'Pistas que explican el porqué del siguiente paso.', 'Ocho especies de las profundidades, cada una con un dato curioso real.', 'En español, inglés, francés y portugués.'],
        'en': ['30 levels across six depth zones, from 4×4 to 8×8, each with a single solution you can reach with logic alone.', '3 oxygen bubbles per level: every misplaced animal uses one.', 'Hints that explain why the next step works.', 'Eight deep-sea species, each with a real fun fact.', 'In English, Spanish, French and Portuguese.'],
        'fr': ['30 niveaux dans six zones de profondeur, de 4×4 à 8×8, chacun avec une seule solution qu\'on trouve uniquement par la logique.', '3 bulles d\'oxygène par niveau : chaque animal mal placé en coûte une.', 'Des indices qui expliquent pourquoi l\'étape suivante fonctionne.', 'Huit espèces des abysses, chacune avec une vraie anecdote.', 'En français, anglais, espagnol et portugais.'],
        'pt': ['30 níveis em seis zonas de profundidade, de 4×4 a 8×8, todos com uma única solução que se encontra só com lógica.', '3 bolhas de oxigênio por nível: cada animal no lugar errado gasta uma.', 'Dicas que explicam o porquê do próximo passo.', 'Oito espécies do fundo do mar, cada uma com uma curiosidade real.', 'Em português, inglês, espanhol e francês.'],
    },
    'alt_feature': {'es': 'Tablero de puzzle con parejas de animales de las profundidades que brillan en el fondo del mar', 'en': 'Puzzle board with glowing pairs of deep-sea animals on the ocean floor',
                    'fr': 'Plateau de puzzle avec des paires d\'animaux des abysses qui brillent au fond de la mer', 'pt': 'Tabuleiro de quebra-cabeça com pares de animais do fundo do mar brilhando no oceano'},
    'alt_shot': {'es': 'Captura de Deepdoku', 'en': 'Deepdoku screenshot', 'fr': 'Capture d\'écran de Deepdoku', 'pt': 'Captura de tela do Deepdoku'},
}

# Apps a las que se aplica la política (añade aquí cada app nueva)
APPS = ['Deepdoku']

# Política de privacidad común a todas las apps: (título de sección, HTML) por idioma
def _apps(l):
    return ', '.join(APPS)

POLICY = {
    'es': {
        'title': f'Política de privacidad de {DEV}',
        'meta': f'Última actualización: {UPDATED["es"]}',
        'intro': f'Esta política se aplica a todas las apps y juegos que {DEV}, un desarrollador particular, publica en Google Play (actualmente: {_apps("es")}). Resumen: <b>nuestras apps no piden registro ni recogen datos personales</b>; tu progreso se guarda solo en tu móvil, y los anuncios los sirve Google AdMob, que puede usar el ID de publicidad del dispositivo.',
        'sections': [
            ('Responsable', f'<p>{DEV}. Contacto: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
            ('Datos que no recogemos', '<p>Nuestras apps no tienen cuentas de usuario propias y no recogen tu nombre, correo electrónico, ubicación, contactos, fotos ni ningún otro dato personal. No tenemos servidores propios: no recibimos ni almacenamos información sobre ti.</p>'),
            ('Datos que se guardan en tu móvil', '<p>Las apps guardan en su almacenamiento local tu progreso (por ejemplo, niveles superados, puntuaciones o estrellas) y tus ajustes (sonido, idioma). Estos datos no salen de tu dispositivo y se borran si desinstalas la app o borras sus datos desde los ajustes de Android.</p>'),
            ('Publicidad (Google AdMob)', '<p>Nuestras apps muestran anuncios de Google AdMob, un servicio de Google. Para mostrar los anuncios, medirlos, evitar el fraude y, si lo aceptas, personalizarlos, el SDK de Google Mobile Ads puede recoger y tratar:</p><ul><li>el ID de publicidad de tu dispositivo;</li><li>la dirección IP y una ubicación aproximada deducida de ella;</li><li>información del dispositivo y del sistema (modelo, versión de Android, idioma);</li><li>tus interacciones con los anuncios y datos de diagnóstico y rendimiento de la app.</li></ul><p>Algunas apps ofrecen anuncios bonificados: los ves solo si quieres, a cambio de una ventaja en el juego (por ejemplo, una pista), y no se recoge ningún dato adicional por ello.</p><p>Google trata estos datos según su propia política: <a href="https://policies.google.com/privacy">Política de privacidad de Google</a> y <a href="https://policies.google.com/technologies/partner-sites">cómo usa Google la información de las apps que utilizan sus servicios</a>.</p>'),
            ('Clasificaciones y logros (Google Play Juegos)', '<p>Si una app tiene clasificaciones o logros, usa Google Play Juegos. Si decides iniciar sesión, Google comparte con la app tu nombre de jugador, tu avatar y tus puntuaciones para mostrarlos en las clasificaciones. Lo gestiona Google según su <a href="https://policies.google.com/privacy">Política de privacidad</a> y puedes cambiar la visibilidad de tu perfil en la app Google Play Juegos.</p>'),
            ('Consentimiento', '<p>Si estás en el Espacio Económico Europeo, el Reino Unido o Suiza, al abrir la app se te pide el consentimiento para el uso de datos en la publicidad. Puedes cambiar tu elección cuando quieras en <b>Opciones de privacidad</b>, dentro de la información o los ajustes de cada app. También puedes restablecer o eliminar el ID de publicidad en <b>Ajustes de Android → Google → Anuncios</b>.</p>'),
            ('Menores', '<p>Nuestras apps no están dirigidas a menores de 13 años, aunque su contenido sea apto para todos los públicos. No recogemos a sabiendas datos de menores. Si crees que un menor nos ha facilitado datos, escríbenos y los eliminaremos.</p>'),
            ('Con quién se comparten los datos', '<p>No vendemos ni compartimos datos personales. Los únicos datos que salen del dispositivo son los que tratan los servicios de Google descritos arriba, siempre transmitidos de forma cifrada.</p>'),
            ('Tus derechos', '<p>De acuerdo con el RGPD tienes derecho de acceso, rectificación, supresión, oposición, limitación y portabilidad. Como nosotros no guardamos datos tuyos, para los datos de los servicios de Google puedes ejercerlos directamente ante Google o escribirnos y te ayudaremos. También puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es">www.aepd.es</a>).</p>'),
            ('Cambios en esta política', '<p>Si cambiamos esta política, publicaremos la nueva versión en esta misma página con la fecha de actualización.</p>'),
        ],
    },
    'en': {
        'title': f'{DEV} privacy policy',
        'meta': f'Last updated: {UPDATED["en"]}',
        'intro': f'This policy applies to all apps and games that {DEV}, an individual developer, publishes on Google Play (currently: {_apps("en")}). In short: <b>our apps do not ask you to sign up and do not collect personal data</b>; your progress is stored only on your phone, and ads are served by Google AdMob, which may use the device\'s advertising ID.',
        'sections': [
            ('Controller', f'<p>{DEV}. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
            ('Data we do not collect', '<p>Our apps have no user accounts of their own and do not collect your name, email address, location, contacts, photos or any other personal data. We have no servers of our own: we do not receive or store any information about you.</p>'),
            ('Data stored on your phone', '<p>The apps store your progress (for example completed levels, scores or stars) and your settings (sound, language) in their local storage. This data never leaves your device and is deleted if you uninstall the app or clear its data in Android settings.</p>'),
            ('Advertising (Google AdMob)', '<p>Our apps show ads from Google AdMob, a Google service. To show ads, measure them, prevent fraud and, if you agree, personalise them, the Google Mobile Ads SDK may collect and process:</p><ul><li>your device\'s advertising ID;</li><li>your IP address and an approximate location derived from it;</li><li>device and system information (model, Android version, language);</li><li>your interactions with ads, and app diagnostics and performance data.</li></ul><p>Some apps offer rewarded ads: you only watch them if you want to, in exchange for an in-game advantage (for example, a hint), and no additional data is collected for this.</p><p>Google processes this data under its own policy: <a href="https://policies.google.com/privacy">Google Privacy Policy</a> and <a href="https://policies.google.com/technologies/partner-sites">how Google uses information from apps that use its services</a>.</p>'),
            ('Leaderboards and achievements (Google Play Games)', '<p>If an app has leaderboards or achievements, it uses Google Play Games. If you choose to sign in, Google shares your player name, avatar and scores with the app to show them on the leaderboards. This is handled by Google under its <a href="https://policies.google.com/privacy">Privacy Policy</a>, and you can change your profile visibility in the Google Play Games app.</p>'),
            ('Consent', '<p>If you are in the European Economic Area, the United Kingdom or Switzerland, the app asks for your consent to the use of data for advertising when you open it. You can change your choice at any time in <b>Privacy options</b>, in each app\'s information or settings. You can also reset or delete your advertising ID in <b>Android Settings → Google → Ads</b>.</p>'),
            ('Children', '<p>Our apps are not directed at children under 13, even when their content is suitable for everyone. We do not knowingly collect data from children. If you believe a child has given us data, contact us and we will delete it.</p>'),
            ('Who data is shared with', '<p>We do not sell or share personal data. The only data that leaves the device is the data processed by the Google services described above, always transmitted in encrypted form.</p>'),
            ('Your rights', '<p>Under the GDPR you have the right of access, rectification, erasure, objection, restriction and portability. As we do not hold any of your data, you can exercise these rights for data processed by Google services directly with Google, or write to us and we will help you. You can also complain to your local data protection authority.</p>'),
            ('Changes to this policy', '<p>If we change this policy, we will publish the new version on this page with the date it was updated.</p>'),
        ],
    },
    'fr': {
        'title': f'Politique de confidentialité de {DEV}',
        'meta': f'Dernière mise à jour : {UPDATED["fr"]}',
        'intro': f'Cette politique s\'applique à toutes les applications et à tous les jeux que {DEV}, un développeur particulier, publie sur Google Play (actuellement : {_apps("fr")}). En résumé : <b>nos applications ne demandent pas de créer de compte et ne collectent pas de données personnelles</b> ; ta progression est enregistrée uniquement sur ton téléphone, et les publicités sont diffusées par Google AdMob, qui peut utiliser l\'identifiant publicitaire de l\'appareil.',
        'sections': [
            ('Responsable', f'<p>{DEV}. Contact : <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
            ('Données que nous ne collectons pas', '<p>Nos applications n\'ont pas de comptes utilisateur propres et ne collectent ni ton nom, ni ton adresse e-mail, ni ta position, ni tes contacts, ni tes photos, ni aucune autre donnée personnelle. Nous n\'avons pas de serveurs : nous ne recevons ni ne stockons aucune information sur toi.</p>'),
            ('Données enregistrées sur ton téléphone', '<p>Les applications enregistrent ta progression (par exemple niveaux terminés, scores ou étoiles) et tes réglages (son, langue) dans leur stockage local. Ces données ne quittent pas ton appareil et sont supprimées si tu désinstalles l\'application ou effaces ses données dans les paramètres d\'Android.</p>'),
            ('Publicité (Google AdMob)', '<p>Nos applications affichent des publicités Google AdMob, un service de Google. Pour afficher les publicités, les mesurer, prévenir la fraude et, si tu l\'acceptes, les personnaliser, le SDK Google Mobile Ads peut collecter et traiter :</p><ul><li>l\'identifiant publicitaire de ton appareil ;</li><li>ton adresse IP et une localisation approximative qui en est déduite ;</li><li>des informations sur l\'appareil et le système (modèle, version d\'Android, langue) ;</li><li>tes interactions avec les publicités ainsi que des données de diagnostic et de performance de l\'application.</li></ul><p>Certaines applications proposent des publicités récompensées : tu ne les regardes que si tu le veux, en échange d\'un avantage dans le jeu (par exemple un indice), et aucune donnée supplémentaire n\'est collectée pour cela.</p><p>Google traite ces données selon sa propre politique : <a href="https://policies.google.com/privacy">Règles de confidentialité de Google</a> et <a href="https://policies.google.com/technologies/partner-sites">comment Google utilise les informations des applications qui utilisent ses services</a>.</p>'),
            ('Classements et succès (Google Play Jeux)', '<p>Si une application a des classements ou des succès, elle utilise Google Play Jeux. Si tu choisis de te connecter, Google partage avec l\'application ton nom de joueur, ton avatar et tes scores pour les afficher dans les classements. Google gère ces données selon ses <a href="https://policies.google.com/privacy">Règles de confidentialité</a>, et tu peux modifier la visibilité de ton profil dans l\'application Google Play Jeux.</p>'),
            ('Consentement', '<p>Si tu te trouves dans l\'Espace économique européen, au Royaume-Uni ou en Suisse, l\'application te demande ton consentement à l\'utilisation des données pour la publicité à l\'ouverture. Tu peux modifier ton choix à tout moment dans <b>Options de confidentialité</b>, dans les informations ou les réglages de chaque application. Tu peux aussi réinitialiser ou supprimer ton identifiant publicitaire dans <b>Paramètres Android → Google → Annonces</b>.</p>'),
            ('Mineurs', '<p>Nos applications ne s\'adressent pas aux enfants de moins de 13 ans, même lorsque leur contenu convient à tous. Nous ne collectons pas sciemment de données concernant des mineurs. Si tu penses qu\'un enfant nous a fourni des données, contacte-nous et nous les supprimerons.</p>'),
            ('Avec qui les données sont partagées', '<p>Nous ne vendons ni ne partageons de données personnelles. Les seules données qui quittent l\'appareil sont celles traitées par les services Google décrits ci-dessus, toujours transmises de manière chiffrée.</p>'),
            ('Tes droits', '<p>Conformément au RGPD, tu disposes d\'un droit d\'accès, de rectification, d\'effacement, d\'opposition, de limitation et de portabilité. Comme nous ne conservons aucune donnée te concernant, tu peux exercer ces droits pour les données traitées par les services Google directement auprès de Google, ou nous écrire et nous t\'aiderons. Tu peux aussi introduire une réclamation auprès de la CNIL (<a href="https://www.cnil.fr">www.cnil.fr</a>) ou de l\'autorité de ton pays.</p>'),
            ('Modifications de cette politique', '<p>Si nous modifions cette politique, nous publierons la nouvelle version sur cette page avec sa date de mise à jour.</p>'),
        ],
    },
    'pt': {
        'title': f'Política de privacidade da {DEV}',
        'meta': f'Última atualização: {UPDATED["pt"]}',
        'intro': f'Esta política se aplica a todos os apps e jogos que a {DEV}, um desenvolvedor individual, publica no Google Play (atualmente: {_apps("pt")}). Em resumo: <b>nossos apps não pedem cadastro e não coletam dados pessoais</b>; seu progresso fica salvo só no seu celular, e os anúncios são exibidos pelo Google AdMob, que pode usar o ID de publicidade do dispositivo.',
        'sections': [
            ('Responsável', f'<p>{DEV}. Contato: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
            ('Dados que não coletamos', '<p>Nossos apps não têm contas de usuário próprias e não coletam seu nome, e-mail, localização, contatos, fotos nem nenhum outro dado pessoal. Não temos servidores próprios: não recebemos nem armazenamos informações sobre você.</p>'),
            ('Dados salvos no seu celular', '<p>Os apps salvam no armazenamento local o seu progresso (por exemplo, níveis concluídos, pontuações ou estrelas) e as suas configurações (som, idioma). Esses dados não saem do seu dispositivo e são apagados se você desinstalar o app ou limpar os dados dele nas configurações do Android.</p>'),
            ('Publicidade (Google AdMob)', '<p>Nossos apps exibem anúncios do Google AdMob, um serviço do Google. Para exibir os anúncios, medi-los, evitar fraudes e, se você concordar, personalizá-los, o SDK do Google Mobile Ads pode coletar e tratar:</p><ul><li>o ID de publicidade do seu dispositivo;</li><li>o endereço IP e uma localização aproximada obtida a partir dele;</li><li>informações do dispositivo e do sistema (modelo, versão do Android, idioma);</li><li>suas interações com os anúncios e dados de diagnóstico e desempenho do app.</li></ul><p>Alguns apps oferecem anúncios premiados: você só assiste se quiser, em troca de uma vantagem no jogo (por exemplo, uma dica), e nenhum dado adicional é coletado por isso.</p><p>O Google trata esses dados de acordo com a própria política: <a href="https://policies.google.com/privacy">Política de Privacidade do Google</a> e <a href="https://policies.google.com/technologies/partner-sites">como o Google usa as informações de apps que utilizam seus serviços</a>.</p>'),
            ('Placares e conquistas (Google Play Games)', '<p>Se um app tiver placares ou conquistas, ele usa o Google Play Games. Se você decidir entrar, o Google compartilha com o app seu nome de jogador, seu avatar e suas pontuações para exibi-los nos placares. Isso é gerenciado pelo Google de acordo com a <a href="https://policies.google.com/privacy">Política de Privacidade</a> dele, e você pode alterar a visibilidade do seu perfil no app Google Play Games.</p>'),
            ('Consentimento', '<p>Se você estiver no Espaço Econômico Europeu, no Reino Unido ou na Suíça, o app pede seu consentimento para o uso de dados em publicidade ao ser aberto. Você pode mudar sua escolha quando quiser em <b>Opções de privacidade</b>, nas informações ou configurações de cada app. Também pode redefinir ou excluir o ID de publicidade em <b>Configurações do Android → Google → Anúncios</b>.</p>'),
            ('Menores de idade', '<p>Nossos apps não são direcionados a menores de 13 anos, mesmo quando o conteúdo é adequado para todos os públicos. Não coletamos intencionalmente dados de menores. Se você acha que uma criança nos forneceu dados, entre em contato e vamos excluí-los.</p>'),
            ('Com quem os dados são compartilhados', '<p>Não vendemos nem compartilhamos dados pessoais. Os únicos dados que saem do dispositivo são os tratados pelos serviços do Google descritos acima, sempre transmitidos de forma criptografada.</p>'),
            ('Seus direitos', '<p>De acordo com a LGPD e o RGPD, você tem direito de acesso, correção, eliminação, oposição, limitação e portabilidade. Como não guardamos dados seus, para os dados tratados pelos serviços do Google você pode exercer esses direitos diretamente com o Google ou nos escrever, que ajudamos. Você também pode reclamar à ANPD (<a href="https://www.gov.br/anpd">www.gov.br/anpd</a>).</p>'),
            ('Alterações nesta política', '<p>Se alterarmos esta política, publicaremos a nova versão nesta página com a data de atualização.</p>'),
        ],
    },
}

def each(fn):
    """Un bloque por idioma: fn(l) → HTML."""
    return ''.join(f'<div data-l="{l}">{fn(l)}</div>' for l in LANGS)


def span(d):
    return ''.join(f'<span data-l="{l}">{d[l]}</span>' for l in LANGS)


def page(path, titles, body, desc, dark=False):
    depth = len(path.split('/')) if path else 0
    up = '../' * depth
    metas = ''.join(f'<meta name="title-{l}" content="{titles[l]}">' for l in LANGS)
    html = f'''<!doctype html>
<html lang="es" data-lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{titles["es"]}</title>
{metas}
<meta name="description" content="{desc}">
<meta name="theme-color" content="{'#081428' if dark else '#1f5fd6'}">
<link rel="icon" href="{up}favicon.png">
<link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Nunito:wght@500;700;800&display=swap">
<meta property="og:image" content="https://rirofer82.github.io/assets/img/og.jpg">
<link rel="stylesheet" href="{up}assets/css/site.css">
<script src="{up}assets/js/lang.js"></script>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="{up or './'}"><img src="{up}assets/img/rrf-logo.png" alt="">{DEV}</a>
  <nav class="links"><a href="{up or './'}#apps">{span(UI["nav_apps"])}</a><a href="{up}privacy/">{span(UI["nav_privacy"])}</a></nav>
  <div class="langs" id="langs">
    <button type="button" class="lang-toggle" aria-expanded="false" aria-controls="lang-list" aria-label="Idioma / Language"><span class="cur">ES</span><svg width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
    <div class="lang-list" id="lang-list" role="group" aria-label="Idioma / Language">{''.join(f'<button type="button" data-set="{l}" aria-pressed="{str(l == "es").lower()}"><b>{l.upper()}</b><span class="lname">{NAMES[l]}</span></button>' for l in LANGS)}</div>
  </div>
</div></header>
{body}
<footer class="bottom"><div class="wrap">
  <span>© 2026 {DEV}</span>
  <span>{span(UI["contact"])}: <a href="mailto:{EMAIL}">{EMAIL}</a></span>
</div></footer>
</body>
</html>
'''
    out = os.path.join(ROOT, path, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(html)
    print(out)


def play_button(l):
    if PLAY_LIVE:
        return f'<a class="btn" href="{PLAY_URL}">{UI["play"][l]}</a>'
    return f'<span class="btn soon">{UI["soon"][l]}</span>'


# portada
page('', HOME['title'], f'''
<main class="wrap">
  <section class="hero"><img class="banner" src="assets/img/banner.webp" alt="RRF-APPS" width="1600" height="900">{each(lambda l: f'<h1>{HOME["h1"][l]}</h1><p>{HOME["lead"][l]}</p>')}</section>
  <h2 class="section" id="apps">{span(HOME["apps"])}</h2>
  <div class="apps">
    <a class="app" href="deepdoku/"><img src="deepdoku/img/icon.webp" alt="" width="84" height="84">
      <div><h3>Deepdoku</h3>{each(lambda l: f'<p>{HOME["dd_short"][l]}</p><span class="tag">{HOME["dd_tag"][l]}</span>')}</div></a>
  </div>
</main>''', 'RRF-APPS: juegos y utilidades para Android.')

# Deepdoku
page('deepdoku', DD['title'], f'''
<main class="dd"><div class="wrap">
  <div class="dd-head"><img src="img/icon.webp" alt="" width="88" height="88"><div><h1>Deepdoku</h1><p>{span(DD["tag"])}</p></div></div>
  {each(lambda l: f'<img class="feature" src="img/feature-{l}.webp" alt="{DD["alt_feature"][l]}" width="1024" height="500"><div class="cta">{play_button(l)}<a href="../privacy/">{UI["privacy"][l]}</a></div>')}
  <div class="dd-body">
    {each(lambda l: f'<p>{DD["lead"][l]}</p><h2>{DD["rules_h"][l]}</h2><ul class="rules">' + ''.join(f'<li><span class="n">{i + 1}</span><span>{r}</span></li>' for i, r in enumerate(DD["rules"][l])) + '</ul>')}
    {each(lambda l: f'<h2>{DD["more_h"][l]}</h2><ul>' + ''.join(f'<li>{x}</li>' for x in DD["more"][l]) + '</ul>')}
  </div>
  {each(lambda l: '<div class="shots">' + ''.join(f'<img src="img/{l}-{n}.webp" alt="{DD["alt_shot"][l]}" width="540" height="960" loading="lazy">' for n in ("1_portada", "2_inmersion", "3_partida", "4_victoria", "5_niveles")) + '</div>')}
</div></main>''', 'Deepdoku: puzzle de lógica de parejas de animales de las profundidades para Android.', dark=True)

# política de privacidad
def policy(l):
    p = POLICY[l]
    secs = ''.join(f'<h2>{i + 1}. {h}</h2>{b}' for i, (h, b) in enumerate(p['sections']))
    return f'<h1>{p["title"]}</h1><p class="meta">{p["meta"]}</p><div class="box"><p>{p["intro"]}</p></div>{secs}'

page('privacy', {l: POLICY[l]['title'] for l in LANGS}, f'<main class="wrap narrow legal">{each(policy)}</main>',
     f'Política de privacidad de las apps de {DEV}.')
