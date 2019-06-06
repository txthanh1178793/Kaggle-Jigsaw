
class Config:
    logdir = "/raid/bac/kaggle/logs/jigsaw/"
    experiment = 'train_all_11layer'
    max_sequence_length = 220
    lr = 2e-5
    batch_size = 128
    accumulation_steps = 1
    train_percent = 1.0
    valid_percent = 0.05

    seed = 12345
    epochs = 2
    data_dir = "/raid/data/kaggle/jigsaw/"
    toxicity_column = 'target'
    bert_weight = "../bert_weight/uncased_L-11_H-768_A-12/"
    features = '../meta/'
    checkpoint = f"{logdir}/{experiment}_{epochs}epoch_{train_percent * 100}train_{valid_percent * 100}/"

    aux_columns = ['target', 'severe_toxicity', 'obscene', 'identity_attack', 'insult', 'threat']
    n_aux_targets = len(aux_columns)

    identity_columns = [
        'male', 'female', 'homosexual_gay_or_lesbian', 'christian', 'jewish',
        'muslim', 'black', 'white', 'psychiatric_or_mental_illness'
    ]


class ConfigLSTM:
    logdir = "/raid/bac/kaggle/logs/jigsaw/"
    experiment = 'lstm'
    max_sequence_length = 300
    lr = 2e-5
    batch_size = 512
    train_percent = 0.95
    valid_percent = 0.05

    seed = 12345
    epochs = 2

    LSTM_UNITS = 256
    DENSE_HIDDEN_UNITS = 4 * LSTM_UNITS + 64

    data_dir = "/raid/data/kaggle/jigsaw/"
    toxicity_column = 'target'
    bert_weight = "../bert_weight/uncased_L-11_H-768_A-12/"
    features = '../lstm_features/'
    checkpoint = f"{logdir}/{experiment}_{epochs}epoch_{train_percent * 100}train_{valid_percent * 100}/"

    aux_columns = ['target', 'severe_toxicity', 'obscene', 'identity_attack', 'insult', 'threat']
    n_aux_targets = len(aux_columns)

    identity_columns = [
        'male', 'female', 'homosexual_gay_or_lesbian', 'christian', 'jewish',
        'muslim', 'black', 'white', 'psychiatric_or_mental_illness'
    ]
