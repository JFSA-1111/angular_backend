"""Profile model."""

# Django
from django.db import models


class Character(models.Model):
    """Character model.

    Un personaje contiene datos públicos como descripcion e imagen
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Fecha y hora en que se creó el objeto.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Fecha y hora en que se modificó el objeto por última vez.'
    )
    user = models.ForeignKey('usuarios.User', on_delete=models.CASCADE)

    name = models.CharField(max_length=70)
    image = models.ImageField(
        'foto de perfil',
        upload_to='users/pictures/',
        null=False,
        blank=False
    )
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        """Return character's str() representation."""
        return str(self.name)
