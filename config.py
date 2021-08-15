DEVICE = 3
LOCAL_TEMP_FOLDER = 'temp'
DELETE_TEMP_FILES = True

MODEL_PATHS = {
    'token-single_oov': {'model': 'NEMO/data/token.char_lstm.ft_oov_tok.44_seed.146.model',
                         'dset': 'NEMO/data/token.char_lstm.ft_oov_tok.44_seed.dset'},
    'token-single': {'model': 'NEMO/data/token.char_cnn.ft_tok.46_seed.104.model',
                     'dset': 'NEMO/data/token.char_cnn.ft_tok.46_seed.dset'},
    'token-multi_oov': {'model': 'NEMO/data/multitok.char_cnn.ft_oov_tok.48_seed.123.model',
                        'dset': 'NEMO/data/multitok.char_cnn.ft_oov_tok.48_seed.dset'},
    'token-multi': {'model': 'NEMO/data/multitok.char_cnn.ft_tok.52_seed.173.model',
                    'dset': 'NEMO/data/multitok.char_cnn.ft_tok.52_seed.dset'},
    'morph_oov': {'model': 'NEMO/data/morph.char_cnn.ft_oov_yap.49_seed.87.model',
                  'dset': 'NEMO/data/morph.char_cnn.ft_oov_yap.49_seed.dset'},
    'morph': {'model': 'NEMO/data/morph.char_cnn.ft_yap.50_seed.80.model',
              'dset': 'NEMO/data/morph.char_cnn.ft_yap.50_seed.dset'}
}
MULTI_MODEL_FOR_HYBRID = 'token-multi'

YAP_PATH = '../yapproj/src/yap/yap'

YAP_API_URL = 'http://localhost:8000'

YAP_API_HEADERS = {'content-type': 'application/json'}
