import datetime
from time import sleep
#   import button as button
#   import LinkedIn
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#   from selenium.webdriver.support.ui import Select
import aos_locators as locators

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


# ==================================================================================================================
# using Fixture method - to open web browser:
def set_up():
    print(f'--------------------------------------------* Test Start Day/Time *---------------------------------------')
    print(f'Test Started at: {datetime.datetime.now()}')
    print(f'-----------------------* Current Website: url and Title  *---------------------------------')
#   maximize the browser window
    driver.maximize_window()
#   time how long website will be displayed(30s)
    driver.implicitly_wait(30)
#   navigating to the "advantage shopping" website
    driver.get(locators.aos_url)
    print(f'aos url: --{locators.aos_url}')
    print(f'Current page url: --{driver.current_url}')
    print(f'Current page Title: --{locators.aos_title}')
    print(f'------------------------------------* Home page, Home title *---------------------------------------------')
#   URL and home page title are as expected {confirmed} or ---is not = in {else}
    print(f'Home page url is: -- {locators.aos_url}')
    print(f'Home page title is: ', {driver.title})
    print(f'---------------------------* Login into Advantage Shopping" web site *------------------------------------')
    if driver.current_url == locators.aos_url and driver.title == locators.aos_title:
        print(f'We\' are at "Advantage Shopping" web page:-- {driver.current_url}')
        print(f'Thank you for coming today at the website of  -- {driver.title}')
    else:
        print(f'We\'re not at the "Advantage Shopping" home page. Please try again!')
        sleep(1)
        teardown()


# ===================================================================================================================
#   Creating New Account - using Faker library fake data
def create_user():
    sleep(1)
    print(f'--------------------------* Creating New User Account *------------------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(1)
    #   if driver.current_url == locators.aos_register_url and driver.title == locators.aos_title:
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    sleep(1)
    print(f'new user name: -- {locators.new_username}')
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(1)
    print(f'new user email address: -- {locators.email}')
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    sleep(1)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
    sleep(1)
    print(f'new user password: -- {locators.new_password}')

    # else:
    # print('something is wrong in this part of code')
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(1)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(1)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
    sleep(1)
    driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)
    sleep(1)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(1)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    sleep(1)
    # driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state_province_region)
    # sleep(3)
    # driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    # sleep(3)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(1)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(1)
    print(f'Account for New User: **{locators.full_name}** is created.')


#   ================================================================================================================
# Validating New Account created:(user name displayed)
def validate_account():
    sleep(2)
    print(f'--------------------------* Validating User Account *------------------------------------')
    if driver.current_url == locators.aos_url and driver.title == locators.aos_title:
        sleep(1)
        if driver.find_element(By.XPATH, f'//a[contains(.,"{locators.new_username}")]'):
            sleep(1)
            print(f'*Username {locators.new_username} is displayed on the Menu on the Top right corner of the screen*')
        else:
            print('User not found.')


#   =================================================================================================================
#   Logout:
def log_out():
    sleep(1)
    print(f'---------------------------------* Logout Information *-----------------------------------------------')
    if driver.current_url == locators.aos_url:
        #   driver.find_element(By.LINK_TEXT, 'My account').click()
        driver.find_element(By.XPATH, '//*[@id="menuUserLink"]').click()
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
        sleep(1)
        print("Successfully logged out from the User account")
    else:
        print("Something went wrong.Maybe user is logged out or deleted.")


