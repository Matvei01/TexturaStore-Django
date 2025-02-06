from django.core.mail import send_mail
from django.conf import settings
from users.models import User
from promotions.models import Promotion
from django_q.tasks import async_task
from django_q.models import Schedule

def send_promotion_email():
    """Отправляет email всем подписанным пользователям с последней акцией."""
    subscribers = User.objects.filter(is_subscribed=True)
    
    if not subscribers.exists():
        return  # Если подписчиков нет, ничего не делаем

    try:
        last_promotion = Promotion.objects.latest("created_at")
    except Promotion.DoesNotExist:
        return  # Если акций нет, ничего не отправляем

    subject = f"{last_promotion.title}"
    message = last_promotion.description
    from_email = settings.EMAIL_HOST_USER

    recipient_list = [user.email for user in subscribers if user.email]

    if recipient_list:
        send_mail(subject, message, from_email, recipient_list)


def send_promotion_email_task():
    """Запускает рассылку писем в фоне через Django Q."""
    async_task(send_promotion_email)  # Запуск в фоне


Schedule.objects.update_or_create(
    name="Promotion Email Every 6 Days",
    func="users.tasks.send_promotion_email_task",  # Путь к задаче
    defaults={
        "schedule_type": Schedule.CRON,
        "cron": "0 0 */6 * *",  # Запуск каждые 6 дней в 00:00
        "repeats": -1,  # Бесконечные повторы
    },
)
