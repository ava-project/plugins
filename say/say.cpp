#include <Python.h>
#include <string>

std::string say_hello(char *what) {
  return std::string("Hello, ") + std::string(what) + std::string(" !");
}

static PyObject *hello(PyObject *self, PyObject *args)
{
  char *input;

  if (!PyArg_ParseTuple(args, "s", &input)) {
    return NULL;
  }

  return Py_BuildValue("s", say_hello(input));
}

static PyMethodDef HelloMethods[] = {
 { "hello", (PyCFunction)hello, METH_VARARGS, "Say Hello" },
 { NULL, NULL, 0, NULL }
};

static struct PyModuleDef say =
{
    PyModuleDef_HEAD_INIT,
    "say",
    "",
    -1,
    HelloMethods
};

PyMODINIT_FUNC PyInit_say(void)
{
    return PyModule_Create(&say);
}