#  ==================================================================================================================
#  Login:
def log_in(username, password):
    sleep(2)
    print(f'--------------------------------* User Login Information *-------------------------------------------')
    if driver.current_url == locators.aos_url:
        sleep(1)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(1)
        driver.find_element(By.NAME, 'username').send_keys(username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(password)
        sleep(1)
        driver.find_element(By.NAME, 'remember_me').click()
        sleep(1)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(1)
        print(f'Client is login to --{locators.aos_url} website.')
        print(f'Username: {locators.new_username}\nPassword: {locators.new_password}')
    else:
        print("We do not have user with this name. Please check your spelling.")


#  ===================================================================================================================
#   Checking availability/clickability = social media images(Facebook,Twitter, Linkedin) at HOME PAGE (FOLLOW US section)
def check_social_network_facebook_twitter_linkedin():
    sleep(2)
    print(f'--------------------------------* Check Social Network - Facebook *---------------------------------------')
    if driver.find_element(By.XPATH, '//h3[contains(., "FOLLOW US")]').is_displayed():
        print('We could find image  "FOLLOW US" displayed')
        print(f' -----------------------------')
        sleep(2)
        facebook = driver.find_element(By.XPATH, '//img[@name="follow_facebook"]')
        sleep(2)
        print(f' the Facebook img display is: {facebook.is_displayed()}')
        print(f' the Facebook img is clickable: {facebook.is_enabled()}')
        driver.find_element(By.XPATH, '//img[@name="follow_facebook"]').click()
        sleep(2)
        if driver.current_url == 'https://www.facebook.com/MicroFocus/':
            sleep(2)
            print(f'Social media link Facebook is available and clickable')
            #   driver.back()
        else:
            print('Facebook page not found')
            #   driver.switch_to.window(driver.window_handles[0])
            #   driver.back()
            sleep(2)
            print(f' -----------------------------')
#    ------------------------------------------------------------------------------------------------------------------
        twitter = driver.find_element(By.XPATH, '//img[@name="follow_twitter"]')
        sleep(2)
        print(f' the Twitter img display is: {twitter.is_displayed()}')
        print(f' the Twitter img clickable condition is: {twitter.is_enabled()}')
        driver.find_element(By.XPATH, '//img[@name="follow_twitter"]').click()
        sleep(2)
        if driver.current_url == 'https://twitter.com/MicroFocus/':
            sleep(2)
            print(f'Social media link Twitter is available and clickable')
            #   driver.back()
        else:
            print('Twitter page not found')
            #   driver.back()
            print(f' -----------------------------')
#   ----------------------------------------------------------------------------------------------------------------
        linkedin = driver.find_element(By.XPATH, '//img[@name="follow_linkedin"]')
        sleep(2)
        # print(f' the LinkedIn img display is: {linkedin.is_displayed()}')
        # print(f' the LinkedIn img display is: {linkedin.is_enabled()}')
        driver.find_element(By.XPATH, '//img[@name="follow_linkedin"]').click()
        sleep(2)
        if driver.current_url == 'https://www.linkedin.com/company/micro-focus/':
            sleep(2)
            print(f'Social media link Linkedin is available and clickable')
        else:
            print('Expected Linkedin page not found.')
            print('Please check your code.')


#  ===================================================================================================================
#   checking shopping cart, paying for the order
def check_out_shopping_cart():
    sleep(2)
    print(f'------------------------------* Check Out Shopping Cart *----------------------------------------------')
    # if driver.current_url == 'https://www.advantageonlineshopping.com/#/':
    driver.get('https://advantageonlineshopping.com/#/product/10')
    sleep(2)
    driver.find_element(By.NAME, 'save_to_cart').click()
    sleep(2)
    driver.find_element(By.ID, 'shoppingCartLink').click()
    sleep(2)
    driver.find_element(By.NAME, 'check_out_btn').click()
    sleep(2)
    if driver.current_url == 'https://advantageonlineshopping.com/#/login':
        driver.find_element(By.NAME, 'usernameInOrderPayment').send_keys(locators.new_username)
        sleep(2)
        driver.find_element(By.NAME, 'passwordInOrderPayment').send_keys(locators.new_password)
        sleep(2)
        driver.find_element(By.ID, 'login_btnundefined').click()
        sleep(2)
        # information about buyer
        print(f' ORDER PAYMENT and SHIPPING DETAILS are displayed on order page.')
        print(f' ORDER SUMMARY information is displayed.')
        print(f' Customer Name {locators.full_name} is displayed on shipping details page.')
        sleep(2)
        driver.find_element(By.ID, 'next_btn').click()
        sleep(2)
        if driver.current_url == 'https://advantageonlineshopping.com/#/orderPayment':
            sleep(2)
            driver.find_element(By.NAME, 'safepay').click()
            sleep(2)
            driver.find_element(By.NAME, 'safepay_username').send_keys(locators.new_username)
            sleep(2)
            driver.find_element(By.NAME, 'safepay_password').send_keys(locators.new_password)
            sleep(2)
            print(f' -----------------------------')
            print(f' Payment info entered for SafePay are included.')
            print(f' Customer Name: {locators.full_name}')
            print(f' Username for Payments for this Orderis: {locators.new_username}')
            print(f' Customer Password: {locators.new_password}')
            driver.find_element(By.NAME, 'save_safepay')
            sleep(2)
            driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
            sleep(2)
        else:
            print(f'You are not at "Advantage Online Shopping" site, you are at:', driver.current_url)
    else:
        print("current_url:", driver.current_url)


#  ===================================================================================================================
def validate_order_created():
    sleep(2)
    print(f'------------------------------* Validated Order Created *----------------------------------------------')
    if driver.current_url == 'https://advantageonlineshopping.com/#/orderPayment':
        sleep(2)
        print(f' Order Payment was made and thank you message was displayed:"Thank you for buying with Advantage"')
        sleep(2)
        locators.tracking_number = driver.find_element(By.ID, 'trackingNumberLabel').text
        sleep(2)
        print(f' Tracking number was captured for this order:', locators.tracking_number)
        sleep(2)
        locators.order_number = driver.find_element(By.ID, 'orderNumberLabel').text
        print(f' Order number was captured for this order: {locators.order_number}')
        print(f' Shipping to: {locators.full_name}, Address:{locators.address}')
        print(f' Phone number: {locators.phone_number}')
        print(f' Date and Time: {datetime.datetime.now()}')
    else:
        print(f'current url:', driver.current_url)


#  ===================================================================================================================
#   checking if order is deleted
def delete_order_and_validate():
    sleep(2)
    print(f'--------------------------------* Delete Order and Validation order Deleted *---------------------------')
    driver.get('https://advantageonlineshopping.com/#/MyOrders')
    if driver.current_url == 'https://advantageonlineshopping.com/#/MyOrders':
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'REMOVE').click()
        sleep(2)
        driver.find_element(By.ID, 'confBtn_1').click()
        sleep(2)
        print(f'Order is deleted.')
