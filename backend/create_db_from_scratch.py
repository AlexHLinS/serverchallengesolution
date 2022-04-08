# скрипт для создания SQLlite базы данных с необходимой для работы структурой
import db_worker

db_worker.create_db_from_scratch()
db_worker.create_tables_from_scratch()
db_worker.put_dummy_values()

