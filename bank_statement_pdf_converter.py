from PyPDF2 import PdfReader
import pandas as pd
import numpy as np

#Current Month(s)
l = '09/'
t = '10/'

#PDF File
pdf = "YOUR-BANK-STATEMENT.PDF"

#Read file
reader = PdfReader(pdf)
totalPages = len(reader.pages)

#Get the transactions
segments = 0
transaction = ''
all_transactions = []

for p in range(0, totalPages):
    page = reader.pages[p]
    text = page.extract_text().split("\n")
    segments = len(text)
    for i in range(0, segments):
        if 'Beginning Balance' in text[i]:
            continue
        elif 'Ending Balance' in text[i]:
            continue
        elif 'For additional information' in text[i]:
            continue
        elif 'Statement Period' in text[i]:
            continue
        elif l in text[i]:
            transaction = text[i]
            all_transactions.append(transaction)
        elif t in text[i]:
            transaction = text[i]
            all_transactions.append(transaction)
        else:
            continue

#Split Data (Date, Balance, Type, Vendor)
dates = []
balances = []
typeTransaction = []
vendor = []
descriptions = []
split_desc = []

#Select All Dates
for d in range (0, len(all_transactions)):
    transaction = all_transactions[d]
    dates.append(transaction[:5])

#Update Transaction Descriptions
for a in range (0, len(all_transactions)):
    transaction = all_transactions[a]
    descriptions.append(transaction[6:])

#Take Balance From Descriptions
for b in range (0, len(descriptions)):
    description = descriptions[b]
    splitList = description.split(" ")
    balance = splitList[0]
    balance = balance.replace(',', '')
    balances.append(balance)

#Remove Balance From Description
for bd in range (0, len(descriptions)):
    description = descriptions[bd]
    balance = balances[bd]

    if balance in description:
        description = description.replace(f'{balance}', '')
        split_desc.append(description)
    else:
        split_desc.append(description)

#Find Transaction Types
final_dates = []
final_balances = []
transactionTypes = []
final_desc = []

debit = 'DEBIT CARD PURCHASE'
recurring = 'RECURRING PURCHASE'
merchant = 'MERCHANT PAYMENT'
web = 'WEB INITIATED PAYMENT'
tele = 'TELEPHONE INITIATED PAYMENT'
overdraft = 'OVERDRAFT FEE'
international = 'INTERNATIONAL TRANS FEE'
fee = 'FEE'
zellePay = 'ONLINE TRANSFER TO'
zelleRec = 'ONLINE TRANSFER FROM'
withdrawal = 'WITHDRAWAL'
deposit = 'DEPOSIT'
dcReturn = 'DEBIT CARD RETURN'
payroll = 'PAYROLL'
idalert = '5/3 ID ALERT'
moneylink = 'MONEYLINK'
other = 'PYMT'

for dc in range (0, len(split_desc)):
    current = split_desc[dc]
    if debit in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Purchase')
        final_desc.append(split_desc[dc])
    elif recurring in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Recurring')
        final_desc.append(split_desc[dc])
    elif merchant in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Purchase')
        final_desc.append(split_desc[dc])
    elif moneylink in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Investment')
        final_desc.append(split_desc[dc])
    elif web in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Bill')
        final_desc.append(split_desc[dc])
    elif tele in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Bill')
        final_desc.append(split_desc[dc])
    elif overdraft in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Overdraft')
        final_desc.append(split_desc[dc])
    elif international in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('International Fee')
        final_desc.append(split_desc[dc])
    elif fee in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Fee')
        final_desc.append(split_desc[dc])
    elif other in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Purchase')
        final_desc.append(split_desc[dc])
    elif zellePay in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Zelle Expense')
        final_desc.append(split_desc[dc])
    elif zelleRec in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Zelle Income')
        final_desc.append(split_desc[dc])
    elif withdrawal in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('ATM Withdrawal')
        final_desc.append(split_desc[dc])
    elif deposit in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Deposit')
        final_desc.append(split_desc[dc])
    elif dcReturn in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Return')
        final_desc.append(split_desc[dc])
    elif payroll in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Income')
        final_desc.append(split_desc[dc])
    elif idalert in current:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('Fee')
        final_desc.append(split_desc[dc])
    else:
        final_dates.append(dates[dc])
        final_balances.append(balances[dc])
        transactionTypes.append('N/A')
        final_desc.append(split_desc[dc])

