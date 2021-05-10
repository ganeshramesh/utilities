# -*- coding: utf-8 -*-
import os, sys

def getYearMonthDayFromString(input_date_string, format='yyyymmdd'):
    if format == 'yyyy-mm-dd' or format == 'yyyy/mm/dd':
        if len(input_date_string) != 10:
            return None
        year = int(input_date_string[0:4])
        month = int(input_date_string[5:7])
        day = int(input_date_string[8:10])
    else:
        if len(input_date_string) != 8:
            return None
        year = int(input_date_string[0:4])
        month = int(input_date_string[4:6])
        day = int(input_date_string[6:8])
    return year, month, day

def getDateString(year, month, day, format='yyyymmdd'):
    month_str = str(month)
    if month < 10:
        month_str = '0' + month_str
    day_str = str(day)
    if day < 10:
        day_str = '0' + day_str
    year_str = str(year)
    delim = ''
    if format == 'yyyy/mm/dd':
        delim = '/'
    elif format == 'yyyy-mm-dd':
        delim = '-'
    return year_str + delim + month_str + delim + day_str

def getLastDayOfMonth(month, isLeapYear=False):
    if month == 2:
        if isLeapYear:
            return 29
        else:
            return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31
        
def isLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    elif year % 4 == 0:
        return True
    return False

def getNextDate(year, month, day):
    next_month = month
    next_year = year
    if day == getLastDayOfMonth(month, isLeapYear(year)):
        next_day = 1
        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_month = month + 1
    else:
        next_day = day + 1
    return next_year, next_month, next_day

def getPreviousDate(year, month, day):
    prev_month = month
    prev_year = year
    if day == 1:
        if month == 1:
            prev_year = year - 1
            prev_month = 12
        else:
            prev_month = month - 1
            prev_year = year
        prev_day = getLastDayOfMonth(prev_month, isLeapYear(prev_year))
    else:
        prev_day = day - 1
    return prev_year, prev_month, prev_day

def getNextDateForString(input_date_string, format='yyyymmdd'):
    (year, month, day) = getYearMonthDayFromString(input_date_string, format)
    (n_year, n_month, n_day) = getNextDate(year, month, day)
    return getDateString(n_year, n_month, n_day, format)

def checkDatesAround(input_date_string, format='yyyymmdd'):
    (year, month, day) = getYearMonthDayFromString(input_date_string, format)
    (p_year, p_month, p_day) = getPreviousDate(year, month, day)
    (n_year, n_month, n_day) = getNextDate(year, month, day)
    print(getDateString(p_year, p_month, p_day, 'yyyy-mm-dd'))    
    print(getDateString(n_year, n_month, n_day, 'yyyy-mm-dd'))    
