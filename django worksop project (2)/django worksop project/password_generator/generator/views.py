import random
import string
from django.http import JsonResponse
from .models import GeneratedPassword
from django.shortcuts import render

def generate_password(length):
    if length < 3:  # Minimum length to include at least one of each required character type
        raise ValueError("Password length must be at least 3 characters.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    all_characters = lower + upper + digits
    password += random.choices(all_characters, k=length - 3)

    random.shuffle(password)

    return ''.join(password)

def generate_passwords(request):
    length = int(request.GET.get('length', 8))
    count = int(request.GET.get('count', 1))

    passwords = [generate_password(length) for _ in range(count)]
    return JsonResponse({'passwords': passwords})

def index(request):
    return render(request, 'index.html')

def generate(request):
    length = int(request.GET.get('length', 8))
    allow_numbers = request.GET.get('allowNumbers') == 'true'
    allow_uppercase = request.GET.get('allowUppercase') == 'true'
    allow_symbols = request.GET.get('allowSymbols') == 'true'
    allow_lowercase = request.GET.get('allowLowercase') == 'true'
    exclude_similar = request.GET.get('excludeSimilar') == 'true'
    exclude_duplicates = request.GET.get('excludeDuplicates') == 'true'
    allow_other_symbols = request.GET.get('allowOtherSymbols') == 'true'

    characters = ''
    if allow_numbers:
        characters += string.digits
    if allow_uppercase:
        characters += string.ascii_uppercase
    if allow_symbols:
        characters += '!@#$%^&*()+'
    if allow_lowercase:
        characters += string.ascii_lowercase
    if allow_other_symbols:
        characters += '~[];:,.'

    if exclude_similar:
        characters = characters.replace('I', '').replace('l', '').replace('1', '').replace('o', '').replace('O', '').replace('0', '')

    if not characters:
        return JsonResponse({'passwords': ['o+6D%wUq']})

    passwords = []
    for _ in range(1):
        password = ''.join(random.choice(characters) for _ in range(length))
        if exclude_duplicates:
            while len(set(password)) != len(password):
                password = ''.join(random.choice(characters) for _ in range(length))
        passwords.append(password)

        # Save the password to the database
        GeneratedPassword.objects.create(password=password)

    return JsonResponse({'passwords': passwords})

def generate_aws_password(request):
    length = 16
    allow_numbers = True
    allow_uppercase = True
    allow_symbols = True
    allow_lowercase = True

    password = generate_custom_password(length, allow_numbers, allow_uppercase, allow_symbols, allow_lowercase)
    GeneratedPassword.objects.create(password=password)
    return JsonResponse({'passwords': [password]})

def generate_amazon_password(request):
    length = 12
    allow_numbers = True
    allow_uppercase = True
    allow_symbols = True
    allow_lowercase = True

    password = generate_custom_password(length, allow_numbers, allow_uppercase, allow_symbols, allow_lowercase)
    GeneratedPassword.objects.create(password=password)
    return JsonResponse({'passwords': [password]})

def generate_custom_password(length, allow_numbers, allow_uppercase, allow_symbols, allow_lowercase):
    characters = ''
    if allow_numbers:
        characters += string.digits
    if allow_uppercase:
        characters += string.ascii_uppercase
    if allow_symbols:
        characters += '!@#$%^&*()+'
    if allow_lowercase:
        characters += string.ascii_lowercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