# --------------------------------------------------------------------------------------------------------------------
        sleep(2)
        print(f'Label with information that "--No orders--" is displayed')
        #   assert driver.find_element(By.XPATH, '//label[contains(text(), "No orders"]').is_displayed()
        sleep(2)
        locators.continue_shopping = driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').text
        print(f'Message for next step was captured: {locators.continue_shopping}')
        print(f'Order deleted is validated by validating "No orders" text displayed.')
    else:
        print(f'Order is not deleted., print url: {driver.current_url}')


#  ===================================================================================================================
#   checking items on home page clickable yes/no
def check_availability_logo():
    sleep(2)
    print(f'---------------------------* Items on Home page: LOGO available/clickable   *--------------------')
    if driver.current_url == locators.aos_url:
        sleep(2)
        logo = driver.find_element(By.ID, 'Layer_1')
        sleep(2)
        # logo = driver.find_element(By.CLASS_NAME, 'roboto-medium ng-binding')
        # logo = driver.find_element(By.CLASS_NAME, 'logoDemo roboto-light ng-binding')
        print(f'The display feature of the logo is: {logo.is_displayed()}')
        print(f'The enable feature of the logo is: {logo.is_enabled()}')
        print(f'LOGO of Advantage Shopping is displayed and clickable.You can proceed with your shopping!')


