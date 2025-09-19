import win32com.client as win32
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

# Конфигурация
EXCEL_FILE_PATH = 'I:\ОИС\протокол операционных задач\подключение в базу.xlsx'  # Путь к файлу на сервере
SMTP_SERVER = 'smtp.yourmailserver.com'  # SMTP сервер
SMTP_PORT = 587  # Порт SMTP
EMAIL_FROM = 'boklogov.vs@7utra.ru'  # Отправитель
EMAIL_TO = 'boklogov.vs@7utra.ru'  # Получатель
EMAIL_SUBJECT = 'Отчет "протокол операционных задач" обновлен'  # Тема письма
SMTP_USERNAME = 'your_email@domain.com'  # Логин SMTP
SMTP_PASSWORD = 'your_password'  # Пароль SMTP


def refresh_excel_connections():
    """Обновляет все подключения в Excel файле"""
    try:
        # Инициализируем Excel
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = False  # Работаем в фоновом режиме
        excel.DisplayAlerts = False  # Отключаем предупреждения

        # Открываем файл
        wb = excel.Workbooks.Open(EXCEL_FILE_PATH)

        # Обновляем все подключения
        wb.RefreshAll()

        # Ждем завершения обновления
        excel.CalculateUntilAsyncQueriesDone()

        # Сохраняем и закрываем
        wb.Save()
        wb.Close()
        excel.Quit()

        print(f"Все подключения в файле {EXCEL_FILE_PATH} успешно обновлены")
        return True
    except Exception as e:
        print(f"Ошибка при обновлении Excel: {str(e)}")
        return False
    finally:
        # Убедимся, что Excel закрыт
        if 'excel' in locals():
            excel.Quit()


def send_email_notification():
    """Отправляет email уведомление"""
    try:
        # Создаем сообщение
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = EMAIL_SUBJECT

        # Текст письма
        body = f"""
        Все подключения к данным в отчете были успешно обновлены.

        Путь к файлу: {EXCEL_FILE_PATH}
        Время обновления: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}

        Это автоматическое сообщение, пожалуйста, не отвечайте на него.
        """
        msg.attach(MIMEText(body, 'plain'))

        # Отправляем письмо
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        print("Email уведомление отправлено")
        return True
    except Exception as e:
        print(f"Ошибка при отправке email: {str(e)}")
        return False


def main():
    print(f"Начало процесса обновления: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    # Обновляем подключения в Excel
    if refresh_excel_connections():
        # Отправляем уведомление
        send_email_notification()

    print("Процесс завершен")


if __name__ == "__main__":
    main()