import numpy as np
import trainingDataGenerator
import converter
import createModel
import generateTxtFile

# variables
trainingDataLength = 10000
seed = 1337
file_name=f'prediction'
    
# get training data
y_bin_f32, xUncompressed_bin_f32, xCompressed_bin_f32, xSegwit_bin_f32 = trainingDataGenerator.createTrainingData(trainingDataLength, seed)

# flag to create and save a model
create_Model = True

if create_Model:
    createModel.createAndSaveModel(16, 8, 8, file_name, xUncompressed_bin_f32, y_bin_f32)

# flag to load and write a txt from predictions
loadModelAndWrite = True
    
if loadModelAndWrite: 
    generateTxtFile.createTextFileFromModelPrediction(file_name, xUncompressed_bin_f32)
