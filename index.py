__":
  app.run()from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Flask route to display the form and handle the SMS sending
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mobile_number = request.form['mobile']
        sms_text = request.form['sms_text']

        # URL and headers for the POST request
        url = "https://sms.link3.net/send_single_sms"

        headers = {
            "Host": "sms.link3.net",
            "Connection": "keep-alive",
            "Content-Length": "135",
            "Cache-Control": "max-age=0",
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "Origin": "https://sms.link3.net",
            "Content-Type": "application/x-www-form-urlencoded",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://sms.link3.net/send_single_sms",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
            "Cookie": "PHPSESSID=oefkthbrri51o7clpa3m0atnt4"
        }

        # Form data to be sent
        data = {
            "lan": "1",
            "mobile": mobile_number,
            "contact": "",
            "sms_text": sms_text,
            "sms_txt": "",
            "submit": "submit",
            "formSubmitted": "true"
        }

        # Send the request to the external API
        response = requests.post(url, headers=headers, data=data)

        # Display the response after sending the SMS
        return f"SMS sent! Response from server: {response.text}"

    # HTML Template for the form
    html_form = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Send SMS</title>
        <style>
            body {
                background-color: #0d0d0d;
                color: #ffffff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
            }

            .sms-form {
                background-color: #1a1a1a;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
                border: 2px solid #00ffff;
                width: 400px;
                text-align: center;
            }

            input, textarea {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 2px solid #00ffff;
                border-radius: 5px;
                background-color: #333;
                color: #fff;
            }

            input:focus, textarea:focus {
                outline: none;
                border-color: #ff00ff;
            }

            .submit-btn {
                background-color: #00ffff;
                color: #0d0d0d;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 18px;
                transition: background-color 0.3s ease;
            }

            .submit-btn:hover {
                background-color: #ff00ff;
            }

            h1 {
                margin-bottom: 20px;
                font-size: 24px;
            }
        </style>
    </head>
    <body>
        <div class="sms-form">
            <h1>Send SMS</h1>
            <form method="POST">
                <input type="text" name="mobile" placeholder="Enter Mobile Number" required>
                <textarea name="sms_text" rows="4" placeholder="Enter your message" required></textarea>
                <button type="submit" class="submit-btn">Send</button>
            </form>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_form)

if __name__ == '__main__':
    app.run(debug=True)
