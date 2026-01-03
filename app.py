from exceptions import PaymentException
from user import User


class MiniVenmo:
    def create_user(self, username, balance, credit_card_number):
        # TODO: add code here
        user = User(username)
        user.add_to_balance(balance)
        user.add_credit_card(credit_card_number)
        return user

    def retrieve_feed(self, user):
        feed = user.retrieve_feed(user)
        return feed

    def render_feed(self, feed):
        # Bobby paid Carol $5.00 for Coffee
        # Carol paid Bobby $15.00 for Lunch
        # TODO: add code here
        for entry in feed:
            print(entry)
        

    @classmethod
    def run(cls):
        venmo = cls()

        bobby = venmo.create_user("Bobby", 5.00, "4111111111111111")
        carol = venmo.create_user("Carol", 10.00, "4242424242424242")

        try:
            # should complete using balance
            bobby.pay(carol, 5.00, "Coffee")
        
            # should complete using card
            carol.pay(bobby, 16.00, "Lunch")
        except PaymentException as e:
            print(e)

        bobby.add_friend(carol)
        feed = bobby.retrieve_feed()
        venmo.render_feed(feed)


if __name__ == '__main__':
    MiniVenmo.run()
