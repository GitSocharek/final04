### 🔴 Ćwiczenie M04L06

# Narodowy Bank Polski udostępnia przez swoje API historyczne kursy walut. Otrzymałæś odpowiedź taką jak poniżej

response = {
    "table": "A",
    "currency": "dolar amerykański",
    "code": "USD",
    "rates": [
        {
            "no": "148/A/NBP/2021",
            "effectiveDate": "2021-08-03",
            "mid": 3.8315,
        },
    ],
}

rate = response['rates']
mid_currency = rate[0]
mid = mid_currency['mid']

print(mid)

