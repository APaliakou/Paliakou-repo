#!/usr/bin/env python
# coding: utf-8



class NewsFeed:
  
    def __init__(self, txt, txt2 ,txt3 = ''):
        from datetime import datetime
        from datetime import date
        self.txt = txt #use in def News and Privat_Ad as text of new or AD
        self.txt2 = txt2 #use in def News and Privat_Ad for City(news) and for expariationdate for Privat_Ad
        self.txt3 = txt3 #use in Doct_Reminder for place
        self.today = datetime.today()     
        self.t_day = datetime.strptime(str(date.today()), '%Y-%m-%d') #need to get only date without time to calculate diff

    
    def News(self):
        Begin = 'News --------------------\n'
        end = '\n-------------------------\n' 
        with open("C:/temp/Test.txt", "a") as text_file:
            text_file.write(f'{Begin} {self.txt} \n {self.txt2} {self.today} {end}')
        print(f'{Begin} {self.txt} \n {self.txt2} {self.today} {end}')
    
    def Privat_Ad(self):
        from datetime import datetime
        Begin = 'Private Ad ------------------\n'
        end = '\n-----------------------------\n'
        exp_date = datetime.strptime(self.txt2, '%Y-%m-%d')
        days_left = abs((self.t_day - exp_date).days)
        with open("C:/temp/Test.txt", "a") as text_file:
            text_file.write(f'{Begin} {self.txt} \nActual until: {exp_date}, {days_left} days left {end}')
        print(f'{Begin} {self.txt} \nActual until: {exp_date}, {days_left} days left {end}')
        
    def Doct_Reminder(self):
        Begin = 'Doctor Appointment ----------\n'
        End = '\n----------------------------\n'
        with open("C:/temp/Test.txt", "a") as text_file:
            text_file.write(f'{Begin} You have to visit: {self.txt} \nWhere:{self.txt3} . Your timeslot is: {self.txt2} {End}')
        print(f'{Begin} You have to visit: {self.txt} \nWhere:{self.txt3} . Your timeslot is: {self.txt2} {End}')
        
        
    


a = NewsFeed('LOR','2021-10-30','Nezavisimosti 58')

#a.News()
#a.Privat_Ad()
a.Doct_Reminder()
