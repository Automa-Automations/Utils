import requests
import threading
import os

total_pages = int(input("Enter the number of pages you want to download **10 per page** (Default 10): ")) or 10
queries = input("Enter the search query (Default pixar) (Comma seperated): ").split(",") or ["pixar"]

for i in range(total_pages):
    for query in queries:
        cookies = {
            '__Host-next-auth.csrf-token': '38fe64a67437b3562695aa3bbf02f9cbfa35c189b25d3e264fc5ad3100f514b5%7Ce834e84cdca2c8cee798a1e4fc37ca2d2215f4012ff17084dc6de2669084c2a6',
            '_gcl_au': '1.1.1449038009.1714724658',
            '_ga': 'GA1.1.1107488985.1714724659',
            '_tt_enable_cookie': '1',
            '_ttp': 'Nd1CN1XLPPx6HVMpOHCCv8dbU7B',
            '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.prompthunt.com%2Fexplore%3FauthSuccess%3Dtrue',
            'AMP_MKTG_b1ac6ebe69': 'JTdCJTdE',
            '__Secure-next-auth.session-token': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..YDBmjZMYlMaj0NkF.gYkIGkin1w6036_YoK0ywA5uxKTH9xdMxZzOzDtTWPVko8hFJfJBEJrx0XIYfpS1r7_7RMbqY5cZjHqCOEEVe2T7Z4ai3-afn1ddu6SaTVh1cy_FdVvlH-5XgPpvbNM8f54_RZRSOL1Ja7CzQmL4PGu2orujptGbJYKkRXzaBTs3FPyRZKX9Eiq-1wWV66uL4HHCcrNyQIWR6ElEaHDw9kI0Hxs0MrRknB09oyPPz4XrjQtwQBp0Ff2_TNTJNYRFE1g01myHlug9tJgDEpoLSEjJA7MJnmL0vHQ-r_0_aCyQqhekhI9cYnUIN8rytrAX2RDIQdRye3-dubRuU0rk5NpOoHymf8xQ_Gm4mgjsLh7vfY3Q-yeZxcXmTujklyb_7w80xept7LtFZObE5kY4O3uvJodAbkeoZT4osya9ZJU9O4uYWa4wuhbTPcGn56AZkQc2V91U6jgQVukxlS8TKch7OSOCTBKs43dOD5niFbZT6husp0Ejjf40syZwoAyJX21m32pZ08Nw1SmB5H8U4_ZR5dY6d8JIKtm69w-NJqcqRv3eXb3RFz6C7425Mo4hatf0LBaaYAntgbNxry148S6vH-TnzOAHWOp12EgwcILIUl8BRCr4kjQOXv_SVcWXOIpPDPmLLPLPmlGEMjtlpbZAoe5URaZw_CWIKO_Mb78OXwEo_R5sQyIzjyhkYp5aVaR4evJBnNy3TUMozpSLUE5hFLs1GgqEvqcJ_rXkxgaiCVYqiVu68Rxr73eN8KGfYjZTjV9wbRBYs2RwJ2-5xWXXoXyO_2ElC1TVN3k9cuOAkb8HWdDP58xNOaKGUxWKi4BkXgakqR8k0lp2B0WMpqAIXivB_rNCTQzwcxJncyStZUptfDh5hGude9frVEBjU6-FaCTxZctKOzcXaWc8D0r4_MR-kihhT8DWkJ_BMz4.GHOu3PqOLzk_2joz-ThsaA',
            'AMP_b1ac6ebe69': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIyM2RmMzQ2ZS0wOWY0LTQ0YWEtOGMzOC1lY2JjYWEyMmFjM2ElMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJzLmYuYnVzaW5lc3NhY2MlNDBnbWFpbC5jb20lMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE0NzI0Njc4ODk1JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNDcyNDg3MTg0MSU3RA==',
            '_ga_6XQ24B75V9': 'GS1.1.1714724658.1.1.1714724872.0.0.0',
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': '__Host-next-auth.csrf-token=38fe64a67437b3562695aa3bbf02f9cbfa35c189b25d3e264fc5ad3100f514b5%7Ce834e84cdca2c8cee798a1e4fc37ca2d2215f4012ff17084dc6de2669084c2a6; _gcl_au=1.1.1449038009.1714724658; _ga=GA1.1.1107488985.1714724659; _tt_enable_cookie=1; _ttp=Nd1CN1XLPPx6HVMpOHCCv8dbU7B; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.prompthunt.com%2Fexplore%3FauthSuccess%3Dtrue; AMP_MKTG_b1ac6ebe69=JTdCJTdE; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..YDBmjZMYlMaj0NkF.gYkIGkin1w6036_YoK0ywA5uxKTH9xdMxZzOzDtTWPVko8hFJfJBEJrx0XIYfpS1r7_7RMbqY5cZjHqCOEEVe2T7Z4ai3-afn1ddu6SaTVh1cy_FdVvlH-5XgPpvbNM8f54_RZRSOL1Ja7CzQmL4PGu2orujptGbJYKkRXzaBTs3FPyRZKX9Eiq-1wWV66uL4HHCcrNyQIWR6ElEaHDw9kI0Hxs0MrRknB09oyPPz4XrjQtwQBp0Ff2_TNTJNYRFE1g01myHlug9tJgDEpoLSEjJA7MJnmL0vHQ-r_0_aCyQqhekhI9cYnUIN8rytrAX2RDIQdRye3-dubRuU0rk5NpOoHymf8xQ_Gm4mgjsLh7vfY3Q-yeZxcXmTujklyb_7w80xept7LtFZObE5kY4O3uvJodAbkeoZT4osya9ZJU9O4uYWa4wuhbTPcGn56AZkQc2V91U6jgQVukxlS8TKch7OSOCTBKs43dOD5niFbZT6husp0Ejjf40syZwoAyJX21m32pZ08Nw1SmB5H8U4_ZR5dY6d8JIKtm69w-NJqcqRv3eXb3RFz6C7425Mo4hatf0LBaaYAntgbNxry148S6vH-TnzOAHWOp12EgwcILIUl8BRCr4kjQOXv_SVcWXOIpPDPmLLPLPmlGEMjtlpbZAoe5URaZw_CWIKO_Mb78OXwEo_R5sQyIzjyhkYp5aVaR4evJBnNy3TUMozpSLUE5hFLs1GgqEvqcJ_rXkxgaiCVYqiVu68Rxr73eN8KGfYjZTjV9wbRBYs2RwJ2-5xWXXoXyO_2ElC1TVN3k9cuOAkb8HWdDP58xNOaKGUxWKi4BkXgakqR8k0lp2B0WMpqAIXivB_rNCTQzwcxJncyStZUptfDh5hGude9frVEBjU6-FaCTxZctKOzcXaWc8D0r4_MR-kihhT8DWkJ_BMz4.GHOu3PqOLzk_2joz-ThsaA; AMP_b1ac6ebe69=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIyM2RmMzQ2ZS0wOWY0LTQ0YWEtOGMzOC1lY2JjYWEyMmFjM2ElMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJzLmYuYnVzaW5lc3NhY2MlNDBnbWFpbC5jb20lMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE0NzI0Njc4ODk1JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNDcyNDg3MTg0MSU3RA==; _ga_6XQ24B75V9=GS1.1.1714724658.1.1.1714724872.0.0.0',
            'priority': 'u=1, i',
            'referer': 'https://www.prompthunt.com/search?q=pixar&provider=All%20services&type=Creations',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }

        params = {
            'page': str(i),
            'query': query,
            'provider': 'All services',
        }

        response = requests.get('https://www.prompthunt.com/api/search', params=params, cookies=cookies, headers=headers)

        response_json = response.json()
        threads = []
        for result in response_json['prompts']:
            # Download the image in result['assets'][0]['src']
            thread = threading.Thread()

            def do_something(url, id):
                global query
                query = query.replace(" ", "_")
                try:
                    if not os.path.exists(f'images/{query}'):
                        os.makedirs(f"images/{query}")
                except:
                    return
                
                try:
                    with open(f'images/{query}/{id}.jpg', 'wb') as f:
                        print(f"Downloading images/{query}/{id}.jpg")
                        f.write(requests.get(url).content)
                except:
                   return 

            thread = threading.Thread(target=do_something, args=(result['assets'][0]['src'],result["id"]))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

