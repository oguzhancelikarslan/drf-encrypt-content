# drf-encrypt-content

drf-encrypt-content is a Django app to help you encrypt your data, serialized through ModelSerializer. It also contains some helper functions. Which helps you to encrypt your data.  drf-encrypt-content is built on top of the **cryptography** package. This package makes fernet available to us.

##### Personal Warning
Because I don't have enough time, I could not add tests yet. 
I just tested it by hand based on Django 3.x and Django REST framework 3.11. 
As soon as I find some free time. I am gonna add tests and some feature requests. I am open to criticism. 
This is the first package that I made available to the Django community so looking forward to your comments to improve myself.

##### TODO
* Tests
* Code refactoring.
* Helper methods to encrypt various data structures.

### What is the Fernet?

Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. 
Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography. 

### Quick start

* Add "drf_encrypt_content" to your INSTALLED_APPS setting like this.

    ```
    INSTALLED_APPS = [
        ...
        'drf_encrypt_content',
    ]
    ````

* Jump terminal and cd where manage.py is.

* Run ``python manage.py generate_key`` to get a fresh fernet key and copy the key.

* Open settings.py file and provide the below variable. 

   `` REST_ENCRYPT_SECRET_KEY = 'key_you_copied_at_step_3' ``

* Open the file where your serializer using ModelSerializer stays and import and then use this mixin. 

    ```python
        from drf_encrypt_content import RestEncryptContentMixin 
        class MySerializer(RestEncryptContentMixin, ModelSerializer)
                                ...
    ```

That is it. This is going to encrypt all of your exposed data.

### Installation

```bash
pip install drf-encrypt-content
```

### Usage
This package makes you available three class **EncryptedModelSerializer**, **RestEncryptContentMixin** and **RestEncryptContent**


**RestEncryptContentMixin**: This is the mixin where the magic happens. You basically need to provide this mixin to the class where you inherited ModelSerializer. This is going to **encrypt all of the data** ModelSerializer serialize by default. 

You can specify which fields in your model you want to encrypt. Just define a list with the name 'encrypted_fields' in the class Meta where you define your model and fields.
    
        from drf_encrypt_content import RestEncryptContentMixin 
        class MySerializer(RestEncryptContentMixin, ModelSerializer)
            class Meta:
                model = Model
                fields = '__all__'
                encrypted_fields = [
                    'field_name'
                ]

Instead of typing all of the fields by one by, you can type only the ones you don't want to encrypt.

        from drf_encrypt_content import RestEncryptContentMixin 
        class MySerializer(RestEncryptContentMixin, ModelSerializer)
            class Meta:
                model = Model
                fields = '__all__'
                excluded_fields = [
                    'field_name'
                ]


**EncryptedModelSerializer**: If you want to use model serializer and also RestEncryptContentMixin mixin, change your ModelSerializer with EncryptedModelSerializer. EncryptedModelSerializer is based on ModelSerializer and RestEncryptContentMixin. You can do everything just like you do with Rest Encrypt Content Mixin.

        from drf_encrypt_content import EncryptedModelSerializer
        class MySerializer(EncryptedModelSerializer)
            class Meta:
                model = Model
                fields = '__all__'
                excluded_fields = [
                    'field_name'
                ]

### What if I use base Serializer class?
I do not support base Serializer yet but you can find some helper methods in **RestEncryptContent** class. 

You can use the below methods.

**encrypt_list:**  iterates an unencrypted list and encrypt items in the list and returns a list of encrypted data.

        from drf_encrypt_content import RestEncryptContent
        list_one = [1,2,3]
        rest_encrypt = RestEncryptContent()
        rest_enctypt.encrypt_list(data) # a list of encrypted data.

**encrypt_data:** returns fernet token which is the encrypted form of passed data.

        from drf_encrypt_content import RestEncryptContent
        data = 'example_content'
        rest_encrypt = RestEncryptContent()
        rest_enctypt.encrypt_data(data) # this is going to return encrypted data.


### License
BSD

### Author
Oğuzhan Çelikarslan

### Special Thanks to
Developing this package, I read through some codes and articles. I want to say thanks to persons who wrote and coded these.

Gajesh Naik

Tom Christie



