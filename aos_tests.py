import unittest
import aos_methods as methods
import aos_locators as locators


class AosPositiveTestCases(unittest.TestCase):
    @staticmethod  # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_aos():
        methods.set_up()
        methods.create_user()
        methods.validate_account()
        methods.check_out_shopping_cart()
        methods.validate_order_created()
        methods.delete_order_and_validate()
        methods.delete_user_account()
        methods.validate_account_deleted()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.check_availability_logo()
        methods.check_availability_text()
        methods.check_availability_links()
        methods.log_out()
        methods.contact_us_form()
        methods.check_social_network_facebook_twitter_linkedin()
        methods.teardown()









