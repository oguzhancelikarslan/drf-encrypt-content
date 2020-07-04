from collections import OrderedDict

from django.core.exceptions import ImproperlyConfigured

from drf_encrypt_content.rest_encrypt_content import RestEncryptContent


class RestEncryptContentMixin(RestEncryptContent):
    __ALL__ = '__all__'

    def to_representation(self, instance):
        representation = super(RestEncryptContentMixin, self).to_representation(instance)
        encrypted_fields = getattr(self.Meta, 'encrypted_fields', self.__ALL__)
        excluded_fields = getattr(self.Meta, 'excluded_fields', None)
        fields_list = list()
        model_class = getattr(self.Meta, 'model')

        if encrypted_fields and encrypted_fields != self.__ALL__ and not isinstance(encrypted_fields, (list, tuple)):
            raise TypeError(
                'The `encrypted_fields` option must be a list or tuple or "__all__". '
                'Got %s.' % type(encrypted_fields).__name__
            )

        if excluded_fields and not isinstance(excluded_fields, (list, tuple)):
            raise TypeError(
                'The `excluded_fields` option must be a list or tuple. Got %s.' %
                type(excluded_fields).__name__
            )

        assert not ((encrypted_fields != self.__ALL__) and excluded_fields), (
            "Cannot set both 'encrypted_fields' and 'excluded_fields' options on "
            "serializer {serializer_class}.".format(
                serializer_class=self.__class__.__name__
            )
        )

        if encrypted_fields == self.__ALL__:
            fields_list = [key for key, value in representation.items()]
        else:
            for field in encrypted_fields:
                if not (field in representation.keys()):
                    raise ImproperlyConfigured(
                        'Field name `%s` is not valid for model `%s`.' %
                        (field, model_class.__name__)
                    )

            for key in representation.keys():
                if key in encrypted_fields:
                    fields_list.append(key)

        if excluded_fields is not None:
            for field in excluded_fields:
                if not (field in fields_list):
                    raise ImproperlyConfigured(
                        'Field name `%s` is not valid for model `%s`.' %
                        (field, model_class.__name__)
                    )
                else:
                    fields_list.remove(field)

        for key, value in representation.items():
            if key in fields_list:
                if type(representation[key]) is not OrderedDict:
                    representation[key] = self.encrypt_data(str(value))

        return representation
