# Shortcuts for your database lifecycle
migrate:
	alembic revision --autogenerate -m "new migration"

upgrade:
	alembic upgrade head

# A command to quickly check your database state
db-list:
	sudo -u postgres psql -d cava_db -c "\dt"

# A command to run your database test one-liner
db-test:
	python -c "from app.core.database import SQLALCHEMY_DATABASE_URL; print(SQLALCHEMY_DATABASE_URL)"