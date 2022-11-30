
#Variables

isLogin = False
isAdmin = False

category = None
user = None

#Data

categoryes = [
    'Все',
    'Мучное',
    'Мясное',
    'Напитки'
]

products = [
    {
        'name': 'Багет',
        'img': 'https://i.obozrevatel.com/food/recipemain/2020/2/22/oblozhka1.jpg?size=636x424',
        'price': float(4),
        'category': 'Мучное'
    },
    {
        'name': 'Колбаса',
        'img': 'https://greenferma.com.ua/image/44499.jpg',
        'price': float(8),
        'category': 'Мясное'
    },
    {
        'name': 'Живчик',
        'img': 'https://aquamarket.ua/6670-large_default/zyvchik-yabloko-2.jpg',
        'price': float(2.99),
        'category': 'Напитки'
    },
    {
        'name': 'Булочки',
        'img': 'https://receptisalatov.com/content/recipes/1005/main_b_bulochki-s-izyumom-i-tsukatami.jpg',
        'price': float(1.99),
        'category': 'Мучное'
    },
    {
        'name': "Сосиски в тесет",
        'img': 'https://img-global.cpcdn.com/recipes/fce136b538504ba0/680x482cq70/bulochki-s-sosiskoi-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D0%B5-%D1%84%D0%BE%D1%82%D0%BE-%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D0%B0.jpg',
        'price': float(3.99),
        'category': 'Мучное'
    },
    {
        'name': "Шашлык",
        'img': 'https://e1.edimdoma.ru/data/posts/0002/4755/24755-ed4_wide.jpg?1651762197',
        'price': float(10),
        'category': 'Мясное'
    },
    {
        'name': "Кола",
        'img': 'https://produkty24.com.ua/db_pic/products/original/original_1459283981.4437038898468.jpg',
        'price': float(1.99),
        'category': 'Напитки'
    },
    {
        'name': "Балтика",
        'img': 'https://produkty24.com.ua/db_pic/products/original/img_64949_[1575469971.2531].jpg',
        'price': float(3.99),
        'category': 'Напитки'
    },
    {
        'name': "Шаурма",
        'img': 'https://img.delo-vcusa.ru/2019/11/arabskaja-shaurma.jpg',
        'price': float(5),
        'category': 'Мясное'
    },
]

basket = []

users = [
    {
        'login': 'user',
        'password': '1234',
        'img': 'https://www.president.gov.ua/storage/j-image-storage/14/34/45/b6638a3f2f9eb132a2315e2bebabcd3e_1572854231_wysiwyg.jpeg',
        'isAdmin': False
    },
    {
        'login': 'admin',
        'password': 'admin',
        'img': 'https://i.ytimg.com/vi/PV55crnLk0A/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AGYBYAC4AOKAgwIABABGEMgUShlMA8=&rs=AOn4CLBECtAowFChAzuDRIIW5niEtLo9xQ',
        'isAdmin': True
    }
]

#Functions

def GetProductByName(name: str):
    for product in products:
        if(product['name'] == name):
            return product
    return None
