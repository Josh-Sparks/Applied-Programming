import pandas as pd

##total numbers
sheet = pd.read_excel('table01.xlsx',sheet_name='Readable')
sum = sheet['total population'].sum()
count = sheet['total population'].count()
average = round(sheet['total population'].mean(),2)

##to make things look better
print("***************Total Population of Voters***************")

##non voted numbers
NumberNotVoted = sheet['Number not voted'].sum()
PercentageNotVoted = round((NumberNotVoted/sum)*100,2)

#voter numbers
NumberVoted = sheet['Number Voted'].sum()
PercentageVoted = round((NumberVoted/sum)*100,2)

##print the total numbers to give us some reference
print(f'Total Citizens Polled: {sum}')
print(f'Average in each age Group: {average}')
print('')

##print number voted
print('***************Average Voter to Non-Voter***************')
print(f'Total of the population that voted: {NumberVoted} or %{PercentageVoted} as a whole')
print(f"Total of the population that didn't vote: {NumberNotVoted} or %{PercentageNotVoted} as a whole")
print('')

##number of 18-21 year olds
selectedCells = sheet[0:3]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print('***************Averages by Age Group***************')
print(f'%{printablePercentage} of 18-21 year olds voted')
print(f"%{printableNonPercentage} of 18-21 year olds didn't voted")

##number of 21-24 year olds
print()
selectedCells = sheet[4:6]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 21-24 year olds voted')
print(f"%{printableNonPercentage} of 21-24 year olds didn't voted")

##number of 25-27 year olds who voted and didn't vote
selectedCells = sheet[7:9]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 25-27 year olds voted')
print(f"%{printableNonPercentage} of 25-27 year olds didn't voted")

##number of 28-30 year olds who voted and didn't vote
selectedCells = sheet[10:12]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 28-30 year olds voted')
print(f"%{printableNonPercentage} of 28-30 year olds didn't voted")

##number of 31-33 year olds who voted and didn't vote
selectedCells = sheet[13:15]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 31-33 year olds voted')
print(f"%{printableNonPercentage} of 31-33 year olds didn't voted")

##number of 34-36 year olds who voted and didn't vote
selectedCells = sheet[16:18]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 34-36 year olds voted')
print(f"%{printableNonPercentage} of 34-36 year olds didn't voted")

##number of 37-39 year olds who voted and didn't vote
selectedCells = sheet[19:21]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 37-39 year olds voted')
print(f"%{printableNonPercentage} of 37-39 year olds didn't voted")

##number of 40-42 year olds who voted and didn't vote
selectedCells = sheet[22:24]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 40-42 year olds voted')
print(f"%{printableNonPercentage} of 40-42 year olds didn't voted")

##number of 43-45 year olds who voted and didn't vote
selectedCells = sheet[25:27]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 43-45 year olds voted')
print(f"%{printableNonPercentage} of 43-45 year olds didn't voted")

##number of 46-48 year olds who voted and didn't vote
selectedCells = sheet[28:30]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 46-48 year olds voted')
print(f"%{printableNonPercentage} of 46-48 year olds didn't voted")

##number of 49-51 year olds who voted and didn't vote
selectedCells = sheet[31:33]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 49-51 year olds voted')
print(f"%{printableNonPercentage} of 49-51 year olds didn't voted")

##number of 52-54 year olds who voted and didn't vote
selectedCells = sheet[34:36]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 52-54 year olds voted')
print(f"%{printableNonPercentage} of 52-54 year olds didn't voted")

##number of 55-57 year olds who voted and didn't vote
selectedCells = sheet[37:39]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 55-57 year olds voted')
print(f"%{printableNonPercentage} of 55-57 year olds didn't voted")

##number of 58-60 year olds who voted and didn't vote
selectedCells = sheet[40:42]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 58-60 year olds voted')
print(f"%{printableNonPercentage} of 58-60 year olds didn't voted")

##number of 61-63 year olds who voted and didn't vote
selectedCells = sheet[43:45]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 61-63 year olds voted')
print(f"%{printableNonPercentage} of 61-63 year olds didn't voted")

##number of 64-66 year olds who voted and didn't vote
selectedCells = sheet[46:48]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 64-66 year olds voted')
print(f"%{printableNonPercentage} of 64-66 year olds didn't voted")

##number of 67-69 year olds who voted and didn't vote
selectedCells = sheet[49:51]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 67-69 year olds voted')
print(f"%{printableNonPercentage} of 67-69 year olds didn't voted")


##number of 70-72 year olds who voted and didn't vote
selectedCells = sheet[52:54]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 70-72 year olds voted')
print(f"%{printableNonPercentage} of 70-72 year olds didn't voted")


##number of 73-75 year olds who voted and didn't vote
selectedCells = sheet[55:57]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 73-75 year olds voted')
print(f"%{printableNonPercentage} of 73-75 year olds didn't voted")


##number of 76-79 year olds who voted and didn't vote
selectedCells = sheet[58:60]
selectedVoters = selectedCells['Number Voted']
selectedNonVoter = selectedCells['Number not voted']
selectedTotal = selectedCells['total population']
selectedSum = selectedVoters.sum()
selectedNonSum = selectedNonVoter.sum()
selectedPopulation = selectedTotal.sum()
selectedPercentage = selectedSum/selectedPopulation
selectedNonPercentage = selectedNonSum/selectedPopulation
printablePercentage = round((selectedPercentage*100),2)
printableNonPercentage = round((selectedNonPercentage*100),2)

##print the findings
print()
print(f'%{printablePercentage} of 76-79 year olds voted')
print(f"%{printableNonPercentage} of 76-79 year olds didn't voted")
