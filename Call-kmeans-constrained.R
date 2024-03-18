#install.packages("reticulate")
library(reticulate)
py_discover_config()
py_module_available("k-means-constrained")
py_install(envname = "C:\\Users\\ademiriz\\Documents\\.virtualenvs\\r-reticulate", packages="k-means-constrained")
py_module_available("k-means-constrained")
reticulate::py_version()

py_run_file("constKeyMeansIris.py")

#py$mylabels
table(py$mylabels)
