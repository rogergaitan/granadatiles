from apps.utils import BaseModel
from apps.utils.methods import model_directory_path


class Catalog(BaseModel):
    file = FileField(upload_to=model_directory_path)
