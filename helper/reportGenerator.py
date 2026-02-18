from helper.dateAndTime import reportDateCompare
from data.database import DBmanager
from pathlib import Path

def monthlyReport():
    with open('helper/reportSavingPath.txt', 'r') as pathFile:
        path = Path(pathFile.read())

    if path.exists():
        with open('helper/reportGenerationDate.txt','r') as reportLog:
            data = reportLog.read()
        update, year, month = reportDateCompare(data)
        if update == 'Outdated':
            print('Outdated')
            db = DBmanager()
            categories, total_income = db.ReportData(year, month)
            total_expense = db.Expense()

            with open('data/budget.txt', 'r') as file:
                budgetRead = file.readline()

            TXT = f'''FundTrack Monthly Report
=========================
Year: {year}
Month: {month}

Total Income: {total_income} AED

Budget: {float(budgetRead):,.2f} AED
Total Expense: {total_expense} AED
Saved: {float(budgetRead)-total_expense:,.2f} AED

Expenses By Category:

'''
            for i in categories:
                TXT+=f'- {i[0]}: {i[1]:,.2f} AED\n'


            with open(str(path)+f'/Report{year}-{month}.txt','a') as report:
                report.write(TXT)
            with open('helper/reportGenerationDate.txt','w') as reportLog:
                reportLog.write(f'{year}-{month}')