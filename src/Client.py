from numpy import random

from src.ApplicationServer import ApplicationServer
from src.DatabaseServer import DatabaseServer
from src.Firewall import Firewall
from src.InteractionType import InteractionType
import src.constants as const
import src.Messages as Msg
from src.WebServer import WebServer


class Client(object):

    def __init__(self):
        self.pa = 0
        self.pb = 0

        self.interaction = InteractionType.INTERACTION_ONE
        self.arrivedAt = 0
        self.requestDuration = 0

        self.wsIn = 0
        self.wsInDuration = 0

        self.asIn = 0
        self.asInDuration = 0

        self.bdIn = 0
        self.bdDuration = 0
        self.bdOut = 0

        self.asOut = 0
        self.asOutDuration = 0

        self.wsOut = 0
        self.wsOutDuration = 0

        self.receivingDuration = 0
        self.firewallDelay = 0

        self.get_msgs()
        self.decide_interaction()
        self.get_processing_durations()

    def get_msgs(self):
        self.m1 = Msg.get_m1()
        self.m2 = Msg.get_m2()
        self.m3 = Msg.get_m3()
        self.m4 = Msg.get_m4()
        self.m5 = Msg.get_m5()
        self.m6 = Msg.get_m6()
        self.m7 = Msg.get_m7()
        self.m8 = Msg.get_m8()

    def decide_interaction(self):
        self.pa = random.uniform(0, 1)  # Random float x, 1.0
        self.pb = random.uniform(0, 1)

        if self.pa > const.p1_ws_to_as:
            self.interaction = InteractionType.INTERACTION_ONE
        elif self.pb > const.p2_as_to_db:
            self.interaction = InteractionType.INTERACTION_TWO
        else:
            self.interaction = InteractionType.INTERACTION_THREE

    def get_processing_durations(self):
        self.wsInDuration, self.wsOutDuration = WebServer.get_processing_time(self.interaction)
        self.asInDuration, self.asOutDuration = ApplicationServer.get_processing_time()
        self.firewallDelay = Firewall.get_processing_time(self.interaction)
        self.bdDuration = DatabaseServer.get_processing_time()
