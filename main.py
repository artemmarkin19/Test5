import tkinter as tk
from tkinter import ttk, messagebox
import requests

CURRENCY_NAMES = {
    'USD': 'Американский доллар',
    'EUR': 'Евро',
    'RUB': 'Российский рубль',
    'GBP': 'Британский фунт',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахстанский тенге',
    'BYN': 'Белорусский рубль',
    'TRY': 'Турецкая лира',
    'INR': 'Индийская рупия'
}