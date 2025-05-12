import requests

def get_bravi_data(tickers, token):
    url_base  = "https://brapi.dev/api/quote/"
    total_data = []

    for tickers in tickers:
        try:
            url = f"https://brapi.dev/api/quote/{tickers}?token={token}"
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                if "results" in data and data["results"]:
                    acao = data["results"][0]
                    total_data.append({
                        "nome": acao.get("longName", "Desconhecido"),
                        "simbolo": acao.get("symbol", tickers),
                        "preco": acao.get("regularMarketPrice", 0),
                        "variacao": acao.get("regularMarketChangePercent", 0),
                        "logo": acao.get("logourl", "")
                    })
                else:
                    print(f"[!] Sem resultados para {tickers}")
            else:
                print(f"[!] Erro {response.status_code} ao consultar {tickers}")

        except requests.exceptions.RequestException as e:
            print(f"[!] Falha na requisição para {tickers}: {e}")
        except Exception as e:
            print(f"[!] Erro inesperado com {tickers}: {e}")

    return total_data