
# Conversation - a Generic ChatBot conversation
#
# This class represents a generic chatbot conversation.
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# SPDX-License-Identifier: MIT
from langchain.schema import (SystemMessage)

# This class represents a generic chatbot conversion. It contains the chat history of the messages and the cost of each one.
class Conversation:
    def __init__(self):
        self.__init()

    def __init(self):
        self.messages = [
            SystemMessage(
                content="You are a helpful AI assistant. Reply your answer in mardkown format.")
        ]
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

    def clear(self):
        self.__init()