#  ===================================================================================================================
#   checking items on home page (shown by "text" on home page)  available and clickable
def check_availability_text():
    sleep(2)
    print(f'---------------------------* Items on Home page available/clickable (text)  *--------------------')
    if driver.current_url == 'https://www.advantageonlineshopping.com/#/':
        assert driver.find_element(By.XPATH, '//span[contains(., "SPEAKERS")]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'speakersTxt').click()
        sleep(2)
        driver.back()
        driver.find_element(By.ID, 'speakersLink').click()
        sleep(2)
        driver.back()
        print(f'Item SPEAKERS is displayed and clickable.You can proceed with your shopping!')
#   -----------------------------------------------------------------------------------------------------------------
        assert driver.find_element(By.XPATH, '//span[contains(., "TABLETS")]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'tabletsTxt').click()
        sleep(2)
        driver.back()
        driver.find_element(By.ID, 'tabletsLink').click()
        sleep(2)
        driver.back()
        print(f'Item TABLETS is displayed and clickable.You can proceed with your shopping-HOME PAGE')
#  ----------------------------------------------------------------------------------------------------
        assert driver.find_element(By.XPATH, '//span[contains(., "HEADPHONES")]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'headphonesTxt').click()
        sleep(2)
        driver.back()
        driver.find_element(By.ID, 'headphonesLink').click()
        sleep(2)
        driver.back()
        print(f'Item HEADPHONES is displayed and clickable.You can proceed with your shopping!')
#       ----------------------------------------------------------------------------------------------------
        assert driver.find_element(By.XPATH, '//span[contains(., "LAPTOPS")]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'laptopsTxt').click()
        sleep(2)
        driver.back()
        driver.find_element(By.ID, 'laptopsLink').click()
        sleep(2)
        driver.back()
        print(f'Item LAPTOPS is displayed and clickable. You can proceed with your shopping!')
#       ----------------------------------------------------------------------------------------------------
        assert driver.find_element(By.XPATH, '//span[contains(., "MICE")]').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'miceTxt').click()
        sleep(2)
        driver.back()
        sleep(2)
        driver.find_element(By.ID, 'miceLink').click()
        sleep(2)
        driver.back()
        print(f'Item MICE is displayed and clickable.You can proceed with your shopping!')


#  ===================================================================================================================
#   checking for:our [products,special offer.popular items, contact us]
def check_availability_links():
    sleep(3)
    print(f'---------------------------* Items on Home page available/clickable (links)  *--------------------')
    print(f'*Home Page Menu:Items on Home page clickable (links)[our products,special offer,popular items,contact us]*')
    if driver.current_url == locators.aos_url:
        #   driver.find_element(By.CLASS_NAME, 'nav-li-Links').is_displayed()
        driver.find_element(By.XPATH, '//a[contains(., "OUR PRODUCTS")]').click()
        sleep(2)
        # driver.find_element(By.NAME, 'mobileSearch').click()
        # sleep(2)
        # driver.back()
        sleep(2)
        print(f'Link to "OUR PRODUCTS" is displayed and clickable.on click opens page with "Our Products"!')
#   -----------------------------------------------------------------------------------------------------------------
#       assert driver.find_element(By.CLASS_NAME, 'menu navLinks roboto-regular ng-scope').()
        driver.find_element(By.XPATH, '//a[contains(., "SPECIAL OFFER")]').click()
        sleep(2)
        # driver.find_element(By.NAME, 'mobileSearch').click()
        # sleep(2)
        # driver.back()
        sleep(2)
        print(f'Link to "SPECIAL OFFER" is displayed and clickable.On click opens page with "Special Offer!"')
#     ------------------------------------------------------------------------------------------------------------------
#    assert driver.find_element(By.CLASS, [ng-scope]').is_displayed()
        sleep(2)
        driver.find_element(By.XPATH, '//a[contains(., "POPULAR ITEMS")]').click()
        sleep(2)
        # driver.find_element(By.NAME, 'mobileSearch').click()
        # sleep(2)
        # driver.back()
        sleep(2)
        print(f'Link to "POPULAR ITEMS" is displayed and clickable.On click opens page with list of "Popular Items!"')
#    ------------------------------------------------------------------------------------------------------------------
#     assert driver.find_element(By.CLASS, [menu navLinks roboto-regular ng-scope]').is_displayed()
        sleep(2)
        driver.find_element(By.XPATH, '//a[contains(., "CONTACT US")]').click()
        sleep(2)
        # driver.find_element(By.NAME, 'mobileSearch').click()
        # sleep(2)
        # driver.back()
        sleep(2)
        print(f'Link to "CONTACT US" form is displayed and clickable.On click opening form "Contact Us".')


#  ===================================================================================================================
#  checking form contact us, fill out, send, etc.
def contact_us_form():
    sleep(2)
    print(f'--------------------------* Contact Us form:filling out & sending *------------------------------------')
    driver.find_element(By.XPATH, '//a[contains(., "CONTACT US")]').click()
    #  driver.find_element(By.XPATH, '//*[@id = "supportCover"]/div/h1').click()
    sleep(2)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(2)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject)
    sleep(2)
    driver.find_element(By.ID, 'registerSuccessCover').is_displayed()
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(2)
    print(f'Form "CONTACT US" was submitted.')
    sleep(2)
    print(f'Message "Thank you for contacting Advantage support." is confirmed visually.')
    sleep(2)
    driver.find_element(By.XPATH, '//a[contains(., "CONTINUE SHOPPING")]').click()
    print(f'On Submit text-link to "CONTINUE SHOPPING" is displayed and clickable. On click opening product page.')
    sleep(2)


#  ===================================================================================================================
#  deleting user, checking if user is deleted
def delete_user_account():
    sleep(2)
    print(f'------------------------------* Deleted User Account - Information *-------------------------------------')
    driver.find_element(By.XPATH, f'//a[@id="menuUserLink"]/span[contains(.,{locators.new_username})]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    sleep(1)
    if driver.find_element(By.XPATH, f'//*[contains(., "{locators.full_name}")]').is_displayed():
        sleep(1)
        #   print({locators.new_username}, 'is different from ', {locators.aos_username})
        print(f'User Account Full Name is displayed: {locators.full_name}')
        driver.find_element(By.XPATH, '//button/div[contains(., "Delete Account")]').click()
        sleep(1)
        driver.find_element(By.XPATH, '//div[@class="deletePopupBtn deleteRed"]').click()
        sleep(1)
        print(f'------------------------* Account Deleted: Information *--------------------------------------------')
        print(f'The user account for {locators.full_name} was deleted successfully')
    else:
        print(f'The user account for {locators.full_name} was NOT deleted ')


#  ===================================================================================================================
#   validating that account is deleted
def validate_account_deleted():
    sleep(2)
    print(f'--------------------------------* Validate-Account is Deleted *----------------------------------------')
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(3)
        driver.find_element(By.XPATH, "//input[@name = 'username']").send_keys(locators.new_username)
        sleep(3)
        driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys(locators.new_password)
        sleep(3)
        #  assert driver.find_element(By.XPATH, f'//label[contains[text(), "Incorrect user name or password.")]').is_displayed()
        sleep(2)
        print("Confirmed that account is deleted.[Incorrect user name or password.].")
    else:
        print("Account Deleted: needs further confirmation.")


#  ===================================================================================================================
#   Close the browser and display user-friendly messages:
def teardown():
    sleep(2)
    if driver is not None:
        print(f' ----------------------* Thank you for visiting advantage online shopping website  *----------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        print(f'----------------------------------------------------------------------------------------------------')
        sleep(1)
        #   driver.close()
        sleep(1)
        driver.quit()
        sleep(1)


#  ===================================================================================================================
#   ----------*  List of Functions: *----------
# set_up()
# create_user()
# validate_account()
# check_availability_logo()
# check_availability_text()
# check_availability_links()
# log_out()
# log_in(locators.new_username, locators.new_password)
# check_out_shopping_cart()
# validate_order_created()
# delete_order_and_validate()
# delete_user_account()
# validate_account_deleted()
# contact_us_form()
# check_social_network_facebook_twitter_linkedin()
# teardown()
