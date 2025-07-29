import ssl
import certifi
import smtplib
from django.core.mail.backends.smtp import EmailBackend
from .models import Notification

def create_notification(user, title, description):
    Notification.objects.create(user=user, title=title, description=description)

class CertifiEmailBackend(EmailBackend):
    """
    SMTP backend that uses certifi's CA bundle when doing STARTTLS.
    """

    def open(self):
        """
        Open a network connection and call EHLO/STARTTLS with certifi's bundle.
        """
        if self.connection:
            return False
        try:
            # 1) establish plain connection
            self.connection = smtplib.SMTP(self.host, self.port, timeout=self.timeout)
            self.connection.ehlo()
            # 2) if using TLS, wrap with certifi bundle
            if self.use_tls:
                context = ssl.create_default_context(cafile=certifi.where())
                self.connection.starttls(context=context)
                self.connection.ehlo()
            # 3) authenticate if needed
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception:
            if self.fail_silently:
                return False
            raise

    def close(self):
        """
        Close the SMTP connection (same as parent).
        """
        super().close()
