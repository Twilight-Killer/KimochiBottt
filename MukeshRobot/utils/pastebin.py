import socket,requests
from asyncio import get_running_loop
from functools import partial


def _netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096).decode("utf-8").strip("\n\x00")
        if not data:
            break
        return data
    s.close()


async def paste(content):
    url ="https://pastebin.com/api/api_post.php"
    data = {"api_dev_key":"vd3B7OUCoHGBtktvmVv6Y0n8bpZ8IMem","api_paste_code": content,"api_option": "paste"}
    response = requests.post(url, data=data)
    link=response.text
    return link
