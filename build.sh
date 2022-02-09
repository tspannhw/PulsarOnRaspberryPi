# edit CMakeList.txt and remove tests, examples, gmock, gtest, anything that failed
cmake . -DBUILD_TESTS=OFF -DBoost_NO_WARN_NEW_VERSIONS=1
make
make install
cd python

python3 setup.py  install
