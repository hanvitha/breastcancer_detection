Refer to breastcancer_portal repo on my profile for clear instructions to run this model in Openshift

oc new-app --name bc-model quay.io/hanvithag/model-pipeline-s2i:master~https://github.com/hanvitha/breastcancer_detection --build-env S2I_SOURCE_NOTEBOOK_LIST="image_processing_model.ipynb" 
