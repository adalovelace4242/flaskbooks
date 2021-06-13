set -e

# todo: test with mypy, add it to docker containers too
cd recommendations
bash run.sh

cd ..

cd marketplace
bash run.sh
