import matplotlib.pyplot as pt
import numpy as np
import pandas as pd
import csv

df = pd.read_csv('banking_data.csv')
#distribution of clients' ages:
# ages = df['age']
# pt.hist(ages, color = 'red', edgecolor = 'black', bins = 50)
# pt.xlabel(r'Age(years)')
# pt.ylabel(r'Number')
# pt.title(r"Distribution of clients' ages")
# pt.show()

#distribution of clients' jobs:
# jobs = df['job']
# job_count = jobs.value_counts()
# print(job_count)
# print(job_count.describe())
# pt.barh(job_count.index, job_count.values, color = 'red', edgecolor = 'black')
# pt.ylabel(r'Job')
# pt.xlabel(r'Number')
# pt.title(r"Distribution of clients' jobs")
# pt.yticks(fontsize = 7)
# for value, index in enumerate(job_count.values):
#   pt.text(value, index, str(index), color = 'black', ha = 'center', va = 'bottom')
# pt.show()

#distribution of clients' marital status:
# marital = df['marital']
# marital_count = marital.value_counts()
# pt.pie(marital_count, labels = marital_count.index, autopct = '%2.2f%%')
# pt.title(r"Distribution of clients' marital status")
# pt.show()

#distribution of clients' education level:
# education = df['education']
# education_count = education.value_counts()
# pt.pie(education_count, labels = education_count.index, autopct = '%2.2f%%')
# pt.title(r"Distribution of clients' education level")
# pt.show()

#distribution of clients' default status:
# default = df['default']
# default_count = default.value_counts()
# pt.pie(default_count, labels = default_count.index, autopct = '%2.2f%%')
# pt.title(r"Distribution of clients' default status")
# pt.show()

#distribution of clients' average yearly balance:
# balance = df['balance']
# pt.hist(balance, color = 'red', edgecolor = 'black', bins = 60, log = True)
# pt.xlabel(r'Balance')
# pt.ylabel(r'Number')
# pt.title(r"Distribution of clients' average yearly balance")
# pt.show()

#distribution of clients' housing loans:
# housing = df['housing']
# housing_count = housing.value_counts()
# pt.pie(housing_count, labels = housing_count.index, autopct = '%2.2f%%')
# pt.title(r"Distribution of clients' housing loans")
# pt.show()

#distribution of clients' personal loans:
# personal = df['loan']
# personal_count = personal.value_counts()
# pt.pie(personal_count, labels = personal_count.index, autopct = '%2.2f%%')
# pt.title(r"Distribution of clients' personal loans")
# pt.show()

#distribution of clients' communication types:
# communication = df['contact']
# communication_count = communication.value_counts()
# pt.pie(communication_count, labels = communication_count.index, autopct = '%2.2f%%')
# pt.title(r"Distribution of clients' communication types")
# pt.show()

#distribution of last contact day:
# last_contact = df['day']
# last_contact_count = last_contact.value_counts()
# pt.bar(last_contact_count.index, last_contact_count.values, color = 'red', edgecolor = 'black')
# pt.title(r"Distribution of last contact day")
# pt.ylabel(r'Number')
# pt.xlabel(r'Day')
# pt.show()

#distribution of last contact month:
# month = df['month']
# month_count = month.value_counts()
# month_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
# month_count = month_count.reindex(month_order)
# pt.bar(month_count.index, month_count.values, color = 'red', edgecolor = 'black')
# pt.title(r"Distribution of last contact month")
# pt.ylabel(r'Number')
# pt.xlabel(r'Month')
# for value, index in enumerate(month_count.values):
#   pt.text(value, index, str(index), color = 'black', ha = 'center', va = 'bottom')
# pt.show()

#distribution of duration of last contact:
# duration = df['duration']
# pt.hist(duration, color = 'red', edgecolor = 'black', bins = 60, log = True)
# pt.title(r"Distribution of duration of last contact")
# pt.xlabel(r'Duration(sec)')
# pt.ylabel(r'Number')
# pt.show()

