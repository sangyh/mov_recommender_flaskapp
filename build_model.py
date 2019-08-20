from model import content_rec_engine
import pickle

def build_model():
	model=content_rec_engine

	
	print('Loading data...')
	path='../ml-10m'
	O=content_rec_engine()
	O.load_data(path)
	O.create_feature_lists()

	print(O.find_similar_movs('batman'))


	O.pickle_rec()



if __name__=="__main__":
	build_model()
