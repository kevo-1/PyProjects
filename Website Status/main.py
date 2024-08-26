import requests
from requests import Response , RequestException
from requests.structures import CaseInsensitiveDict

def CheckStatus(link: str) -> None:
    try:
        response: Response = requests.get(link)

        status_code: int = response.status_code
        headers_info: CaseInsensitiveDict[str] = response.headers
        content_type: str = headers_info.get('Content-Type', 'Unknown')
        server:str = headers_info.get('Server' , 'Unknown')
        response_time: float = response.elapsed.total_seconds()

        print("-" * 20)
        print("URL: {}".format(link))
        print("Status Code: {}".format(status_code))
        print("Content type: {}".format(content_type))
        print("Server: {}".format(server))
        print(f"Server: {response_time:.2f} seconds")
        print("-" * 20)

    except RequestException:
        print(f'Error: {RequestException}')

def main()-> None:
    URL: str = input("Enter the website's link you want to check: ")
    CheckStatus(link=URL)


if __name__ == "__main__":
    main()