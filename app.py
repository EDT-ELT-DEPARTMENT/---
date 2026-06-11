import streamlit as st
import uuid
import smtplib
from email.message import EmailMessage

# دالة توليد كود التفعيل الفريد
def توليد_كود_فريد():
    return str(uuid.uuid4())[:8].upper()

# دالة إرسال الكود عبر البريد الإلكتروني
def إرسال_كود_التفعيل(بريد_الطالب, الكود):
    msg = EmailMessage()
    msg.set_content(f"أهلاً بك في منصة قصتي دراستي. كود التفعيل الخاص بك هو: {الكود}")
    msg['Subject'] = 'كود تفعيل اشتراكك'
    msg['From'] = 'ton_email@gmail.com'
    msg['To'] = بريد_الطالب
    
    # إعدادات الاتصال الآمن بالسيرفر
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login('ton_email@gmail.com', 'كلمة_سر_التطبيق_الخاصة_بالإيميل')
        server.send_message(msg)

# واجهة تسجيل الطالب
st.title("تسجيل الدخول والاشتراك")
بريد = st.text_input("أدخل بريدك الإلكتروني")

if st.button("تأكيد الاشتراك وتفعيل الحساب"):
    if بريد:
        الكود = توليد_كود_فريد()
        # هنا يجب ربط بوابة الدفع Stripe أولاً
        إرسال_كود_التفعيل(بريد, الكود)
        st.success("تم إرسال كود التفعيل الفريد إلى بريدك الإلكتروني!")
    else:
        st.error("الرجاء إدخال بريد إلكتروني صالح.")
