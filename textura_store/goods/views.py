from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Textura - Каталог",
        "goods": [
            {
                "name": "Хлопковая ткань для постельного белья",
                "description": "Мягкая и дышащая ткань из 100% хлопка для комфортного сна.",
                "price": 15.00,
                "image": "deps/images/fabrics/cotton_bedding.jpg",
            },
            {
                "name": "Хлопковая ткань для рубашек",
                "description": "Лёгкая и прочная ткань для пошива стильной одежды.",
                "price": 12.50,
                "image": "deps/images/fabrics/cotton_shirts.jpg",
            },
            {
                "name": "Хлопковая ткань для скатертей",
                "description": "Плотная ткань с защитным покрытием, идеальная для кухонных аксессуаров.",
                "price": 10.00,
                "image": "deps/images/fabrics/cotton_tablecloths.jpg",
            },
            {
                "name": "Ткань из органического хлопка",
                "description": "Экологически чистая ткань для пошива одежды и аксессуаров.",
                "price": 18.00,
                "image": "deps/images/fabrics/organic_cotton.jpg",
            },
            {
                "name": "Хлопковая ткань с цветочным узором",
                "description": "Яркий и привлекательный узор для создания летнего настроения.",
                "price": 14.00,
                "image": "deps/images/fabrics/cotton_flower_pattern.jpg",
            },
            {
                "name": "Плотный хлопковый сатин",
                "description": "Шелковистая ткань, подходящая для постельного белья премиум-класса.",
                "price": 20.00,
                "image": "deps/images/fabrics/cotton_satin.jpg",
            },
            {
                "name": "Шерстяной кашемир",
                "description": "Ультра мягкая ткань для тёплых пальто и шарфов.",
                "price": 35.00,
                "image": "deps/images/fabrics/wool_cashmere.jpg",
            },
            {
                "name": "Шерсть мериноса",
                "description": "Дышащая и эластичная ткань для активного образа жизни.",
                "price": 25.00,
                "image": "deps/images/fabrics/wool_merino.jpg",
            },
            {
                "name": "Плотная шерстяная ткань",
                "description": "Идеально подходит для создания зимних пальто и жакетов.",
                "price": 30.00,
                "image": "deps/images/fabrics/wool_thick.jpg",
            },
            {
                "name": "Шерстяная ткань с узором «гусиная лапка»",
                "description": "Классический узор для стильных костюмов.",
                "price": 28.00,
                "image": "deps/images/fabrics/wool_houndstooth.jpg",
            },
            {
                "name": "Шерстяной твид",
                "description": "Прочная и теплая ткань для костюмов и юбок.",
                "price": 22.00,
                "image": "deps/images/fabrics/wool_tweed.jpg",
            },
            {
                "name": "Шерстяная ткань с кашемиром",
                "description": "Смесь шерсти и кашемира для создания уютных вещей.",
                "price": 40.00,
                "image": "deps/images/fabrics/wool_cashmere_mix.jpg",
            },
            {
                "name": "Натуральный шёлк",
                "description": "Роскошная ткань для вечерних платьев и блузок.",
                "price": 50.00,
                "image": "deps/images/fabrics/silk_natural.jpg",
            },
            {
                "name": "Шёлковый атлас",
                "description": "Идеален для создания свадебных платьев и костюмов.",
                "price": 55.00,
                "image": "deps/images/fabrics/silk_atlas.jpg",
            },
            {
                "name": "Шёлковый шифон",
                "description": "Прозрачная ткань для лёгких платьев и шарфов.",
                "price": 45.00,
                "image": "deps/images/fabrics/silk_chiffon.jpg",
            },
            {
                "name": "Шёлковая органза",
                "description": "Лёгкая и блестящая ткань для декоративных элементов.",
                "price": 48.00,
                "image": "deps/images/fabrics/silk_organza.jpg",
            },
            {
                "name": "Шёлковый крепдешин",
                "description": "Матовая ткань для пошива элегантной одежды.",
                "price": 52.00,
                "image": "deps/images/fabrics/silk_crepe.jpg",
            },
            {
                "name": "Шёлковая ткань с узором",
                "description": "Яркий дизайн для уникальных изделий.",
                "price": 60.00,
                "image": "deps/images/fabrics/silk_patterned.jpg",
            },
            {
                "name": "Натуральный лен",
                "description": "Дышащая ткань для создания летней одежды.",
                "price": 18.00,
                "image": "deps/images/fabrics/linen_natural.jpg",
            },
            {
                "name": "Льняная ткань для штор",
                "description": "Прочная и стильная ткань для декорирования окон.",
                "price": 20.00,
                "image": "deps/images/fabrics/linen_curtains.jpg",
            },
            {
                "name": "Цветной лен",
                "description": "Яркая и стойкая ткань для различных интерьеров.",
                "price": 22.00,
                "image": "deps/images/fabrics/linen_colored.jpg",
            },
            {
                "name": "Льняной габардин",
                "description": "Износостойкая ткань для стильных изделий.",
                "price": 25.00,
                "image": "deps/images/fabrics/linen_gabardine.jpg",
            },
            {
                "name": "Льняной жаккард",
                "description": "Уникальная ткань с замысловатым узором.",
                "price": 30.00,
                "image": "deps/images/fabrics/linen_jacquard.jpg",
            },
            {
                "name": "Смесь льна и хлопка",
                "description": "Приятная на ощупь ткань для универсального использования.",
                "price": 15.00,
                "image": "deps/images/fabrics/linen_cotton_mix.jpg",
            },
            {
                "name": "Полиэстер",
                "description": "Прочная и износостойкая ткань для пошива одежды.",
                "price": 12.00,
                "image": "deps/images/fabrics/synthetic_polyester.jpg",
            },
            {
                "name": "Нейлон",
                "description": "Лёгкая ткань для спортивной и повседневной одежды.",
                "price": 15.00,
                "image": "deps/images/fabrics/synthetic_nylon.jpg",
            },
            {
                "name": "Акриловая ткань",
                "description": "Ткань, напоминающая шерсть, но более лёгкая.",
                "price": 10.00,
                "image": "deps/images/fabrics/synthetic_acrylic.jpg",
            },
            {
                "name": "Эластан",
                "description": "Эластичная ткань для спортивной и комфортной одежды.",
                "price": 20.00,
                "image": "deps/images/fabrics/synthetic_lycra.jpg",
            },
            {
                "name": "Микрофибра",
                "description": "Мягкая ткань для постельного белья и одежды.",
                "price": 18.00,
                "image": "deps/images/fabrics/synthetic_microfiber.jpg",
            },
            {
                "name": "Полиамид",
                "description": "Прочная ткань для верхней одежды.",
                "price": 22.00,
                "image": "deps/images/fabrics/synthetic_polyamide.jpg",
            },
            {
                "name": "Трикотажная ткань для платьев",
                "description": "Эластичная и мягкая ткань для пошива повседневной одежды.",
                "price": 15.00,
                "image": "deps/images/fabrics/knit_dress.jpg",
            },
            {
                "name": "Трикотажный хлопок",
                "description": "Дышащая ткань для спортивной одежды.",
                "price": 18.00,
                "image": "deps/images/fabrics/knit_cotton.jpg",
            },
            {
                "name": "Шерстяной трикотаж",
                "description": "Теплая ткань для создания уютных вещей.",
                "price": 22.00,
                "image": "deps/images/fabrics/knit_wool.jpg",
            },
            {
                "name": "Трикотаж с узором",
                "description": "Ткань с ярким дизайном для уникальных изделий.",
                "price": 25.00,
                "image": "deps/images/fabrics/knit_pattern.jpg",
            },
            {
                "name": "Эластичный трикотаж",
                "description": "Идеален для создания обтягивающей одежды.",
                "price": 20.00,
                "image": "deps/images/fabrics/knit_stretch.jpg",
            },
            {
                "name": "Смешанный трикотаж",
                "description": "Смесь натуральных и синтетических волокон для универсальности.",
                "price": 18.00,
                "image": "deps/images/fabrics/knit_mix.jpg",
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
