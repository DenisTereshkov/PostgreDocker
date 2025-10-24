set -e

if [ -f /app/.env ]; then
    export $(grep -v '^#' /app/.env | xargs)
fi


cat > /pgadmin4/servers.json <<EOF
{
  "Servers": {
    "1": {
      "Name": "Local Dev DB",
      "Group": "Servers",
      "Host": "pg_db",
      "Port": 5432,
      "MaintenanceDB": "${POSTGRES_DB}",
      "Username": "${POSTGRES_USER}",
      "PassFile": "/pgadmin4/.pgpass"
    }
  }
}
EOF

echo "pg_db:5432:${POSTGRES_DB}:${POSTGRES_USER}:${POSTGRES_PASSWORD}" > /pgadmin4/.pgpass
chmod 600 /pgadmin4/.pgpass
exec "$@"