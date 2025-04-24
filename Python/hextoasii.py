from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

# Dummy values to auto-fill
dummy_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "gamil": "john@example.com",
    "phone": "1234567890",
    "mobile": "1234567890",
    "tel": "1234567890",
    "user": "johnny123",
    "username": "johnny123",
    "password": "Test@1234",
    "pass": "Test@1234",
    "address": "123 Main Street",
    "city": "New York",
    "message": "Hello!",
    "comment": "This is a test comment.",
    "url": "https://example.com"
}

def guess_value(name, input_type="text", placeholder=""):
    basis = f"{name} {placeholder} {input_type}".lower()
    for key in dummy_data:
        if key in basis:
            return dummy_data[key]
    if "email" in basis:
        return "test@example.com"
    if "phone" in basis or "tel" in basis:
        return "1234567890"
    if "pass" in basis:
        return "Pass@123"
    if "url" in basis:
        return "https://example.com"
    return "SampleText"

def auto_fill_form(url, iteration=1):
    options = FirefoxOptions()
    options.add_argument("--headless")  # Remove if you want to see browser
    service = FirefoxService(executable_path="/usr/bin/geckodriver")  # Update path if different

    for i in range(iteration):
        print(f"\n🌀 Iteration {i+1}/{iteration}")
        driver = webdriver.Firefox(service=service, options=options)

        try:
            driver.get(url)
            time.sleep(2)

            form = driver.find_element(By.TAG_NAME, "form")
            inputs = form.find_elements(By.TAG_NAME, "input")
            textareas = form.find_elements(By.TAG_NAME, "textarea")
            selects = form.find_elements(By.TAG_NAME, "select")

            for field in inputs + textareas:
                name = field.get_attribute("name") or field.get_attribute("id") or f"field_{i}"
                input_type = field.get_attribute("type") or "text"
                placeholder = field.get_attribute("placeholder") or ""

                if input_type in ["submit", "button", "hidden"]:
                    continue

                value = guess_value(name, input_type, placeholder)
                try:
                    field.clear()
                    field.send_keys(value)
                except:
                    continue

            for select in selects:
                try:
                    Select(select).select_by_index(1)
                except:
                    continue

            form.submit()
            print("✅ Submitted successfully.")
            time.sleep(1)

        except Exception as e:
            print("❌ Error:", e)
        finally:
            driver.quit()

if __name__ == "__main__":
    url = input("🔗 Enter form URL: ").strip()
    try:
        times = int(input("🔁 How many times to submit the form? "))
    except:
        times = 1
    if url.startswith("http"):
        auto_fill_form(url, iteration=times)
    else:
        print("❌ Invalid URL")
