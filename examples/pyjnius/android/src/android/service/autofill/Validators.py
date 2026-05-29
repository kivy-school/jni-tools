from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Validators"]

class Validators(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/Validators"
    not = JavaStaticMethod("(Landroid/service/autofill/Validator;)Landroid/service/autofill/Validator;")
    and = JavaStaticMethod("([Landroid/service/autofill/Validator;)Landroid/service/autofill/Validator;", varargs=True)
    or = JavaStaticMethod("([Landroid/service/autofill/Validator;)Landroid/service/autofill/Validator;", varargs=True)