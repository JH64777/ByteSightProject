from django.apps import AppConfig
import tensorflow as tf

class StaganalysisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staganalysis'
    model = tf.keras.models.load_model('C:/Users/asdew32/Desktop/final_project/WebSite/Newbytesight/bytesight/AI_Model/model_17.keras') # 모델 불러오기

