import os
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file, override=True)

TOKEN = os.environ.get("TOKEN")