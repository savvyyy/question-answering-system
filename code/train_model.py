import gzip
import gensim
import logging

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)

def show_file_contents(input_file):
    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):
            print(line)
            break

def read_input(input_file):
    logging.info("reading file {0}...this may take a while".format(input_file))
    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):
            if (i % 10000 == 0):
                logging.info("read {0} reviews".format(i))
            yield gensim.utils.simple_preprocess(line)

if __name__ == '__main__':

    data_file = '/home/itadmin/Desktop/mlproject/python/reviews_data.txt.gz'

    documents = list(read_input(data_file))
    logging.info("Done reading data file")

    model = gensim.models.Word2Vec(
        documents,
        size=150,
        window=10,
        min_count=2,
        workers=10)
    model.train(documents, total_examples=len(documents), epochs=10)

    model.wv.save('/home/itadmin/Desktop/mlproject/python')

    w1 = "dirty"
    print("Most similar to {0}".format(w1), model.wv.most_similar(positive=w1))

    w1 = ["polite"]
    print(
        "Most similar to {0}".format(w1),
        model.wv.most_similar(
            positive=w1,
            topn=6))

    w1 = ["france"]
    print(
        "Most similar to {0}".format(w1),
        model.wv.most_similar(
            positive=w1,
            topn=6))

    w1 = ["shocked"]
    print(
        "Most similar to {0}".format(w1),
        model.wv.most_similar(
            positive=w1,
            topn=6))

    w1 = ["beautiful"]
    print(
        "Most similar to {0}".format(w1),
        model.wv.most_similar(
            positive=w1,
            topn=6))

    w1 = ["bed", 'sheet', 'pillow']
    w2 = ['couch']
    print(
        "Most similar to {0}".format(w1),
        model.wv.most_similar(
            positive=w1,
            negative=w2,
            topn=10))

    print("Similarity between 'dirty' and 'smelly'",
          model.wv.similarity(w1="dirty", w2="smelly"))

    print("Similarity between 'dirty' and 'dirty'",
          model.wv.similarity(w1="dirty", w2="dirty"))

    print("Similarity between 'dirty' and 'clean'",
          model.wv.similarity(w1="dirty", w2="clean"))