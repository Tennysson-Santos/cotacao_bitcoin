import json

import websocket

import ssl


def ao_abrir(ws,):
	print('Abriu a conexão...')

	json_subscribe = """
{
"event": "bts:subscribe",
"data": {
"channel": "live_trades_btcusd"
}

}
"""

	ws.send(json_subscribe)

def erro(ws, error):
	print(error)

def fechou(ws):
	print("### Fechou ###")

def ao_receber_mensagem(ws,mensagem):
	mensagem = json.loads(mensagem)
	price = (mensagem['data']['price'])
	print('Cotação BTC:','$',price)


if __name__ == "__main__":
	ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
							on_open=ao_abrir,
							on_message=ao_receber_mensagem,
							on_error=erro,
							on_close=fechou)

ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
