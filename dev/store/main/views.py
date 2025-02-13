from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Textura - Главная'
        context['content'] = "Магазин тканей Textura"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Textura - О нас",
            "content": "О нас",
            "text_on_page": (
                "Добро пожаловать в **Textura** — интернет-магазин тканей, где качество, стиль и уют встречаются в каждой фактуре!\n\n"
                "🔹 **О нас**\n"
                "Мы предлагаем широкий ассортимент тканей для штор, мебели, одежды и текстильного декора, помогая воплотить самые смелые дизайнерские идеи.\n\n"
                "🎯 **Что мы предлагаем?**\n"
                "- Натуральные и синтетические ткани высокого качества\n"
                "- Коллекции от ведущих производителей\n"
                "- Большой выбор расцветок, фактур и дизайнов\n"
                "- Индивидуальный пошив и бесплатные образцы\n\n"
                "💡 **Почему выбирают нас?**\n"
                "- Широкий ассортимент тканей в наличии\n"
                "- Доставка по всей России\n"
                "- Гибкие условия оплаты и скидки для постоянных клиентов\n"
                "- Консультации по подбору материалов и дизайнерским решениям\n\n"
                "Создавайте стильный и уютный интерьер с **Textura** – вашим надежным партнером в мире тканей!"
            ),
        })
        return context
    
class ContactsView(TemplateView):
    template_name = 'main/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Textura - Контакты",
            "content": "Наши контакты",
            "text_on_page": "",
            "city": "Москва",
            "street": "Тверская",
            "house_number": "10",
            "office_number": "15",
            "phone_mobile": "+7 (999) 123-45-67",
            "phone_landline": "+7 (495) 765-43-21",
            "email_info": "info@example.com",
            "email_partners": "partners@example.com",
            "email_support": "support@example.com",
            "work_hours_week": "09:00 – 18:00",
            "work_hours_weekend": "Выходной",
            "social_telegram": "#",
            "social_vk": "#",
            "social_instagram": "#",
            "social_youtube": "#",
        })
        return context
 
    