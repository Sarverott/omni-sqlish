import re
from typing import List

# Typowe mapowanie typów SQLite -> MySQL
SQLITE_TO_MYSQL_TYPES = {
    'INTEGER': 'INT',
    'TEXT': 'VARCHAR(255)',
    'REAL': 'DOUBLE',
    'BLOB': 'BLOB',
    'NUMERIC': 'DECIMAL(10,2)',
    'BOOLEAN': 'TINYINT(1)',
    'DATETIME': 'DATETIME',
    'DATE': 'DATE',
}


def parse_create_table(sqlite_sql: str) -> List[str]:
    """
    Parsuje CREATE TABLE z dumpa SQLite i przekształca do składni MySQL.
    """
    statements = []
    tables = re.findall(r'CREATE TABLE\s+(.*?)\s*\((.*?)\);', sqlite_sql, re.DOTALL)
    for table_name, body in tables:
        columns = []
        lines = [line.strip() for line in body.strip().split(',')]
        for line in lines:
            if line.upper().startswith('CONSTRAINT') or line.upper().startswith('PRIMARY KEY'):
                continue  # Pominięcie constraintów (na razie)
            name_type = line.split()
            if len(name_type) < 2:
                continue
            col_name = name_type[0].strip('"')
            col_type = name_type[1].upper()
            mysql_type = SQLITE_TO_MYSQL_TYPES.get(col_type.split('(')[0], 'TEXT')
            columns.append(f"  `{col_name}` {mysql_type}")
        
        stmt = f"CREATE TABLE IF NOT EXISTS `{table_name.strip('"')}` (\n" + ",\n".join(columns) + "\n);"
        statements.append(stmt)
    return statements


# Przykład użycia
dump = '''
CREATE TABLE IF NOT EXISTS "migrations"(
  "id" integer primary key autoincrement not null,
  "migration" varchar not null,
  "batch" integer not null
);
'''


converted = parse_create_table(dump)
for stmt in converted:
    print(stmt)