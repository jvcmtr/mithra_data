from pathlib import Path
from datetime import datetime
import program.DAL.Repository as repository 
import program.Services.ProceduresPipe as procedures
import program.Utils.JsonHelper as jsonHelper


def main(input_directory, output_file, backup_dir = None):
    data = repository.load_modules_from(input_directory)
    data = procedures.exec(data)
    
    if(backup_dir != None):
        save_backup(output_file, backup_dir)
    jsonHelper.write_file(output_file, data)


def save_backup(output_file, backup_dir):
    try:
        dt = jsonHelper.read_file(output_file)
        file_path = backup_dir / datetime.now().strftime("%Y-%m-%d_%H-%M-%S.bak.json")
        jsonHelper.write_file(file_path, dt)
    except:
        raise("unable to create backup file")



if __name__ == "__main__":
    main()