from django.conf import settings
from sqlalchemy import create_engine


def save_df_in_db(df, table_name: str):
    user = settings.DATABASES["default"]["USER"]
    password = settings.DATABASES["default"]["PASSWORD"]
    database_name = settings.DATABASES["default"]["NAME"]
    host = settings.DATABASES["default"]["HOST"]
    port = settings.DATABASES["default"]["DATABASE_PORT"]

    database_url = (
        "postgresql://{user}:{password}@{host}:{port}/{database_name}".format(
            user=user,
            password=password,
            database_name=database_name,
            host=host,
            port=port,
        )
    )

    engine = create_engine(database_url, echo=False)
    with engine.connect() as connection:
        df.to_sql(table_name, connection, if_exists="append", index=False)
