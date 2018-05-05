# -*- coding: utf-8 -*-

import sys
from Spider import cryptocurrency_spider
from Database import mongoDB_controller


class Motor_Extracion_Injection:

    def __init__(self):
        print "[*] Motor init  MongoBD"
        self.mongo = mongoDB_controller.database_Mongo()

    #----------------- Injector Options  ------------
    def insert_data(self, moneyList):
        print "[*] Motor insert data"
        self.mongo.insert_data("Money_Collection", moneyList)

    #----------------- Menu options ------------
    def view_collection(self):
        print "[*] Motor view collection"
        self.mongo.view_data_incollection('Money_Collection')

    def view_MongoData(self):
        print "[*] Mottor view data"
        self.mongo.view_all_collections()
        #mongo.view_data_incollection('censys')

    def Spider(self):
        print "[*] Mottor init Spider"
        moneyList = cryptocurrency_spider.init_twisted_CryptoSpider()
        print "[*] Spider call Motor insert Data"
        self.insert_data(moneyList)
        print "[*] Data saved"

    def help(self):
        print "                       - Options -"
        print ""
        print "               exit"
        print "               help"
        print "               spider"
        print "               view"
        print "               collection"
        print "\n"

    def exit(self):
        print "[*] Exit \n"
        sys.exit()

    def Menu(self):
        while True:
            try:
                command = raw_input('[Motor] $: ')
                if command == 'exit':
                    exit()
                elif command == 'help':
                    self.help()
                elif command == 'spider':
                    self.Spider()
                elif command == 'view':
                    self.view_MongoData()
                elif command == 'collection':
                    self.view_collection()
                else:
                    print("[-] Command " + str(command) + " not recognise")
            except KeyboardInterrupt:
                print "[*] Stopping Information gathering"
                sys.exit()

def init_Motor():
    print "[*] Motor Gaaaaas !!!"
    motor = Motor_Extracion_Injection()
    motor.Menu()

if __name__ == "__main__":
    init_Motor()