SELECT
    table_schema AS TABLE_SCHEMA,
    table_name AS TABLE_NAME,
    column_name AS COLUMN_NAME,
    column_default AS COLUMN_DEFAULT,
    is_nullable AS IS_NULLABLE,
    ordinal_position AS ORDINAL_POSITION,
    character_maximum_length AS CHARACTER_MAXIMUM_LENGTH,
    numeric_precision AS NUMERIC_PRECISION,
    udt_name AS DATA_TYPE,
    '' AS COLUMN_KEY,  -- PostgreSQL não possui uma coluna equivalente direta para COLUMN_KEY
    '' AS EXTRA  -- PostgreSQL não possui uma coluna equivalente direta para EXTRA
FROM information_schema.columns
WHERE table_schema = 'minha_tabela';


SELECT
    owner AS TABLE_SCHEMA,
    table_name AS TABLE_NAME,
    column_name AS COLUMN_NAME,
    data_type AS DATA_TYPE,
    data_default AS COLUMN_DEFAULT,
    nullable AS IS_NULLABLE,
    column_id AS ORDINAL_POSITION,
    char_length AS CHARACTER_MAXIMUM_LENGTH,
    data_precision AS NUMERIC_PRECISION,
    '' AS COLUMN_KEY,  -- Oracle não possui uma coluna equivalente direta para COLUMN_KEY
    '' AS EXTRA  -- Oracle não possui uma coluna equivalente direta para EXTRA
FROM all_tab_columns
WHERE owner = 'MINHA_TABELA';


SELECT
    TABLE_SCHEMA,
    TABLE_NAME,
    COLUMN_NAME,
    COLUMN_DEFAULT,
    IS_NULLABLE,
    ORDINAL_POSITION,
    CHARACTER_MAXIMUM_LENGTH,
    NUMERIC_PRECISION,
    DATA_TYPE,
    COLUMNPROPERTY(object_id(TABLE_SCHEMA + '.' + TABLE_NAME), COLUMN_NAME, 'IsIdentity') AS EXTRA,
    CASE 
        WHEN COLUMNPROPERTY(object_id(TABLE_SCHEMA + '.' + TABLE_NAME), COLUMN_NAME, 'IsPrimaryKey') = 1 THEN 'PRI'
        WHEN COLUMNPROPERTY(object_id(TABLE_SCHEMA + '.' + TABLE_NAME), COLUMN_NAME, 'IsUnique') = 1 THEN 'UNI'
        ELSE ''
    END AS COLUMN_KEY
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'minha_tabela';
