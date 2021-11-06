#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ParseTxt:
    def __init__(self,txttype, filefolder):
        import os
        self.txttype = txttype
        self.filefolder = filefolder
        
    def ReadFile(self):
        try:
            #filefolder = 'C:/Users/Aliaksandr_Paliakou/Desktop'
            with open ('%s/Test.txt' % (self.filefolder), "r") as myfile:
                data=myfile.readlines()
        except OSError:
            print('Wrong file path')
        else:
            outputtxt = ''
            for i in range(len(data)):
                outputtxt += data[i]
        return outputtxt
            os.remove('%s/Test.txt' % (filefolder))


class NewsFeed:
  
    def __init__(self, txttype, filefolder, txt2 = '',txt3 = ''):
        from datetime import datetime
        from datetime import date
        self.txttype = txttype
        txt = ParseTxt(self.txttype, filefolder)
        txt_txt = txt.ReadFile()
        self.txt = txt_txt #use in def News and Privat_Ad as text of news or AD
        self.txt2 = txt2 #use in def News and Privat_Ad for City(news) and for expariationdate for Privat_Ad
        self.txt3 = txt3 #use in Doct_Reminder for place
        self.today = datetime.today()     
        self.t_day = datetime.strptime(str(date.today()), '%Y-%m-%d') #need to get only date without time to calculate diff

    
    def News(self):
        Begin = 'News --------------------\n'
        end = '\n-------------------------\n' 
        #print(self.txt)
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
        
        
    def Main_Funct(self):
        if self.txttype == 'News':
            a = self.News()
            return a
        elif self.txttype == 'Ad':
            a = self.Privat_Ad()
            return a
        elif self.txttype == 'Doctor Appointment':
            a = self.Doct_Reminder()
            return a
        else: 
            print('Please input correct text type: News, Ad or Doctor Appointment') 
        
a = NewsFeed('test', 'C:/Users/Aliaksandr_Paliakou/Desktop', '2021-11-01')

a.Main_Funct()
