import argparse
import numpy as np
import trainingDataGenerator
import converter
import createModel
import generateTxtFile

def main():
    parser = argparse.ArgumentParser(description='Bitcoin TensorFlow Private Key Prediction')
    parser.add_argument('--seed', type=int, default=1337, help='Random seed for training data generation')
    parser.add_argument('--length', type=int, default=1000, help='Number of training samples')
    parser.add_argument('--model', type=str, default='prediction.keras', help='Model filename')
    parser.add_argument('--create', action='store_true', help='Create and save a new model')
    parser.add_argument('--predict', action='store_true', help='Load model and write predictions to txt')
    parser.add_argument('--first-dim', type=int, default=512, help='First dense layer size')
    parser.add_argument('--hidden-layers', type=int, default=8, help='Number of hidden layers')
    parser.add_argument('--hidden-dim', type=int, default=256, help='Hidden layer size')
    args = parser.parse_args()

    print(f"Generating {args.length} training samples with seed {args.seed}...")
    y_bin_f32, xUncompressed_bin_f32, xCompressed_bin_f32, xSegwit_bin_f32 = trainingDataGenerator.createTrainingData(
        args.length, args.seed
    )

    if args.create:
        print("Creating and saving model...")
        createModel.createAndSaveModel(
            args.first_dim, args.hidden_layers, args.hidden_dim,
            args.model, xUncompressed_bin_f32, y_bin_f32
        )

    if args.predict:
        print("Loading model and writing predictions...")
        generateTxtFile.createTextFileFromModelPrediction(args.model, xUncompressed_bin_f32)


if __name__ == '__main__':
    main()