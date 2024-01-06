# BardChatbot

Inside main.py cookie_dict provide the necessary cookies using the steps below:

> **Warning** Do not expose the `__Secure-1PSID` 
1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID`, `_Secure-1PSIDTS`, `__Secure-1PSIDCC` cookies.

Note that while I referred to `__Secure-1PSID`, `_Secure-1PSIDTS`, `__Secure-1PSIDCC` values as an API key for convenience, it is not an officially provided API key. 
Cookie value subject to frequent changes. Verify the value again if an error occurs. Most errors occur when an invalid cookie value is entered.

Once cookies provided:
Run App using command: streamlit run main.py
