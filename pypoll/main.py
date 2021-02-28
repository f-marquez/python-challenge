#import dependencies
import os
import csv

# name variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# set file path
voter_path = os.path.join('../pypoll/resources/election_data.csv')

#open and read path
with open(voter_path) as voter_file:
    reader = csv.reader(voter_file, delimter=',')

    #read the header row first
    header = next(voter_file)

    #read row after header
    for row in reader:

        #total votes
        total_votes += 1

        #total votes per candidate
        if(row[2] == 'Khan'):
            khan_votes += 1
        elif(row[2]) == 'Correy':
            correy_votes += 1
        elif(row[2]) == 'Li':
            li_votes += 1
        else:
            otooley_votes += 1
    #determine percentage of votes per candidate
    percent_khan = khan_votes / total_votes
    percent_correy = correy_votes / total_votes
    percent_li = li_votes / total_votes
    percent_otooley = otooley_votes / total_votes

    #calculate the winner of the election via popular votes
    popular_winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if popular_winner == khan_votes:
        name_of_winner = 'Khan'
    elif popular_winner == correy_votes:
        name_of_winner = 'Correy'
    elif popular_winner == li_votes:
        name_of_winner = 'Li'
    else:
        name_of_winner = 'O\'Tooley'

    #print election results
    print(f'Election Results')
    print(f'--------------------------')
    print(f'Total Votes:{total_votes}')
    print(f'--------------------------')
    print(f'Kahn:{percent_khan:.3%} ({khan_votes}))
    print(f'Correy:{percent_correy:.3%} ({correy_votes}')
    print(f'Li:{percent_li:.3%} ({li_votes})')
    print(f'O\'Tooley:{percent_otooley:.3%}({correy_votes})')
    print(f'--------------------------')
    print(f'The Winner Is:{name_of_winner}')
    print(f'--------------------------')

    #setting where to write edited data to
    results_voter_file = os.path.join('../pypoll/resources/election_data_results.txt')

    #open file as text voter_file

    with open(results_voter_file,'w',)as txtfile:

        #format election results
        txtfile.writer()
        txtfile.writer(f'Election Results')
        txtfile.writer(f'--------------------------')
        txtfile.writer(f'Total Votes:{total_votes}')
        txtfile.writer(f'--------------------------')
        txtfile.writer(f'Kahn:{percent_khan:.3%} ({khan_votes})')
        txtfile.writer(f'Correy:{percent_correy:.3%}({correy_votes}')
        txtfile.writer(f'Li:{percent_li:.3%} ({li_votes})')
        txtfile.writer(f'O\'Tooley:{percent_otooley:.3%}({correy_votes})')
        txtfile.writer(f'--------------------------')
        txtfile.writer(f'The Winner Is:{name_of_winner}')
        txtfile.writer(f'--------------------------')
