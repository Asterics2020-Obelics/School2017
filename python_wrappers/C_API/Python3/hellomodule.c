#include <Python.h>
#include "hello.h"

static PyObject * hello_wrapper(PyObject * self, PyObject * args)
{
  char * input;
  char * result;
  PyObject * ret;

  // parse arguments
  if (!PyArg_ParseTuple(args, "s", &input)) {
    return NULL;
  }

  // run the actual function
  result = hello(input);

  // build the resulting string into a Python object.
  ret = PyBytes_FromString(result);
  free(result);

  return ret;
}



static PyMethodDef SpamMethods[] = {
    {"say_hello", hello_wrapper, METH_VARARGS,
     "Say hello"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


static struct PyModuleDef hellomodule = {
   PyModuleDef_HEAD_INIT,
   "hello",   /* name of module */
   NULL,     /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   SpamMethods
};

PyMODINIT_FUNC
PyInit_hello(void)
{
    PyObject *m;

    m = PyModule_Create(&hellomodule);
    if (m == NULL)
        return NULL;
    return m;
}
