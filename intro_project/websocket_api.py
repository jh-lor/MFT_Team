import websocket
import time

try:
    import thread
except ImportError:
    import _thread as thread


f = open("binanceusdt.log", "a")


def on_message(ws, message):
    print(message)
    f.write(message + "\n")
    f.flush()
    # TO DO: vwap calculation


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        # TO DO: Interaction with websocket
        pass
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://stream.binance.us:9443/ws",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
