import pandas
import numpy as np

data_file = open('./assets/ebdJan2019.txt')
full_data = pandas.read_csv(data_file, '\t')

metadata_folder = "./metadata/"

def writeColumns(df):
    print('Started Writing columns.txt\n')
    cols = df.columns.values
    cf =  open(metadata_folder + "columns.txt", "w") #columns file; overwrite if exists
    for col in cols:
        cf.write(col + '\n')
    cf.close()
    print('Finished Writing columns.txt\n')

def numberOfObservations(df):
    print('Started Writing observations.txt\n')
    obf =  open(metadata_folder + "observations.txt", "w") #observation file

    #Total Data

    print('Total Entries: '+ str(df.shape[0]))
    obf.write('Total Rows: ' + str(df.shape[0]) + '\n')

    #Individual Observers


    individual_observations = len(df[(df['NUMBER OBSERVERS']==1)])
    obf.write('Individual Observations: '+ str(individual_observations))
    print('Individual Observations: ' + str(individual_observations))

    #Group Observations


    group_observations = df[(df['NUMBER OBSERVERS']>1)]
    g_obs = pandas.DataFrame.to_csv(group_observations, sep='\t')
    g_obsf = open(metadata_folder+'all_group_observations.csv','w')
    g_obsf.write(g_obs)

    print('\nGroup Observation(With Duplicates): '+str(group_observations.shape[0]))
    obf.write('\nGroup Observation(With Duplicates): '+str(group_observations.shape[0]))

    #Handling Empty GROUP IDENTIFIER
    #TODO



    group_observations_unique = group_observations.drop_duplicates(subset='GROUP IDENTIFIER')

    #Total observers in group
    total_observers = group_observations_unique['NUMBER OBSERVERS'].sum()
    print('Total Number of Group Observers: ' + str(total_observers))
    obf.write('\nTotal Number of Group Observers: ' + str(total_observers))

    g_obs_no_dup = pandas.DataFrame.to_csv(group_observations_unique, sep='\t')
    g_obs_no_dup_f = open(metadata_folder+'group_observations_no_duplicates.csv','w')
    g_obs_no_dup_f.write(g_obs_no_dup)

    num_group_obs = group_observations_unique.shape[0]
    print('\nGroup Observations(Without Duplicates): ' + str(num_group_obs))
    obf.write('\nGroup Observations(Without Duplicates): '+ str(num_group_obs))
    obf.close()
    print('\nFinished Writing observations.txt')
    

writeColumns(full_data)
numberOfObservations(full_data)

