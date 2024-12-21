from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver (Chrome)
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # STEP 1: Open the Text Box Page
    print("Opening the Text Box page...")
    driver.get("https://demoqa.com/text-box")

    # Initialize Explicit Wait
    wait = WebDriverWait(driver, 10)

    # STEP 2: Locate Input Fields and Enter Data
    print("Entering data into the Text Box form...")

    # Input data for testing
    full_name = "Md. Tausif Alam"
    email = "tausifalam.study@gmail.com"
    current_address = "Adabor 15, Dhaka"
    permanent_address = "Adabor 15, Dhaka"

    # Locate and enter Full Name
    full_name_input = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
    full_name_input.send_keys(full_name)

    # Locate and enter Email
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "userEmail")))
    email_input.send_keys(email)

    # Locate and enter Current Address
    current_address_input = wait.until(EC.visibility_of_element_located((By.ID, "currentAddress")))
    current_address_input.send_keys(current_address)

    # Locate and enter Permanent Address
    permanent_address_input = wait.until(EC.visibility_of_element_located((By.ID, "permanentAddress")))
    permanent_address_input.send_keys(permanent_address)

    # STEP 3: Submit the Form
    print("Submitting the form...")
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)  # Scroll to the Submit button
    submit_button.click()

    # STEP 4: Validate Output
    print("Validating the submitted data...")

    # Verify the output data
    output_name = driver.find_element(By.ID, "name").text
    output_email = driver.find_element(By.ID, "email").text
    output_current_address = driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
    output_permanent_address = driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text

    assert full_name in output_name, "Full Name does not match!"
    assert email in output_email, "Email does not match!"
    assert current_address in output_current_address, "Current Address does not match!"
    assert permanent_address in output_permanent_address, "Permanent Address does not match!"

    print("Form submitted and data validated successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # STEP 5: Close the Browser
    print("Closing the browser...")
    time.sleep(3)
    driver.quit()
