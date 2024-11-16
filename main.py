import matplotlib.pyplot as plt
import networkx as nx

# Based on the tournament odds provided, create a directed graph to represent the predicted winners
# at each stage of the tournament. The nodes represent the teams and the edges direct from the
# predicted loser to the predicted winner of each match-up.

# The edges are created based on the highest probability of winning at each stage

# East region winners based on provided probabilities
east_winners = {
    'Round of 64': [('Connecticut', 'Stetson'), ('Florida Atlantic', 'Northwestern'), 
                    ('San Diego State', 'UAB'), ('Auburn', 'Yale'), ('Brigham Young', 'Duquesne'), 
                    ('Illinois', 'Morehead State'), ('Washington State', 'Drake'), ('Iowa State', 'South Dakota State')],
    'Round of 32': [('Connecticut', 'Florida Atlantic'), ('San Diego State', 'Auburn'), 
                    ('Brigham Young', 'Illinois'), ('Iowa State', 'Washington State')],
    'Sweet 16': [('Connecticut', 'San Diego State'), ('Illinois', 'Iowa State')],
    'Elite 8': [('Connecticut', 'Illinois')],
    'Final 4': [('Connecticut',)],
}

# West region winners based on provided probabilities
west_winners = {
    'Round of 64': [('North Carolina', 'Howard'), ('Mississippi State', 'Michigan State'), 
                    ('Saint Mary\'s', 'Grand Canyon'), ('Alabama', 'Charleston'), 
                    ('Clemson', 'New Mexico'), ('Baylor', 'Colgate'), 
                    ('Dayton', 'Nevada'), ('Arizona', 'Long Beach State')],
    'Round of 32': [('North Carolina', 'Mississippi State'), ('Alabama', 'Saint Mary\'s'), 
                    ('Baylor', 'Clemson'), ('Arizona', 'Dayton')],
    'Sweet 16': [('North Carolina', 'Alabama'), ('Baylor', 'Arizona')],
    'Elite 8': [('North Carolina', 'Baylor')],
    'Final 4': [('North Carolina',)],
}

# South region winners based on provided probabilities
south_winners = {
    'Round of 64': [('Houston', 'Longwood'), ('Texas A&M', 'Nebraska'), 
                    ('Wisconsin', 'James Madison'), ('Duke', 'Vermont'), 
                    ('Texas Tech', 'North Carolina State'), ('Kentucky', 'Oakland'), 
                    ('Colorado', 'Florida'), ('Marquette', 'Western Kentucky')],
    'Round of 32': [('Houston', 'Texas A&M'), ('Duke', 'Wisconsin'), 
                    ('Kentucky', 'Texas Tech'), ('Marquette', 'Colorado')],
    'Sweet 16': [('Houston', 'Duke'), ('Kentucky', 'Marquette')],
    'Elite 8': [('Houston', 'Kentucky')],
    'Final 4': [('Houston',)],
}

# Midwest region winners based on provided probabilities
midwest_winners = {
    'Round of 64': [('Purdue', 'Montana State'), ('TCU', 'Utah State'), 
                    ('Gonzaga', 'McNeese State'), ('Kansas', 'Samford'), 
                    ('South Carolina', 'Oregon'), ('Creighton', 'Akron'), 
                    ('Texas', 'Virginia'), ('Tennessee', 'St. Peter\'s')],
    'Round of 32': [('Purdue', 'TCU'), ('Gonzaga', 'Kansas'), 
                    ('Creighton', 'South Carolina'), ('Tennessee', 'Texas')],
    'Sweet 16': [('Purdue', 'Gonzaga'), ('Tennessee', 'Creighton')],
    'Elite 8': [('Purdue', 'Tennessee')],
    'Final 4': [('Purdue',)],
}

# Adjusting 'Final 4' entries to be 2-tuples with placeholder nodes
east_winners['Final 4'] = [('Connecticut', 'Final 4 East')]
west_winners['Final 4'] = [('North Carolina', 'Final 4 West')]
south_winners['Final 4'] = [('Houston', 'Final 4 South')]
midwest_winners['Final 4'] = [('Purdue', 'Final 4 Midwest')]

# Final game prediction based on the highest probability
final_game = [('Connecticut', 'North Carolina'), ('Houston', 'Purdue')]
champion = 'Connecticut'

# Create a directed graph
G = nx.DiGraph()

# Add edges for each winner in the East region
for round, winners in east_winners.items():
    G.add_edges_from(winners)

# Add edges for each winner in the West region
for round, winners in west_winners.items():
    G.add_edges_from(winners)

# Add edges for each winner in the South region
for round, winners in south_winners.items():
    G.add_edges_from(winners)

# Add edges for each winner in the Midwest region
for round, winners in midwest_winners.items():
    G.add_edges_from(winners)

# Add edges for the final game and champion
G.add_edges_from(final_game)
G.add_node(champion)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
plt.show()