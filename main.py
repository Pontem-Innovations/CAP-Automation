import logging
import logging.handlers
import os
import json
import requests
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


if __name__ == "__main__":
    
    start_time = time.time()
    r = requests.get('https://capconnect.azurewebsites.net/refresh/contracts/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/jobs/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/contract-items/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/job-pms/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/phases/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/job-phases/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/headquarters/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/provinces/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/customers/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/vendors/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/employees/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/earn-codes/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/pay-period/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/phases_cost_types/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/unit_of_measure/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)

    r = requests.get('https://capconnect.azurewebsites.net/refresh/estimates/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    if r.status_code == 200:
        r.encoding='utf-8-sig'
        data = json.loads(r.text)
        print(data)
        logger.info(data)
        
    #r = requests.get('https://capconnect.azurewebsites.net/refresh/gl-accounts/4UhjlvAFQCBFPDb5UrA3u3yhozyEwoS3')
    #if r.status_code == 200:
    #    r.encoding='utf-8-sig'
    #    data = json.loads(r.text)
    #    print(data)
    #    logger.info(data)

    print(f"--- {time.time() - start_time} seconds ---")
