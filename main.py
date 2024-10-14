from  uuid import uuid4
from requests import post 

def target():
    global username
    username = input("Enter your target Without '@': ")
    if username[0]=='@':
        print("\n\nplease no need to add '@' in the username\n\n")
        target()


    url_target = "https://i.instagram.com/api/v1/users/lookup/"

    header_target = {

        'X-Ig-Www-Claim': '0',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'User-Agent': 'Instagram 219.0.0.12.117 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 346138365)',
        'Accept-Language': 'en-US',
        'X-Mid': 'YjKpKwABAAEBChfhQ0jDY79zjPt4',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '674',
        'Accept-Encoding': 'gzip, deflate'
        }

    data_target = {

        "phone_id": uuid4(),
        "q": username,
        "guid": uuid4(),
        "device_id": uuid4(),
        "android_build_type":"release",
        "waterfall_id": uuid4(),
        "directly_sign_in":"true",
        "is_wa_installed":"false"
        }

    req_target = post(url=url_target, headers=header_target , data=data_target)

    try:     
        if '"user":{"pk"' not in req_target.text:
            user_id= req_target.json()["user"]["pk"]
            print("user_id not found")
            
        elif '"can_email_reset":true' and '"can_sms_reset":true' in req_target.text:
            choose = input("""
1. send to Email 

2. send to phone number 

Choose one of them please: """)

            if choose == "1":
                send_email()
            elif choose == "2":
                send_phone()

        elif '"can_email_reset":true' in req_target.text:
            send_email()

        elif '"can_sms_reset":true' in req_target.text:
            send_phone()

        else:
            input(req_target.text)
    except:
        input("Please wait a few minutes before you try again.")


def send_email():
    url_send_email = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
    
    header_send_email = {

        'X-Ig-Www-Claim': '0',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'User-Agent': 'Instagram 219.0.0.12.117 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 346138365)',
        'Accept-Language': 'en-US',
        'X-Mid': 'YjKpKwABAAEBChfhQ0jDY79zjPt4',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '674',
        'Accept-Encoding': 'gzip, deflate'
        }

    data_send_email = {

        "adid": uuid4(),
        "query": username,
        "guid": uuid4(),
        "device_id": uuid4(),
        "waterfall_id": uuid4()
        }

    req_send_email = post(url=url_send_email, headers=header_send_email , data=data_send_email)
    if "email" in req_send_email.text:
        email = req_send_email.json()["email"]
        print(f"We sent an email to {email}")

def send_phone():
    
    url_send_phone = "https://i.instagram.com/api/v1/users/lookup_phone/"
    
    header_send_phone = {

        'X-Ig-Www-Claim': '0',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'User-Agent': 'Instagram 219.0.0.12.117 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 346138365)',
        'Accept-Language': 'en-US',
        'X-Mid': 'YjKpKwABAAEBChfhQ0jDY79zjPt4',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '674',
        'Accept-Encoding': 'gzip, deflate'
        }

    data_send_phone = {

        "supports_sms_code": "true",
        "guid": uuid4(),
        "device_id": uuid4(),
        "query": username,
        "android_build_type":"release",
        "waterfall_id": uuid4(),
        "use_whatsapp": "false"
        }

    req_send_phone = post(url=url_send_phone, headers=header_send_phone , data=data_send_phone)
    if "phone_number" in req_send_phone.text:
        phone_number= req_send_phone.json()["phone_number"]
        print(f"We sent an phone number to {phone_number}")

if __name__ == "__main__":
    print(f"[+] Welcome To Reset Password  [+]\n\n\n")
    target()

    # This is the main file of the project, which is responsible for sending the email or phone number to the target user.