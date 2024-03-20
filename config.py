import os
"""
Указываю путь к файлу products.json, чтобы в дальнейшем его использовать
На случай, если не верно:
Если есть возможность, в ответе на ДЗ поправьте, пожалуйста, как правильно указывать путь к файлу 
через os.path
"""
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'data/products.json')
