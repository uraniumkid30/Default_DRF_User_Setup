from typing import NoReturn, List

from django.db import models


class TimeBaseModel(models.Model):
    """
    This model defines base models that implements common fields like:
    created_at
    updated_at
    is_deleted
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self: object) -> NoReturn:
        """Soft delete a model instance"""
        self.is_deleted: bool = True
        self.save()

    class Meta:
        abstract: bool = True
        ordering: List[str] = ['-created_at']