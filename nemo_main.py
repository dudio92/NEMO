import requests

from NEMO.config import MULTI_MODEL_FOR_HYBRID
from NEMO.nemo import run_ner_model
texts = [
    'לייבניץ היה מתמטיקאי ופילוסוף.\n מרטין היידיגר התכתב עם חנה ארדנט.\n פילוסופיה היא שאלה',
]

class NemoHebrewNer():

    def get_hebrew_nemo_ner(self, text_input: str):
        '''
        text_input is a textual string input, which may contain more than one sentence separated with.
        The model will analyze each sentence separately and will extract entities from all sentences.
        '''
        print('get_hebrew_nemo_ner', text_input)
        if not text_input:
            return None

        # vanilla_ner_model_result = run_ner_model(text_input, model=self.loaded_models['token-multi'],
        #                                                model_name='token-multi'


        v2 = run_ner_model(MULTI_MODEL_FOR_HYBRID,text_input, "/tetst.txt")
        print('vanilla_ner_model_result', v2)

        # text_entity_tuple_list_v = list(zip(vanilla_ner_model_result['tokenized_text'][0], vanilla_ner_model_result['nemo_predictions'][0]))
        text_entity_tuple_list = [list(zip(v2['tokenized_text'][i],
                                           v2['nemo_predictions'][i]))
                                  for i in range(v2['sentences_number'])]

        flatten_list = [item for sublist in text_entity_tuple_list for item in sublist]
        output_entities_list = []
        print('flatten_list', flatten_list)

        for word_entity_tuple in flatten_list:
            # TODO: combine first + last name ini output
            if word_entity_tuple[1] not in ['O', 'O^O']:
                output_entities_list.append(word_entity_tuple[0])

        # print(output_entities_list)
        # print(text_entity_tuple_list)
        # print(flatten_list)
        #
        # print(vanilla_ner_model_result['sentences_number'])

        print(output_entities_list)
        return output_entities_list


if __name__ == '__main__':
    nm = NemoHebrewNer()
    nm.get_hebrew_nemo_ner(texts[0])

