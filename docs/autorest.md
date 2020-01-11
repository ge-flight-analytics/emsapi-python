# Autorest Usage

The emsapi client code in this package is generated using the `ems-api.json` swagger specification in the root and the [AutoRest](https://github.com/Azure/autorest) tool.

## Installing

Autorest should be installed according to the instructions in its github repository, it's distributed as an npm package and is out of scope of this document.

## Updating

Run the following commands from the root of the repository:

```bash
# Only run this if the swagger spec has been updated in the repository
python ./tools/clean_swagger.py --file ems-api.json

autorest --input-file=ems-api.json --python --keep-version-file --output-folder=. --add-credentials --override-client-name=emsapi

python ./tools/autorest_patch.py
```
