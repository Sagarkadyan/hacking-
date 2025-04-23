
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Intelligent default values
default_values = {
    "name": "John Doe",
    "email": "john@example.com",
    "gamil": "john@example.com",  # common typo
    "username": "johnny123",
    "user": "johnny123",
    "pass": "Test@1234",
    "password": "Test@1234",
    "phone": "1234567890",
    "tel": "1234567890",
    "mob": "1234567890",
    "mobile": "1234567890",
    "address": "123 Main Street",
    "city": "New York",
    "message": "This is a test message.",
    "comment": "Test comment",
    "url": "https://example.com",
    "website": "https://example.com"
}

def smart_guess(name_or_type):
    lower = name_or_type.lower()
    for key in default_values:
        if key in lower:
            return default_values[key]

    # Guess by type
    if "email" in lower:
        return "auto@example.com"
    elif "tel" in lower or "phone" in lower:
        return "1234567890"
    elif "url" in lower or "site" in lower:
        return "https://example.com"
    elif "pass" in lower:
        return "Pass@123"
    elif "number" in lower:
        return "123"
    return "SampleText"

def fetch_fill_submit(url):
    session = requests.Session()
    
    try:
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        form = soup.find("form")
        if not form:
            print("❌ No form found on the page.")
            return

        # Determine form submission details
        action = form.get("action") or url
        method = form.get("method", "get").lower()
        full_action_url = urljoin(url, action)

        form_data = {}

        for field in form.find_all(["input", "textarea", "select"]):
            name = field.get("name") or field.get("id")
            if not name:
                continue

            input_type = field.get("type", "text").lower()
            placeholder = field.get("placeholder", "")
            basis = f"{name} {placeholder} {input_type}"

            # For select dropdowns
            if field.name == "select":
                options = field.find_all("option")
                selected = next((opt.get("value") for opt in options if opt.get("value")), "Default")
                form_data[name] = selected
                continue

            # Guess value
            value = smart_guess(basis)
            form_data[name] = value

        print("\n📤 Submitting this data:")
        for k, v in form_data.items():
            print(f"  {k}: {v}")

        # Submit the form
        if method == "post":
            submit_response = session.post(full_action_url, data=form_data)
        else:
            submit_response = session.get(full_action_url, params=form_data)

        print("\n✅ Response:")
        print(f"Status Code: {submit_response.status_code}")
        print(submit_response.text[:500])  # Only print first 500 chars

    except Exception as e:
        print("❌ Error:", e)

# 🔽 Entry point
if __name__ == "__main__":
    user_url = input("🔗 Enter the form URL: ").strip()
    if not user_url.startswith("http"):
        print("❌ Please enter a valid URL (starting with http or https).")
    else:
        fetch_fill_submit(user_url)
