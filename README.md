# DeepLearning_SegmentationModel_PV
Automation of rooftop solar panel detection and segmentation from satellite imagery using machine learning. A U-Net model was built and trained in Python with PyTorch to identify solar panels through pixel-level semantic segmentation. Satellite imagery of Stuttgart courtesy of Stadtmessungsamt Stuttgart.

## Hyperparameters:

experiment | lr | batch size | # epochs | dataset_size
1 | 0.001 | 8 | 100 | 304
2 | 0.0001 | 40 | 200 | 304
3 | 0.0001 | 40 | 200 | 527
4 | 0.001 | 8 | 100 | 527
5 | 0.0000 | 60 | 300 | 527
6 | 0.01 | 40 | 200 |527
7 | 0.0001 | 20 | 200 | 161 (100% of images have solar panels)

Authors:

Acosta Vega Monica
Esguerra Montaña Johanna
Martínez García Emerson
- - - - - - -  - - - --  - -
Master Photogrammetry and Geoinformatics
Hochschule für Technik Stuttgart

Juni 2024