#distribution of calls performed in campaign:
# campaign = df['campaign']
# pt.hist(campaign, color = 'red', edgecolor = 'black', bins = 60, log = True)
# pt.title(r"Distribution of calls performed in campaign")
# pt.ylabel(r'Number')
# pt.xlabel(r'Number of calls')
# pt.show()

#distribution of days since client contacted was contacted from previous campaign:
# pdays = df['pdays']
# pt.hist(pdays, color = 'red', edgecolor = 'black', bins = 75, log = True)
# pt.title(r"Distribution of days since client was contacted from previous campaign")
# pt.xlabel(r'Days')
# pt.ylabel(r'Number')
# pt.show()

#distribution of contacts made before campaign:
# previous = df['previous']
# pt.hist(previous, color = 'red', edgecolor = 'black', bins = 40, log = True)
# pt.title(r"Distribution of contacts made before campaign")
# pt.ylabel(r'Number')
# pt.xlabel(r'Number of contacts')
# pt.show()

#outcomes of previous marketing campaign:
# outcomes = df['poutcome']
# outcomes_count = outcomes.value_counts()
# pt.bar(outcomes_count.index, outcomes_count.values, color = 'red', edgecolor = 'black')
# pt.title(r"Outcomes of previous marketing campaign")
# pt.ylabel(r'Number')
# pt.xlabel(r'Outcome')
# pt.show()

#distribution of clients subscribed to term deposit:
# term = df['y']
# term_count = term.value_counts()
# pt.pie(term_count, labels = term_count.index, autopct = '%2.2f%%')
# pt.title(r"Distribution of clients subscribed to term deposit")
# pt.show()

#correlation between jobs and term deposit:
# job_categories = {}

# for job in df['job'].unique():
#     job_categories[job] = {'yes': 0, 'no': 0}

# for index, row in df.iterrows():
#     if row['y'] == 'yes':
#         job_categories[row['job']]['yes'] += 1
#     elif row['y'] == 'no':
#         job_categories[row['job']]['no'] += 1

# subs_yes = [job_categories[job]['yes'] for job in job_categories]
# subs_no = [job_categories[job]['no'] for job in job_categories]

# subs_rate = [0]*len(subs_yes)

# for i in range(len(subs_yes)):
#   subs_rate[i] = (subs_yes[i] * 100) // (subs_yes[i] + subs_no[i]) 

# pt.barh(np.arange(len(job_categories)), subs_rate, color='red', edgecolor='black')
# pt.yticks(np.arange(len(job_categories)), job_categories.keys(), fontsize = 7)
# pt.title(r"Correlation between term deposit and job categories")
# pt.xlabel(r'Percentage of clients subscribed')
# pt.legend(['Yes', 'No'])
# pt.show()


#correlation between marital status and term deposit:

marital_categories = {}

for marriage in df['marital_status'].unique():
  marital_categories[marriage] = {'yes': 0, 'no': 0}

for index, row in df.iterrows():
  if row['y'] == 'yes':
    marital_categories[row['marital_status']]['yes'] += 1
  elif row['y'] == 'no':
    marital_categories[row['marital_status']]['no'] += 1

subs_yes = [marital_categories[marriage]['yes'] for marriage in marital_categories]
subs_no = [marital_categories[marriage]['no'] for marriage in marital_categories]

subs_rate = [0]*len(subs_yes)

for i in range(len(subs_yes)):
  subs_rate[i] = (subs_yes[i] * 100) // (subs_yes[i] + subs_no[i])

married = {}

for i in range(len(marital_categories)):
  if (marital_categories[i] != ):
    married[i] = marital_categories[i]

pt.barh(np.arange(len(married)), subs_rate, color='red', edgecolor = 'black')
pt.yticks(np.arange(len(married)), married.keys(), fontsize = 7)
pt.title(r"Correlation between term deposit and marital status")
pt.xlabel(r'Percentage of clients subscribed')
pt.legend(['Yes', 'No'])
pt.show()
