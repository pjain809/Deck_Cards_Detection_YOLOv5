
import os
import sys
import logging
from datetime import datetime
from from_root import from_root


LOG_FILE = f"Logs @ {datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = f"Logs @ {datetime.now().strftime('%m_%d_%Y')}"
LOG_PATH = os.path.join(from_root(), "Logs", LOG_DIR)

os.makedirs(LOG_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
                    handlers=[logging.FileHandler(LOG_FILE_PATH),
                              logging.StreamHandler(sys.stdout)])

logger = logging.getLogger("YOLO_Object_Detection")
