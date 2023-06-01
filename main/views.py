from django.shortcuts import render, redirect
import requests 
import random
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Word
import random
import string

from django.shortcuts import render
from django.http import JsonResponse

def get_random_words(num_words):
    word_list = ["able", "baby", "cake", "door", "easy", "face", "game", "help", "idea", "jump", "keep", "love", "meet", "nice", "open", "park", "quit", "rate", "song", "tall", "undo", "vast", "wait", "year", "zoom", "army", "book", "city", "desk", "even", "flag", "gift", "home", "idea", "join", "kick", "lamp", "mute", "nine", "ouch", "pink", "quiz", "ring", "ship", "talk", "unit", "vase", "wake", "year", "zero", "apple", "baby", "cat", "dog", "egg", "fish", "goat", "hat", "ice", "jam", "kite", "lion", "moon", "nest", "owl", "pig", "quack", "rain", "sun", "toy", "umbrella", "van", "whale", "zoo", "ant", "bear", "cow", "duck", "ear", "frog", "hen", "ink", "jug", "key", "lamp", "mouse", "nut", "queen", "rat", "sun", "up", "web", "yak", "zebra", "add", "bed", "car", "fox", "gum", "log", "map", "net", "pen", "log", "cat", "fox", "gum", "log", "map", "net", "pen", "owl", "rug", "sun", "toy", "ant", "bat", "cat", "fox", "gum", "hat", "ink", "jug", "kit", "log", "man", "nut", "owl", "rat", "sun", "toy", "ant", "bat", "cat", "dog", "ear", "fog", "gun", "hat", "ink", "jug", "kit", "log", "man", "nut", "owl", "rat", "sun", "toy", "ant", "bat", "cat", "dog", "ear", "fog", "gun", "hat", "ink", "jug", "kit", "log", "man", "nut", "owl", "rat", "sun", "toy", "ant", "bat", "cat", "dog", "ear", "fog", "gun", "hat", "ink", "jug", "kit", "log", "man", "nut", "owl", "rat", "sun", "toy", "van", "web", "yak", "zebra", "ant", "bat", "cat", "dog", "ear", "fog", "gun", "hat", "ink", "jug", "kit", "log", "man", "nut", "owl", "rat", "sun", "toy", "van", "web", "yak", "zebra", "ant", "bat", "cat", "dog", "ear", "fog", "gun", "hat", "ink", "jug", "kit", "log", "man", "nut", "owl", "rat", "sun", "toy", "van", "web", "yak", "zebra", "ant", "bat", "cat", "dog", "ear", "fog", "gun", "hat", "ink", "jug", "kit", "log", "man", "nut", "owl", "rat", "sun", "toy", "van", "web", "yak", "zebra", "apple", "baby", "cat", "dog", "egg", "fish", "goat", "hat", "ice", "jam", "kite", "lion", "moon", "nest", "owl", "pig", "quack", "rain", "sun", "toy"]

    random.shuffle(word_list)
    return (word_list[:num_words])

def typing_test(request):
    words = get_random_words(150)
    return home(request, words)

def home(request, words=None):
    if words is None:
        words = get_random_words(150)
    context = {
        'words': words
    }
    return render(request, 'html/home.html', context)