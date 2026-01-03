from payment import Payment
from exceptions import (UsernameException, CreditCardException, PaymentException)
import re


class User:

    def __init__(self, username):
        self.credit_card_number = None
        self.balance = 0.0

        # activity feed, stores payment and friend events
        self.activity = []

        # store friends
        self.friends = set()

        if self._is_valid_username(username):
            self.username = username
        else:
            raise UsernameException('Username not valid.')


    def retrieve_feed(self):
        # TODO: add code here
        return self.activity

    def add_friend(self, new_friend):
        # TODO: add code here
        if new_friend.username == self.username:
            return

        self.friends.add(new_friend.username)
        new_friend.friends.add(self.username)

        friendship_msg = f"{self.username} and {new_friend.username} are now friends"
        
        self._log(friendship_msg)
        new_friend._log(friendship_msg)

    def _log(self, message):
        self.activity.append(message)

    def add_to_balance(self, amount):
        self.balance += float(amount)

    def add_credit_card(self, credit_card_number):
        if self.credit_card_number is not None:
            raise CreditCardException('Only one credit card per user!')

        if self._is_valid_credit_card(credit_card_number):
            self.credit_card_number = credit_card_number

        else:
            raise CreditCardException('Invalid credit card number.')

    def pay(self, target, amount, note):
        # TODO: add logic to pay with card or balance
        if self.balance >= amount:
            self.pay_with_balance(target, amount, note)
        else:
            self.pay_with_card(target, amount, note)

    def pay_with_card(self, target, amount, note):
        if self.credit_card_number is None:
            raise PaymentException("Must have a credit card to make a payment.")

        # simulate credit card charge
        self._charge_credit_card(self.credit_card_number)

        target.add_to_balance(amount)

        payment = Payment(amount, self.username, target.username, note)

        message = f"{payment.actor} paid {payment.target} ${payment.amount:.2f} for {payment.note}"

        # log on both feeds
        self._log(message)
        target._log(message)

    def pay_with_balance(self, target, amount, note):
        # TODO: add code here
        self.balance -= amount
        target.add_to_balance(amount)

        payment = Payment(amount, self.username, target.username, note)

        message = f"{payment.actor} paid {payment.target} ${payment.amount:.2f} for {payment.note}"

        # log on both feeds
        self._log(message)
        target._log(message)

    def _is_valid_credit_card(self, credit_card_number):
        return credit_card_number in ["4111111111111111", "4242424242424242"]

    def _is_valid_username(self, username):
        return re.match('^[A-Za-z0-9_\\-]{4,15}$', username)

    def _charge_credit_card(self, credit_card_number):
        # magic method that charges a credit card thru the card processor
        pass