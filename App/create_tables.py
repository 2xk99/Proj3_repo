from Proj3_repo.App.database import engine
from Proj3_repo.App.models import metadata


metadata.create_all(
    engine
)


print(
    "Tables created successfully!"
)