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


def get_rates():
    url = "https://cbr-xml-daily.ru/daily_json.js"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        messagebox.showerror("Ошибка сети", f"Не удалось получить данные ЦБ РФ.")
        return None

def exchange():
    base1 = combo_base1.get()
    base2 = combo_base2.get()
    target = combo_target.get()

    if base1 == base2:
        messagebox.showwarning("Внимание, базовая и вторая базовая валюты не должны совпадать.")
        return

    data = get_rates()
    if data is None:
        return

    def get_rate_to_rub(currency_code):
        if currency_code == 'RUB':
            return 1
        try:
            valute = data['Valute'].get(currency_code)
            if valute is None:
                return None
            return valute['Value'] / valute['Nominal']
        except KeyError:
            return None

    rate1_rub = get_rate_to_rub(base1)
    rate2_rub = get_rate_to_rub(base2)
    rate_rub_target = get_rate_to_rub(target)

    if None in (rate1_rub, rate2_rub, rate_rub_target):
        messagebox.showerror("Не удалось найти курс для одной из выбранных валют.")
        return

    rate1 = rate1_rub / rate_rub_target
    rate2 = rate2_rub / rate_rub_target

    result_text = (
        f"1 {base1} = {rate1:.4f} {target}\n"
        f"1 {base2} = {rate2:.4f} {target}"
    )
    result.config(text=result_text)

def update_currency_names(event=None):
    name1.config(text=CURRENCY_NAMES.get(combo_base1.get(), ''))
    name2.config(text=CURRENCY_NAMES.get(combo_base2.get(), ''))
    target.config(text=CURRENCY_NAMES.get(combo_target.get(), ''))