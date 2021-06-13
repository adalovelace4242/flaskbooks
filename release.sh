set -ex

VERSION=$(cat VERSION)
USERNAME=adalovelace4242

echo "version: $VERSION"


# tag it
git add -A
git commit -m "version $VERSION"
git tag -a "$VERSION" -m "version $VERSION"
git push
git push --tags

# 1st image
# run build
./build.sh marketplace
IMAGE=marketplace

# push it
docker push $USERNAME/$IMAGE:latest
docker push $USERNAME/$IMAGE:$VERSION


# 2nd image
# run build
./build.sh recommendations
IMAGE=recommendations

# push it
docker push $USERNAME/$IMAGE:latest
docker push $USERNAME/$IMAGE:$VERSION

# increment version
major=$(echo $VERSION | cut -d. -f1)
minor=$(echo $VERSION | cut -d. -f2)
revision=$(echo $VERSION | cut -d. -f3)
revision=$(expr $revision + 1)

new_version=$major.$minor.$revision
echo $new_version >| VERSION

git add -A
git commit -m "next version will be $VERSION"
git push