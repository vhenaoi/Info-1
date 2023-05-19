import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://prueba1.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'cfj7f3LRGJ6BcErljnDMf2R14yxb1VIMJI6sehnNQtXgKtFx2Kz4GZWmJeyoM7LyQZsKvMT7TfeXACDbVMZw3g=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}

#settings = {
#    'host': os.environ.get('ACCOUNT_HOST', 'https://prueba1.documents.azure.com:443/'),
#    'master_key': os.environ.get('ACCOUNT_KEY', 'cfj7f3LRGJ6BcErljnDMf2R14yxb1VIMJI6sehnNQtXgKtFx2Kz4GZWmJeyoM7LyQZsKvMT7TfeXACDbVMZw3g==/KEY1'),
#    'database_id': os.environ.get('COSMOS_DATABASE', 'INFO1'),
#    'container_id': os.environ.get('COSMOS_CONTAINER', 'miContenedor'),
#
#}


