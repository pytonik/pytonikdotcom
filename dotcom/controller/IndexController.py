from pytonik import Web as mvc

m = mvc.App()
Doc = mvc.Load('Doc')

def index():

    impnav = Doc.importantnav(1, 9)
    data = {
        'title': "Pytonik",
        'countnav': impnav[0],
        'listnav': impnav[1],
        "about": "about",
        "aboutxt": "Pytonik is a python framework built to enhance web development, also helps web developers to build more apps with less codes. It uses expressive architectural patterns, structured on Model View Controller (MVC) and bundles of component to reuse while deploying the framework.",
        'v': '1.9.11',
        'description': 'Pytonik is a python framework built to enhance web development, also helps web developers to build more apps with less codes. It uses expressive architectural patterns, structured on Model View Controller (MVC) and bundles of component to reuse while deploying the framework. ',
        'keyword': 'code, python code, web ai, pytonik, python, mvc, python framework, framework, web framework, mvc framework, web, web with python, web with pytonik, web design, web developer, web development, webpy, web python, python developer, python programmers ',
        'subtitle': "how to? ",
        'subtitlesub': "Pytonik is a portable web framework, it uses expressive architectural pattern, structured on model view controller <strong>(MVC)</strong> ",
        'text': 'Enhances app development faster and easier with less codes',
        'fast': 'Fast',
        'fastxt': 'Pytonik framework was built to enhance faster and easier web development',
        'scalable': 'Scalable',
        'versatile': 'Versatile',
        'versatiletxt': 'Pytonik create an open door for developers to improve their skills also increase jobs opportunities for freelancing and full-time employment.',
        'secure': 'Secure',
        'scalabletxt': 'Pytonik is structured on Model View Controller (MVC) and offers a lite-weight template engine that make app development more faster.',
        'securetxt': "Pytonik responds to security and provides help for developers to eradicates vulnerabilities.",

    }

    return m.views('home/index', data)