#Identify Vendors
vendors = [['Subway', 'Subway', 'Food'], ['CIRCLE K', 'Circle K', 'Gas'], ['SCHWAB', 'Schwab', 'Investments'], ['APPLE.COM', 'Apple', 'Apps'], ["MCDONALD'S", "McDonald's", 'Food'], ['Prime Video', 'Amazon', 'Streaming'], ['CVS/PHARM', 'CVS', 'Convenience'], ['STARBUCKS', 'Starbucks', 'Coffee'], ['DD/BR', 'Dunkin', 'Food'], ['BURGER KING', 'Burger King', 'Food'], ['CHICK-FIL-A', 'Chick-fil-a', 'Food'], ['Los Bravos Mexican', 'Los Bravos', 'Food'], ['SPOTIFY', 'Spotify', 'Apps'], ['Amazon Prime', 'Amazon', 'Shopping'], ['SOCIETY OF ST VINC', 'Society of St. Vincent de Paul', 'Non-Profit'], ['DOORDASH', 'Doordash', 'Food'], ['STEAMGAMES.COM', 'Steam', 'Videogames'], ['CODECADEMY', 'Codecademy', 'Education'], ['BEST BUY', 'Best Buy', 'Technology'], ['MICROSOFT*XBOX', 'Xbox', 'Videogames'], ['Nyx*Five Star Food', 'Unknown Fast Food', 'Food'], ['TARGET', 'Target', 'Shopping'], ['G.D. RITZYS', "G.D. Ritzy's", 'Food'], ['Purdue FCU', 'Purdue Federal Credit Union', 'Bank'], ['Peacock', 'Peacock', 'Streaming'], ['ESPN Plus', 'ESPN+', 'Streaming'], ['STEAK-N-SHAKE', "Steak N' Shake", 'Food'], ['MLB.TV', 'MLB.TV', 'Streaming'], ['HELP.MAX.COM', 'HBO Max', 'Streaming'], ['CRUNCH F', 'Crunch Fitness', 'Gym'],['AI SHORT COURSE', 'Augustine Institute', 'Education'], ["DOMINO'S", 'Dominos', 'Food'], ['GOOGLE *Youtube', 'Youtube TV', 'Streaming'], ['IBJ ONLINE', 'Indiana Business Journal', 'Journal'], ['JIMMY JOHNS', "Jimmy John's", 'Food'], ['VGINSIGHTS.COM', 'vginsights.com', 'Subscription'], ['WITHDRAWAL', 'ATM Withdrawal', 'ATM'], ['INTERNATIONAL TRANS FEE', 'International Transaction Fee', 'Fee'], ['POPEYES', 'Popeyes', 'Food'], ['EVANSVILLE COURIER', 'Evansville Courier', 'Journal'], ['TREASURE COAST', 'Treasure Coast', 'Unknown'], ['ONLINE TRANSFER TO', 'Zelle', 'Zelle'], ['ONLINE TRANSFER FROM', 'Zelle', 'Zelle'], ['DONUT BANK', 'Donut Bank', 'Coffee'], ['CHASE', 'Chase Bank', 'Bank'], ['NEELKANTH', 'Neelkanth', 'Unknown'], ['RULER FOO', 'Ruler Foods', 'Groceries'], ['LIBERTY MUTUAL', 'Liberty Mutual', 'Insurance'], ['KOHLS', 'Kohls', 'Shopping'], ['SQ *HARWOOD BOOST', 'SQ HARWOOD', 'Unknown'], ['Dropbox', 'Dropbox', 'Technology'], ['HARDEES', "Hardee's", 'Food'], ['Microsoft*Xbox', 'Xbox', 'Videogames'], ['*RED SWING COFF', 'Red Swing Coffee', 'Coffee'], ["FREDDY'S", "Freddy's", 'Food'], ['GREAT CLIPS', 'Great Clips', 'Haircuts'], ['SQSP*', 'Squarespace', 'Technology'], ["PAPA JOHN'S", "Papa John's", 'Food'], ['HOLY CROSS COLLEGE', 'Holy Cross College', 'Education'], ['ADOBE', 'Adobe', 'Technology'], ['ID ALERT', 'Fifth Third Bank', 'Bank'], ['PLANET FIT', 'Planet Fitness', 'Gym'], ['JPMS LLC', 'Chase', 'Broker'], ['DEACONESS HEALTH', 'Deaconess', 'Health'], ['JEANIE DEPOSIT', 'Check Deposit', 'Deposit']]
fin_date = []
fin_balance = []
fin_type = []
final_vendors = []
final_categories = []
error_transactions = []

for d in range (0, len(split_desc)):
    desc = split_desc[d]
    for v in range (0, len(vendors)):
        if vendors[v][0] in desc:
            fin_date.append(final_dates[d])
            fin_balance.append(final_balances[d])
            fin_type.append(transactionTypes[d])
            final_vendors.append(vendors[v][1])
            final_categories.append(vendors[v][2])
            break
        elif v < len(vendors):
            continue
        else:
            error_transactions.append(desc)




#Create Data Frame
trn = pd.DataFrame({'Date': fin_date, 'Balance': fin_balance, 'Transaction Type': fin_type, 'Vendor': final_vendors, 'Category': final_categories})
error_exp = pd.DataFrame({'Transaction': error_transactions})

trn.to_csv('transactions.csv', index=False)
error_exp.to_csv('errors.csv', index=False)

print('Transactions Loaded Successfully!')
