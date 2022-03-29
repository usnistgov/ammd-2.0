""" Visit model that represents a user visit on the web app
"""
from django_mongoengine import fields, Document
from mongoengine import errors as mongoengine_errors

from core_main_app.commons import exceptions


class Visit(Document):
    """Visit object that represents a visit on the website"""

    user = fields.StringField()
    sessions = fields.ListField(blank=True)
    related_date = fields.ListField(blank=True)

    @staticmethod
    def get_all():

        """Get all Visits objects.

        Returns:

        """
        return Visit.objects().all()

    @staticmethod
    def get_by_id(visit_id):

        """Return the object with the given id.

        Args:
        data_cached_id:

        Returns:
        DataCached Object

        """

        try:
            return Visit.objects.get(pk=str(visit_id))
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    @staticmethod
    def get_by_user(user):
        try:
            # print(Visit.objects.get(user=str(user)))
            return Visit.objects.get(user=str(user))
        except mongoengine_errors.DoesNotExist as e:
            return None
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    def save_object(self):

        """Custom save.

        Returns:
        Saved Instance.

        """

        try:
            return self.save()
        except mongoengine_errors.NotUniqueError as e:
            raise exceptions.NotUniqueError(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    @staticmethod
    def delete_objects():
        """Delete all Visits objects from the database.

        Returns:

        """
        return Visit.objects().delete()
