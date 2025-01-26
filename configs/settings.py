import os
import subprocess

print(os.listdir())

settings = {
    'log_level': 'DEBUG',
    'admin_username': 'user',
    'admin_password': 'bitnami',
    "product": {
        "product_name": "auto1_test1",
        "tag":"auto_test1",
        "model":"auto_test1",
        "seo":"auto1_test1",
    },
    "new_user":{
        "first_name":"test",
        "last_name":"test",
        "email":"test100@mail.ru",
        "password":"test123.",
    }
}