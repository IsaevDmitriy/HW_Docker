docker image build -t my-flask:1.0 . 

docker container run -d -p 5000:5000 -e DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/postgres my-flask:1.0
