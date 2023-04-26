cd docs/
make clean
rm -rf source/{igm.rst,modules.rst}
sphinx-apidoc -o source ../src
make html
touch _build/html/.nojekyll
