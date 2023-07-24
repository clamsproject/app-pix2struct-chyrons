"""
The purpose of this file is to define the metadata of the app with minimal imports. 

DO NOT CHANGE the name of the file
"""

from mmif import DocumentTypes, AnnotationTypes

from clams.app import ClamsApp
from clams.appmetadata import AppMetadata


# DO NOT CHANGE the function name 
def appmetadata() -> AppMetadata:
    """
    Function to set app-metadata values and return it as an ``AppMetadata`` obj.
    Read these documentations before changing the code below
    - https://sdk.clams.ai/appmetadata.html metadata specification. 
    - https://sdk.clams.ai/autodoc/clams.appmetadata.html python API
    
    :return: AppMetadata object holding all necessary information.
    """
    
    # first set up some basic information
    metadata = AppMetadata(
        name="Pix2struct Docvqa Wrapper",
        description="extracts text from input timeframes based on user queries using the pix2struct Doc-VQA model",
        app_license="MIT",
        identifier="pix2struct-docvqa-wrapper",
        url="https://github.com/clamsproject/app-pix2struct-docvqa-wrapper",
        # use the following if this app is a wrapper of an existing computational analysis tool
        # (it is very important to pinpoint the primary analyzer version for reproducibility)
        analyzer_version='1',
        analyzer_license="apache-2.0",
    )
    # and then add I/O specifications: an app must have at least one input and ont output
    metadata.add_input(DocumentTypes.VideoDocument)
    metadata.add_output(DocumentTypes.TextDocument, description="extracted text from input timeframes based on user"
                                                                " queries using the pix2struct Doc-VQA model")
    metadata.add_output(AnnotationTypes.Alignment, description="alignment between text document and timeframes")

    # (optional) and finally add runtime parameter specifications

    return metadata


# DO NOT CHANGE the main block
if __name__ == '__main__':
    import sys
    metadata = appmetadata()
    for param in ClamsApp.universal_parameters:
        metadata.add_parameter(**param)
    sys.stdout.write(appmetadata().jsonify(pretty=True))
