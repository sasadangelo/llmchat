
# Conversation - a Generic ChatBot conversation
#
# This class represents a generic chatbot conversation.
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# SPDX-License-Identifier: MIT

# This class represents a generic chatbot conversion. It contains the chat history of the messages and the cost of each one.
class Conversation:
    def __init__(self):
        self.messages = []
        self.costs = []

    def add_message(self, message):
        self.messages.append(message)

    def add_cost(self, cost):
        self.costs.append(cost)

    def get_messages(self):
        return self.messages

    def get_total_cost(self):
        return sum(self.costs)

    def get_costs(self):
        return self.costs