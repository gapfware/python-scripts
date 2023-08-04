import speedtest as st


def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = f"{nbytes:.2f}".rstrip('0').rstrip('.')
    return f"{f} {suffixes[i]}"


def run():
    server = st.Speedtest()
    server.get_best_server()

    print("Retrieving download speed...")
    ds = server.download()

    print("Retrieving upload speed...")
    us = server.upload()
    ping = server.results.ping

    print(f'Download speed {humansize(ds)}')
    print(f'Upload speed {humansize(us)}')
    print(f'Ping: {ping}')


if __name__ == '__main__':
    run()
