import os
import sys
# sys.path.append("../Pharmaceutical-Sales-prediction/")
sys.path.append(os.path.abspath(os.path.join("../Pharmaceutical-Sales-prediction/")))

sys.path.append('../scripts')

from scripts.logger import logger
logger.info("Pharmaceutical-Sales-prediction Logger")