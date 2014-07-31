# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# For license information, see the LICENSE.txt file

#This only contains basic views for basic TAXII Services

from django.views.decorators.csrf import csrf_exempt
import handlers
from utils import request_utils, response_utils

@csrf_exempt
@request_utils.validate_taxii()
def service_router(request, path=None, taxii_message=None):
    """
    """
    service = handlers.get_service_from_path(request.path)
    message_handler = handlers.get_message_handler(service, taxii_message)
    
    response_message = message_handler.handle_message(service, taxii_message, request)
    #TODO: Consider intelligently selecting the response headers
    return response_utils.HttpResponseTaxii(response_message.to_xml(), response_utils.TAXII_11_HTTP_Headers)
    
