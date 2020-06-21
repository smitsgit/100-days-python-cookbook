def url_print(proto, host, domain):
    url = f"{proto}://{host}.{domain}"
    print(url)


def main():
    url_print('http', 'www', 'example.com')


if __name__ == '__main__':
    main()
