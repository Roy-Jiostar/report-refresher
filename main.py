import os
import threading
import requests
import schedule
import time
from flask import Flask

# 1. Web server required for Render's free tier
app = Flask(__name__)

@app.route('/')
def home():
    return "Report Refresher App is active!"

# 2. Main Refresh Task
def job():
    print("Triggering report refresh at 07:00 AM...")
    try:
        import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Basic YWRzOmFkc3NlY3JldA==',
    # 'content-length': '0',
    'origin': 'https://brands.hotstar.com',
    'priority': 'u=1, i',
    'referer': 'https://brands.hotstar.com/',
    'sec-ch-ua': '"Google Chrome";v="153", "Not_A Brand";v="8", "Chromium";v="153"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
    'x-captcha-token': '0cAFcWeA7oqdYp8Zpn08Dc6vW0GZfFahDFtQqjbP6d-RimI9kM0PFEkLZwZnDsn6fc3LWvqa35iUQ6KcyIvzwR-t48oX5k_5-PaYb3T9lgTkI9g6EspHm7xP_EEB5VOcw4UIHywB0Y2_imC2FZ7QnLB3zqZboMlxBNa6veGnqSH-5LTk75Nr9tejIPfp0YMRlcKhKEg2Bqx54gelJPDh-g8sUtO_lU1wWFrhCc_Bz3LHqnKWII6aTJP9he4w8zJddPGj-gd9Lgoq5uNFcZ7EttvqJTVipTApJzP6IDVeYm9SW8I2pDBQzXX9-P8jqYlVAC5fkKWSDcVzgNqNOa2UZBRGRwfIOHDnGLL4LFiOInK7E3EupZhO4KJg2OQty1tBm1b4yRBuBiYtdiN_FiOizt4P_r4nOCjiLbeNrPr3l9dUl9x167tWKlgiBiWJB0SK6zRGMl6NUzKOhW091UDHRMb2ldCKPLPMWblATwYG8EChxWhTaRDPkzLc6n9MaPWeAIQTcBJNc9a98wq89vm0PczE02QJgx6wU_kXsKdnuLbhOjSdJLH_U2EPFdx4356RnAiW7W81dtLKzx89GIB3pQvenlM17leHWbO5yA3iKVbNImFPfo5WrxGawOffeW0lzjc43drX9GWcVUxW_F9kXhMRlPleROaVVCQCXZFzI07cMxIgZ4TVevoowh0sYPj7MmBTiutMoya8i37rHWCI1kj8ev7ZLYij0P3JXly1sObtAtJHhXVwQrBB1jBbFxflnb_sahlG9ed0dSV0AaYDyNnFQN4BNU-YgrimbPvgUhoO5I8mg1fuKhd-TWPbivlaDioNBaN3yq5-ttDW640m_Gh9HhMtbloYbgHwF_j7jWiMSxOscEf3EEnse5hanvqMgUy_fAYOyXCvlhtRLF9PAlV-w_V4MtWxjXj4JA1AlOJluo5Xog8m-EBYvba0ESFeX_2Xt8KoOvixhEDdDqKYg7siXLyMijw7rZoOf4jZaDvC9f1QGFhwpafM5uymXgXcLZL6MV4yoMEwgy-Te_gXFtzVyYcvLxb2e1PPrydjWyvCtse6PjX8VRFMCLhHsd6sObIBo4OST_eAGeGbn2drwBB_w3Jespohv422BRLaM1XxhhTFn0-xyC5vjmY9EjYTSGwGIDtvvCQiNITvMq0kAPdc4JiWOt3-ZJkLPwRNXS-w0Ci3ennGw4qGiWwn3oTTFy01bwx3rxRpCCMUr8fzEn80TE-k6Z0UnFVCQURlKbLq__hQuQ439SB6Rrkhai6-w5cPLcfAbpuMiDwgdU41rJmUTRt7NG6bQZQ2HxYNe9xODRx55__HyPbUh-kpRR8lAQMSXNHm1-NZ2GfyyK4nj6gmARvUR3hgaj2pd86kVAaOIXNMOLCN9fY_QfrpJn6qxiZw1q0G9LNJRoaITdYspWE6pdJFJffRAk-eZg7odhQ4JH3lax_zOmxDlVdJ6DTPp5OIJwQ-iwZj6ZEw48wICVLy9_WmNUUKbMj8CrxMKwuukHXUmdSuH9xQkOUe9TRZEPEV0M1ICiSaP0R17SfWl3qrgth6ItFN8Q-JwFxw_sojVJJpOZYQvj0fiUh4ZUH0324c0oq0lRZs9ukKGc-nEI-3Iah125KIWjqHfl4OnSVKRNpcHl2pafx3ES9fIMnjtnYVhqLkeiTHWMWC0dbfAA6_yfbpnD9MzVz3eqAjeFeCYajWcw89efioabx8tnFYMBpE9urpXkKDaslUqtjjLsnCA8FvhxLKx3iIKdfpJoRVnK7LHAxlbvS1szGghmguKuMo6_F57IGbfDFS_dd3VGdAki81T8u3Iw5qHUud3A9WhPLD4Qy_1l4kwGmYGFQQKeZLymeZhDPStKcd9UnmP0gZiogqKdoC4rSLsIoEk48Zier7P097LAgzI3Xb63Y4IAYzOEHyvPwMA74IzbmJisP-A_YA5Mg8xsyvUb2djGBB3aPakFwALIkhsR6S96yQpwXlWEdOi-GS6X_6umRfpv6ZyHxToctdx0H3-j-h6EzpTmX4hOMg1z4bjsKPsnN6ht3htkRLHTqSEYJVw3BN5-Q0bxNB3DGfwJnd3U3Vau6LMVO_bEgyXj0DhP0H8mQ1DIB12I9dVDcE2qRXRd1j8-ud5b1wFoUZ4MNtBLYdZblnpkrSlLLmfwsJS4Uj9em6bQvZGJUdYtsXpjzo54hohlDEEwWw8uuXKhUegIyohlSBvSwg_lYw05Cldmm-KYqBySnRh6crOqaR9eXfqbqEhLusZ_2rwOcJJwIRRC9sv37ux0U2IRCPVhB17Q-fhp4HZS8Eejl-2KbzkNOOneePS8ZwWoTjlNutp5NU0LKmB0wGKRNPGSA9YgQV15rWEpL0Gtd1UTUaEY-H4RXVcZgszxBavTHve3B7Tl6Q',
}

params = {
    'verifyToken': '2c3ee3be6bc076c8e93a131c732cb266c479b1c15b5bab360c13c69525634563',
    'expDate': '16-11-2026',
}

response = requests.put(
    'https://ads-api.hotstar.com/api/v2/ads-report/6ea3dcf3-8d50-47dd-ae81-647da34361ff/refresh',
    params=params,
    headers=headers,
)
        print("Refresh request successfully sent!")
    except Exception as e:
        print(f"Error firing refresh request: {e}")

# 3. Daily 7:00 AM Scheduler
def run_scheduler():
    schedule.every().day.at("07:00").do(job)
    print("Scheduler thread started. Waiting for 07:00 AM trigger...")
    while True:
        schedule.run_pending()
        time.sleep(60)

# Start scheduler in a background thread
threading.Thread(target=run_scheduler, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
