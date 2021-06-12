set -ex

VERSION=$(cat VERSION)

echo "version: $VERSION"

docker build -t adalovelace4242/$1:$VERSION -f $1/Dockerfile .
docker tag adalovelace4242/$1:$VERSION adalovelace4242/$1:latest