import os
import uuid
import shutil

UPLOAD_DIR = "uploads"

class FileManager:
    @staticmethod
    def save(upload_file):
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        extension = os.path.splitext(upload_file.filename)[1]
        filename = f"{uuid.uuid4()}{extension}"

        file_path = os.path.join(
            UPLOAD_DIR,
            filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                upload_file.file,
                buffer
            )
        return file_path

    @staticmethod
    def delete(file_path):

        if os.path.exists(file_path):
            os.remove(file_path)