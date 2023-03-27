from pandas import read_csv

DATASET = 'Distraction'

def distraction_data_exploration(data_folder: str) -> None:
    """ Runs data exploration for Distraction dataset. """
    nbr_unique_drivers = 30
    data_types = ['car', 'face', 'speech']
    # Set paths based on data_types
    paths = {data_type: [] for data_type in data_types}
    for data_type in data_types:
        for i in range(1, nbr_unique_drivers + 1):
            if i < 10: paths[data_type].append(f'{data_folder}/00{i}_{data_type}.csv')
            else: paths[data_type].append(f'{data_folder}/0{i}_{data_type}.csv')
    
    # Load first data car
    df_car = read_csv(paths['car'][0])
    print(df_car)
    quit()

def main(dataset: str) -> None:
    """ Runs main function of data exploration script. """
    if dataset == 'Distraction': 
        data_folder = './data/DistractionDetectionDataset/Data_processed'
        distraction_data_exploration(data_folder)
        
    else: raise NotImplementedError(f'Dataset {dataset} not implemented.')

if __name__ == '__main__':
    main(dataset=DATASET)