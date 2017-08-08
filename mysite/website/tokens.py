from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

"""
 Generador de Tokens para desbloquear cuentas de usuarios basado en el
 generador de tokens 'PasswordResetTokenGenerator' default de Django
 Inspiracion: https://simpleisbetterthancomplex.com/tutorial/2016/08/24/how-to-create-one-time-link.html
"""
class AccountUnlockTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.perfil.esta_bloqueado)
        )

account_unlock_token = AccountUnlockTokenGenerator()