
# phase 1 - rename pyjnius-wrapper to jni-wrapper 
the wrapper should now be called jni-wrapper, also when calling the cli

# phase 2 - test suite for jni-wrapper 

since we can also run Java on desktop, then atleast for now on macos
make it soo we got an example in test-suite which uses https://commons.apache.org/proper/commons-csv/
too read some csv data with and print an overview of it in python.

both for pyjnius and jni_core exports..

soo we can verify both wrappers works and also in the future when changes to it.. 

soo 2 packages needs to made for this example/test one for pyjnius and one for jni_core
and ofc always newly generated content for each type when testing..
